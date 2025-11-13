# Geometrix

**Matrix representation**
Matrix has to contain complex number. The real part expresses an 'address'
where to add new number to vector. The imaginary part contains information
about the sign of produc.
E.g.
```
    3y  ^ 5x  =  15yx = -15xy
    3xy ^ 5xy = -15I          (I = 1 as basis element)
```
As  elements `1`, `x`, `y`, `xy`, `...`, `yz`, `xyz...` are mapped as number `0-n` 
representing indices, number zero can't bear information about sign.
For example element `1 (I)` has index `0` and information of sign if it was
was `+1` or `-1` can't be recovered.

therefore, item `-15I` is stored as `(15; 0-i)` and `3y` as `(3; 2+i)`

Resulting matrix has to have similar form (here is example of matrix for G2)

```python
matrix_g2 = [
                [	  1j,	  1+1j,	    2+1j,	3+1j,	],
                [	1+1j,   	1j,	    3+1j,	2+1j,	],
                [	2+1j,	  3-1j,	      1j,	1-1j,	],
                [	3+1j,	  2-1j,	    1+1j,    -1j,	],
            ]
```
and is applied to abstract class `Algebra` as follows
```python
# Geometric algebra |G2|=4 of standart 2D physical space
class G2(Algebra):
    def init_table(self):
        labels = ["1", "x", "y", "xy"]
        matrix = [
                    [	  1j,	  1+1j,	    2+1j,	3+1j,	],
                    [	1+1j,   	1j,	    3+1j,	2+1j,	],
                    [	2+1j,	  3-1j,	      1j,	1-1j,	],
                    [	3+1j,	  2-1j,	    1+1j,    -1j,	],
                ]
        return matrix, labels, None
```
## Example of code run

**code**

```python
#example
with G3() as alg:
    alg.no_labels = False

    r = 2*alg["x"] + -5*alg["y"] # Lever
    F = 5*alg["x"] + 3*alg["y"]  # Force
    
    product = r ^ F
    
    print("r= ", r)
    print("F= ", F)
    print("Fr=", product)
#-----------------------------------------------
# RESULT
# r=  (I~[[x]= 2, [y]= -5, [z]= 0])
# F=  (I~[[x]= 5, [y]= 3, [z]= 0])
# Fr= (-5;  II~[[xy]= 31, [xz]= 0, [yz]= 0])
#
#
# note:
#   p is some scalar number which appeared (and can expres some work done?)
#   M is moment of force and it is bivector (or sometimes pseudovector)
```

```python
#example
with G3() as alg:
    alg.no_labels = True

    r = 2*alg["x"] + -5*alg["y"] # Lever
    F = 5*alg["x"] + 3*alg["y"]  # Force
    
    product = r ^ F
    
    print("r= ", r)
    print("F= ", F)
    print("Fr=", product)
    
#-----------------------------------------------
# RESULT (no labels allowed)
# r=  (I~[2, -5, 0])
# F=  (I~[5, 3, 0])
# Fr= (-5;  II~[31, 0, 0])
#
#
# note:
#   p is some scalar number which appeared (and can expres some work done?)
#   M is moment of force and it is bivector (or sometimes pseudovector)

```
