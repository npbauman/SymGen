"""
Equation building module for SymGen.

This module contains functions extracted from SymGen.py for building final equations
from processed contraction data. It handles the combination of isomorphic terms,
equation generation, and output formatting.

The module provides the final stage of equation generation:
1. Processing weight values and converting to formatted strings
2. Determining operator positions (fixed vs free)
3. Labeling positions based on creation/annihilation properties
4. Generating final equation strings with proper formatting
5. Outputting statistics and formatted results

Example Usage:
    >>> final_equations = generate_final_equations(final_dict, operator_mapping, OperatorsDict)
    >>> format_equation_output(final_equations)
    >>> print_statistics(final_dict)
    >>> weight_str = process_weight(0.5)  # Returns "(1.0/2.0) * "

Functions:
    process_weight: Convert weight values to formatted strings
    determine_positions: Identify fixed and free operator positions
    label_positions: Generate labels for operator positions
    generate_final_equations: Create final equation strings
    format_equation_output: Print formatted equations
    print_statistics: Display statistics about terms
"""

import copy
from fractions import Fraction
from Utilities import find_tuple_with_value


def process_weight(sweight):
    """
    Process the weight value and convert it to a formatted string.

    Converts numerical weight values to properly formatted strings for equation output.
    Handles special cases like unity weights and zero weights.

    Args:
        sweight (float): The weight value to process

    Returns:
        str or None: Formatted weight string (e.g., "1.0 * ", "(1.0/2.0) * ")
                    or None if weight is zero

    Examples:
        >>> process_weight(1.0)
        "1.0 * "
        >>> process_weight(-1.0)
        "-1.0 * "
        >>> process_weight(0.5)
        "(1.0/2.0) * "
        >>> process_weight(0.0)
        None
    """
    if abs(sweight) != 0.0:
        weight_frac = Fraction(sweight).limit_denominator(1000).as_integer_ratio()
        if weight_frac == (1, 1):
            return "1.0 * "
        elif weight_frac == (-1, 1):
            return "-1.0 * "
        else:
            return f"({weight_frac[0]}.0/{weight_frac[1]}.0) * "
    return None


def determine_positions(identities, operators, operators_dict):
    """
    Determine fixed and free positions based on operator properties.

    Separates operator positions into fixed (core orbitals) and free (virtual orbitals)
    based on the "Fixed" property in the operator dictionary.

    Args:
        identities (list): List of identity values mapping positions to operators
        operators (list): List of operator names
        operators_dict (dict): Dictionary of operator properties

    Returns:
        tuple: (fixed_positions, free_positions) where each is a list of position indices

    Examples:
        >>> identities = [1, 1, 2, 2]
        >>> operators = ["T1", "H1"]
        >>> fixed, free = determine_positions(identities, operators, OperatorsDict)
    """
    fixed_positions = []
    free_positions = []
    for pos, identity in enumerate(identities):
        operator = operators[identity - 1]
        if operators_dict[operator].get("Fixed"):
            fixed_positions.append(pos)
        else:
            free_positions.append(pos)
    return fixed_positions, free_positions


def label_positions(identities, contractions, creation_annihilation_values, operators, operators_dict):
    """
    Generate labels for operator positions based on contractions and creation/annihilation values.

    Creates appropriate labels (h1, h2, p1, p2, etc.) for each operator position
    based on whether they are hole (H) or particle (P) operators and whether
    they are fixed or free positions.

    Args:
        identities (list): List of identity values mapping positions to operators
        contractions (list): List of contraction tuples (pairs of contracted indices)
        creation_annihilation_values (list): List of creation/annihilation operator types
        operators (list): List of operator names
        operators_dict (dict): Dictionary of operator properties

    Returns:
        list: List of position labels (e.g., ["h1", "h1", "p1", "p1"])

    Examples:
        >>> labels = label_positions([1,1,2,2], [(0,1),(2,3)], ["H+","H","P+","P"], ["T1","H1"], OperatorsDict)
    """
    fixed_start = 1
    free_start = len([i for i in identities if operators_dict[operators[i-1]].get("Fixed")]) + 1
    labels = [None] * len(identities)

    for pos, identity in enumerate(identities):
        contraction = find_tuple_with_value(contractions, pos)
        creation_annihilation_1 = creation_annihilation_values[contraction[0]]
        creation_annihilation_2 = creation_annihilation_values[contraction[1]]
        fixed1 = operators_dict[operators[identity - 1]].get("Fixed")
        fixed2 = operators_dict[operators[identity - 1]].get("Fixed")

        if fixed1:
            if "H" in creation_annihilation_1 or "H" in creation_annihilation_2:
                labels[contraction[0]] = f"h{fixed_start}"
                labels[contraction[1]] = f"h{fixed_start}"
                fixed_start += 1
            elif "P" in creation_annihilation_1 or "P" in creation_annihilation_2:
                labels[contraction[0]] = f"p{fixed_start}"
                labels[contraction[1]] = f"p{fixed_start}"
                fixed_start += 1
        else:
            if not fixed1 and not fixed2 and labels[contraction[0]] is None:
                if "H" in creation_annihilation_1 or "H" in creation_annihilation_2:
                    labels[contraction[0]] = f"h{free_start}"
                    labels[contraction[1]] = f"h{free_start}"
                    free_start += 1
                elif "P" in creation_annihilation_1 or "P" in creation_annihilation_2:
                    labels[contraction[0]] = f"p{free_start}"
                    labels[contraction[1]] = f"p{free_start}"
                    free_start += 1
    return labels


