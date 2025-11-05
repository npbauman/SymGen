"""
Combination Generator Module

This module contains functions for generating operator combinations and applying filters.
Extracted from SymGen.py to improve code organization and readability.

The module handles three main tasks:
1. Exponential expansion of operator lists using commutator orders
2. Generation of all possible operator combinations from input components
3. Application of spin and count filters to eliminate invalid combinations

Example Usage:
    >>> exp1 = generate_exponential_expansions(["T1", "T2"], 2, flip_sign=True)
    >>> combinations = generate_all_combinations(bra, left, exp1, ham, exp2, right, ket, 2)
    >>> filtered, eliminated = apply_spin_filter(combinations)
    >>> validated = apply_count_filter(filtered)

Functions:
    generate_exponential_expansions: Expand operators using commutator rules
    generate_all_combinations: Create all valid operator combinations
    apply_spin_filter: Remove combinations with isolated spin operators
    apply_count_filter: Validate sufficient operators for pairing
"""

from Utilities import expand_exponential
from Operators import OperatorsDict


def generate_exponential_expansions(operator_list, commutator_order, flip_sign=False):
    """
    Generate exponential expansions for left and right exponentials.

    Args:
        operator_list: List of operators to expand
        commutator_order: Order of commutator expansion
        flip_sign: Whether to flip signs for left exponential

    Returns:
        List of expanded exponential terms

    Raises:
        TypeError: If inputs are not of expected types
        ValueError: If commutator_order is invalid
    """
    if not isinstance(operator_list, list):
        raise TypeError(f"operator_list must be a list, got {type(operator_list)}")

    if not isinstance(commutator_order, int):
        raise TypeError(f"commutator_order must be an integer, got {type(commutator_order)}")

    if commutator_order <= 0:
        raise ValueError(f"commutator_order must be positive, got {commutator_order}")

    try:
        return expand_exponential(operator_list, commutator_order, flip_sign)
    except Exception as e:
        raise RuntimeError(f"Failed to expand exponential: {e}")


def generate_all_combinations(bra, left, exp1, hamiltonian, exp2, right, ket, commutator_order):
    """
    Generate all possible operator combinations from the given components.

    Args:
        bra: Bra operators
        left: Left operators
        exp1: Left exponential expansion
        hamiltonian: Hamiltonian operators
        exp2: Right exponential expansion
        right: Right operators
        ket: Ket operators
        commutator_order: Maximum commutator order allowed

    Returns:
        List of all valid operator combinations

    Raises:
        TypeError: If inputs are not lists
        ValueError: If any input list is empty when it shouldn't be
    """
    # Validate input types
    inputs = {
        'bra': bra, 'left': left, 'exp1': exp1, 'hamiltonian': hamiltonian,
        'exp2': exp2, 'right': right, 'ket': ket
    }

    for name, value in inputs.items():
        if not isinstance(value, list):
            raise TypeError(f"{name} must be a list, got {type(value)}")

    # Check for critical empty lists
    if not exp1:
        raise ValueError("Left exponential expansion (exp1) cannot be empty")
    if not exp2:
        raise ValueError("Right exponential expansion (exp2) cannot be empty")
    if not hamiltonian:
        raise ValueError("Hamiltonian operators cannot be empty")

    try:
        operator_combinations = [
            f"{b}{l}{e1.replace('-', '')}{h}{e2.replace('-', '')}{r}{k}" if ((e1 + e2).count("-") % 2) == 0 else
            f"- {b}{l}{e1.replace('-', '')}{h}{e2.replace('-', '')}{r}{k}"
            for b in bra
            for l in left
            for e1 in exp1
            for h in hamiltonian
            for e2 in exp2
            for r in right
            for k in ket
            if ((e1 + e2).count("T") <= commutator_order)
        ]

        return operator_combinations
    except Exception as e:
        raise RuntimeError(f"Failed to generate operator combinations: {e}")

