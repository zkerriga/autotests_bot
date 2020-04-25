# ******************************************************************************* #
#                                                                             	  #
#     test.py                                                    ♥           	  #
#                                                                 ¨/\_/\ ♥    	  #
#     By: zkerriga                                                 >^,^<     	  #
#                                                                   / \     	  #
#     Created: 2020-04-25 10:11:47 by zkerriga                     (___)__  	  #
#     Updated: 2020-04-25 17:55:39 by zkerriga                              	  #
#                                                                             	  #
# ******************************************************************************* #

from telethon import TelegramClient, events 
from config import api_id, api_hash
import logging
 
logging.basicConfig(filename='log', level=logging.INFO)

TEST_BOT = 1103314091
BACK = 'Вернуться'
GOTIT = 'Понятно'
flag = False
want_to_help = [ BACK, 'Поддержать НКО и местные инициативы',
				'Распространить полезную информацию',
				'Стать волонтером', 'Обратная связь']
become_a_volunteer = [BACK, 'У меня есть медицинские навыки',
					 'Хочу помочь нуждающимся']
who_need_help = [BACK, 'Уязвимым людям', 'Медицинским работникам',
				'Малому бизнесу и культуре']

client = TelegramClient('zkerriga', api_id, api_hash)

@client.on(events.NewMessage(outgoing=True, pattern=r'/start'))
async def handler(event):
	logging.info('[+] Bot started')
	print('[+] Bot started')
	await client.send_message(TEST_BOT, 'Хочу помочь')

@client.on(events.NewMessage(pattern=r'Отлично! Вот несколько вариантов\.'))
async def handler(event):
	logging.info('[+] Want to help started')
	print('[+] Want to help started')
	await client.send_message(TEST_BOT, want_to_help.pop())

@client.on(events.NewMessage(pattern=r'Напишите здесь, что вы хотели бы мне передать\.'))
async def handler(event):
	logging.info('[+] Want to help -> Feedback')
	print('[+] Want to help -> Feedback')
	await client.send_message(TEST_BOT, "[+] Zkerriga's test feedback")

@client.on(events.NewMessage(pattern=r'Спасибо за ваше сообщение, оно передано разработчикам!.*'))
async def handler(event):
	logging.info('[+] Want to help -> Feedback -> Send')
	print('[+] Want to help -> Feedback -> Send')
	await client.send_message(TEST_BOT, BACK)

@client.on(events.NewMessage(pattern=r'.*test feedback'))
async def handler(event):
	if event.forward and event.text.find('test feedback') > 0:
		logging.info('[+] Want to help -> Feedback -> Send -> Ok')
		print('[+] Want to help -> Feedback -> Send -> Ok')

@client.on(events.NewMessage(pattern=r'Какая форма волонтерства вам подходит.*'))
async def handler(event):
	logging.info('[+] Want to help -> Voluntier')
	print('[+] Want to help -> Voluntier')
	await client.send_message(TEST_BOT, become_a_volunteer.pop())

@client.on(events.NewMessage(pattern=r'.*волонтеры фонда помогают.*'))
async def handler(event):
	logging.info('[+] Want to help -> Voluntier -> I want -> Ok')
	print('[+] Want to help -> Voluntier -> I want -> Ok')
	await client.send_message(TEST_BOT, GOTIT)

@client.on(events.NewMessage(pattern=r'.*главной больницы Москвы.*'))
async def handler(event):
	logging.info('[+] Want to help -> Voluntier -> I have -> Ok')
	print('[+] Want to help -> Voluntier -> I have -> Ok')
	await client.send_message(TEST_BOT, GOTIT)

@client.on(events.NewMessage(pattern=r'.*распространить информацию о коронавирусе.*'))
async def handler(event):
	logging.info('[+] Want to help -> Share -> Ok')
	print('[+] Want to help -> Share -> Ok')
	await client.send_message(TEST_BOT, GOTIT)

@client.on(events.NewMessage(pattern=r'Кому вы хотели бы помочь.*'))
async def handler(event):
	logging.info('[+] Want to help -> Who need help')
	print('[+] Want to help -> Who need help')
	await client.send_message(TEST_BOT, who_need_help.pop())

@client.on(events.NewMessage(pattern=r'.*местных предпринимателей рядом с вами.*'))
async def handler(event):
	logging.info('[+] Want to help -> Who need help -> Business -> Ok')
	print('[+] Want to help -> Who need help -> Business -> Ok')
	await client.send_message(TEST_BOT, GOTIT)

@client.on(events.NewMessage(pattern=r'.*акцию помощи одиноким пожилым людям.*'))
async def handler(event):
	logging.info('[+] Want to help -> Who need help -> Grandpeople -> Ok')
	print('[+] Want to help -> Who need help -> Grandpeople -> Ok')
	await client.send_message(TEST_BOT, GOTIT)

@client.on(events.NewMessage(pattern=r'.*сбор средств на покупку индивидуальной защиты.*'))
async def handler(event):
	logging.info('[+] Want to help -> Who need help -> Medecine -> Ok')
	print('[+] Want to help -> Who need help -> Medecine -> Ok')
	global flag
	flag = True
	await client.send_message(TEST_BOT, GOTIT)

@client.on(events.NewMessage(pattern=r'Чем еще я могу быть полезен.*'))
async def handler(event):
	if flag:
		logging.info('[+] SUCCESS')
		print('[+] SUCCESS\n')
		exit(0)

client.start()
client.run_until_disconnected()
