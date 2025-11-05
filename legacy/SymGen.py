# TODO: put in contraction logic if you have multiple operators with general indices.

# import json
import jsbeautifier
import time
import math
import sys
import copy
import networkx as nx
# from fractions import Fraction
from Operators import *
from Utilities import *
from Graphs import *
from ContractionRules import *
from Input import *
from Strings import *

options = jsbeautifier.default_options()
options.indent_size = 2

tic = time.perf_counter()
# Print_opt can be "verbose".
print_opt = "erbose"

# remove_disconnected = bool(True)

# Input operators are declared in Input.py

# Generate the expanded lists for the left and right exponentials
exp1 = expand_exponential(Opp, Comm_order, flip_sign=True)
exp2 = expand_exponential(Opp, Comm_order)

if print_opt == "verbose":
    print("Left Exponential Expanded: ", exp1)
    print("Right Exponential Expanded: ", exp2)

# Form all combinations
operator_combs = [
    f"{b}{l}{e1.replace('-', '')}{h}{e2.replace('-', '')}{r}{k}" if ((e1 + e2).count("-") % 2) == 0 else
    f"- {b}{l}{e1.replace('-', '')}{h}{e2.replace('-', '')}{r}{k}"
    for b in Bra
    for l in Left
    for e1 in exp1
    for h in Hamiltonian
    for e2 in exp2
    for r in Right
    for k in Ket
    if ((e1 + e2).count("T") <= Comm_order)
]

if print_opt == "verbose":
    print("\nALL POSSIBLE COMBINATIONS")
    print(*operator_combs, sep = "\n")
    print("TOTAL POSSIBLE COMBINATIONS = ", len(operator_combs))

del exp1, exp2, Comm_order

# Preliminary eliminations
print("\nELIMINATING SETS THAT HAVE AN OPERATOR WITH ONLY ONE SPIN WHEN ALL OTHER SPINS ARE THE OTHER SPIN.")

eliminated_set = []
tentative_allowed_set = []

for op_set in operator_combs[:]:
    operators_with_alpha = 0
    operators_with_beta = 0

    if len(op_set.split()) == 1:
        tentative_allowed_set.append(op_set)
    else:
        for operator in op_set.split():
            if "-" not in operator:

                # CHECK THE SPINS OF ALL OPERATORS AND COUNT HOW MANY HAVE
                # AN ALPHA SPIN INDEX AND HOW MANY HAVE A BETA SPIN INDEX.
                spins = OperatorsDict[operator].get("Spins").split()
                if "0" in spins:
                    operators_with_alpha += 1
                if "1" in spins:
                    operators_with_beta += 1

        # FOR SETS WITH MORE THAN 1 OPERATOR, ELIMINATE THE SET IF
        # ONLY ONE OPERATOR HAS ALPHA OR BETA SPIN.
        if operators_with_alpha == 1 or operators_with_beta == 1:
            eliminated_set.append(op_set)
        else:
            tentative_allowed_set.append(op_set)

print("ELIMINATED {0} COMBINATIONS / {1} COMBINATIONS REMAINING\n".format(len(eliminated_set), len(tentative_allowed_set)))

# if print_opt == "verbose":
# print("\nTENTATIVE ALLOWED SETS")
# print(*tentative_allowed_set, sep = "\n")
# print("\nELIMINATED SETS")
# print(*eliminated_set, sep = "\n")

del operator_combs, op_set, operators_with_alpha, operators_with_beta, operator, eliminated_set

print("ELIMINATING SETS IF THERE IS NOT ENOUGH POSSIBLE ALPHA/BETA P/H/G C/A OPERATORS TO FORM PAIRS.")

final_allowed_set = []
for op_set in tentative_allowed_set[:]:
    alpha_hole_c, alpha_hole_a, beta_hole_c, beta_hole_a = 0, 0, 0, 0
    alpha_particle_c, alpha_particle_a, beta_particle_c, beta_particle_a = 0, 0, 0, 0
    alpha_gen_c, alpha_gen_a, beta_gen_c, beta_gen_a = 0, 0, 0, 0

    for operator in op_set.split():
        if operator == "-":
            continue

        Operator_spins = OperatorsDict[operator].get("Spins").split()
        Operator_C_A = OperatorsDict[operator].get("C A").split()

        for i in range(len(Operator_C_A)):
            if Operator_spins[i] == "0":
                if Operator_C_A[i] == "H+":
                    alpha_hole_c += 1
                elif Operator_C_A[i] == "H":
                    alpha_hole_a += 1
                elif Operator_C_A[i] == "P+":
                    alpha_particle_c += 1
                elif Operator_C_A[i] == "P":
                    alpha_particle_a += 1
                elif Operator_C_A[i] == "G+":
                    alpha_gen_c += 1
                elif Operator_C_A[i] == "G":
                    alpha_gen_a += 1
            elif Operator_spins[i] == "1":
                if Operator_C_A[i] == "H+":
                    beta_hole_c += 1
                elif Operator_C_A[i] == "H":
                    beta_hole_a += 1
                elif Operator_C_A[i] == "P+":
                    beta_particle_c += 1
                elif Operator_C_A[i] == "P":
                    beta_particle_a += 1
                elif Operator_C_A[i] == "G+":
                    beta_gen_c += 1
                elif Operator_C_A[i] == "G":
                    beta_gen_a += 1

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

    final_allowed_set.append(op_set)

