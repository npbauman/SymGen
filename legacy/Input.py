# [Bra][Left][exp(-O)][Hamiltonian][exp(O)][Right][Ket]

### Bra ###
Bra = [""]

### Ket ###
Ket = [""]

### Left ###
# Left = ["Y1A ", "Y1B ", "Y2AA ", "Y2AB ", "Y2BB "]
# Left = ["", "Y1A ", "Y2AA "]
Left = [""]

### Right ###
Right = [""]

### Hamiltonian ###
# Hamiltonian = ["FA ", "FB ", "VAA ", "VAB ", "VBB "]
Hamiltonian = ["FA ", "VAA "]

### Exponential ###
# Also, only the operator for exp(O) is defined as exp(-O) will be taken care of internally
# Example 1: exp(T1-T1+) = ["T1 "," -T1+ "]
# Example 2: exp(T-T+), where T=T1+T2 = ["T1 ","-T1+ ","T2 ","-T2+ "] or ["T1 ","T2 ","-T1+ ","-T2+ "]
Opp = ["T1A ", "T2AA ", "T3AAA "]
# Opp = ["T1A ", "T1B ", "T2AA ", "T2AB ", "T2BB "]


### Highest Order or Commutator ###
# Sets max number of operators per exponential, but also the commutator limit.
Comm_order = 4

print("              INPUT")
print("-"*35)
print("        Bra = ", Bra)
print("        Ket = ", Ket)
print("       Left = ", Left)
print("      Right = ", Right)
print("Hamiltonian = ", Hamiltonian)
print("        Opp = ", Opp)
print(" Comm_order = ", Comm_order)
print("-"*35+"\n")