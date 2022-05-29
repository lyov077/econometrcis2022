import numpy as np


matrix1 = np.array([(1,2,3),(4,5,6),(7,8,9)])

matrix1.shape

print(matrix1.ndim)

print(matrix1.size)

print(matrix1.reshape(1,9))

print(np.ones((3,3)))

print(np.eye(5))


print(np.full((3,3),5))

print(np.empty((3,3)))

print(np.empty(2))

matrix2 = np.array([(10,11,12),(13,14,15),(16,17,18)])

print(matrix1+matrix2)


print(np.delete(matrix1, 1, axis=0))

print(np.mean(matrix1, axis=0))

print(matrix2[1,2])
print(matrix2[: , 1])
print(matrix2[matrix2 > 10])
print(matrix1 < 5)

matrix3 = np.array([(1,4,7),(3,8,5),(9,2,6),(11,0,22)])
print(matrix3[:,1])
print(matrix3[2,:])


matrix4 = np.array([(67,4,23),(44,12,7),(88,6,0),(65,2,17)])
print(np.append(matrix4,np.array([1,2,3])))
print(matrix4[matrix4 > 5])