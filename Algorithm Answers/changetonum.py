def solution(s):
    answer=''
    nums={
    0:'zero',
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine'
}
    
    li_nums=list(nums)

    for num in range(0,10):
        di=nums[num]
        
        if di in s:
            s=s.replace(nums[num],str(li_nums[num]))
            
            print(s)
    return answer

print(solution("one4seveneight"))