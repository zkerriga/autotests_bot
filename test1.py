# ******************************************************************************* #
#                                                                             	  #
#     test1.py                                                   ♥           	  #
#                                                                 ¨/\_/\ ♥    	  #
#     By: zkerriga                                                 >^,^<     	  #
#                                                                   / \     	  #
#     Created: 2020-04-25 18:00:43 by zkerriga                     (___)__  	  #
#     Updated: 2020-04-25 18:51:22 by zkerriga                              	  #
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
useful_to_know = [BACK, 'Напомнить меры профилактики', 'Советы юристов']
legal_advice = [ BACK, 'Что будет, если нарушить карантин?',
				'Как вести себя при задержании?', 'Могут ли меня уволить?']
prevention_measures = [	 BACK, 'Как не заразиться?', 'Как не заразить окружающих?',
						'Когда стоит вызывать врача?']

client = TelegramClient('zkerriga', api_id, api_hash)

@client.on(events.NewMessage(outgoing=True, pattern=r'/start'))
async def handler(event):
	logging.info('[+] Bot started')
	print('[+] Bot started')
	await client.send_message(TEST_BOT, 'Полезно знать')

@client.on(events.NewMessage(pattern=r'Что вам подсказать.*'))
async def handler(event):
	logging.info('[+] Info started')
	print('[+] Info started')
	await client.send_message(TEST_BOT, useful_to_know.pop())

@client.on(events.NewMessage(pattern=r'Что вы хотели бы узнать.*'))
async def handler(event):
	logging.info('[+] Info -> Legal advice')
	print('[+] Info -> Legal advice')
	await client.send_message(TEST_BOT, legal_advice.pop())

@client.on(events.NewMessage(pattern=r'.*если работодатель решил отправить вас.*'))
async def handler(event):
	logging.info('[+] Info -> Legal advice -> Fired -> Ok')
	print('[+] Info -> Legal advice -> Fired -> Ok')
	await client.send_message(TEST_BOT, GOTIT)

@client.on(events.NewMessage(pattern=r'Нужна ли вам еще юридическая помощь.*'))
async def handler(event):
	logging.info('[+] Info -> Legal advice')
	print('[+] Info -> Legal advice')
	await client.send_message(TEST_BOT, legal_advice.pop())

@client.on(events.NewMessage(pattern=r'.*К сожалению, введение режима повышенной.*'))
async def handler(event):
	logging.info('[+] Info -> Legal advice -> Arrest -> Ok')
	print('[+] Info -> Legal advice -> Arrest -> Ok')
	await client.send_message(TEST_BOT, GOTIT)

@client.on(events.NewMessage(pattern=r'.*если выйти на улицу без пропуска.*'))
async def handler(event):
	logging.info('[+] Info -> Legal advice -> Low break -> Ok')
	print('[+] Info -> Legal advice -> Low break -> Ok')
	await client.send_message(TEST_BOT, GOTIT)

@client.on(events.NewMessage(pattern=r'Чем еще я могу быть полезен.*'))
async def handler(event):
	logging.info('[+] Main')
	print('[+] Main')
	if flag:
		logging.info('[+] SUCCESS')
		print('[+] SUCCESS\n')
		exit(0)
	else:
		await client.send_message(TEST_BOT, 'Полезно знать')

@client.on(events.NewMessage(pattern=r'Берегите себя и близких!'))
async def handler(event):
	logging.info('[+] Info -> How')
	print('[+] Info -> How')
	await client.send_message(TEST_BOT, prevention_measures.pop())

@client.on(events.NewMessage(pattern=r'.*панику может вызвать даже легкое недомогание.*'))
async def handler(event):
	logging.info('[+] Info -> How -> When call a doctor -> Ok')
	print('[+] Info -> How -> When call a doctor -> Ok')
	await client.send_message(TEST_BOT, GOTIT)

@client.on(events.NewMessage(pattern=r'Хотите ли вы уточнить что-то еще.*'))
async def handler(event):
	logging.info('[+] Info -> How')
	print('[+] Info -> How')
	await client.send_message(TEST_BOT, prevention_measures.pop())

@client.on(events.NewMessage(pattern=r'.*При появлении признаков ОРВИ.*'))
async def handler(event):
	logging.info('[+] Info -> How -> How not 2 -> Ok')
	print('[+] Info -> How -> How not 2 -> Ok')
	await client.send_message(TEST_BOT, GOTIT)

@client.on(events.NewMessage(pattern=r'.*имеющими признаки простуды и ОРВИ.*'))
async def handler(event):
	logging.info('[+] Info -> How -> How not 1 -> Ok')
	print('[+] Info -> How -> How not 1 -> Ok')
	global flag
	flag = True
	await client.send_message(TEST_BOT, GOTIT)

client.start()
client.run_until_disconnected()
