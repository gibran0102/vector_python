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

    def rotate(self, theta):
        cos_theta = math.cos(theta)
        sin_theta = math.sin(theta)
        
        if self.z <= 0:
            self.x2 = cos_theta * self.x - sin_theta * self.y 
            self.y2 = sin_theta * self.x + cos_theta * self.y 

        return [self.x2, self.y2]


def multiplication_of_products(vector_one, vector_two):
    return vector_one.dot_product() * vector_two.dot_product()