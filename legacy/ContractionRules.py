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