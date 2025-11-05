"""
Basic input validation utilities.

This module provides functions for validating inputs to the SymGen system.
It ensures that all required variables from Input.py are properly defined
and that all operators exist in the OperatorsDict.

The validation process includes:
1. Type checking for all input variables
2. Existence checking for all operators in OperatorsDict
3. Range validation for numerical parameters
4. Comprehensive error reporting with helpful messages

Example Usage:
    >>> if validate_all_inputs():
    ...     print("All inputs are valid")
    >>> errors = validate_input_variables()
    >>> missing = validate_operator_existence()
    >>> handle_processing_error("Step 1", RuntimeError("Test error"))

Functions:
    validate_input_variables: Check types and structure of Input.py variables
    validate_operator_existence: Verify all operators exist in OperatorsDict
    validate_all_inputs: Perform complete input validation
    handle_processing_error: Handle and format processing errors
    validate_processing_step_inputs: Validate inputs for specific processing steps
"""

from typing import List


def validate_input_variables() -> List[str]:
    """
    Validate that Input.py variables exist and are correct types.

    Returns:
        List of validation error messages (empty if all valid)
    """
    errors = []

    try:
        from Input import Bra, Left, Right, Ket, Hamiltonian, Opp, Comm_order
    except ImportError as e:
        errors.append(f"Failed to import Input.py variables: {e}")
        return errors

    # Validate that all required variables exist and are correct types
    required_list_vars = {
        'Bra': Bra,
        'Left': Left,
        'Right': Right,
        'Ket': Ket,
        'Hamiltonian': Hamiltonian,
        'Opp': Opp
    }

    # Check list variables
    for var_name, var_value in required_list_vars.items():
        if not isinstance(var_value, list):
            errors.append(f"Variable '{var_name}' must be a list, got {type(var_value).__name__}")
        else:
            # Check that all elements in the list are strings
            for i, item in enumerate(var_value):
                if not isinstance(item, str):
                    errors.append(f"Variable '{var_name}[{i}]' must be a string, got {type(item).__name__}")

    # Check Comm_order variable
    if not isinstance(Comm_order, int):
        errors.append(f"Variable 'Comm_order' must be an integer, got {type(Comm_order).__name__}")
    elif Comm_order <= 0:
        errors.append(f"Variable 'Comm_order' must be positive, got {Comm_order}")
    elif Comm_order > 10:  # Reasonable upper limit
        errors.append(f"Variable 'Comm_order' seems too large ({Comm_order}), consider reducing for performance")

    return errors


def validate_operator_existence() -> List[str]:
    """
    Check that all operators in Input.py exist in OperatorsDict.

    Returns:
        List of validation error messages (empty if all valid)
    """
    errors = []

    try:
        from Input import Bra, Left, Right, Ket, Hamiltonian, Opp
        from Operators import OperatorsDict
    except ImportError as e:
        errors.append(f"Failed to import required modules: {e}")
        return errors

    # Collect all unique operators from Input.py
    all_operators = set()
    operator_sources = {
        'Bra': Bra,
        'Left': Left,
        'Right': Right,
        'Ket': Ket,
        'Hamiltonian': Hamiltonian,
        'Opp': Opp
    }

    for source_name, operator_list in operator_sources.items():
        if not isinstance(operator_list, list):
            continue  # Skip if not a list (error will be caught by validate_input_variables)

        for operator in operator_list:
            if isinstance(operator, str) and operator.strip():
                # Clean operator name (remove spaces)
                clean_operator = operator.strip()
                all_operators.add((clean_operator, source_name))

    # Check if operators exist in OperatorsDict
    missing_operators = []
    for operator, source in all_operators:
        if operator not in OperatorsDict:
            missing_operators.append(f"'{operator}' (from {source})")

    if missing_operators:
        available_ops = list(OperatorsDict.keys())
        errors.append(
            f"Missing operators in OperatorsDict: {', '.join(missing_operators)}. "
            f"Available operators include: {', '.join(available_ops[:10])}..."
        )

    return errors


def validate_all_inputs() -> bool:
    """
    Perform complete input validation.
    
    Returns:
        True if all validations pass, False otherwise
    """
    print("Validating input variables...")
    
    # Validate variable types and structure
    type_errors = validate_input_variables()
    if type_errors:
        print("INPUT VALIDATION ERRORS:")
        for error in type_errors:
            print(f"  - {error}")
        return False
    
    print("Input variable types validated successfully.")
    
    # Validate operator existence
    print("Validating operator existence...")
    operator_errors = validate_operator_existence()
    if operator_errors:
        print("OPERATOR VALIDATION ERRORS:")
        for error in operator_errors:
            print(f"  - {error}")
        return False
    
    print("All operators validated successfully.")
    return True


def handle_processing_error(step_name: str, error: Exception, critical: bool = True) -> None:
    """
    Handle processing errors with descriptive messages.

    Args:
        step_name: Name of the processing step that failed
        error: The exception that occurred
        critical: Whether this error should stop execution
    """
    error_type = type(error).__name__
    print(f"\n❌ ERROR in {step_name}:")
    print(f"   Error Type: {error_type}")
    print(f"   Error Message: {str(error)}")

    if critical:
        print(f"   This is a critical error. Processing cannot continue.")
        print(f"   Please check your input configuration and try again.")
    else:
        print(f"   This is a non-critical error. Processing will continue.")


def validate_processing_step_inputs(step_name: str, **kwargs) -> List[str]:
    """
    Validate inputs for processing steps.

    Args:
        step_name: Name of the processing step
        **kwargs: Input parameters to validate

    Returns:
        List of validation error messages
    """
    errors = []

    for param_name, param_value in kwargs.items():
        if param_value is None:
            errors.append(f"{step_name}: Parameter '{param_name}' cannot be None")
        elif isinstance(param_value, list) and len(param_value) == 0:
            errors.append(f"{step_name}: Parameter '{param_name}' cannot be empty list")

    return errors