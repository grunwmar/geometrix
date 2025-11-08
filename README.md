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
```
...
with G3() as a:

    r = 2*a["x"] + -5*a["y"] # Lever
    F = 5*a["x"] + 3*a["y"]  # Force
    
    print("r =          ", r)
    print("F =          ", F)
    print("M + s = rF = ", r ^ F)
...
```
**run**
```
$python ./alg_test.py

 r =           {    2·[x]    -5·[y] }
 F =           {    5·[x]     3·[y] }
 p + M = rF =  {   -5·[1]    31·[xy] }

note:
  p is some scalar number which appeared (and can expres some work done?)
  M is moment of force and it is bivector (or sometimes pseudovector)

```
