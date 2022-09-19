from posixpath import split


id_list=["muzi", "frodo", "apeach", "neo"]
report=["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k=2

report_set=set(report)
id_dic={}
mail_dic={}
Send_dic={}

#id를 딕셔너리로 바꿈
for id in id_list:
    id_dic[id]=0
    mail_dic[id]=[]
    Send_dic[id]=0
#신고당한 수를 카운트
for repo in report_set:
    a,b=repo.split(" ")
    id_dic[b]=+1
    mail_dic[b]=mail_dic[b]+[a]

#메일 보내기
for i in id_list:
    if len(mail_dic[i]) >2:
    

    