def combine_isomorphic_terms_across_expressions(short_dict):
    """
    Combine isomorphic terms across different expressions (final level combination).

    Args:
        short_dict (dict): Dictionary of processed contractions from expression level

    Returns:
        dict: Final dictionary with combined weights across expressions
    """
    from Graphs import check_isomorphism

    final_dict = {}
    ignore_list = []

    for key_1, value_1 in short_dict.items():
        if key_1 not in ignore_list:
            combined_weight = 1.0 * value_1['S-Weight']

            for key_2, value_2 in short_dict.items():
                if key_2 > key_1 and key_2 not in ignore_list:
                    if (sorted(value_1['Operators']) == sorted(value_2['Operators'])):
                        if check_isomorphism(value_1['Graph'], value_2['Graph']):
                            if value_1['Parity'] == value_2['Parity']:
                                combined_weight += value_2['S-Weight']
                            else:
                                combined_weight -= value_2['S-Weight']

                            ignore_list.append(key_2)

            final_dict[key_1] = copy.deepcopy(short_dict[key_1])
            final_dict[key_1]['S-Weight'] = round(combined_weight, 9)

    return final_dict


def generate_final_equations(final_dict, operator_mapping, operators_dict, print_opt="normal"):
    """
    Generate final equation strings from the processed contraction dictionary.
    
    Args:
        final_dict (dict): Dictionary of final processed contractions
        operator_mapping (dict): Mapping of operators to their string templates
        operators_dict (dict): Dictionary of operator properties
        print_opt (str): Print option ("verbose" or "normal")
        
    Returns:
        list: List of final equation strings
    """
    final_equations = []
    
    for key, value in final_dict.items():
        if print_opt == "verbose":
            print("\n", key, value)

        sweight = value.get("S-Weight")
        eqn_str = process_weight(sweight)

        if eqn_str:
            identities = value["Identities"]
            operators = value["Operators"]
            contractions = value["Oriented Contractions"]
            creation_annihilation_values = value["CA"]

            fixed_positions, free_positions = determine_positions(identities, operators, operators_dict)
            labels = label_positions(identities, contractions, creation_annihilation_values, operators, operators_dict)

            operator_creation_annihilation_list = [[] for x in range(len(value["Operators"]))]
            for position in range(len(labels)):
                identity = value["Identities"][position]
                operator_creation_annihilation_list[identity-1].append(labels[position])

            length = len(operator_creation_annihilation_list)
            for _ in range(length):
                operator = value["Operators"][_]
                op_str = ""
                flipsign = False

                if operator not in operator_mapping:
                    if not operators_dict[operator].get("Fixed"):
                        print("{} is not programmed".format(operator))
                else:
                    labels_for_operator = operator_creation_annihilation_list[_]
                    key_tuple = tuple(label[0] for label in labels_for_operator)
                    op_template = operator_mapping[operator].get(key_tuple)

                    if op_template:
                        flipsign = op_template[1]
                        op_str = op_template[0].format(*labels_for_operator)
                        if _ != length - 1:
                            eqn_str += op_str + " * "
                        else:
                            eqn_str += op_str

                        if flipsign:
                            if "-" in eqn_str:
                                eqn_str = eqn_str.replace("-", "")
                            elif "-" not in eqn_str:
                                eqn_str = "-" + eqn_str
                    else:
                        print(f"No template found for {key_tuple}")
            
            final_equations.append(eqn_str)

            if print_opt == "verbose":
                print(eqn_str)
    
    return final_equations


def format_equation_output(final_equations):
    """
    Format and print the final equations.
    
    Args:
        final_equations (list): List of equation strings to output
    """
    print("\nFINAL EQUATIONS ")
    for equation in final_equations:
        print(equation)


def print_statistics(final_dict):
    """
    Print statistics about the final dictionary terms.

    Args:
        final_dict (dict): Dictionary of final processed contractions
    """
    print("")
    count = sum(1 for value in final_dict.values() if abs(value['S-Weight']) == 0.0 and not value['Connected'])
    print(count, "vanishing disconnected terms.")
    count = sum(1 for value in final_dict.values() if abs(value['S-Weight']) != 0.0 and not value['Connected'])
    print(count, "nonvanishing disconnected terms.")
    count = sum(1 for value in final_dict.values() if abs(value['S-Weight']) == 0.0 and value['Connected'])
    print(count, "vanishing connected terms.")
    count = sum(1 for value in final_dict.values() if abs(value['S-Weight']) != 0.0 and value['Connected'])
    print(count, "nonvanishing connected terms.")

    for value in final_dict.values():
        if abs(value['S-Weight']) != 0.0 and value['Connected']:
            print(value)