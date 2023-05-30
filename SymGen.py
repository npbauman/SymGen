# %%
# TODO: put in contraction logic if you have multiple operators with general indices.
import json
import jsbeautifier
options = jsbeautifier.default_options()
options.indent_size = 2

# Print_opt can be "verbose".
print_opt = "erbose"

# remove_disconnected = bool(True)

# %%
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! NEED TO DEFINE AN IDENTITY OPERATOR "I" for computing weights from exponentials!!!!
E_O_V__ADict = {
    "C A": "H+ P ",
    "Spins": "0 0 ",
    "Weight": 1.0,
    "Fixed": bool(True),
    "Particle": ["1", "1"]
}

E_O_V__BDict = {
    "C A": "H+ P ",
    "Spins": "1 1 ",
    "Weight": 1.0,
    "Fixed": bool(True),
    "Particle": ["1", "1"]
}

E_OO_VV__AADict = {
    "C A": "H+ P H+ P ",
    "Spins": "0 0 0 0 ",
    "Weight": 1.0,
    "Fixed": bool(True),
    "Particle": ["1", "1", "2", "2"]
}

E_OO_VV__ABDict = {
    "C A": "H+ P H+ P ",
    "Spins": "0 0 1 1 ",
    "Weight": 1.0,
    "Fixed": bool(True),
    "Particle": ["1", "1", "2", "2"]
}

E_OO_VV__BBDict = {
    "C A": "H+ P H+ P ",
    "Spins": "1 1 1 1 ",
    "Weight": 1.0,
    "Fixed": bool(True),
    "Particle": ["1", "1", "2", "2"]
}

E_OOO_VVV__AAADict = {
    "C A": "H+ P H+ P H+ P ",
    "Spins": "0 0 0 0 0 0 ",
    "Weight": 1.0,
    "Fixed": bool(True),
    "Particle": ["1", "1", "2", "2", "3", "3"]
}

E_OOO_VVV__AABDict = {
    "C A": "H+ P H+ P H+ P ",
    "Spins": "0 0 0 0 1 1 ",
    "Weight": 1.0,
    "Fixed": bool(True),
    "Particle": ["1", "1", "2", "2", "3", "3"]
}

E_OOO_VVV__ABBDict = {
    "C A": "H+ P H+ P H+ P ",
    "Spins": "0 0 1 1 1 1 ",
    "Weight": 1.0,
    "Fixed": bool(True),
    "Particle": ["1", "1", "2", "2", "3", "3"]
}

E_OOO_VVV__BBBDict = {
    "C A": "H+ P H+ P H+ P ",
    "Spins": "1 1 1 1 1 1 ",
    "Weight": 1.0,
    "Fixed": bool(True),
    "Particle": ["1", "1", "2", "2", "3", "3"]
}

E_O___ADict = {
    "C A": "H+ ",
    "Spins": "0 ",
    "Weight": 1.0,
    "Fixed": bool(True),
    "Particle": ["1"]
}

E__O__ADict = {
    "C A": "H ",
    "Spins": "0 ",
    "Weight": 1.0,
    "Fixed": bool(True),
    "Particle": ["1"]
}

E_OO___AADict = {
    "C A": "H+ H+ ",
    "Spins": "0 0 ",
    "Weight": 1.0,
    "Fixed": bool(True),
    "Particle": ["1", "2"]
}

E__OO__AADict = {
    "C A": "H H ",
    "Spins": "0 0 ",
    "Weight": 1.0,
    "Fixed": bool(True),
    "Particle": ["1", "2"]
}

FADict = {
    "C A": "G+ G ",
    "Spins": "0 0 ",
    "Weight": 1.0,
    "String": '(LTOp)f1'
}

FBDict = {
    "C A": "G+ G ",
    "Spins": "1 1 ",
    "Weight": 1.0,
    "String": '(LTOp)f1'
}

VAADict = {
    "C A": "G+ G G+ G ",
    "Spins": "0 0 0 0 ",
    "Weight": (1.0/4.0),
    "String": '(LTOp)v2tensors.v2("aaaa")'
}

VABDict = {
    "C A": "G+ G G+ G ",
    "Spins": "0 0 1 1 ",
    "Weight": 1.0,
    "String": '(LTOp)v2tensors.v2("abab")'
}

VBBDict = {
    "C A": "G+ G G+ G ",
    "Spins": "1 1 1 1 ",
    "Weight": (1.0/4.0),
    "String": '(LTOp)v2tensors.v2("bbbb")'
}

T1ADict = {
    "C A": "P+ H ",
    "Spins": "0 0 ",
    "Weight": 1.0,
    "String": '(LTOp)t1("aa")'
}

T1BDict = {
    "C A": "P+ H ",
    "Spins": "1 1 ",
    "Weight": 1.0,
    "String": '(LTOp)t1("bb")'
}

T1ADagDict = {
    "C A": "H+ P ",
    "Spins": "0 0 ",
    "Weight": 1.0,
    "String": '(LTOp)t1("aa")'
}

T1BDagDict = {
    "C A": "H+ P ",
    "Spins": "1 1 ",
    "Weight": 1.0,
    "String": '(LTOp)t1("bb")'
}

T2AADict = {
    "C A": "P+ H P+ H ",
    "Spins": "0 0 0 0 ",
    "Weight": (1.0/4.0),
    "String": '(LTOp)t2("aaaa")'
}

T2ABDict = {
    "C A": "P+ H P+ H ",
    "Spins": "0 0 1 1 ",
    "Weight": 1.0,
    "String": '(LTOp)t2("abab")'
}

T2BBDict = {
    "C A": "P+ H P+ H ",
    "Spins": "1 1 1 1 ",
    "Weight": (1.0/4.0),
    "String": '(LTOp)t2("bbbb")'
}

T2AADagDict = {
    "C A": "H+ P H+ P ",
    "Spins": "0 0 0 0 ",
    "Weight": (1.0/4.0),
    "String": '(LTOp)t2("aaaa")'
}

T2ABDagDict = {
    "C A": "H+ P H+ P ",
    "Spins": "0 0 1 1 ",
    "Weight": 1.0,
    "String": '(LTOp)t2("abab")'
}

T2BBDagDict = {
    "C A": "H+ P H+ P ",
    "Spins": "1 1 1 1 ",
    "Weight": (1.0/4.0),
    "String": '(LTOp)t2("bbbb")'
}

T3AAADict = {
    "C A": "P+ H P+ H P+ H ",
    "Spins": "0 0 0 0 0 0 ",
    "Weight": (1.0/36.0)
}

T3AABDict = {
    "C A": "P+ H P+ H P+ H ",
    "Spins": "0 0 0 0 1 1 ",
    "Weight": (1.0/4.0)
}

