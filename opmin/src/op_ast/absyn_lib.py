from .error import ASTError
from .absyn import Array, Addition, Multiplication


def renameIndices(e, ren_tab):
    if (len(list(ren_tab.keys())) == 0):
        return e

    if (isinstance(e, Array)):
        e.upper_inds = [ren_tab.get(x, x) for x in e.upper_inds]
        e.lower_inds = [ren_tab.get(x, x) for x in e.lower_inds]
        e.sym_groups = [[ren_tab.get(x, x) for x in g] for g in e.sym_groups]

    elif (isinstance(e, Addition)):
        e.upper_inds = [ren_tab.get(x, x) for x in e.upper_inds]
        e.lower_inds = [ren_tab.get(x, x) for x in e.lower_inds]
        e.sym_groups = [[ren_tab.get(x, x) for x in g] for g in e.sym_groups]
        for se in e.subexps:
            renameIndices(se, ren_tab)

    elif (isinstance(e, Multiplication)):
        ren_tab = filterRenamingTable(ren_tab, e.upper_inds + e.lower_inds)
        ren_tab = extendRenamingTable(ren_tab, e.sum_inds)
        e.upper_inds = [ren_tab.get(x, x) for x in e.upper_inds]
        e.lower_inds = [ren_tab.get(x, x) for x in e.lower_inds]
        e.sum_inds = [ren_tab.get(x, x) for x in e.sum_inds]
        e.sym_groups = [[ren_tab.get(x, x) for x in g] for g in e.sym_groups]
        e.sum_sym_groups = [[ren_tab.get(x, x) for x in g] for g in e.sum_sym_groups]
        for o in e.ops:
            o.sym_groups = [[ren_tab.get(x, x) for x in g] for g in o.sym_groups]
        for se in e.subexps:
            renameIndices(se, ren_tab)

    else:
        raise ASTError('%s: unknown expression' % __name__)


def buildRenamingTable(from_inames, to_inames):
    ren_tab = {}
    for (f, t) in zip(from_inames, to_inames):
        if (f != t):
            ren_tab[f] = t
    return ren_tab


def filterRenamingTable(ren_tab, inames):
    filtered_ren_tab = {}
    for (f, t) in ren_tab.items():
        if (f in inames):
            filtered_ren_tab[f] = t
    return filtered_ren_tab


def extendRenamingTable(ren_tab, inames):
    if (len(inames) > 0):
        ren_tab = ren_tab.copy()
        reversed_ren_tab = {}
        for (f, t) in ren_tab.items():
            reversed_ren_tab[t] = f
        for i in inames:
            cur_i = i
            while (cur_i in reversed_ren_tab):
                cur_i = reversed_ren_tab[cur_i]
            if (i != cur_i):
                ren_tab[i] = cur_i
    return ren_tab
