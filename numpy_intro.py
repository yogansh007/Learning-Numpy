import numpy as np

arr0=np.array(112)
arr1=np.array([1,2,3,4])
arr2=np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4]])
arr3=np.array([[[1,2,3,4],[1,2,3,4],[1,2,3,4]],[[1,2,3,4],[1,2,3,4],[1,2,3,4]]],ndmin=10)
print(arr0)
print(arr0.ndim)

print(arr1)
print(arr1.ndim)


print(arr2)
print(arr2.ndim)

print(arr3)
print(arr3.ndim)