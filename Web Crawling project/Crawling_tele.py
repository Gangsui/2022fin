#cmd_handler_bot.py
from telegram.ext import Updater
from telegram.ext import CommandHandler
from Crawling_site import Search_shoes
from Crawling_site import Change_price
import telegram
import time


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

 
updater = Updater( token=token, use_context=True )
dispatcher = updater.dispatcher
 
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="신발을 찾습니다.")
 
def stop(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="작업을 중단합니다.")
 
def Shoes(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="신발을 검색합니다" )
    Send_me=Search_shoes()

    # 신발 사이트 링크가 여러개라면 풀어서 하나씩 보내기
    a=1
    for Final_send in Send_me:
        name1=str(Final_send[0])
        Price1=str(Final_send[1])
        for lin1 in Final_send[2]:
            tot=[name1,Price1,lin1]
            
            
        #     bot.send_message(Group_ID," ".join(tot))
        #     time.sleep(1)
        # time.sleep(10)

    bot.send_message(Group_ID,'조회 완료')
 
start_handler = CommandHandler('start', start)
stop_handler = CommandHandler('stop', stop)
zigbang_handler = CommandHandler('Shoes', Shoes)
 
dispatcher.add_handler(start_handler)
dispatcher.add_handler(stop_handler)
dispatcher.add_handler(zigbang_handler)
 
updater.start_polling()
updater.idle()