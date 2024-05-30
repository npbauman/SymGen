from sympy.combinatorics.permutations import Permutation

#########################################################
# LIST OF UTILITIES
#-------------------------------------------------------#
# remove_last_star
#   |->  Removes last multiplication star when formatting the final product
#
# find_tuple_with_value
#   |-> returns tuple in a list with a given value
#
# 



def remove_last_star(string):
    # Find the index of the last non-whitespace character
    last_non_whitespace_index = None
    for i in range(len(string) - 1, -1, -1):
        if string[i] != ' ':
            last_non_whitespace_index = i
            break

    # Check if the last non-whitespace character is "*"
    if last_non_whitespace_index is not None and string[last_non_whitespace_index] == '*':
        # Remove the "*" character
        string = string[:last_non_whitespace_index] + string[last_non_whitespace_index + 1:]

    return string



def find_tuple_with_value(lst, value):
    for tuple in lst:
        if value in tuple:
            return tuple
    return None  # Return None if the value is not found in any tuple



def reorder_paths(path, index_path):
    index_order = []
    for position in index_path:
        index_order.append(position[0])
    for _ in range(index_order.index(min(index_order))):
        path.append(path[0])
        path.pop(0)
        index_path.append(index_path[0])
        index_path.pop(0)



def parity_and_sign(permutation_list, op_set):
    p = Permutation(permutation_list)
    parity = p.parity()
    
    # Final sign depends on the sign of the expression and the parity
    sign = 1 if (parity == 1 and "-" in op_set) or (parity == 0 and "-" not in op_set) else -1

    # DEBUG   
    # print(permutation_list)
    # print("Sign =", sign, "Parity =", parity)

    return sign


def expand_exponential(operator_list, commutator_order, flip_sign=False):
# FORM THE EXPANSIONS OF THE LEFT AND RIGHT EXPONENTIALS
# ------------------------------------------------------
# Only gives the combination of terms, not the weight. 

    expanded_list = [""]
    for _ in range(commutator_order):
        new_expanded_list = [""]
        for term in expanded_list:
            for o in operator_list:
                if flip_sign:
                    # Flip the sign of operators
                    o = o[1:] if o.startswith("-") else "-" + o
                # Determine the sign based on the count of "-" in the new term
                sign = "" if (term + o).count("-") % 2 == 0 else "-"
                # Append the new term with adjusted sign and without "-" in the operands
                new_expanded_list.append(sign + term.replace('-', '') + o.replace('-', ''))
        expanded_list = new_expanded_list
    return expanded_list