T3ABBDict = {
    "C A": "P+ H P+ H P+ H ",
    "Spins": "0 0 1 1 1 1 ",
    "Weight": (1.0/4.0)
}

T3BBBDict = {
    "C A": "P+ H P+ H P+ H ",
    "Spins": "1 1 1 1 1 1 ",
    "Weight": (1.0/36.0)
}

OperatorsDict = {
    "E_O_V__A": E_O_V__ADict,
    "E_O_V__B": E_O_V__BDict,
    "E_OO_VV__AA": E_OO_VV__AADict,
    "E_OO_VV__AB": E_OO_VV__ABDict,
    "E_OO_VV__BB": E_OO_VV__BBDict,
    "E_OOO_VVV__AAA": E_OOO_VVV__AAADict,
    "E_OOO_VVV__AAB": E_OOO_VVV__AABDict,
    "E_OOO_VVV__ABB": E_OOO_VVV__ABBDict,
    "E_OOO_VVV__BBB": E_OOO_VVV__BBBDict,
    "E_O___A": E_O___ADict,
    "E__O__A": E__O__ADict,
    "E_OO___AA": E_OO___AADict,
    "E__OO__AA": E__OO__AADict,
    "FA": FADict,
    "FB": FBDict,
    "VAA": VAADict,
    "VAB": VABDict,
    "VBB": VBBDict,
    "T1A": T1ADict,
    "T1B": T1BDict,
    "T1A+": T1ADagDict,
    "T1B+": T1BDagDict,
    "T2AA": T2AADict,
    "T2AB": T2ABDict,
    "T2BB": T2BBDict,
    "T2AA+": T2AADagDict,
    "T2AB+": T2ABDagDict,
    "T2BB+": T2BBDagDict,
    "T3AAA": T3AAADict,
    "T3AAB": T3AABDict,
    "T3ABB": T3ABBDict,
    "T3BBB": T3BBBDict
}


# %%
# [Bra][Left][exp(-O)][Hamiltonian][exp(O)][Right][Ket]

### Bra ###
Bra = ["E_OO_VV__BB "]

### Ket ###
Ket = [""]

### Left ###
Left = [""]

### Right ###
Right = [""]

### Hamiltonian ###
Hamiltonian = ["FA ", "FB ", "VAA ", "VAB ", "VBB "]

### Exponential ###
# Also, only the operator for exp(O) is defined as exp(-O) will be taken care of internally
# Example 1: exp(T1-T1+) = ["T1 "," -T1+ "]
# Example 2: exp(T-T+), where T=T1+T2 = ["T1 ","-T1+ ","T2 ","-T2+ "] or ["T1 ","T2 ","-T1+ ","-T2+ "]
# Opp = [""]
Opp = ["T1A ", "T1B ", "T2AA ", "T2AB ", "T2BB "]
# Opp = ["T1A ", "T1B ", "-T1A+ ", "-T1B+ ", "T2AA ", "T2AB ", "T2BB ", "-T2AA+ ", "-T2AB+ ", "-T2BB+ "]
# Opp = ["T1A ", "-T1A+ ", "T2AA ", "-T2AA+ "]
# Opp = ["T1A ", "T2AA "]
# Opp = ["T1A ", "-T1A+ "]

### Highest Order or Commutator ###
# Sets max number of operators per exponential, but also the commutator limit.
Comm_order = 4

print("Bra = ", Bra)
print("Ket = ", Ket)
print("Left = ", Left)
print("Right = ", Right)
print("Hamiltonian = ", Hamiltonian)
print("Opp = ", Opp)
print("Comm_order = ", Comm_order)


# %%
# This can be simplified. exp1 =  exp2 for terms with an even number of operators and
# exp1 = -exp2 for Operatorss with an odd number of operators.

# exp(-o), Left exponential of the similarity transformed Hamiltonian
exp1 = [""]
# exp(o), Right exponential of the similarity transformed Hamiltonian
exp2 = [""]

for i in range(0, Comm_order):
    expanded_list = [""]
    for term in exp1:
        for o in Opp:
            # Flip the sign of operators since it is exp(-O)
            if (o.count("-") == 1):
                o = o.replace('-', '')
            else:
                o = "-"+o
            #
            if ((term+o).count("-") % 2) == 0:
                sign = ""
            else:
                sign = "-"
            expanded_list.append(sign+term.replace('-', '')+o.replace('-', ''))
    exp1 = expanded_list[:]

for i in range(0, Comm_order):
    expanded_list = [""]
    for term in exp2:
        for o in Opp:
            if ((term+o).count("-") % 2) == 0:
                sign = ""
            else:
                sign = "-"
            expanded_list.append(sign+term.replace('-', '')+o.replace('-', ''))
    exp2 = expanded_list[:]

if print_opt == "verbose":
    print("Left Exponential Expanded: " , exp1)
    print("Right Exponential Expanded: ", exp2)

if(Comm_order>0):
    del term, o, i, expanded_list



# %%
# Form all combinations

operator_combs = []
for b in Bra:
    for l in Left:
        for e1 in exp1:
            for o in Hamiltonian:
                for e2 in exp2:
                    if ((e1+e2).count("T") <= Comm_order):  # Limits the expansion
                    # if ((e1+e2).count("T") == Comm_order):  # Limits the expansion
                        for r in Right:
                            for k in Ket:
                                if ((e1+e2).count("-") % 2) == 0:
                                    sign = ""
                                else:
                                    sign = "- "
                                operator_combs.append(
                                    sign+b+l+e1.replace('-', '')+o+e2.replace('-', '')+r+k)

if print_opt == "verbose":
    # print("ALL POSSIBLE COMBINATIONS")
    print(*operator_combs, sep = "\n")
    print("TOTAL POSSIBLE COMBINATIONS = ", len(operator_combs))

del b, l, e1, e2, o, r, k, sign, exp1, exp2


# %%
print(
    "ELIMINATING SETS THAT HAVE AN OPERATOR WITH ONLY ONE SPIN WHEN ALL OTHER SPINS ARE THE OTHER SPIN."
)

eliminated_set = []
tentative_allowed_set = []
for _ in range(len(operator_combs)):
    op_set = operator_combs.pop(0)
    operators_with_alpha = 0
    operators_with_beta = 0

    if len(op_set.split()) == 1:
        tentative_allowed_set.append(op_set)

    if len(op_set.split()) > 1:
        for operator in op_set.split():
            if "-" not in operator:

                # CHECK THE SPINS OF ALL OPERATORS AND COUNT HOW MANY HAVE
                # AN ALPHA SPIN INDEX AND HOW MANY HAVE A BETA SPIN INDEX.
                if "0" in OperatorsDict[operator].get("Spins").split():
                    operators_with_alpha += 1
                if "1" in OperatorsDict[operator].get("Spins").split():
                    operators_with_beta += 1

        # FOR SETS WITH MORE THAN 1 OPERATOR, ELIMINATE THE SET IF
        # ONLY ONE OPERATOR HAS ALPHA OR BETA SPIN.
        if operators_with_alpha == 1 or operators_with_beta == 1:
            eliminated_set.append(op_set)
        else:
            tentative_allowed_set.append(op_set)

