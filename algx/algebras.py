from algx import Algebra

# Geometric algebra |G2|=4 of standart 2D physical space
class G2(Algebra):
    def init_table(self):
        dim = 2
        labels = ["1", "x", "y", "xy"]
        table = [
                    [	  1j,	  1+1j,	    2+1j,	3+1j,	],
                    [	1+1j,   	1j,	    3+1j,	2+1j,	],
                    [	2+1j,	  3-1j,	      1j,	1-1j,	],
                    [	3+1j,	  2-1j,	    1+1j,    -1j,	],
                ]
        return dim, table, labels, None
        
        
# Geometric algebra |G3|=8 of standart 3D physical space
class G3(Algebra):
    def init_table(self):
        dim = 3
        labels = ["1", "x", "y", "z", "xy","xz","yz","xyz"]
        table = [
[	1j,  	1+1j,  	2+1j,  	3+1j,  	4+1j,  	5+1j,  	6+1j,  	7+1j,  	],
[	1+1j,  	1j,  	4+1j,  	5+1j,  	2+1j,  	3+1j,  	7+1j,  	6+1j,  	],
[	2+1j,  	4-1j,  	1j,  	6+1j,  	1-1j,  	7-1j,  	3+1j,  	5-1j,  	],
[	3+1j,  	5-1j,  	6-1j,  	1j,  	7+1j,  	1-1j,  	2-1j,  	4+1j,  	],
[	4+1j,  	2-1j,  	1+1j,  	7+1j,  	-1j,  	6-1j,  	5+1j,  	3-1j,  	],
[	5+1j,  	3-1j,  	7-1j,  	1+1j,  	6+1j,  	-1j,  	4-1j,  	2-1j,  	],
[	6+1j,  	7+1j,  	3-1j,  	2+1j,  	5+1j,  	4-1j,  	-1j,  	1-1j,  	],
[	7+1j,  	6+1j,  	5-1j,  	4+1j,  	3-1j,  	2-1j,  	1-1j,  	-1j,  	],
                ]
        return dim, table, labels, None
        
        
"""
Matrix has to contain complex number. The real part expresses an 'address'
where to add new number to vector. The imaginary part contains information
about the sign of produc.
E.g.
    3y ^ 5x = 15yx = -25xy
    3xy ^ 5xy = -15I  (I = 1 as basis element)
    
As  elements 1,x,y,xy....,yz,xyz... are mapped as number 0-n representing
indices, number zero can't bear information about sign.
For example element 1 (I) has index 0 and information if original element
was +1 or -1 can't be recovered.

therefore, item -15I is stored as (15; 0-i) and 3y as (3; 2+i)
"""
