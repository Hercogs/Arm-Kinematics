"""
Find the Denavit-Hartenberg parameters for all three joints.
Compute the Homogeneous Matrix for transforming from Frame 0 to Frame 3.
Save all the Homogeneous matrixes, simplified, in png files (as shown in this course).
The matrixes that have to be generated are: A0_1,A1_2,A2_3, A0_3, A1_3.
This script is recomended to be in a class
"""
from sympy import Matrix, cos, sin, Symbol, simplify, trigsimp
from sympy.interactive import printing
from sympy import preview
import math

class GenerateMatrixes:
    def __init__(self):
        


# To make display prety
printing.init_printing(use_latex = True)

theta_i = Symbol("theta_i")
alpha_i = Symbol("alpha_i")
r_i = Symbol("r_i")
d_i = Symbol("d_i")

DH_Matric_Generic = Matrix([[cos(theta_i), -sin(theta_i)*cos(alpha_i), sin(theta_i)*sin(alpha_i), r_i*cos(theta_i)],
                            [sin(theta_i), cos(theta_i)*cos(alpha_i), -cos(theta_i)*sin(alpha_i), r_i*sin(theta_i)],
                            [0, sin(alpha_i), cos(alpha_i), d_i],
                            [0,0,0,1]])

# Create A01
theta_1 = Symbol('theta_1')
r_1 = Symbol('r_1') # 0.0
d_1 = 0
alpha_1 = math.radians(90)

A01 = DH_Matric_Generic.subs(r_i,r_1).\
                        subs(alpha_i,alpha_1).\
                        subs(d_i,d_1).\
                        subs(theta_i, theta_1)
A01_simplify = trigsimp(A01)

# Create A12
theta_2 = Symbol('theta_2')
r_2 = Symbol('r_2') # 1.0
d_2 = 0
alpha_2 = 0

A12 = DH_Matric_Generic.subs(r_i,r_2).\
                        subs(alpha_i,alpha_2).\
                        subs(d_i,d_2).\
                        subs(theta_i, theta_2)
A12_simplify = trigsimp(A12)

# Create A23
theta_3 = Symbol('theta_3')
r_3 = Symbol('r_3') # 1.0
d_3 = 0
alpha_3 = 0

A23 = DH_Matric_Generic.subs(r_i,r_3).\
                        subs(alpha_i,alpha_3).\
                        subs(d_i,d_3).\
                        subs(theta_i, theta_3)
A23_simplify = trigsimp(A23)

# Create A03
A03 = A01 * A12 * A23
A03_simplify = trigsimp(A03)

# Create A13
A13 = A12 * A23
A13_simplify = trigsimp(A13)


# Save to images
preview(A01, viewer='file', filename='A01.png', dvioptions=['-D','300'])
preview(A12, viewer='file', filename='A12.png', dvioptions=['-D','300'])
preview(A23, viewer='file', filename='A23.png', dvioptions=['-D','300'])

preview(A03, viewer='file', filename='A03.png', dvioptions=['-D','300'])
preview(A13, viewer='file', filename='A13.png', dvioptions=['-D','300'])


preview(A01_simplify, viewer='file', filename='A01_simplify.png', dvioptions=['-D','300'])
preview(A12_simplify, viewer='file', filename='A12_simplify.png', dvioptions=['-D','300'])
preview(A23_simplify, viewer='file', filename='A23_simplify.png', dvioptions=['-D','300'])

preview(A03_simplify, viewer='file', filename='A03_simplify.png', dvioptions=['-D','300'])
preview(A13_simplify, viewer='file', filename='A13_simplify.png', dvioptions=['-D','300'])




if __name__=='__main__':
    print('Jēkabs')
