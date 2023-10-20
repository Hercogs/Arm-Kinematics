#! /usr/bin/env python3
import math

# https://robotacademy.net.au/lesson/inverse-kinematics-for-a-2-joint-robot-arm-using-geometry/

def normalize(angle):
    return math.atan2(math.sin(angle), math.cos(angle))

def compute_ik(point: list):
    result = []

    # DH parameters 
    r_1 = 0.0
    r_2 = 1.0
    r_3 = 1.0

    # Calculate phi1
    phi_1_positive = math.atan2(point[1], point[0])
    phi_1_negative = normalize(phi_1_positive + math.pi)
    phi_1 = [phi_1_positive, phi_1_negative]
    #print(phi_1)

    for phi1 in phi_1:
        # Project from 3D to 2D space
        x = point[0] * math.cos(phi1) + point[1] * math.sin(phi1)
        y = point[2]
        #print(x, y)
        phi_3_positive = math.acos((x**2 + y**2 - r_2**2 - r_3**2)/(2 * r_2 * r_3))
        phi_3_negative = normalize(-phi_3_positive)
        phi_3 = [phi_3_positive, phi_3_negative]

        for phi3 in phi_3:
            phi2 = normalize(math.atan2(y, x) - math.atan2(r_3*math.sin(phi3), r_2 + r_3 * math.cos(phi3)))

            # Check angle limitations
            status = False

            if -math.pi/4 <= phi2 <= 3*math.pi/4 and -3*math.pi/4 <= phi3 <= 3*math.pi/4:
                status = True
            # if -3*math.pi/4 <= phi3 <= 3*math.pi/4:
            #     status = True
            

            result.append(([phi1, phi2, phi3], status))
            result.sort(key=lambda x: x[0][2])




    return result


if __name__=='__main__':
    P3 = [0.5,0.6,0.7]

    print(f'Point P3: {P3}')
    res = compute_ik(P3)
    
    for r in res:
        print(r)
