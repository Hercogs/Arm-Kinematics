#! /usr/bin/env python3
from sympy import preview, N

from antropomorphic_project.generate_matrixes import GenerateMatrixes
# import antropomorphic_project
# m = antropomorphic_project.generate_matrixes.GenerateMatrixes()


if __name__ == '__main__':
    theta_1 = input('Please, enter theta_1: ')
    theta_2 = input('Please, enter theta_2: ')
    theta_3 = input('Please, enter theta_3: ')
    # theta_1 = 2.356194490192345
    # theta_2 = 0.5074842211955768
    # theta_3 = -2.2459278597319283

    # Get class object
    matrix = GenerateMatrixes()

    # Get given data
    r_1 = 0.0
    r_2 = 1.0
    r_3 = 1.0
    
    # Get tranfomation matrix
    A03 = matrix.A03_simplify

    # Substitute with angles
    A03_substituted = A03.subs('theta_1', theta_1)\
                                .subs('theta_2', theta_2)\
                                .subs('theta_3', theta_3)
    # Substitute with r parameter
    A03_substituted = A03_substituted.subs('r_1', r_1)\
                                    .subs('r_2', r_2)\
                                    .subs('r_3', r_3)
    # Evaluate
    A03_evaluated = N(A03_substituted)


    #preview(A03_substituted, viewer='file', filename='A03_substituted.png', dvioptions=['-D','300'])
    preview(A03_evaluated, viewer='file', filename='A03_evaluated.png', dvioptions=['-D','300'])
    print('Position: ', A03_evaluated[0:3, -1])
    print('Orientation: ', A03_evaluated[0:3, 0:3])

    