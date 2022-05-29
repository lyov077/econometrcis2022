import numpy as np
arr1 = np.array([1,2,3,4,5])
print(arr1.shape)

arr1 = np.array([1,2,3,4,5], dtype=np.float)
print(arr1.dtype)

arr2 = np.arange(10,20)
print(arr2)

arr3 = np.arange(0,10,1.5)
print(arr3)

arr_random = np.random.random((10,))
print(arr_random)

arr2_sqrt=np.sqrt(arr2)
print(arr2_sqrt)

arr2_sin = np.sin(arr2)
print(arr2_sin)

arr4 = np.arange(10,20)
print(arr4+arr2)
print(arr4*arr2)
print(arr4**3)
print(arr4.max())
print(arr4.mean())
print(arr4.sum())
print(arr4.std())
print(arr4 > 14)
print(arr4.ndim)
print(np.insert(arr4, 5, 4))
print(np.delete(arr4, 4))
print(np.sort(arr4))

arr5 = np.concatenate((arr1,arr2))
print(arr5)

print(arr5[(arr5 < 5)])
print(arr5[(arr5 < 10) & (arr5 > 5)])
print(arr5[(arr5 < 3) & (arr5 > 170)])
