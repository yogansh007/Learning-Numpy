import numpy as np
import time
arr0=np.array(112)
arr1=np.array([1,2,3,4])
arr2=np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4]])
arr3=np.array([[[1,2,3,4],[1,2,3,4],[1,2,3,4]],[[1,2,3,4],[1,2,3,4],[1,2,3,4]]])
print(arr0)
print(arr0.ndim)

print(arr1)
print(arr1.ndim)


print(arr2)
print(arr2.ndim)

print(arr3)
print(arr3.ndim)


# accessing the elements with indexing

print(arr0)

print(arr1[1])

print(arr2[2,3])

print(arr3[1,0,2])



arrnew=np.array([1,2,3,4,5,6,7,8])
print(arrnew[1:5:])


arrnext=np.array([1,2,3,4],dtype='i4')
print(arrnext)
print(arrnext.dtype)



arr9=np.array([1.5,5,2,5,6,3])
arrdub=arr9.astype('i8')
print(arr9.dtype)
print(arrdub.dtype)

arr10=np.array([1,0,3,0,4])
arr10dub=arr10.astype(bool)
print(arr10.dtype)
print(arr10dub.dtype)


pyarr=[1,2,3,4]*2
print(pyarr)

numarr=np.array([1,2,3,4])*2
print(numarr)


start=time.time()
py=[x*2 for x in range(1000)]
print("time:",time.time()-start)


start=time.time()
num=np.arange(1000)*2 # numpy is FASTER than PYTHON in terms of CALCULATION with ARRAYS
print("time :",time.time()-start)



#generate arrays

zero=np.zeros((3,4))
print(zero)

one=np.ones((4,3))
print(one)

full=np.full((2,2),69)
print(full)
randm=np.random.random((2,3))*10
print(randm)

sequence=np.arange(0,20,2)
print(sequence)


#scalar 
dim1=np.array(3)
print(dim1.ndim)
print(dim1)

#vector

dim2=np.array([1,2,3,4])
print(dim2.ndim)
print(dim2)

#matrix

dim3=np.array([[1,2,3,4],[5,6,7,8]])
print(dim3.ndim)
print(dim3)


#tensor
tensor=np.array([[[1,2,3,4],[5,6,7,8]],
                 [[1,2,3,4],[5,6,7,8]]])

print(tensor)
print(tensor.ndim)


#array properties

array=np.array([[1,2,3,4],[5,6,7,8]])
print(array.size)
print(array.dtype)
print(array.ndim)
print(array.shape)


#more array proprties

arr=np.arange(12)
print(arr)
shaped=arr.reshape(3,4)
print(shaped)
flatten=shaped.flatten()
print(flatten)
raveled=shaped.ravel()
print(raveled)

flatten[0]=100
print(shaped)
#trnaspose
transpose=shaped.T
print(transpose)

