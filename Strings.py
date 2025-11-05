from fractions import Fraction
from Utilities import *

# def process_weight(weight, sign):
#     if abs(weight) != 0.0:
#         weight_frac = Fraction(weight).limit_denominator(1000).as_integer_ratio()
#         if sign == -1:
#             return f"-({weight_frac[0]}.0/{weight_frac[1]}.0) * " if weight_frac != (1, 1) else "-1.0 * "
#         elif sign == 1:
#             return f"({weight_frac[0]}.0/{weight_frac[1]}.0) * " if weight_frac != (1, 1) else "1.0 * "
#         else:
#             raise ValueError("Invalid sign")
#     return None

def process_weight(sweight):
    if abs(sweight) != 0.0:
        weight_frac = Fraction(sweight).limit_denominator(1000).as_integer_ratio()
        if weight_frac == (1, 1):
            return "1.0 * "
        elif weight_frac == (-1, 1):
            return "-1.0 * "
        else:
            return f"({weight_frac[0]}.0/{weight_frac[1]}.0) * "

def determine_positions(identities, operators, operators_dict):
    fixed_positions = []
    free_positions = []
    for pos, identity in enumerate(identities):
        operator = operators[identity - 1]
        if operators_dict[operator].get("Fixed"):
            fixed_positions.append(pos)
        else:
            free_positions.append(pos)
    return fixed_positions, free_positions

def label_positions(identities, contractions, ca_values, operators, operators_dict):
    fixed_start = 1
    free_start = len([i for i in identities if operators_dict[operators[i-1]].get("Fixed")]) + 1
    labels = [None] * len(identities)
    
    for pos, identity in enumerate(identities):
        contraction = find_tuple_with_value(contractions, pos)
        ca1 = ca_values[contraction[0]]
        ca2 = ca_values[contraction[1]]
        fixed1 = operators_dict[operators[identity - 1]].get("Fixed")
        fixed2 = operators_dict[operators[identity - 1]].get("Fixed")

        if fixed1:
            if "H" in ca1 or "H" in ca2:
                labels[contraction[0]] = f"h{fixed_start}"
                labels[contraction[1]] = f"h{fixed_start}"
                fixed_start += 1
            elif "P" in ca1 or "P" in ca2:
                labels[contraction[0]] = f"p{fixed_start}"
                labels[contraction[1]] = f"p{fixed_start}"
                fixed_start += 1
        else:
            if not fixed1 and not fixed2 and labels[contraction[0]] is None:
                if "H" in ca1 or "H" in ca2:
                    labels[contraction[0]] = f"h{free_start}"
                    labels[contraction[1]] = f"h{free_start}"
                    free_start += 1
                elif "P" in ca1 or "P" in ca2:
                    labels[contraction[0]] = f"p{free_start}"
                    labels[contraction[1]] = f"p{free_start}"
                    free_start += 1
    return labels




