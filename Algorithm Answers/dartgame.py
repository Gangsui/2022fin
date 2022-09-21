def solution(dartResult):
    answer = 0
    dartResult=dartResult.replace('10','k')
    dartResult=list(dartResult)
    temp=[]
    
    for dart1 in range(len(dartResult)):
        dart=dartResult[dart1]
        
        if dartResult[dart1] in ['0','1','2','3','4','5','6','7','8','9']:
            dart=int(dart)
            answer=dart
            print(answer,temp)
        elif dartResult[dart1]=='k':
            dart=10
            answer=dart


            
        elif dart in 'S':
            answer=answer
            temp.append(answer)
            print(answer,temp)

            

        elif dart in 'D':
            answer=answer**2
            temp.append(answer)
            print(answer,temp)

            

        elif dart in 'T':
            answer=answer**3
            temp.append(answer)
            print(answer,temp)

            
        elif dart in '*':
            if len(temp) >= 2:
                temp[-1]=temp[-1]*2
                temp[-2]=temp[-2]*2
                print(answer,temp)

            else:
                temp[-1]=temp[-1]*2
                print(answer,temp)

                        
        elif dart in '#':
            temp[-1]=temp[-1]*(-1)
            print(answer,temp)

            

            
    print(sum(temp))
    return sum(temp)


solution('1S2D*3T')