print(
    "ELIMINATED {0} COMBINATIONS / {1} COMBINATIONS REMAINING\n".format(
        len(eliminated_set), len(tentative_allowed_set)
    )
)

# if print_opt == "verbose":
# print("\nTENTATIVE ALLOWED SETS")
# print(*tentative_allowed_set, sep = "\n")
# print("\nELIMINATED SETS")
# print(*eliminated_set, sep = "\n")

del operator_combs, op_set, operators_with_alpha, operators_with_beta, operator, eliminated_set

print("ELIMINATING SETS IF THERE IS NOT ENOUGH POSSIBLE ALPHA/BETA P/H/G C/A OPERATORS TO FORM PAIRS.")

eliminated_set = []
final_allowed_set = []
for _ in range(len(tentative_allowed_set)):
    op_set = tentative_allowed_set.pop(0)

    alpha_hole_c = 0
    alpha_hole_a = 0
    beta_hole_c = 0
    beta_hole_a = 0
    alpha_particle_c = 0
    alpha_particle_a = 0
    beta_particle_c = 0
    beta_particle_a = 0
    alpha_gen_c = 0
    alpha_gen_a = 0
    beta_gen_c = 0
    beta_gen_a = 0

    for operator in op_set.split():
        if operator != "-":
            Operator_spins = OperatorsDict[operator].get("Spins").split()
            Operator_C_A = OperatorsDict[operator].get("C A").split()

            for i in range(0, len(Operator_C_A)):
                if (Operator_spins[i] == "0" and Operator_C_A[i] == "H+"):
                    alpha_hole_c += 1
                if (Operator_spins[i] == "0" and Operator_C_A[i] == "H"):
                    alpha_hole_a += 1
                if (Operator_spins[i] == "1" and Operator_C_A[i] == "H+"):
                    beta_hole_c += 1
                if (Operator_spins[i] == "1" and Operator_C_A[i] == "H"):
                    beta_hole_a += 1
                if (Operator_spins[i] == "0" and Operator_C_A[i] == "P+"):
                    alpha_particle_c += 1
                if (Operator_spins[i] == "0" and Operator_C_A[i] == "P"):
                    alpha_particle_a += 1
                if (Operator_spins[i] == "1" and Operator_C_A[i] == "P+"):
                    beta_particle_c += 1
                if (Operator_spins[i] == "1" and Operator_C_A[i] == "P"):
                    beta_particle_a += 1
                if (Operator_spins[i] == "0" and Operator_C_A[i] == "G+"):
                    alpha_gen_c += 1
                if (Operator_spins[i] == "0" and Operator_C_A[i] == "G"):
                    alpha_gen_a += 1
                if (Operator_spins[i] == "1" and Operator_C_A[i] == "G+"):
                    beta_gen_c += 1
                if (Operator_spins[i] == "1" and Operator_C_A[i] == "G"):
                    beta_gen_a += 1

    if (alpha_hole_c > (alpha_hole_a + alpha_gen_a)):
        eliminated_set.append(op_set)
        continue
    elif (alpha_particle_c > (alpha_particle_a + alpha_gen_a)):
        eliminated_set.append(op_set)
        continue
    elif (alpha_hole_a > (alpha_hole_c + alpha_gen_c)):
        eliminated_set.append(op_set)
        continue
    elif (alpha_particle_a > (alpha_particle_c + alpha_gen_c)):
        eliminated_set.append(op_set)
        continue
    elif (beta_hole_c > (beta_hole_a + beta_gen_a)):
        eliminated_set.append(op_set)
        continue
    elif (beta_particle_c > (beta_particle_a + beta_gen_a)):
        eliminated_set.append(op_set)
        continue
    elif (beta_hole_a > (beta_hole_c + beta_gen_c)):
        eliminated_set.append(op_set)
        continue
    elif (beta_particle_a > (beta_particle_c + beta_gen_c)):
        eliminated_set.append(op_set)
        continue
    else:
        final_allowed_set.append(op_set)

print(
    "ELIMINATED {0} COMBINATIONS / {1} COMBINATIONS REMAINING\n".format(
        len(eliminated_set), len(final_allowed_set)
    )
)

del alpha_hole_c, alpha_hole_a, beta_hole_c, beta_hole_a
del alpha_particle_c, alpha_particle_a, beta_particle_c, beta_particle_a
del alpha_gen_c, alpha_gen_a, beta_gen_c, beta_gen_a
del eliminated_set, op_set, operator, Operator_spins, Operator_C_A, i, tentative_allowed_set


# %%
import sys
from sympy.combinatorics.permutations import Permutation


def all_pairs(lst, identities, all_spin_operators, all_CA_operators, operator_list):
    if len(lst) < 2:
        yield []
        return
    if len(lst) % 2 == 1:
        print("ERROR: ODD NUMBER OF C/A OPERATORS")
        exit()
    else:
        a = lst[0]
        for i in range(1, len(lst)):
            allow = True
            pair = (a, lst[i])

            # CONTRACTIONS WITHIN AN OPERATOR ARE NOT ALLOWED
            if (identities[a] == identities[lst[i]]):
                allow = False
            # CONTRACTIONS BETWEEN DIFFERENT SPIN ARE NOT ALLOWED
            if (all_spin_operators[a] != all_spin_operators[lst[i]]):
                allow = False
            # CANNOT CONTRACT TWO ANNIHILATION OPERATORS
            if (("+" not in all_CA_operators[a]) and ("+" not in all_CA_operators[lst[i]])):
                allow = False
            # CANNOT CONTRACT TWO CREATION OPERATORS
            if (("+" in all_CA_operators[a]) and ("+" in all_CA_operators[lst[i]])):
                allow = False
            # X-X+ CONTRACTIONS CANNOT HAPPEN IF EITHER OPERATOR IS OCCUPIED/HOLE
            if (("+" not in all_CA_operators[a]) and ("+" in all_CA_operators[lst[i]]) and ("H" in all_CA_operators[a])):
                allow = False
            if (("+" not in all_CA_operators[a]) and ("+" in all_CA_operators[lst[i]]) and ("H" in all_CA_operators[lst[i]])):
                allow = False
            # X+-X CONTRACTIONS CANNOT HAPPEN IF EITHER OPERATOR IS UNOCCUPIED/PARTICLE
            if (("+" in all_CA_operators[a]) and ("+" not in all_CA_operators[lst[i]]) and ("P" in all_CA_operators[a])):
                allow = False
            if (("+" in all_CA_operators[a]) and ("+" not in all_CA_operators[lst[i]]) and ("P" in all_CA_operators[lst[i]])):
                allow = False
            # DO NOT CONTRACT BETWEEN TWO EXCITATION OPERATORS (BRA AND KET FOR EXAMPLE)
            if (("E" in operator_list[identities[a]-1]) and ("E" in operator_list[identities[lst[i]]-1])):
                allow = False
            if (allow is True):
                for rest in all_pairs(lst[1:i]+lst[i+1:], identities, all_spin_operators, all_CA_operators, operator_list):
                    yield [pair] + rest


