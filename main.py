import math

class Vector(object):
    def __init__(self, x, y, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def __mul__(self, vector):
        return self.x * vector.x + self.y * vector.y + self.z * vector.z
    
    def dot_product(self):
        return math.sqrt(self.x**2 + self.y**2+ self.z**2)


def multiplication_of_products(vector_one, vector_two):
    return vector_one.dot_product() * vector_two.dot_product()



def main():
    A = Vector(2, 4)
    B = Vector(5, 2)
    angle = lambda alpha: print(math.degrees(math.acos(alpha)))
    
    alpha = A * B / multiplication_of_products(vector_one = A, vector_two = B)
    angle(alpha)


if __name__ == "__main__":
    main()
