import telegram
import time
from telegram.ext import Updater
from telegram.ext import CommandHandler
from bowon import IpoCrawling

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
updater = Updater(token=token, use_context=True )
dispatcher = updater.dispatcher

ipo_list=IpoCrawling()

def start(update, context):
    context.bot.send_message(chat_id=chat_ID, text="공모주 크롤링을 시작합니다.")

def stop(update, context):
    context.bot.send_message(chat_id=chat_ID, text="공모주 크롤링을 중단합니다.")

def ipo(update, context):
    context.bot.send_message(chat_id=chat_ID, text="청약 일정 안내")
    for ipo in ipo_list:
        bot.send_message(chat_ID,ipo)

start_handler = CommandHandler('start', start)
stop_handler = CommandHandler('stop', stop)
ipo_handler = CommandHandler('ipo', ipo)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(stop_handler)
dispatcher.add_handler(ipo_handler)

updater.start_polling()
updater.idle()