def parity_and_sign(permutation_list):
    p = Permutation(permutation_list)

    # Final sign depends on the sign of the expression and the parity
    if ((p.parity() == 1) and ("-" in op_set)):
        sign = 1
    if ((p.parity() == 1) and ("-" not in op_set)):
        sign = -1
    if ((p.parity() == 0) and ("-" in op_set)):
        sign = -1
    if ((p.parity() == 0) and ("-" not in op_set)):
        sign = 1

    if print_opt == "Verbose":
        print(permutation_list)
        print("Sign = ", sign, "   Parity =", p.parity())

    return sign


def reorder_paths(path, index_path):
    index_order = []
    for position in index_path:
        index_order.append(position[0])
    for _ in range(index_order.index(min(index_order))):
        path.append(path[0])
        path.pop(0)
        index_path.append(index_path[0])
        index_path.pop(0)


# %%
from collections import defaultdict
 
# This class represents a directed graph
# using adjacency list representation
 
 
class Graph:
 
    # Constructor
    def __init__(self):
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
 
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
 
    # Function to print a BFS of graph
    def BFS(self, s, l):
        
        if len(self.graph) != 0 :
            # Mark all the vertices as not visited

            visited = [False] * l

            # Create a queue for BFS
            queue = []
    
            # Mark the source node as
            # visited and enqueue it
            queue.append(s)
            visited[s] = True

            while queue:
            
                # Dequeue a vertex from
                # queue and print it
                s = queue.pop(0)
                # print(s, end=" ")
    
                # Get all adjacent vertices of the
                # dequeued vertex s. If a adjacent
                # has not been visited, then mark it
                # visited and enqueue it
                for i in self.graph[s]:
                    if visited[i] is False:
                        queue.append(i)
                        visited[i] = True
        
        else:
            visited = [False]

        return visited

# %%
import math

collective = []
ContractionDict={}
count = -1
for op_set in final_allowed_set:

    identity = 1
    identities = []
    all_CA_operators = []
    all_spin_operators = []
    operator_list = []
    for operator in op_set.split():
        if operator != "-":

            all_CA_operators.extend(
                OperatorsDict[operator].get("C A").split())
            all_spin_operators.extend(
                OperatorsDict[operator].get("Spins").split())

            for _ in range(len(OperatorsDict[operator].get("Spins").split())):
                identities.append(identity)
            identity += 1

            operator_list.append(operator)
    
    del identity, operator

    evaluated_contractions = []
    # print("operator_list",operator_list)
    for contraction_list in all_pairs(list(range(0, len(all_CA_operators))),identities,all_spin_operators,all_CA_operators,operator_list):
        evaluated_contractions.append(contraction_list)

    del operator_list

    if not evaluated_contractions:
        # eliminated.append(op_set) # Eliminated sets are put in a list for debgging purposes.
        if print_opt == "verbose":
            print(op_set," WAS ELIMINATED BECAUSE NO VIABLE SET OF CONTRACTIONS WERE FOUND\n")
            print("-"*40+"\n")
    else:
        if print_opt == "verbose":
            print(op_set)
            print("CA Operators: ", all_CA_operators)
            print("Spin Operators: ", all_spin_operators)
            print("Identity Indices: ", identities)
            print("Evaluated Contractions: ", *
                  evaluated_contractions, sep="\n")
            print("-"*40+"\n")


    for contraction_list in evaluated_contractions:
        count += 1
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

        ContractionDict[count]['weight'] = weight #Weight can be better defined depending on multiple exponents or explicit weights from the user.

        # List the contracted indices in the same order as the list of contractions.
        # This is used to determine the parity.
        permutation_list = []
        for contracted_pair in contraction_list:
            permutation_list.append(contracted_pair[0])
            permutation_list.append(contracted_pair[1])

        ContractionDict[count]['Sign'] = parity_and_sign(permutation_list)

        del contracted_pair
        del permutation_list

        # Contractions are reordered such that creation operators are listed before annihilation.
        # This is for determing paths, which go from creation operators to annihilation operators.
        for contraction in contraction_list:
            if ("+" not in all_CA_operators[contraction[0]]):
                contraction_list[contraction_list.index(contraction)] = (
                    contraction[1], contraction[0])
        del contraction

        ContractionDict[count]['Oriented Contractions'] = list(contraction_list)

        # Determine if Graph is Disconnected.
        vertex_FFlist = [False]*len(ContractionDict[count].get("Operators"))
        fixed_count = 0
        count_op = 0
        for operator in ContractionDict[count].get("Operators"):
            if OperatorsDict[operator].get("Fixed"):
                fixed_count += 1
                vertex_FFlist[count_op] = True
            count_op += 1

        # OPTION 1: THERE IS NO VERTEX THAT IS NOT "FIXED"
        if len(ContractionDict[count].get("Operators")) - fixed_count == 0: # Not sure if I want this this way.
            # print(count, "NO FREE OPERATOR, MARKING GRAPH AS CONNECTED")
            ContractionDict[count]['Connected'] = bool(True)

        # OPTION 2: THERE IS ONE VERTEX THAT IS NOT "FIXED"
        if len(ContractionDict[count].get("Operators")) - fixed_count == 1: # Not sure if I want this this way.
            # print(count, "ONLY ONE FREE OPERATOR, MARKING GRAPH AS CONNECTED")
            ContractionDict[count]['Connected'] = bool(True)

        # OPTION 3: EVALUATE GRAPH
        if len(ContractionDict[count].get("Operators")) - fixed_count > 1:
            g = Graph()
            vertex_list = []
            start_vertex = -1

            for contraction in ContractionDict[count].get("Oriented Contractions"):
                Identity_1 = ContractionDict[count].get("Identities")[contraction[0]]
                Operator_1 = ContractionDict[count].get("Operators")[Identity_1-1]
                Fixed_1 = OperatorsDict[Operator_1].get("Fixed")

                Identity_2 = ContractionDict[count].get("Identities")[contraction[1]]
                Operator_2 = ContractionDict[count].get("Operators")[Identity_2-1]
                Fixed_2 = OperatorsDict[Operator_2].get("Fixed")

                if not Fixed_1 and not Fixed_2:
                    g.addEdge(Identity_1-1, Identity_2-1)
                    vertex_list.append(Identity_1-1)
                    vertex_list.append(Identity_2-1)
                    start_vertex = Identity_2-1

            # print(vertex_list)
            # print(vertex_FFlist)
            if start_vertex == -1:
                print("did not find a start vertex")
                print(ContractionDict[count])
                ContractionDict[count]['Connected'] = bool(False)
                break
            else:
                ContractionDict[count]['Connected'] = bool(True)
                BFSearch = g.BFS(start_vertex, len(ContractionDict[count].get("Operators")))
                # print(BFSearch)
                for vertex in range(len(vertex_FFlist)):
                    if vertex_FFlist[vertex] is False:
                        if BFSearch[vertex] is False:
                            ContractionDict[count]['Connected'] = bool(False)