operator_mapping = {
    "FA": {
        ("h", "h"): ['(LTOp)f1_OO("aa")({0}_a, {1}_a)', False],
        ("h", "p"): ['(LTOp)f1_OV("aa")({0}_a, {1}_a)', False],
        ("p", "h"): ['(LTOp)f1_OV("aa")({1}_a, {0}_a)', False],
        ("p", "p"): ['(LTOp)f1_VV("aa")({0}_a, {1}_a)', False]
    },
    "FB": {
        ("h", "h"): ['(LTOp)f1_OO("bb")({0}_b, {1}_b)', False],
        ("h", "p"): ['(LTOp)f1_OV("bb")({0}_b, {1}_b)', False],
        ("p", "h"): ['(LTOp)f1_OV("bb")({1}_b, {0}_b)', False],
        ("p", "p"): ['(LTOp)f1_VV("bb")({0}_b, {1}_b)', False]
    },
    "VAA": {
        ("h", "h", "h", "h"): ['(LTOp)v2tensors.v2ijkl("aaaa")({0}_a, {2}_a, {1}_a, {3}_a)', False],

        ("h", "h", "h", "p"): ['(LTOp)v2tensors.v2ijka("aaaa")({0}_a, {2}_a, {1}_a, {3}_a)', False],
        ("h", "h", "p", "h"): ['(LTOp)v2tensors.v2ijka("aaaa")({1}_a, {3}_a, {0}_a, {2}_a)', False],
        ("h", "p", "h", "h"): ['(LTOp)v2tensors.v2ijka("aaaa")({2}_a, {0}_a, {3}_a, {1}_a)', False],
        ("p", "h", "h", "h"): ['(LTOp)v2tensors.v2ijka("aaaa")({3}_a, {1}_a, {2}_a, {0}_a)', False],

        ("h", "h", "p", "p"): ['(LTOp)v2tensors.v2iajb("aaaa")({0}_a, {2}_a, {1}_a, {3}_a)', False],
        ("p", "p", "h", "h"): ['(LTOp)v2tensors.v2iajb("aaaa")({2}_a, {0}_a, {3}_a, {1}_a)', False],
        ("p", "h", "h", "p"): ['(LTOp)v2tensors.v2iajb("aaaa")({2}_a, {0}_a, {1}_a, {3}_a)', True],
        ("h", "p", "p", "h"): ['(LTOp)v2tensors.v2iajb("aaaa")({0}_a, {2}_a, {3}_a, {1}_a)', True],
        
        ("h", "p", "h", "p"): ['(LTOp)v2tensors.v2ijab("aaaa")({0}_a, {2}_a, {1}_a, {3}_a)', False],
        ("p", "h", "p", "h"): ['(LTOp)v2tensors.v2ijab("aaaa")({1}_a, {3}_a, {0}_a, {2}_a)', False],

        ("h", "p", "p", "p"): ['(LTOp)v2tensors.v2iabc("aaaa")({0}_a, {2}_a, {1}_a, {3}_a)', False],
        ("p", "h", "p", "p"): ['(LTOp)v2tensors.v2iabc("aaaa")({1}_a, {3}_a, {0}_a, {2}_a)', False],
        ("p", "p", "h", "p"): ['(LTOp)v2tensors.v2iabc("aaaa")({2}_a, {0}_a, {3}_a, {1}_a)', False],
        ("p", "p", "p", "h"): ['(LTOp)v2tensors.v2iabc("aaaa")({3}_a, {1}_a, {2}_a, {0}_a)', False],

        ("p", "p", "p", "p"): ['(LTOp)v2tensors.v2abcd("aaaa")({0}_a, {2}_a, {1}_a, {3}_a)', False]
    },
    "VBB": {
        ("h", "h", "h", "h"): ['(LTOp)v2tensors.v2ijkl("bbbb")({0}_b, {2}_b, {1}_b, {3}_b)', False],

        ("h", "h", "h", "p"): ['(LTOp)v2tensors.v2ijka("bbbb")({0}_b, {2}_b, {1}_b, {3}_b)', False],
        ("h", "h", "p", "h"): ['(LTOp)v2tensors.v2ijka("bbbb")({1}_b, {3}_b, {0}_b, {2}_b)', False],
        ("h", "p", "h", "h"): ['(LTOp)v2tensors.v2ijka("bbbb")({2}_b, {0}_b, {3}_b, {1}_b)', False],
        ("p", "h", "h", "h"): ['(LTOp)v2tensors.v2ijka("bbbb")({3}_b, {1}_b, {2}_b, {0}_b)', False],

        ("h", "h", "p", "p"): ['(LTOp)v2tensors.v2iajb("bbbb")({0}_b, {2}_b, {1}_b, {3}_b)', False],
        ("p", "p", "h", "h"): ['(LTOp)v2tensors.v2iajb("bbbb")({2}_b, {0}_b, {3}_b, {1}_b)', False],
        ("p", "h", "h", "p"): ['(LTOp)v2tensors.v2iajb("bbbb")({2}_b, {0}_b, {1}_b, {3}_b)', True],
        ("h", "p", "p", "h"): ['(LTOp)v2tensors.v2iajb("bbbb")({0}_b, {2}_b, {3}_b, {1}_b)', True],
        
        ("h", "p", "h", "p"): ['(LTOp)v2tensors.v2ijab("bbbb")({0}_b, {2}_b, {1}_b, {3}_b)', False],
        ("p", "h", "p", "h"): ['(LTOp)v2tensors.v2ijab("bbbb")({1}_b, {3}_b, {0}_b, {2}_b)', False],

        ("h", "p", "p", "p"): ['(LTOp)v2tensors.v2iabc("bbbb")({0}_b, {2}_b, {1}_b, {3}_b)', False],
        ("p", "h", "p", "p"): ['(LTOp)v2tensors.v2iabc("bbbb")({1}_b, {3}_b, {0}_b, {2}_b)', False],
        ("p", "p", "h", "p"): ['(LTOp)v2tensors.v2iabc("bbbb")({2}_b, {0}_b, {3}_b, {1}_b)', False],
        ("p", "p", "p", "h"): ['(LTOp)v2tensors.v2iabc("bbbb")({3}_b, {1}_b, {2}_b, {0}_b)', False],

        ("p", "p", "p", "p"): ['(LTOp)v2tensors.v2abcd("bbbb")({0}_b, {2}_b, {1}_b, {3}_b)', False]
    },
    "VAB": {
        ("h", "h", "h", "h"): ['(LTOp)v2tensors.v2ijkl("abab")({0}_a, {2}_b, {1}_a, {3}_b)', False],

        ("h", "h", "h", "p"): ['(LTOp)v2tensors.v2ijka("abab")({0}_a, {2}_b, {1}_a, {3}_b)', False],
        ("h", "h", "p", "h"): ['(LTOp)v2tensors.v2ijka("abab")({1}_a, {3}_b, {0}_a, {2}_b)', False],
        ("h", "p", "h", "h"): ['(LTOp)v2tensors.v2ijka("baba")({2}_b, {0}_a, {3}_b, {1}_a)', False],
        ("p", "h", "h", "h"): ['(LTOp)v2tensors.v2ijka("baba")({3}_b, {1}_a, {2}_b, {0}_a)', False],

        ("h", "h", "p", "p"): ['(LTOp)v2tensors.v2iajb("abab")({0}_a, {2}_b, {1}_a, {3}_b)', False],
        ("p", "p", "h", "h"): ['(LTOp)v2tensors.v2iajb("baba")({2}_b, {0}_a, {3}_b, {1}_a)', False],

        ("h", "p", "p", "h"): ['(LTOp)v2tensors.v2iabj("abab")({0}_a, {2}_b, {1}_a, {3}_b)', False],  #*
        ("p", "h", "h", "p"): ['(LTOp)v2tensors.v2iabj("abab")({1}_a, {3}_b, {0}_a, {2}_b)', False],
        
        ("h", "p", "h", "p"): ['(LTOp)v2tensors.v2ijab("abab")({0}_a, {2}_b, {1}_a, {3}_b)', False],
        ("p", "h", "p", "h"): ['(LTOp)v2tensors.v2ijab("abab")({1}_a, {3}_b, {0}_a, {2}_b)', False],

        ("h", "p", "p", "p"): ['(LTOp)v2tensors.v2iabc("abab")({0}_a, {2}_b, {1}_a, {3}_b)', False],
        ("p", "h", "p", "p"): ['(LTOp)v2tensors.v2iabc("abab")({1}_a, {3}_b, {0}_a, {2}_b)', False],
        ("p", "p", "h", "p"): ['(LTOp)v2tensors.v2iabc("baba")({2}_b, {0}_a, {3}_b, {1}_a)', False],
        ("p", "p", "p", "h"): ['(LTOp)v2tensors.v2iabc("baba")({3}_b, {1}_a, {2}_b, {0}_a)', False],

        ("p", "p", "p", "p"): ['(LTOp)v2tensors.v2abcd("abab")({0}_a, {2}_b, {1}_a, {3}_b)', False]
    },
    "T1A": {
        ("p", "h"): ['(LTOp)t1("aa")({0}_a, {1}_a)', False]
    },
    "T1B": {
        ("p", "h"): ['(LTOp)t1("bb")({0}_b, {1}_b)', False]
    },
    "T1A+": {
        ("h", "p"): ['(LTOp)t1("aa")({1}_a, {0}_a)', False]
    },
    "T1B+": {
        ("h", "p"): ['(LTOp)t1("bb")({1}_b, {0}_b)', False]
    },
    "T2AA": {
        ("p", "h", "p", "h"): ['(LTOp)t2("aaaa")({0}_a, {2}_a, {1}_a, {3}_a)', False]
    },
    "T2AB": {
        ("p", "h", "p", "h"): ['(LTOp)t2("abab")({0}_a, {2}_b, {1}_a, {3}_b)', False]
    },
    "T2BB": {
        ("p", "h", "p", "h"): ['(LTOp)t2("bbbb")({0}_b, {2}_b, {1}_b, {3}_b)', False]
    },
    "T2AA+": {
        ("h", "p", "h", "p"): ['(LTOp)t2("aaaa")({1}_a, {3}_a, {0}_a, {2}_a)', False]
    },
    "T3AAA": {
        ("p", "h", "p", "h", "p", "h"): ['(LTOp)t3("aaaaaa")({0}_a, {2}_a, {4}_a, {1}_a, {3}_a, {5}_a)', False]
    },
    "T3AAB": {
        ("p", "h", "p", "h", "p", "h"): ['(LTOp)t3("aabaab")({0}_a, {2}_a, {4}_b, {1}_a, {3}_a, {5}_b)', False]
    },
    "T3ABB": {
        ("p", "h", "p", "h", "p", "h"): ['(LTOp)t3("abbabb")({0}_a, {2}_b, {4}_b, {1}_a, {3}_b, {5}_b)', False]
    },
    "T3BBB": {
        ("p", "h", "p", "h", "p", "h"): ['(LTOp)t3("bbbbbb")({0}_b, {2}_b, {4}_b, {1}_b, {3}_b, {5}_b)', False]
    },
    "Y1A": {
        ("h", "p"): ['(LTOp)y1("aa")({0}_a, {1}_a)', False]
    },
    "Y1B": {
        ("h", "p"): ['(LTOp)y1("bb")({0}_b, {1}_b)', False]
    },
    "Y2AA": {
        ("h", "p", "h", "p"): ['(LTOp)y2("aaaa")({0}_a, {2}_a, {1}_a, {3}_a)', False]
    },
    "Y2AB": {
        ("h", "p", "h", "p"): ['(LTOp)y2("abab")({0}_a, {2}_b, {1}_a, {3}_b)', False]
    },
    "Y2BB": {
        ("h", "p", "h", "p"): ['(LTOp)y2("bbbb")({0}_b, {2}_b, {1}_b, {3}_b)', False]
    },
}