print(
    "ELIMINATED {0} COMBINATIONS / {1} COMBINATIONS REMAINING\n".format(
        len(tentative_allowed_set) - len(final_allowed_set), len(final_allowed_set)
    )
)

# Clean up
del alpha_hole_c, alpha_hole_a, beta_hole_c, beta_hole_a
del alpha_particle_c, alpha_particle_a, beta_particle_c, beta_particle_a
del alpha_gen_c, alpha_gen_a, beta_gen_c, beta_gen_a
del op_set, operator, Operator_spins, Operator_C_A, i, tentative_allowed_set

toc = time.perf_counter()
print(f"Step Time = {toc - tic:0.4f} seconds\n")
tic = toc

print("EVALUATING THE FOLLOWING:")
for op_set in final_allowed_set:
    print(final_allowed_set.index(op_set), op_set)
print("")

# collective = []
ContractionDict = {}
ShortDict = {}
count = 0
for op_set in final_allowed_set:

    # Initialize lists for identities, CA operators, spin operators, and the operator list
    all_CA_operators = []
    all_spin_operators = []
    identities = []
    operator_list = []

    # Initialize the identity counter
    identity = 1

    # Iterate over each operator in the split 'op_set'
    for operator in op_set.split():
        if operator != "-":
            # Retrieve CA and Spin operators for the current valid operator
            ca_operators = OperatorsDict[operator].get("C A", "").split()
            spin_operators = OperatorsDict[operator].get("Spins", "").split()

            # Extend the lists with CA and Spin operators
            all_CA_operators.extend(ca_operators)
            all_spin_operators.extend(spin_operators)

            # Append the current identity to the identities list, once for each Spin operator
            identities.extend([identity] * len(spin_operators))

            # Append the current operator to the operator list
            operator_list.append(operator)

            # Increment the identity counter only after processing a valid operator
            identity += 1

    evaluated_contractions = []
    
    for contraction_list in all_pairs(list(range(0, len(all_CA_operators))),identities,all_spin_operators,all_CA_operators,operator_list):
        evaluated_contractions.append(contraction_list)

    del operator_list

    if evaluated_contractions:
        if print_opt == "verbose":
            print(op_set)
            print("CA Operators: ", all_CA_operators)
            print("Spin Operators: ", all_spin_operators)
            print("Identity Indices: ", identities)
            print("Evaluated Contractions: ", *
                  evaluated_contractions, sep="\n")
            print("-"*40+"\n")
    else:
        if print_opt == "verbose":
            print(op_set," WAS ELIMINATED BECAUSE NO VIABLE SET OF CONTRACTIONS WERE FOUND\n")
            print("-"*40+"\n")

    compare_start = count
    for contraction_list in evaluated_contractions:
        ContractionDict[count]={}
        # count = str(evaluated_contractions.index(contraction_list))

        ContractionDict[count]['Term'] = op_set
        if "-" in op_set.split():
            ContractionDict[count]['Operators'] = op_set.split()[1:]
        else:
            ContractionDict[count]['Operators'] = op_set.split()

        ContractionDict[count]['CA'] = all_CA_operators
        ContractionDict[count]['Spins'] = all_spin_operators
        ContractionDict[count]['Identities'] = identities
        # ContractionDict[count]['Contractions'] = contraction_list

        # Weight From Terms
        weight = 1.0
        for operator in op_set.split():
            if operator != "-":
                weight = weight * OperatorsDict[operator].get("Weight")
        del operator

        # Weight from exponentials
        t_count = 0
        for operator in op_set.split():
            if (operator+" " in Opp or "-"+operator+" " in Opp):
                t_count += 1
            if (operator+" " in Hamiltonian):
                left_t_count = t_count
                t_count = 0
        right_t_count = t_count
        weight *= 1/(math.factorial(left_t_count))
        weight *= 1/(math.factorial(right_t_count))
        del operator, t_count, left_t_count, right_t_count

        ContractionDict[count]['Weight'] = weight #Weight can be better defined depending on multiple exponents or explicit weights from the user.

        # Flatten a list of contracted indices pairs into a single list
        permutation_list = [element for pair in contraction_list for element in pair]

        # Determine Sign based on parity and whether there is a negative sign in the operator expression.
        ContractionDict[count]['Parity'], ContractionDict[count]['Sign'] = parity_and_sign(permutation_list,op_set)

        del permutation_list
    
        # Contractions are reordered such that creation operators are listed before annihilation.
        # This is for determing paths, which go from creation operators to annihilation operators.
        for contraction in contraction_list:
            if ("+" not in all_CA_operators[contraction[0]]):
                contraction_list[contraction_list.index(contraction)] = (
                    contraction[1], contraction[0])
        del contraction

        ContractionDict[count]['Oriented Contractions'] = list(contraction_list)

        # Build the graph.
        ContractionDict[count]['Graph'] = build_graph(ContractionDict[count], OperatorsDict)

        # Determine if Graph is Disconnected.
        ContractionDict[count]['Connected'] = check_if_connected(ContractionDict[count]['Graph'], OperatorsDict)

        # Increment count
        count += 1

    compare_end = count

    # The first level of combination is at the expresion level
    ignore_list = []
    for current in range(compare_start, compare_end):
        if current not in ignore_list:
            combined_weight =  1.0 * ContractionDict[current]['Weight']
            for i in range(current+1, compare_end):
                if i not in ignore_list:
                    if(sorted(ContractionDict[current]['Operators']) == sorted(ContractionDict[i]['Operators'])):
                        if check_isomorphism(ContractionDict[current]['Graph'],ContractionDict[i]['Graph']):
                            combined_weight += ContractionDict[i]['Weight']
                            ignore_list.append(i)

            ShortDict[current] = copy.deepcopy(ContractionDict[current])
            del ShortDict[current]['Weight']
            del ShortDict[current]['Sign']
            ShortDict[current]['S-Weight'] = combined_weight * ContractionDict[current]['Sign']

    toc = time.perf_counter()
    print(f"{final_allowed_set.index(op_set)+1}/{len(final_allowed_set)} Evaluating {op_set} = {toc - tic:0.4f} seconds")
    sys.stdout.flush()
    tic = toc

