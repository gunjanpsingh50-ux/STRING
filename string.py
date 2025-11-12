# A="aeiOUz"
# A=A+A
# A=''.join([i for i in A if not i.isupper()])
# for i in 'aeiou':
#     A=A.replace(i,'#')
# print(A)

# print all the sub array of an array
#  def subarray(A, S, E):
#      for i in range(S, E + 1):
#          print(A[i], end=" ")
#      print()


  
#print sum of every single subarray.
def subarray_sum(A, S, E):
     total = 0
     for i in range(S, E + 1):
         total += A[i]
     print(total)
     print()
def allsubarray_sum(A):
     n = len(A)
     for i in range(n):
         for j in range(i, n):
            subarray_sum(A, i, j)
A = [1, 2, 3]
allsubarray_sum(A)
(-2,1,-3,4,-1,2,1,-5,4)
