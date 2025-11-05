"""
Contraction Engine Module

This module contains functions for processing operator combinations and evaluating contractions.
Extracted from SymGen.py to improve code organization and readability.

The module handles the core contraction evaluation process:
1. Processing operator combinations to build contraction data
2. Evaluating contractions using quantum mechanical pairing rules
3. Calculating weights and signs for each contraction
4. Combining isomorphic terms at expression and cross-expression levels

Example Usage:
    >>> contraction_dict, short_dict = process_operator_combinations(validated_combinations)
    >>> final_dict = combine_across_expressions(short_dict)
    >>> weight = calculate_weights("T1 H1")
    >>> parity, sign = calculate_signs([(0, 1), (2, 3)], "T1 H1")

Functions:
    process_operator_combinations: Main processing loop for operator combinations
    evaluate_contractions: Evaluate contractions using all_pairs function
    calculate_weights: Calculate weight factors for operator combinations
    calculate_signs: Calculate parity and sign factors
    combine_expression_level: Combine isomorphic terms within expressions
    combine_across_expressions: Combine isomorphic terms across expressions
"""

import math
import copy
from typing import Dict, List, Tuple, Any
from ContractionRules import all_pairs
from Utilities import parity_and_sign
from Graphs import build_graph, check_if_connected, check_isomorphism
from Operators import OperatorsDict
from Input import Opp, Hamiltonian


def process_operator_combinations(validated_combinations: List[str], print_opt: str = "") -> Tuple[Dict[int, Dict], Dict[int, Dict]]:
    """
    Process operator combinations and evaluate contractions.

    Extracted from the main processing loop in SymGen.py (lines ~200-300).

    Args:
        validated_combinations: List of validated operator combination strings
        print_opt: Print option for verbose output

    Returns:
        Tuple of (ContractionDict, ShortDict) containing processed contractions
    """
    contraction_dict = {}
    short_dict = {}
    count = 0
    
    for operator_combination in validated_combinations:
        # Initialize lists for identities, creation/annihilation operators, spin operators, and the operator list
        all_creation_annihilation_operators = []
        all_spin_operators = []
        identities = []
        operator_list = []

        # Initialize the identity counter
        identity = 1

        # Iterate over each operator in the split operator_combination
        for operator in operator_combination.split():
            if operator != "-":
                # Retrieve creation/annihilation and Spin operators for the current valid operator
                creation_annihilation_operators = OperatorsDict[operator].get("C A", "").split()
                spin_operators = OperatorsDict[operator].get("Spins", "").split()

                # Extend the lists with creation/annihilation and Spin operators
                all_creation_annihilation_operators.extend(creation_annihilation_operators)
                all_spin_operators.extend(spin_operators)

                # Append the current identity to the identities list, once for each Spin operator
                identities.extend([identity] * len(spin_operators))

                # Append the current operator to the operator list
                operator_list.append(operator)

                # Increment the identity counter only after processing a valid operator
                identity += 1

        # Evaluate contractions using the all_pairs function
        evaluated_contractions = evaluate_contractions(
            all_creation_annihilation_operators, identities, all_spin_operators, operator_list
        )

        if evaluated_contractions:
            if print_opt == "verbose":
                print(operator_combination)
                print("Creation/Annihilation Operators: ", all_creation_annihilation_operators)
                print("Spin Operators: ", all_spin_operators)
                print("Identity Indices: ", identities)
                print("Evaluated Contractions: ", *evaluated_contractions, sep="\n")
                print("-" * 40 + "\n")
        else:
            if print_opt == "verbose":
                print(operator_combination, " WAS ELIMINATED BECAUSE NO VIABLE SET OF CONTRACTIONS WERE FOUND\n")
                print("-" * 40 + "\n")

        # Process each contraction and build the contraction dictionary
        compare_start = count
        for contraction_list in evaluated_contractions:
            contraction_dict[count] = {}

            contraction_dict[count]['Term'] = operator_combination
            if "-" in operator_combination.split():
                contraction_dict[count]['Operators'] = operator_combination.split()[1:]
            else:
                contraction_dict[count]['Operators'] = operator_combination.split()

            contraction_dict[count]['CA'] = all_creation_annihilation_operators
            contraction_dict[count]['Spins'] = all_spin_operators
            contraction_dict[count]['Identities'] = identities

            # Calculate weights and signs
            weight, parity, sign = calculate_weights_and_signs(
                operator_combination, contraction_list
            )

            contraction_dict[count]['Weight'] = weight
            contraction_dict[count]['Parity'] = parity
            contraction_dict[count]['Sign'] = sign

            # Reorder contractions so creation operators are listed before annihilation
            oriented_contractions = list(contraction_list)
            for contraction in oriented_contractions:
                if "+" not in all_creation_annihilation_operators[contraction[0]]:
                    oriented_contractions[oriented_contractions.index(contraction)] = (
                        contraction[1], contraction[0]
                    )

            contraction_dict[count]['Oriented Contractions'] = oriented_contractions

            # Build the graph
            contraction_dict[count]['Graph'] = build_graph(contraction_dict[count], OperatorsDict)

            # Determine if Graph is Disconnected
            contraction_dict[count]['Connected'] = check_if_connected(
                contraction_dict[count]['Graph'], OperatorsDict
            )

            # Increment count
            count += 1

        compare_end = count

        # Combine isomorphic terms at the expression level
        short_dict = combine_expression_level(
            contraction_dict, short_dict, compare_start, compare_end
        )

    return contraction_dict, short_dict