# ALL THE DATA IS PUT INTO ContractionDict WHICH WILL BE USED TO FIND EQUIVALENT TERMS AND SUCH.
# IT MAY BE BEST TO BREAK UP collective FOR FASTER PROCESSING OF LATER STEPS.
# print(jsbeautifier.beautify(json.dumps(ContractionDict), options))


# DISCONNECTED TERMS 
# So there are two ways I can think about going about disconnected terms.
# Option 1 is to remove them before any resumming. This saves on the overhead of the resumming because it removes 
# a number of terms before resumming. You can do this by forming list of indices from one loop or path, then 
# expand on this for the remaining loops (recursively) until you have the full set of indices or you find a loop/path that
# cannot continue extending the list of indices and therefore must be disconnected. I will need the list of index paths, which
# was removed from the get_path() routine, but can be put back by adding the same structed lines for path[] as for index_path[].
# Option 2 is that they are removed through resummation. I am choosing this pathway because there are theories that hae disconnected
# terms that don't vanish.

for _ in ContractionDict:

    connections = []
    NewLabels = []
    for operator in ContractionDict[_].get("Operators"):
        connections.append([operator,[],[]])

        Label =str(operator)
        OutFixed = 0
        InFixed = 0

        if not OperatorsDict[operator].get("Fixed"):
            for contraction in ContractionDict[_].get("Oriented Contractions"):
                Identity_1 = ContractionDict[_].get("Identities")[contraction[0]]
                Operator_1 = ContractionDict[_].get("Operators")[Identity_1-1]
                Fixed_1 = OperatorsDict[Operator_1].get("Fixed")
                # Position_1 = ContractionDict[_].get("Identities")[:contraction[0]].count(Identity_1)
        
                Identity_2 = ContractionDict[_].get("Identities")[contraction[1]]
                Operator_2 = ContractionDict[_].get("Operators")[Identity_2-1]
                Fixed_2 = OperatorsDict[Operator_2].get("Fixed")
                # Position_2 = ContractionDict[_].get("Identities")[:contraction[1]].count(Identity_2)

                if Identity_1 == len(connections) and not Fixed_1:
                    if Fixed_2:
                        OutFixed += 1

                if Identity_2 == len(connections) and not Fixed_2:
                    if Fixed_1:
                        InFixed += 1

            Label = Label+"-"+str(InFixed)+"-"+str(OutFixed)

        NewLabels.append(Label)

    # print(NewLabels)

    for contraction in ContractionDict[_].get("Oriented Contractions"):

        Identity_1 = ContractionDict[_].get("Identities")[contraction[0]]
        Operator_1 = ContractionDict[_].get("Operators")[Identity_1-1]
        Fixed_1 = OperatorsDict[Operator_1].get("Fixed")
        Position_1 = ContractionDict[_].get("Identities")[:contraction[0]].count(Identity_1)

        Identity_2 = ContractionDict[_].get("Identities")[contraction[1]]
        Operator_2 = ContractionDict[_].get("Operators")[Identity_2-1]
        Fixed_2 = OperatorsDict[Operator_2].get("Fixed")
        Position_2 = ContractionDict[_].get("Identities")[:contraction[1]].count(Identity_2)

        # Possibility 1: both contraction[0] and contraction[1] belong to 'Fixed' sets.
        # NOT TESTED!!!!
        if Fixed_1 and Fixed_2:
            in_con = [NewLabels[Identity_1-1]+"-"+str(Identity_1),
                       ContractionDict[_].get("Spins")[contraction[0]],
                       OperatorsDict[Operator_1].get("Particle")[Position_1]
                       ]
            connections[Identity_2-1][1].append(in_con)
            out_con = [NewLabels[Identity_2-1]+"-"+str(Identity_2),
                       ContractionDict[_].get("Spins")[contraction[1]],
                       OperatorsDict[Operator_2].get("Particle")[Position_2]
                       ]
            connections[Identity_1-1][2].append(out_con)
        # Possibility 2: only contraction[0] belongs to a 'Fixed' set.
        if Fixed_1 and not Fixed_2:
            in_con = [NewLabels[Identity_1-1]+"-"+str(Identity_1),
                       ContractionDict[_].get("Spins")[contraction[0]],
                       OperatorsDict[Operator_1].get("Particle")[Position_1]
                       ]
            connections[Identity_2-1][1].append(in_con)
        # Possibility 3: only contraction[1] belongs to a 'Fixed' set.
        if not Fixed_1 and Fixed_2:
            out_con = [NewLabels[Identity_2-1]+"-"+str(Identity_2),
                       ContractionDict[_].get("Spins")[contraction[1]],
                       OperatorsDict[Operator_2].get("Particle")[Position_2]
                       ]
            connections[Identity_1-1][2].append(out_con)
        # Possibility 4: neither contraction[0] and contraction[1] belong to a 'Fixed' sets.
        if not Fixed_1 and not Fixed_2:
            in_con = [NewLabels[Identity_1-1],
                      ContractionDict[_].get("Spins")[contraction[0]]]
            out_con = [NewLabels[Identity_2-1],
                       ContractionDict[_].get("Spins")[contraction[1]]]
            connections[Identity_2-1][1].append(in_con)
            connections[Identity_1-1][2].append(out_con)

    for conset in connections:
        conset[1].sort()
        conset[2].sort()
    connections.sort()

    ContractionDict[_]['Connections'] = connections



# print(jsbeautifier.beautify(json.dumps(ContractionDict), options))

# for Dict1 in ContractionDict:
#     ContractionDict[Dict1]['Evaluation'] = Evaluate_Con(ContractionDict[Dict1].get("Operators"),ContractionDict[Dict1].get("Oriented Contractions"),ContractionDict[Dict1].get("Identities"),ContractionDict[Dict1].get("CA"))
#     print(Dict1, ContractionDict[Dict1])


