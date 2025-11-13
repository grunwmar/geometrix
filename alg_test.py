from abc import ABC as Abstract
from abc import abstractmethod as abstract
from algx.algebras import G2, G3


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

