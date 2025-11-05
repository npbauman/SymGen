"""
Simple OperatorManager wrapper around OperatorsDict with basic validation.

This module provides a simple wrapper around the OperatorsDict from Operators.py
to add basic error checking and validation for operator access. It serves as a
safe interface for accessing operator properties and validating operator sets.

Example Usage:
    >>> manager = OperatorManager()
    >>> props = manager.get_operator_properties("T1")
    >>> is_valid = manager.validate_operator_set(["T1", "T2"])
    >>> missing = manager.get_missing_operators(["T1", "InvalidOp"])

Classes:
    OperatorManager: Main wrapper class for operator validation and access
"""

from typing import Dict, List, Any
from Operators import OperatorsDict


class OperatorManager:
    """Simple wrapper around OperatorsDict with error checking."""
    def __init__(self):
        """Initialize the OperatorManager with the global OperatorsDict."""
        self.operators_dict = OperatorsDict
    def get_operator_properties(self, operator_name: str) -> Dict[str, Any]:
        """
        Get operator properties with validation.

        Args:
            operator_name: Name of the operator to retrieve

        Returns:
            Dictionary containing operator properties

        Raises:
            ValueError: If operator_name is not found in OperatorsDict
            TypeError: If operator_name is not a string
        """
        if not isinstance(operator_name, str):
            raise TypeError(f"Operator name must be a string, got {type(operator_name)}")
        if operator_name not in self.operators_dict:
            available_operators = list(self.operators_dict.keys())
            raise ValueError(
                f"Operator '{operator_name}' not found in OperatorsDict. "
                f"Available operators: {available_operators[:10]}..."
            )
        return self.operators_dict[operator_name]
    def validate_operator_set(self, operators: List[str]) -> bool:
        """
        Check if all operators in the list exist in OperatorsDict.

        Args:
            operators: List of operator names to validate

        Returns:
            True if all operators exist, False otherwise

        Raises:
            TypeError: If operators is not a list or contains non-string elements
        """
        if not isinstance(operators, list):
            raise TypeError(f"Operators must be a list, got {type(operators)}")

        for operator in operators:
            if not isinstance(operator, str):
                raise TypeError(f"All operator names must be strings, got {type(operator)}")

            if operator not in self.operators_dict:
                return False

        return True
    
    def get_missing_operators(self, operators: List[str]) -> List[str]:
        """
        Get list of operators that don't exist in OperatorsDict.

        Args:
            operators: List of operator names to check

        Returns:
            List of operator names that are missing from OperatorsDict
        """
        if not isinstance(operators, list):
            raise TypeError(f"Operators must be a list, got {type(operators)}")

        missing = []
        for operator in operators:
            if not isinstance(operator, str):
                raise TypeError(f"All operator names must be strings, got {type(operator)}")

            if operator not in self.operators_dict:
                missing.append(operator)

        return missing
    
    def get_available_operators(self) -> List[str]:
        """
        Get list of all available operator names.

        Returns:
            List of all operator names in OperatorsDict
        """
        return list(self.operators_dict.keys())