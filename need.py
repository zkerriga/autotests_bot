# ******************************************************************************* #
#                                                                             	  #
#     need.py                                                    ♥           	  #
#                                                                 ¨/\_/\ ♥    	  #
#     By: zkerriga                                                 >^,^<     	  #
#                                                                   / \     	  #
#     Created: 2020-04-25 22:20:56 by zkerriga                     (___)__  	  #
#     Updated: 2020-04-25 23:28:52 by zkerriga                              	  #
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
need_help = [ BACK, 'Мои права нарушают', 'Другая помощь']
another_help = [BACK, 'Связаться с волонтерами', 'Психологическая помощь',
				'Помощь врачам', 'Продукты питания']
rights_troubles = [BACK, 'Задержали полицейские', 'Принудительно госпитализируют',
					'Проблемы в университете', 'Проблемы с работой']
job_troubles = [BACK, 'Сократили на работе', 'Работодатель подвергает риску']
hospitalize = [BACK, 'Я против госпитализации. Что делать?',
				'Мне угрожают уголовной ответственностью. Это законно?']

client = TelegramClient('zkerriga', api_id, api_hash)

@client.on(events.NewMessage(outgoing=True, pattern=r'/start'))
async def handler(event):
	logging.info('[+] Bot started')
	print('[+] Bot started')
	await client.send_message(TEST_BOT, 'Нужна помощь')

@client.on(events.NewMessage(pattern=r'Что с вами произошло.*'))
async def handler(event):
	logging.info('[+] Need help started')
	print('[+] Need help started')
	await client.send_message(TEST_BOT, need_help.pop())

@client.on(events.NewMessage(pattern=r'Как еще вам можно помочь.*'))
async def handler(event):
	logging.info('[+] Need help -> Another')
	print('[+] Need help -> Another')
	await client.send_message(TEST_BOT, another_help.pop())

@client.on(events.NewMessage(pattern=r'.*которая занимается помощью мигрантам.*'))
async def handler(event):
	logging.info('[+] Need help -> Another -> Food -> Ok')
	print('[+] Need help -> Another -> Food -> Ok')
	await client.send_message(TEST_BOT, GOTIT)

@client.on(events.NewMessage(pattern=r'.*благотворительный фонд «Правмир».*'))
async def handler(event):
	logging.info('[+] Need help -> Another -> Doctors -> Ok')
	print('[+] Need help -> Another -> Doctors -> Ok')
	await client.send_message(TEST_BOT, GOTIT)

@client.on(events.NewMessage(pattern=r'.*в онлайн-чате или по горячей линии .*'))
async def handler(event):
	logging.info('[+] Need help -> Another -> Pcihol -> Ok')
	print('[+] Need help -> Another -> Pcihol -> Ok')
	await client.send_message(TEST_BOT, GOTIT)

@client.on(events.NewMessage(pattern=r'Пришлите вашу геолокацию.*'))
async def handler(event):
	logging.info('[+] Need help -> Another -> Geo')
	logging.info('[-] Need help -> Another -> Geo <- Not sended')
	print('[+] Need help -> Another -> Geo')
	print('[-] Need help -> Another -> Geo <- Not sended')
	await client.send_message(TEST_BOT, geo_point=(30.379251039815593, 59.80547555591638))
	await client.send_message(TEST_BOT, 'Отмена')

@client.on(events.NewMessage(pattern=r'Чем еще я могу быть полезен.*'))
async def handler(event):
	if flag:
		logging.info('[+] SUCCESS')
		print('[+] SUCCESS\n')
		exit(0)
	else:
		await client.send_message(TEST_BOT, 'Нужна помощь')

@client.on(events.NewMessage(pattern=r'Какая у вас проблема.*'))
async def handler(event):
	logging.info('[+] Need help -> Rights')
	print('[+] Need help -> Rights')
	await client.send_message(TEST_BOT, rights_troubles.pop())

@client.on(events.NewMessage(pattern=r'Какая именно у вас проблема.*'))
async def handler(event):
	logging.info('[+] Need help -> Rights -> Job')
	print('[+] Need help -> Rights -> Job')
	await client.send_message(TEST_BOT, job_troubles.pop())

@client.on(events.NewMessage(pattern=r'.*Работодатель требует выйти на работу.*'))
async def handler(event):
	logging.info('[+] Need help -> Rights -> Job -> Risk -> Ok')
	print('[+] Need help -> Rights -> Job -> Risk -> Ok')
	await client.send_message(TEST_BOT, GOTIT)

@client.on(events.NewMessage(pattern=r'.*Что делать, если работодатель решил.*'))
async def handler(event):
	logging.info('[+] Need help -> Rights -> Job -> Fired -> Ok')
	print('[+] Need help -> Rights -> Job -> Fired -> Ok')
	await client.send_message(TEST_BOT, GOTIT)

@client.on(events.NewMessage(pattern=r'Нужна ли вам еще юридическая помощь.*'))
async def handler(event):
	logging.info('[+] Need help -> Rights')
	print('[+] Need help -> Rights')
	await client.send_message(TEST_BOT, rights_troubles.pop())

@client.on(events.NewMessage(pattern=r'.*Студенческий журнал DOXA.*'))
async def handler(event):
	logging.info('[+] Need help -> Rights -> University -> Ok')
	print('[+] Need help -> Rights -> University -> Ok')
	await client.send_message(TEST_BOT, GOTIT)

@client.on(events.NewMessage(pattern=r'Что именно происходит.*'))
async def handler(event):
	logging.info('[+] Need help -> Hospitalize')
	print('[+] Need help -> Hospitalize')
	await client.send_message(TEST_BOT, hospitalize.pop())

@client.on(events.NewMessage(pattern=r'.*На текущий момент уголовная ответственность.*'))
async def handler(event):
	logging.info('[+] Need help -> Hospitalize -> Menaces-> Ok')
	print('[+] Need help -> Hospitalize -> Menaces -> Ok')
	await client.send_message(TEST_BOT, GOTIT)

@client.on(events.NewMessage(pattern=r'.*Если гражданин категорически не согласен.*'))
async def handler(event):
	logging.info('[+] Need help -> Hospitalize -> Denie-> Ok')
	print('[+] Need help -> Hospitalize -> Denie -> Ok')
	await client.send_message(TEST_BOT, GOTIT)

@client.on(events.NewMessage(pattern=r'.*К сожалению, введение режима повышенной.*'))
async def handler(event):
	logging.info('[+] Need help -> Hospitalize -> Arrest -> Ok')
	print('[+] Need help -> Hospitalize -> Arrest -> Ok')
	global flag
	flag = True
	await client.send_message(TEST_BOT, GOTIT)

client.start()
client.run_until_disconnected()