if print_opt == "verbose":
    print("Full Dictionary")
    for Dict1 in ContractionDict:
        print(Dict1, ContractionDict[Dict1])

print("Shorter Dictionary")
for Dict1 in ShortDict:
    print(Dict1,ShortDict[Dict1])

# There is a final level of combination across expressions
FinalDict={}
ignore_list = []
for key_1, value_1 in ShortDict.items():
    if key_1 not in ignore_list:
        combined_weight =  1.0 * value_1['S-Weight']

        for key_2, value_2 in ShortDict.items():
            if key_2 > key_1 and key_2 not in ignore_list:
                if(sorted(value_1['Operators']) == sorted(value_2['Operators'])):
                    if check_isomorphism(value_1['Graph'],value_2['Graph']):
                        if value_1['Parity'] == value_2['Parity']:
                            combined_weight += value_2['S-Weight']
                        else:
                            combined_weight -= value_2['S-Weight']

                        ignore_list.append(key_2)

        FinalDict[key_1] = copy.deepcopy(ShortDict[key_1])
        FinalDict[key_1]['S-Weight'] = round(combined_weight,9)

print("")
count = sum(1 for value in FinalDict.values() if abs(value['S-Weight']) == 0.0 and not value['Connected'])
print(count, "vanishing disconnected terms.")
count = sum(1 for value in FinalDict.values() if abs(value['S-Weight']) != 0.0 and not value['Connected'])
print(count, "nonvanishing disconnected terms.")
count = sum(1 for value in FinalDict.values() if abs(value['S-Weight']) == 0.0 and value['Connected'])
print(count, "vanishing connected terms.")
count = sum(1 for value in FinalDict.values() if abs(value['S-Weight']) != 0.0 and value['Connected'])
print(count, "nonvanishing connected terms.")
for value in FinalDict.values():
    if abs(value['S-Weight']) != 0.0 and value['Connected']: 
        print(value)

Final_Equations = []
for key, value in FinalDict.items():
    if print_opt == "verbose":
        print("\n", key, value)

    sweight = value.get("S-Weight")
    eqn_str = process_weight(sweight)

    if eqn_str:
        identities = value["Identities"]
        operators = value["Operators"]
        contractions = value["Oriented Contractions"]
        ca_values = value["CA"]

        fixed_positions, free_positions = determine_positions(identities, operators, OperatorsDict)
        labels = label_positions(identities, contractions, ca_values, operators, OperatorsDict)

        Op_CA_list = [[] for x in range(len(value["Operators"]))]
        for position in range(len(labels)):

            identity = value["Identities"][position]
            Op_CA_list[identity-1].append(labels[position])

        length = len(Op_CA_list)
        for _ in range(length):
            Operator = value["Operators"][_]
            op_str = ""
            flipsign = False

            if Operator not in operator_mapping:
                if not OperatorsDict[Operator].get("Fixed"):
                    print("{} is not programmed".format(Operator))
            else:
                labels = Op_CA_list[_]
                key = tuple(label[0] for label in labels)
                op_template = operator_mapping[Operator].get(key)
                flipsign =  op_template[1]
                if op_template:
                    op_str = op_template[0].format(*labels)
                    if _ != length-1:
                        eqn_str +=  op_str + " * "
                    else:
                        eqn_str +=  op_str

                    if flipsign:
                        if "-" in eqn_str:
                            eqn_str = eqn_str.replace("-","")
                        elif "-" not in eqn_str:
                            eqn_str = "-"+eqn_str 

                else:
                    print(f"No template found for {key}")
        
        Final_Equations.append(eqn_str)
        
        if print_opt == "verbose":
            print(eqn_str)
        
print("\nFINAL EQUATIONS ")
for equation in Final_Equations:
    print(equation)
