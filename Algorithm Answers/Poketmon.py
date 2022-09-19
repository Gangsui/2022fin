nums=[3,1,2,3]
Mok=len(nums)//2
Numbs_set=set(nums)
numbs=list(Numbs_set)
count_numbs=len(numbs)

if Mok>count_numbs:
    Mok=count_numbs
else:
    count_numbs=count_numbs


print(count_numbs)
