from vector import Vector, multiplication_of_products

import math

def main():
    A = Vector(2, 4)
    B = Vector(5, 2)
    angle = lambda alpha: print(math.degrees(math.acos(alpha)))
    
    alpha = A * B / multiplication_of_products(vector_one = A, vector_two = B)
    angle(alpha)


if __name__ == "__main__":
    main()
