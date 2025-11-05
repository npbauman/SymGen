"""
Refactored main workflow for the SymGen equation generation system.

This module implements the same workflow as SymGen.py but with extracted functions
and improved variable names for better readability and maintainability.

The main workflow consists of 8 steps:
1. Input validation and setup
2. Exponential expansion generation
3. Operator combination generation
4. Spin filter application
5. Count filter application
6. Contraction processing and evaluation
7. Cross-expression combination
8. Final equation generation and output

Example Usage:
    Run the complete workflow:
    >>> python main.py
    
    Or import and run programmatically:
    >>> from main import main
    >>> main()

The workflow preserves all functionality from the original SymGen.py while
providing better error handling, progress reporting, and code organization.

Functions:
    main: Execute the complete SymGen workflow with error handling
"""

import time
import sys

# Import extracted functions from core modules
from core.combination_generator import (
    generate_exponential_expansions,
    generate_all_combinations,
    apply_spin_filter,
    apply_count_filter
)
from core.contraction_engine import (
    process_operator_combinations,
    combine_across_expressions
)
from core.equation_builder import (
    generate_final_equations,
    format_equation_output,
    print_statistics
)

# Import validation utilities
from utils.validation import validate_all_inputs, handle_processing_error

# Import original modules and data
from Input import Bra, Left, Right, Ket, Hamiltonian, Opp, Comm_order
from Strings import operator_mapping
from Operators import OperatorsDict


def main():
    """
    Main entry point that executes the complete SymGen workflow.
    
    This function follows the same sequence as SymGen.py but uses extracted functions
    with improved variable names for better readability.
    """
    try:
        # Validate all inputs before processing
        if not validate_all_inputs():
            print("\nInput validation failed. Please fix the errors above and try again.")
            sys.exit(1)
        
        print("\n" + "="*50)
        print("INPUT VALIDATION PASSED - STARTING PROCESSING")
        print("="*50)
        
        # Print input information
        print("              INPUT")
        print("-" * 35)
        print("        Bra = ", Bra)
        print("        Ket = ", Ket)
        print("       Left = ", Left)
        print("      Right = ", Right)
        print("Hamiltonian = ", Hamiltonian)
        print("        Opp = ", Opp)
        print(" Comm_order = ", Comm_order)
        print("-" * 35 + "\n")

        # Start timing
        tic = time.perf_counter()
        print_opt = "verbose"  # Can be changed to "verbose" for detailed output

        # Step 1: Generate exponential expansions
        try:
            print("Step 1/8: Generating exponential expansions...")
            left_exponential = generate_exponential_expansions(Opp, Comm_order, flip_sign=True)
            right_exponential = generate_exponential_expansions(Opp, Comm_order)

            if print_opt == "verbose":
                print("Left Exponential Expanded: ", left_exponential)
                print("Right Exponential Expanded: ", right_exponential)
            print("✓ Exponential expansions generated successfully")
        except Exception as e:
            raise RuntimeError(f"Failed to generate exponential expansions: {e}")

        # Step 2: Generate all operator combinations
        try:
            print("\nStep 2/8: Generating all operator combinations...")
            operator_combinations = generate_all_combinations(
                Bra, Left, left_exponential, Hamiltonian, right_exponential, Right, Ket, Comm_order
            )

            if print_opt == "verbose":
                print("\nALL POSSIBLE COMBINATIONS")
                print(*operator_combinations, sep="\n")
                print("TOTAL POSSIBLE COMBINATIONS = ", len(operator_combinations))
            print(f"✓ Generated {len(operator_combinations)} operator combinations")
        except Exception as e:
            raise RuntimeError(f"Failed to generate operator combinations: {e}")

        # Step 3: Apply spin filter
        try:
            print("\nStep 3/8: Applying spin filter...")
            print("ELIMINATING SETS THAT HAVE AN OPERATOR WITH ONLY ONE SPIN WHEN ALL OTHER SPINS ARE THE OTHER SPIN.")
            filtered_combinations, eliminated_combinations = apply_spin_filter(operator_combinations)

            print("ELIMINATED {0} COMBINATIONS / {1} COMBINATIONS REMAINING".format(
                len(eliminated_combinations), len(filtered_combinations)
            ))
            print("✓ Spin filter applied successfully")
        except Exception as e:
            raise RuntimeError(f"Failed to apply spin filter: {e}")

        # Step 4: Apply count filter
        try:
            print("\nStep 4/8: Applying count filter...")
            print("ELIMINATING SETS IF THERE IS NOT ENOUGH POSSIBLE ALPHA/BETA P/H/G C/A OPERATORS TO FORM PAIRS.")
            validated_combinations = apply_count_filter(filtered_combinations)

            print("ELIMINATED {0} COMBINATIONS / {1} COMBINATIONS REMAINING".format(
                len(filtered_combinations) - len(validated_combinations), len(validated_combinations)
            ))
            print("✓ Count filter applied successfully")
        except Exception as e:
            raise RuntimeError(f"Failed to apply count filter: {e}")

        toc = time.perf_counter()
        print(f"\n⏱ Filtering completed in {toc - tic:0.4f} seconds\n")
        tic = toc

        # Step 5: Process operator combinations and evaluate contractions
        try:
            print("Step 5/8: Processing operator combinations and evaluating contractions...")
            print("EVALUATING THE FOLLOWING:")
            for operator_combination in validated_combinations:
                print(validated_combinations.index(operator_combination), operator_combination)
            print("")

            contraction_dict, short_dict = process_operator_combinations(validated_combinations, print_opt)

            if print_opt == "verbose":
                print("Full Dictionary")
                for dict_key in contraction_dict:
                    print(dict_key, contraction_dict[dict_key])

            print("Shorter Dictionary")
            for dict_key in short_dict:
                print(dict_key, short_dict[dict_key])
            print("✓ Operator combinations processed successfully")
        except Exception as e:
            raise RuntimeError(f"Failed to process operator combinations: {e}")

        # Step 6: Combine across expressions (final level combination)
        try:
            print("\nStep 6/8: Combining across expressions...")
            final_dict = combine_across_expressions(short_dict)
            print("✓ Expression combination completed successfully")
        except Exception as e:
            raise RuntimeError(f"Failed to combine across expressions: {e}")

        # Step 7: Print statistics
        try:
            print("\nStep 7/8: Generating statistics...")
            print_statistics(final_dict)
            print("✓ Statistics generated successfully")
        except Exception as e:
            print(f"Warning: Failed to print statistics: {e}")
            # Continue execution as this is not critical

        # Step 8: Generate and format final equations
        try:
            print("\nStep 8/8: Generating and formatting final equations...")
            final_equations = generate_final_equations(
                final_dict, operator_mapping, OperatorsDict, print_opt
            )

            format_equation_output(final_equations)
            print("✓ Final equations generated and formatted successfully")
        except Exception as e:
            raise RuntimeError(f"Failed to generate final equations: {e}")

        # Final timing
        toc = time.perf_counter()
        print(f"\n🎉 PROCESSING COMPLETED SUCCESSFULLY!")
        print(f"⏱ Total execution time: {toc - tic:0.4f} seconds")

    except KeyboardInterrupt:
        print("\n\n⚠️  Processing interrupted by user (Ctrl+C)")
        print("Exiting gracefully...")
        sys.exit(0)
    except RuntimeError as error:
        handle_processing_error("Main Processing", error, critical=True)
        sys.exit(1)
    except Exception as error:
        handle_processing_error("Unexpected Error", error, critical=True)
        print("\nThis appears to be an unexpected error. Please report this issue.")
        sys.exit(1)


if __name__ == "__main__":
    main()