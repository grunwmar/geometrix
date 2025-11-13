""" Helper functions """
import math
import roman


def check_matrix_dim(matrix, dim=None):
    if dim is None:
        dim = len(matrix)
    else:
        if dim != len(matrix):
            raise ValueError

    for row in matrix:
        if len(matrix) != dim:
            raise ValueError

    return dim


def sgn(x):
    if x == 0:
        return 0
    elif x < 0:
        return -1
    else:
        return 1



def _mod_add(a, b, mod):
    if mod is None:
        return a + b
    else:
        return (a + b) % mod



def _mod_mul(a, b, mod):
    if mod is None:
        return a * b
    else:
        return (a * b) % mod


def _apply_on_matrix(matrix, func):
    new_matrix = []
    for row in matrix:
        new_row = []
        for cell in row:
            new_row.append(func(cell))
        new_matrix.append(new_row)
    return new_matrix



def prettyfy(vlist, labels, dim, no_labels=False):

    if no_labels:
        monom_str = "{v}"
    else:
        monom_str = "[{l}]= {v}"
    layout = {}
    item_count = 0
    for n in range(dim+1):
        rank = layout.get(n)
        if rank is None:
            layout[n] = []
        comb = math.comb(dim, n)
        for k in range(comb):
            layout[n] += [(vlist[item_count], labels[item_count])]
            item_count += 1
    
    string_list = []
    
    for k, v in layout.items():
        v_ = [v for v, l in v]
        
        if (k == 0):
            
            sum_ = sum(v_)
            if sum_ == 0:
                continue
            item_ = [f"{v}" for v, l in v]
            item = ", ".join(item_)
            string_list += [item]
            
        else:
            sum_ = sum(v_)
            if sum_ == 0:
                continue
            item_ = [monom_str.format(v=v, l=l) for v, l in v]
            item = f"{roman.toRoman(k)}~["+", ".join(item_)+ f"]"
            string_list += [item]
            
    if len(string_list) > 0:        
        string = "(" +";  ".join(string_list) + ")"
    else:
        string = "(0)"

    return string
