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



#accessing
sample=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(sample[:,2])


#sort


unsorted=np.array([[3,54],[63,62],[253,24]])
print(np.sort(unsorted,axis=0))

#filtering


numbers=np.array([1,2,3,4,5,6,7,8,9,10,19])
print(numbers[numbers%2==0])

#masking=stores expression in variables and diretly using them                                                  

mask=numbers > 5

print(numbers[mask])


#fancy indices

indices=[1,2,5]
print(numbers[indices])

where=np.where(numbers>5)
print(numbers[where])


#creating array with where
new_arr=np.where(numbers>7,True,False)
print(new_arr)

#array concat

arr_one=np.array([1,2,3])
arr_two=np.array([4,5,6])
print(np.concatenate((arr_one,arr_two)))

#compare shape

sh1=np.array([1,2,3,4,5])
sh2=np.array([5,2,5,4,2,4])
print(np.shape(sh1)==np.shape(sh2))

#row and column addition

before=np.array([[1,2,4,5,6],[1,2,3,4,5]])
new_row=np.array([[23,54,2,35,5]])
after=np.vstack((before,new_row))
print(after)


prev=np.array([[1,2,3],[5,6,7]])
nxt=np.array([[7],[8]])
final=np.hstack((prev,nxt))
print(final)


#deletion

before_deletion=np.array([1,3,5,3,5,3,34])
after_deletion=np.delete(before_deletion,3)
print(after_deletion)



# real life data work
# rows = monday to friday
# columms =samsung oppo vivo
sales = np.array([
    [15, 20, 18],
    [12, 25, 16],
    [18, 22, 21],
    [20, 19, 17],
    [25, 30, 28]
])

print(sales)
print("sales of samsung :", sales[:,1])

print("oppo sales thorughout the week :",np.sum(sales[:,1],axis=0))
print("overall shop unit sales on tudesday",np.sum(sales[0,:],axis=0))