def evaluate_contractions(all_creation_annihilation_operators: List[str], identities: List[int],
                         all_spin_operators: List[str], operator_list: List[str]) -> List[List[Tuple]]:
    """
    Evaluate contractions using the all_pairs function.

    Args:
        all_creation_annihilation_operators: List of creation/annihilation operators
        identities: List of identity indices
        all_spin_operators: List of spin operators
        operator_list: List of operator names

    Returns:
        List of evaluated contraction lists
    """
    evaluated_contractions = []

    for contraction_list in all_pairs(
        list(range(0, len(all_creation_annihilation_operators))),
        identities,
        all_spin_operators,
        all_creation_annihilation_operators,
        operator_list
    ):
        evaluated_contractions.append(contraction_list)

    return evaluated_contractions


def calculate_weights(operator_combination: str) -> float:
    """
    Calculate weights for an operator combination.

    Extracted weight calculation logic from SymGen.py.

    Args:
        operator_combination: The operator combination string

    Returns:
        Calculated weight value
    """
    # Weight from terms
    weight = 1.0
    for operator in operator_combination.split():
        if operator != "-":
            weight = weight * OperatorsDict[operator].get("Weight")

    # Weight from exponentials
    t_count = 0
    left_t_count = 0
    right_t_count = 0

    for operator in operator_combination.split():
        if (operator + " " in Opp or "-" + operator + " " in Opp):
            t_count += 1
        if (operator + " " in Hamiltonian):
            left_t_count = t_count
            t_count = 0
    right_t_count = t_count

    weight *= 1 / (math.factorial(left_t_count))
    weight *= 1 / (math.factorial(right_t_count))

    return weight


def calculate_signs(contraction_list: List[Tuple], operator_combination: str) -> Tuple[int, int]:
    """
    Calculate parity and sign for a contraction.

    Extracted sign/parity calculation logic from SymGen.py.

    Args:
        contraction_list: List of contraction pairs
        operator_combination: The operator combination string

    Returns:
        Tuple of (parity, sign)
    """
    # Flatten a list of contracted indices pairs into a single list
    permutation_list = [element for pair in contraction_list for element in pair]

    # Determine Sign based on parity and whether there is a negative sign in the operator expression
    parity, sign = parity_and_sign(permutation_list, operator_combination)

    return parity, sign


def calculate_weights_and_signs(operator_combination: str, contraction_list: List[Tuple]) -> Tuple[float, int, int]:
    """
    Calculate weights and signs for a contraction.

    Args:
        operator_combination: The operator combination string
        contraction_list: List of contraction pairs

    Returns:
        Tuple of (weight, parity, sign)
    """
    weight = calculate_weights(operator_combination)
    parity, sign = calculate_signs(contraction_list, operator_combination)

    return weight, parity, sign


def combine_expression_level(contraction_dict: Dict[int, Dict], short_dict: Dict[int, Dict],
                           compare_start: int, compare_end: int) -> Dict[int, Dict]:
    """
    Combine isomorphic terms at the expression level.

    Extracted from the first-level combination logic in SymGen.py (lines ~300-330).

    Args:
        contraction_dict: Dictionary of all contractions
        short_dict: Dictionary for combined contractions
        compare_start: Starting index for comparison
        compare_end: Ending index for comparison

    Returns:
        Updated short_dict with combined terms
    """
    ignore_list = []

    for current in range(compare_start, compare_end):
        if current not in ignore_list:
            combined_weight = 1.0 * contraction_dict[current]['Weight']

            for i in range(current + 1, compare_end):
                if i not in ignore_list:
                    if (sorted(contraction_dict[current]['Operators']) ==
                        sorted(contraction_dict[i]['Operators'])):
                        if check_isomorphism(
                            contraction_dict[current]['Graph'],
                            contraction_dict[i]['Graph']
                        ):
                            combined_weight += contraction_dict[i]['Weight']
                            ignore_list.append(i)

            short_dict[current] = copy.deepcopy(contraction_dict[current])
            del short_dict[current]['Weight']
            del short_dict[current]['Sign']
            short_dict[current]['S-Weight'] = combined_weight * contraction_dict[current]['Sign']

    return short_dict


def combine_across_expressions(short_dict: Dict[int, Dict]) -> Dict[int, Dict]:
    """
    Combine isomorphic terms across different expressions.

    Extracted from the final-level combination logic in SymGen.py (lines ~350-380).

    Args:
        short_dict: Dictionary of expression-level combined contractions

    Returns:
        Final dictionary with all combinations applied
    """
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