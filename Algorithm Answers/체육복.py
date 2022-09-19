def solution(n, lost, reserve):
    answer = 0
    students={}
    
    
    for n_n in range(1,n+1):
        if n_n in reserve:
            students[n_n]=3
            print("1번")
            answer+=1
        elif n_n in lost:
            students[n_n]=0
        
        else:
            students[n_n]=1
            print("2번")
            
            answer+=1
    List_studnets=list(students.values())
    for List_studnet in range(len(List_studnets)):
        if List_studnets[List_studnet] ==0:
            if List_studnets[List_studnet-1] ==3:
                answer+=1
                List_studnets[List_studnet-1]=1
            elif List_studnets[List_studnet+1]==3:
                answer+=1
                List_studnets[List_studnet+1]=1
            else:
                pass
        else:
            pass

  
    print(answer)
    return answer

solution(5,[2, 4],[ 3])