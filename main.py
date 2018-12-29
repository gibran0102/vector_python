from vector import Vector, multiplication_of_products

import math

def main():
    A = Vector(10, 10, 0)
    B = Vector(10, 10, 0)
    angle = lambda alpha: print(math.degrees(math.acos(alpha)))
    
    alpha = A * B / multiplication_of_products(vector_one = A, vector_two = B)
    angle(alpha)


    a_rotate = A.rotate(math.radians(180))
    b_rotate = B.rotate(math.radians(180))
    
    print(a_rotate, b_rotate)

if __name__ == "__main__":
    main()