def apply_spin_filter(operator_combinations):
    """
    Apply spin elimination filter to remove combinations with isolated spin operators.

    Eliminates sets that have an operator with only one spin when all other spins
    are the other spin.

    Args:
        operator_combinations: List of operator combination strings

    Returns:
        Tuple of (filtered_combinations, eliminated_combinations)

    Raises:
        TypeError: If operator_combinations is not a list
        ValueError: If operator_combinations is empty
        KeyError: If an operator is not found in OperatorsDict
    """
    if not isinstance(operator_combinations, list):
        raise TypeError(f"operator_combinations must be a list, got {type(operator_combinations)}")

    if not operator_combinations:
        raise ValueError("operator_combinations cannot be empty")

    try:
        eliminated_combinations = []
        filtered_combinations = []

        for operator_combination in operator_combinations:
            operators_with_alpha = 0
            operators_with_beta = 0

            if len(operator_combination.split()) == 1:
                filtered_combinations.append(operator_combination)
            else:
                for operator in operator_combination.split():
                    if "-" not in operator:
                        if operator not in OperatorsDict:
                            raise KeyError(f"Operator '{operator}' not found in OperatorsDict")

                        spins = OperatorsDict[operator].get("Spins").split()
                        if "0" in spins:
                            operators_with_alpha += 1
                        if "1" in spins:
                            operators_with_beta += 1

                # For sets with more than 1 operator, eliminate the set if
                # only one operator has alpha or beta spin
                if operators_with_alpha == 1 or operators_with_beta == 1:
                    eliminated_combinations.append(operator_combination)
                else:
                    filtered_combinations.append(operator_combination)

        return filtered_combinations, eliminated_combinations
    except Exception as e:
        raise RuntimeError(f"Failed to apply spin filter: {e}")


def apply_count_filter(tentative_allowed_combinations):
    """
    Apply count validation filter to ensure sufficient operators for pairing.

    Eliminates sets if there are not enough possible alpha/beta particle/hole/general
    creation/annihilation operators to form pairs.

    Args:
        tentative_allowed_combinations: List of tentatively allowed operator combinations

    Returns:
        List of validated operator combinations

    Raises:
        TypeError: If tentative_allowed_combinations is not a list
        ValueError: If tentative_allowed_combinations is empty
    """
    if not isinstance(tentative_allowed_combinations, list):
        raise TypeError(f"tentative_allowed_combinations must be a list, got {type(tentative_allowed_combinations)}")

    if not tentative_allowed_combinations:
        raise ValueError("tentative_allowed_combinations cannot be empty")

    try:
        validated_combinations = []

        for operator_combination in tentative_allowed_combinations:
            alpha_hole_c, alpha_hole_a, beta_hole_c, beta_hole_a = 0, 0, 0, 0
            alpha_particle_c, alpha_particle_a, beta_particle_c, beta_particle_a = 0, 0, 0, 0
            alpha_gen_c, alpha_gen_a, beta_gen_c, beta_gen_a = 0, 0, 0, 0

            for operator in operator_combination.split():
                if operator == "-":
                    continue

                if operator not in OperatorsDict:
                    raise KeyError(f"Operator '{operator}' not found in OperatorsDict")

                operator_spins = OperatorsDict[operator].get("Spins").split()
                operator_creation_annihilation = OperatorsDict[operator].get("C A").split()

                for i in range(len(operator_creation_annihilation)):
                    if operator_spins[i] == "0":
                        if operator_creation_annihilation[i] == "H+":
                            alpha_hole_c += 1
                        elif operator_creation_annihilation[i] == "H":
                            alpha_hole_a += 1
                        elif operator_creation_annihilation[i] == "P+":
                            alpha_particle_c += 1
                        elif operator_creation_annihilation[i] == "P":
                            alpha_particle_a += 1
                        elif operator_creation_annihilation[i] == "G+":
                            alpha_gen_c += 1
                        elif operator_creation_annihilation[i] == "G":
                            alpha_gen_a += 1
                    elif operator_spins[i] == "1":
                        if operator_creation_annihilation[i] == "H+":
                            beta_hole_c += 1
                        elif operator_creation_annihilation[i] == "H":
                            beta_hole_a += 1
                        elif operator_creation_annihilation[i] == "P+":
                            beta_particle_c += 1
                        elif operator_creation_annihilation[i] == "P":
                            beta_particle_a += 1
                        elif operator_creation_annihilation[i] == "G+":
                            beta_gen_c += 1
                        elif operator_creation_annihilation[i] == "G":
                            beta_gen_a += 1

            # Check if there are sufficient operators for pairing
            if (
                alpha_hole_c > (alpha_hole_a + alpha_gen_a)
                or alpha_particle_c > (alpha_particle_a + alpha_gen_a)
                or alpha_hole_a > (alpha_hole_c + alpha_gen_c)
                or alpha_particle_a > (alpha_particle_c + alpha_gen_c)
                or beta_hole_c > (beta_hole_a + beta_gen_a)
                or beta_particle_c > (beta_particle_a + beta_gen_a)
                or beta_hole_a > (beta_hole_c + beta_gen_c)
                or beta_particle_a > (beta_particle_c + beta_gen_c)
            ):
                continue

            validated_combinations.append(operator_combination)

        return validated_combinations
    except Exception as e:
        raise RuntimeError(f"Failed to apply count filter: {e}")