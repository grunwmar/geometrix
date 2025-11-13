from abc import ABC as Abstract
from abc import abstractmethod as abstract
from .helpers import check_matrix_dim
from .helpers import _apply_on_matrix
from .helpers import sgn
from .helpers import _mod_add
from .helpers import _mod_mul
from .helpers import prettyfy
    
    
class Vector:

    def __init__(self, parent, coeffs):
    
        if parent.size != len(coeffs):
            raise ValueError("Incompatible number of elements.")
            
        self._parent = parent
        self._mod = parent.mod
        
        if self._parent.mod is not None:
            self._coeffs = [c % self._mod for c in coeffs]
        else:
            self._coeffs = coeffs

    def __getitem__(self, item):
        if item is ...:
            return tuple(self._coeffs)
        else:
            return self._coeffs[item]

    def __call__(self, coeffs):
        return self.__class__(self._parent, coeffs)

    def _nmul(self, other):
        return self([other*i for i in self._coeffs])

    def __mul__(self, other):
        return self._nmul(other)

    def __rmul__(self, other):
        return self._nmul(other)

    def __neg__(self):
        return self._nmul(-1)

    def __add__(self, other):
        coeff_a = self[...]
        coeff_b = other[...]
        return self([_mod_add(a,b, self._mod) for a, b in zip(coeff_a, coeff_b)])

    def __sub__(self, other):
        coeff_a = self[...]
        coeff_b = other[...]
        return self([_mod_add(a, -b, self._mod) for a, b in zip(coeff_a, coeff_b)])

    def __xor__(self, other):
        coeff_a = self[...]
        coeff_b = other[...]
        result = self._parent.mul(coeff_a, coeff_b)
        return self(result)

    @property
    def pseudo_scalar(self):
        return self[-1]
        
    @property
    def scalar(self):
        return self[0]
        
    def __str__(self):
        return prettyfy(self[...], self._parent._labels, self._parent.dim, self._parent.no_labels)
        


class Algebra(Abstract):

    def __init__(self, labels=None):
        if labels is None:
            dim, matrix, labels, mod = self.init_table()
            
        self.size = check_matrix_dim(matrix, len(labels))
        self.dim = dim
        self._labels = [f"{i}" for i in labels]
        self.mod = mod
        self._matrix = matrix
        self._dict = {self._labels[i]:self[i] for i in range(self.size)}
        self.no_labels = False


    @abstract
    def init_table(self) -> (list[int, int], list[str], int): ...

    @property
    def matrix(self, i, j):
        return self._matrix[i][j]

    def __str__(self):
        return "Algebra[" + ",".join(self._labels) + "]"


    def vector(self, *c):
        return Vector(self, c)

    def __enter__(self):
        if self.dim is None:
            raise ValueError("Variable dim must be set.")
        return self

    def __exit__(self, *x):
        ...

    def mul(self, coeffs_a, coeffs_b):
        new_coeffs = [0 for _ in range(self.size)]
        
        for i,x in enumerate(coeffs_a):
            for j,y in enumerate(coeffs_b):
                c = self._matrix[i][j]
                k, sgn = int(c.real), int(c.imag)
                z = _mod_mul(x, y, self.mod)
                new_coeffs[k] += sgn*z
        return new_coeffs

    def __getitem__(self, item):
        if isinstance(item, int):
            nulls = [0 for _ in range(self.size)]
            nulls[item] = 1
            return self.vector(*nulls)
        elif isinstance(item, str):
            return self._dict[item]

