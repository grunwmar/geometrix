""" Helper functions """

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



def prettyfy(vlist, labels):
    new_list = [f"{x:>4}·[{L}]" for x, L in zip(vlist, labels) if x != 0]
    new_string = "  ".join(new_list)
    return f"{{ {new_string} }}"