searched_conn = []
Final = []

search_sets = []
searched_operators_sets = []
for Dict1 in ContractionDict:
    same_operators_set = []
    Dict1_Ops = sorted(ContractionDict[Dict1].get("Operators"))
    Dict1_Conn = ContractionDict[Dict1].get("Connected")
    Combo_1 = [Dict1_Ops, Dict1_Conn]

    if Combo_1 not in searched_operators_sets:
        same_operators_set.append(Dict1)
        searched_operators_sets.append(Combo_1)

        for Dict2 in ContractionDict:
            Dict2_Ops = sorted(ContractionDict[Dict2].get("Operators"))
            Dict2_Conn = ContractionDict[Dict2].get("Connected")
            Combo_2 = [Dict2_Ops, Dict2_Conn]

            if Combo_1 == Combo_2:
                if Dict2 > Dict1:
                    same_operators_set.append(Dict2)

        search_sets.append(same_operators_set)


for search in search_sets:

    for Dict1 in search:

        op_set1 = ContractionDict[Dict1].get("Term").split()
        Connections_1 = ContractionDict[Dict1].get("Connections")
        Connected_1 = ContractionDict[Dict1].get("Connected")
        Combo_1 = [Connections_1, Connected_1]

        if "-" in op_set1:
            op_set1 = sorted(op_set1[1:])
            sum_weight = -1*ContractionDict[Dict1].get("weight")
        else:
            op_set1 = sorted(op_set1)
            sum_weight = ContractionDict[Dict1].get("weight")

        if Combo_1 not in searched_conn:
            searched_conn.append(Combo_1)
            ContractionDict[Dict1]

            for Dict2 in search[search.index(Dict1)+1:]:

                op_set2 = ContractionDict[Dict2].get("Term").split()
                Connections_2 = ContractionDict[Dict2].get("Connections")
                Connected_2 = ContractionDict[Dict2].get("Connected")
                Combo_2 = [Connections_2, Connected_2]

                if Combo_1 == Combo_2:

                    # print(Dict1, Dict2, ContractionDict[Dict2])

                    if "-" in op_set2:
                        sum_weight += -1*ContractionDict[Dict2].get("weight")

                    if "-" not in op_set2:
                        sum_weight += ContractionDict[Dict2].get("weight")

            # print(sum_weight)

            # NOTE:

            if ("%.6f" % sum_weight) == '0.000000' or ("%.6f" % sum_weight) == '-0.000000':
                if Connected_1 == bool(True):
                    print("Interesting!!!, {} has zero-sum weight, but is not disconnected.".format(Dict1))
                    Final.append(ContractionDict[Dict1])
                    del Final[Final.index(ContractionDict[Dict1])]['weight']
                    Final[Final.index(ContractionDict[Dict1])]['weight'] = ("%.6f" % sum_weight)
                # If it is disconnected, do nothing.

            elif sum_weight > 0 and "-" not in ContractionDict[Dict1].get("Term").split():
                if Connected_1 == bool(False):
                    print("Interesting!!!, {} has non-zero weight, but is disconnected.".format(Dict1))
                else:
                    # print("Here 1")
                    Final.append(ContractionDict[Dict1])
                    del Final[Final.index(ContractionDict[Dict1])]['weight']
                    Final[Final.index(ContractionDict[Dict1])]['weight'] = ("%.6f" % sum_weight)

            elif sum_weight < 0 and "-" in ContractionDict[Dict1].get("Term").split():
                if Connected_1 == bool(False):
                    print("Interesting!!!, {} has non-zero weight, but is disconnected.".format(Dict1))
                else:
                    # print("Here 2")
                    Final.append(ContractionDict[Dict1])
                    del Final[Final.index(ContractionDict[Dict1])]['weight']
                    Final[Final.index(ContractionDict[Dict1])]['weight'] = ("%.6f" % sum_weight)

            else:
                allow = False
                for Dict2 in search[search.index(Dict1)+1:]:

                    if not allow:
                    
                        op_set2 = ContractionDict[Dict2].get("Term").split()
                        Connections_2 = ContractionDict[Dict2].get("Connections")
                        Connected_2 = ContractionDict[Dict2].get("Connected")
                        Combo_2 = [Connections_2, Connected_2]

                        if Combo_1 == Combo_2:

                            if sum_weight > 0 and "-" not in ContractionDict[Dict2].get("Term").split():
                                if not ContractionDict[Dict2].get("Connected"):
                                    print("Interesting!!!, {} has non-zero weight, but is disconnected.".format(Dict2))
                                else:
                                    # print("Here 3")
                                    Final.append(ContractionDict[Dict2])
                                    del Final[Final.index(ContractionDict[Dict2])]['weight']
                                    Final[Final.index(ContractionDict[Dict2])]['weight'] = ("%.6f" % sum_weight)
                                    allow = True

                            elif sum_weight < 0 and "-" in ContractionDict[Dict2].get("Term").split():
                                if not ContractionDict[Dict2].get("Connected"):
                                    print("Interesting!!!, {} has non-zero weight, but is disconnected.".format(Dict2))
                                else:
                                    # print("Here 4")
                                    Final.append(ContractionDict[Dict2])
                                    del Final[Final.index(ContractionDict[Dict2])]['weight']
                                    Final[Final.index(ContractionDict[Dict2])]['weight'] = ("%.6f" % sum_weight)
                                    allow = True

                if not allow:
                    print("Funny Situation: Cannot find a term with same sign as the sum_weight.")


print(*Final, sep="\n")

