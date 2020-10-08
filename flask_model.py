class Car:
    def __init__(self,name, speeed):
        self.name = name
        self.speeed = speeed

car = Car('BMW','100Mph')
car.speeed

li = [1,2,3,4]
print(list(map(lambda x: x+3, li)))
print([i+3 for i in li])

import numpy as np
a = np.array([1,2,3,45,"sd"])
print(a)