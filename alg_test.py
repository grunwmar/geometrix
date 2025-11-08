from abc import ABC as Abstract
from abc import abstractmethod as abstract
from algx.algebras import G2, G3


#example
with G3() as a:

    r = 2*a["x"] + -5*a["y"] # Lever
    F = 5*a["x"] + 3*a["y"]  # Force
    
    print("r =          ", r)
    print("F =          ", F)
    print("M + s = rF = ", r ^ F)

#-----------------------------------------------
#   RESULT
#   r =           {    2·[x]    -5·[y] }
#   F =           {    5·[x]     3·[y] }
#   p + M = rF =  {   -5·[1]    31·[xy] }
#
# note:
#   p is some scalar number which appeared (and can expres some work done?)
#   M is moment of force and it is bivector (or sometimes pseudovector)