# %%
from fractions import Fraction
for dict1 in Final:

    fixed_positions = [] 
    for position in range(len(dict1.get("Identities"))):

        corr_op = dict1.get("Operators")[dict1.get("Identities")[position]-1]
        if OperatorsDict[corr_op].get("Fixed"):
            fixed_positions.append(position)

    
    fixed_start = 1
    free_start = len(fixed_positions)+1

    labels = [None]*len(dict1.get("Identities"))
    for con in dict1.get("Oriented Contractions"):
        CA1 = dict1.get("CA")[con[0]]
        Fixed_1 = OperatorsDict[dict1.get("Operators")[dict1.get("Identities")[con[0]]-1]].get("Fixed")
        CA2 = dict1.get("CA")[con[1]]
        Fixed_2 = OperatorsDict[dict1.get("Operators")[dict1.get("Identities")[con[1]]-1]].get("Fixed")

        if "H" in CA1 or "H" in CA2:
            if Fixed_1 or Fixed_2:
                labels[con[0]] = "h"+str(fixed_start)
                labels[con[1]] = "h"+str(fixed_start)
                fixed_start += 1
            else:
               labels[con[0]] = "h"+str(free_start)
               labels[con[1]] = "h"+str(free_start)
               free_start += 1
            
        elif "P" in CA1 or "P" in CA2:
            if Fixed_1 or Fixed_2:
                labels[con[0]] = "p"+str(fixed_start)
                labels[con[1]] = "p"+str(fixed_start)
                fixed_start += 1
            else:
               labels[con[0]] = "p"+str(free_start)
               labels[con[1]] = "p"+str(free_start)
               free_start += 1

        else:
            print("HAVE NOT PROGRAMMED YET")
    
    weight_frac = Fraction(dict1.get("weight")).limit_denominator(1000).as_integer_ratio()
    if dict1.get("Sign") == -1:
        if weight_frac[0] == 1 and weight_frac[1] == 1:
            eqn_str = "-1.0 * "
        else:
            eqn_str = "-("+str(weight_frac[0])+".0/"+str(weight_frac[1])+".0) * "
    elif dict1.get("Sign") == 1:
        if weight_frac[0] == 1 and weight_frac[1] == 1:
            eqn_str = "1.0 * "
        else:
            eqn_str = "("+str(weight_frac[0])+".0/"+str(weight_frac[1])+".0) * "
    else: 
        print("Sign Error")

    Op_CA_list = [[] for x in range(len(dict1.get("Operators")))]
    for position in range(len(labels)):

        identity = dict1.get("Identities")[position]
        Op_CA_list[identity-1].append(labels[position])
        
    for _ in range(len(Op_CA_list)):
        
        Operator = dict1.get("Operators")[_]

        flipsign = False
        if "String" in OperatorsDict[Operator].keys():

            op_str = OperatorsDict[Operator].get("String")

            if Operator in ["FA","FB"]:
                # Assume we only have OO, OV(=VO), and VV 
                if("h" in Op_CA_list[_][0] and "h" in Op_CA_list[_][1]):
                    if Operator == "FA":
                        op_str = op_str + '_OO("aa")({}, {})'.format(Op_CA_list[_][0], Op_CA_list[_][1])
                    if Operator == "FB":
                        op_str = op_str + '_OO("bb")({}, {})'.format(Op_CA_list[_][0], Op_CA_list[_][1])
                elif("h" in Op_CA_list[_][0] and "p" in Op_CA_list[_][1]):
                    if Operator == "FA":
                        op_str = op_str + '_OV("aa")({}, {})'.format(Op_CA_list[_][0], Op_CA_list[_][1])
                    if Operator == "FB":
                        op_str = op_str + '_OV("bb")({}, {})'.format(Op_CA_list[_][0], Op_CA_list[_][1])
                elif("p" in Op_CA_list[_][0] and "h" in Op_CA_list[_][1]):
                    if Operator == "FA":
                        op_str = op_str + '_OV("aa")({}, {})'.format(Op_CA_list[_][1], Op_CA_list[_][0])
                    if Operator == "FB":
                        op_str = op_str + '_OV("bb")({}, {})'.format(Op_CA_list[_][1], Op_CA_list[_][0])
                elif("p" in Op_CA_list[_][0] and "p" in Op_CA_list[_][1]):
                    if Operator == "FA":
                        op_str = op_str + '_VV("aa")({}, {})'.format(Op_CA_list[_][0], Op_CA_list[_][1])
                    if Operator == "FB":
                        op_str = op_str + '_VV("bb")({}, {})'.format(Op_CA_list[_][0], Op_CA_list[_][1])
                else:
                    print("F term that is not programmed")

            elif Operator in ["VAA","VAB","VBB"]:
                # v2ijkl - "aaaa", "abab", "bbbb" 
                if("h" in Op_CA_list[_][0] and "h" in Op_CA_list[_][1] and "h" in Op_CA_list[_][2] and "h" in Op_CA_list[_][3]):
                    op_str = op_str.replace("v2(","v2ijkl(")
                    op_str = op_str + '({}, {}, {}, {})'.format(Op_CA_list[_][0], Op_CA_list[_][2],Op_CA_list[_][1], Op_CA_list[_][3])

                # v2ijka(=v2jiak)(=v2kaij)(=v2akji) - "aaaa", "abab", "baba", "bbbb" 
                elif("p" in Op_CA_list[_][0] and "h" in Op_CA_list[_][1] and "h" in Op_CA_list[_][2] and "h" in Op_CA_list[_][3]):
                    if Operator == "VAB":
                        op_str = op_str.replace("abab","baba")
                    op_str = op_str.replace("v2(","v2ijka(")
                    op_str = op_str + '({}, {}, {}, {})'.format(Op_CA_list[_][3], Op_CA_list[_][1],Op_CA_list[_][2], Op_CA_list[_][0])  

                elif("h" in Op_CA_list[_][0] and "p" in Op_CA_list[_][1] and "h" in Op_CA_list[_][2] and "h" in Op_CA_list[_][3]):
                    if Operator == "VAB":
                        op_str = op_str.replace("abab","baba")
                    op_str = op_str.replace("v2(","v2ijka(")
                    op_str = op_str + '({}, {}, {}, {})'.format(Op_CA_list[_][2], Op_CA_list[_][0],Op_CA_list[_][3], Op_CA_list[_][1])                
                
                elif("h" in Op_CA_list[_][0] and "h" in Op_CA_list[_][1] and "p" in Op_CA_list[_][2] and "h" in Op_CA_list[_][3]):
                    op_str = op_str.replace("v2(","v2ijka(")
                    op_str = op_str + '({}, {}, {}, {})'.format(Op_CA_list[_][1], Op_CA_list[_][3],Op_CA_list[_][0], Op_CA_list[_][2])
                
                elif("h" in Op_CA_list[_][0] and "h" in Op_CA_list[_][1] and "h" in Op_CA_list[_][2] and "p" in Op_CA_list[_][3]):
                    op_str = op_str.replace("v2(","v2ijka(")
                    op_str = op_str + '({}, {}, {}, {})'.format(Op_CA_list[_][0], Op_CA_list[_][2],Op_CA_list[_][1], Op_CA_list[_][3])
                
                # v2iajb (=v2aibj - "aaaa", "abab", "bbbb") (= -v2aijb - "aaaa", "bbbb") (= -v2iabj - "aaaa", "bbbb")  (= v2aijb - "abab",) (= v2iabj - "abab")  
                elif("h" in Op_CA_list[_][0] and "h" in Op_CA_list[_][1] and "p" in Op_CA_list[_][2] and "p" in Op_CA_list[_][3]):
                    op_str = op_str.replace("v2(","v2iajb(")
                    op_str = op_str + '({}, {}, {}, {})'.format(Op_CA_list[_][0], Op_CA_list[_][2],Op_CA_list[_][1], Op_CA_list[_][3])

                elif("p" in Op_CA_list[_][0] and "p" in Op_CA_list[_][1] and "h" in Op_CA_list[_][2] and "h" in Op_CA_list[_][3]):    
                    if Operator == "VAB":
                        op_str = op_str.replace("abab","baba")
                    op_str = op_str.replace("v2(","v2iajb(")
                    op_str = op_str + '({}, {}, {}, {})'.format(Op_CA_list[_][2], Op_CA_list[_][0],Op_CA_list[_][3], Op_CA_list[_][1])

                elif("h" in Op_CA_list[_][0] and "p" in Op_CA_list[_][1] and "p" in Op_CA_list[_][2] and "h" in Op_CA_list[_][3]):    
                    op_str = op_str.replace("v2(","v2iajb(")
                    if Operator == "VAA" or Operator == "VBB":
                        flipsign = True
                        op_str = op_str + '({}, {}, {}, {})'.format(Op_CA_list[_][0], Op_CA_list[_][2],Op_CA_list[_][3], Op_CA_list[_][1])
                    elif Operator == "VAB":
                        op_str = op_str.replace("abab","abba")
                        op_str = op_str + '({}, {}, {}, {})'.format(Op_CA_list[_][0], Op_CA_list[_][2],Op_CA_list[_][3], Op_CA_list[_][1])

                elif("p" in Op_CA_list[_][0] and "h" in Op_CA_list[_][1] and "h" in Op_CA_list[_][2] and "p" in Op_CA_list[_][3]):    
                    op_str = op_str.replace("v2(","v2iajb(")
                    if Operator == "VAA" or Operator == "VBB":
                        flipsign = True
                        op_str = op_str + '({}, {}, {}, {})'.format(Op_CA_list[_][1], Op_CA_list[_][3],Op_CA_list[_][2], Op_CA_list[_][0])
                    elif Operator == "VAB":
                        op_str = op_str.replace("abab","abba")
                        op_str = op_str + '({}, {}, {}, {})'.format(Op_CA_list[_][1], Op_CA_list[_][3],Op_CA_list[_][2], Op_CA_list[_][0])

                # v2ijab(=v2abij) - "aaaa", "abab", "bbbb" 
                elif("h" in Op_CA_list[_][0] and "p" in Op_CA_list[_][1] and "h" in Op_CA_list[_][2] and "p" in Op_CA_list[_][3]):
                    op_str = op_str.replace("v2(","v2ijab(")
                    op_str = op_str + '({}, {}, {}, {})'.format(Op_CA_list[_][0], Op_CA_list[_][2],Op_CA_list[_][1], Op_CA_list[_][3])
                elif("p" in Op_CA_list[_][0] and "h" in Op_CA_list[_][1] and "p" in Op_CA_list[_][2] and "h" in Op_CA_list[_][3]):
                    op_str = op_str.replace("v2(","v2ijab(")
                    op_str = op_str + '({}, {}, {}, {})'.format(Op_CA_list[_][1], Op_CA_list[_][3],Op_CA_list[_][0], Op_CA_list[_][2])

                # v2iabc(=v2aicb)(=v2bcia)(=v2cbai) - "aaaa", "abab", "baba", "bbbb" 
                elif("h" in Op_CA_list[_][0] and "p" in Op_CA_list[_][1] and "p" in Op_CA_list[_][2] and "p" in Op_CA_list[_][3]):
                    op_str = op_str.replace("v2(","v2iabc(")
                    op_str = op_str + '({}, {}, {}, {})'.format(Op_CA_list[_][0], Op_CA_list[_][2],Op_CA_list[_][1], Op_CA_list[_][3])
                
                elif("p" in Op_CA_list[_][0] and "h" in Op_CA_list[_][1] and "p" in Op_CA_list[_][2] and "p" in Op_CA_list[_][3]):
                    op_str = op_str.replace("v2(","v2iabc(")
                    op_str = op_str + '({}, {}, {}, {})'.format(Op_CA_list[_][1], Op_CA_list[_][3],Op_CA_list[_][0], Op_CA_list[_][2])

                elif("p" in Op_CA_list[_][0] and "p" in Op_CA_list[_][1] and "h" in Op_CA_list[_][2] and "p" in Op_CA_list[_][3]):
                    if Operator == "VAB":
                        op_str = op_str.replace("abab","baba")
                    op_str = op_str.replace("v2(","v2iabc(")
                    op_str = op_str + '({}, {}, {}, {})'.format(Op_CA_list[_][2], Op_CA_list[_][0],Op_CA_list[_][3], Op_CA_list[_][1])

                elif("p" in Op_CA_list[_][0] and "p" in Op_CA_list[_][1] and "p" in Op_CA_list[_][2] and "h" in Op_CA_list[_][3]):
                    if Operator == "VAB":
                        op_str = op_str.replace("abab","baba")
                    op_str = op_str.replace("v2(","v2iabc(")
                    op_str = op_str + '({}, {}, {}, {})'.format(Op_CA_list[_][3], Op_CA_list[_][1],Op_CA_list[_][2], Op_CA_list[_][0])  

                # v2abcd - "aaaa", "abab", "bbbb" 
                elif("p" in Op_CA_list[_][0] and "p" in Op_CA_list[_][1] and "p" in Op_CA_list[_][2] and "p" in Op_CA_list[_][3]):
                    op_str = op_str.replace("v2(","v2abcd(")
                    op_str = op_str + '({}, {}, {}, {})'.format(Op_CA_list[_][0], Op_CA_list[_][2],Op_CA_list[_][1], Op_CA_list[_][3])

                else:
                    print("Have not coded up this", Operator, Op_CA_list[_])

            elif Operator in ["T1A","T1B"]:
                op_str = op_str + '({}, {})'.format(Op_CA_list[_][0], Op_CA_list[_][1])

            elif Operator in ["T1A+","T1B+"]:
                op_str = op_str + '({}, {})'.format(Op_CA_list[_][1], Op_CA_list[_][0])

            elif Operator in ["T2AA","T2AB","T2BB"]:
                op_str = op_str + '({}, {}, {}, {})'.format(Op_CA_list[_][0], Op_CA_list[_][2],Op_CA_list[_][1], Op_CA_list[_][3])

            elif Operator in ["T2AA+","T2AB+","T2BB+"]:
                op_str = op_str + '({}, {}, {}, {})'.format(Op_CA_list[_][1], Op_CA_list[_][3],Op_CA_list[_][0], Op_CA_list[_][2])

            else:
                print("Have not programmed, ",operator)

            if _ != len(Op_CA_list)-1:
                eqn_str = eqn_str + op_str + " * "
            else: 
                eqn_str = eqn_str + op_str

        if flipsign:
            if "-" in eqn_str:
                eqn_str.replace("-","")
            elif "-" not in eqn_str:
                eqn_str = "-"+eqn_str
                


    print(eqn_str) 

# %%



