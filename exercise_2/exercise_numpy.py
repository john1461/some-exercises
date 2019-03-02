import numpy as np
np.random.seed(1488)
array = np.random.randint(1,100, [10,9])
print(array)
list = [i.max()/i.mean() for i in array]
print(list)


