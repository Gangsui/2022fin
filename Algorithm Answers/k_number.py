array=[1, 5, 2, 6, 3, 7, 4]
commands=[4, 4, 1]

answer=[]

array1=array[commands[0]-1:commands[1]]
array1.sort()
print(array1[commands[2]-1])

# print(array1[2])






