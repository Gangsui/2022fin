def solution(queue1, queue2):
    Total=[]
    Total.extend(queue1)
    Total.extend(queue2)


    Count=0
    if sum(queue1)+sum(queue2) %2!=0:
        
        if max(Total) > ((sum(queue1)+sum(queue2))//2):

            Count=-1
        else:

            while True:
                if sum(queue1)!=sum(queue2):
                    if sum(queue1)>sum(queue2):
                        queue2.insert(len(queue2),queue1[0])
                        del queue1[0]
                        Count+=1
                            
                    else:
                        queue1.insert(len(queue1),queue2[0])
                        del queue2[0]
                        Count+=1
                    


                    
                else:
                    break
        
    else:
        Count=-1

    return Count


print(solution([1, 2, 1, 2],[4, 6, 5,1]))