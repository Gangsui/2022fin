from Crawling_site import Search_shoes
import telegram


telegram_config={}
#config 파일 읽기
with open('./telegram_config','r') as f:
    # 모든 줄 읽어오기
    configs=f.readlines()
    # 한줄씩 확인해서
    for config in configs:
        #줄바꿈기호 제거(\n) 후 =로 문자열 분리
        #key ,value 로 언패킹 (2개 나올것이 확실 하기 때문에)
        key,value=config.rstrip().split('=')
        # config 딕셔너리에 키 값 추가
        telegram_config[key]=value
        
token=telegram_config['token']
chat_ID=telegram_config['chat_ID']
Group_ID=telegram_config['Group_ID']

bot = telegram.Bot(token)
updates = bot.get_updates()
last_id = updates[-1].update_id


while True: 
    try:
        # 신규 메시지가 없을 경우 에러가 발생 
        # list index out of range
        # 따라서, try - except 문으로 묶어줌
        new_message = bot.get_updates(offset=last_id)[-1]

        # 만약 신규 메시지가 오늘날씨면,
        if new_message.message.text == '오늘의 신발':
            Send_me=Search_shoes()
            
            
            for Final_send in Send_me:
                Final_send="".join(Final_send)
                bot.send_message(Group_ID,Final_send)
           
        last_id = new_message.update_id + 1
    except:
        pass