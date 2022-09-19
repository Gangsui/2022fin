# a, b = map(int, input().strip().split(' '))
a=3
b=5
answer=''

for hang in range(b):
    for yul in range(a):
        answer=answer+'*'
    answer=answer+'\n'
    
print(answer)