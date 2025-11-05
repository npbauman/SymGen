"""
Simple data models for the SymGen equation generation system.

This module defines basic data structures used in the refactored system.
Most data will continue to use the same dictionary structures as the original SymGen.py.
"""

from typing import Dict, List, Any

# Type aliases for clarity
OperatorDict = Dict[str, Any]  # Same as OperatorsDict entries
ContractionDict = Dict[int, Dict[str, Any]]  # Same as original ContractionDict
EquationDict = Dict[int, Dict[str, Any]]  # Same as original ShortDict/FinalDict