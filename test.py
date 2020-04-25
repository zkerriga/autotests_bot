# ******************************************************************************* #
#                                                                             	  #
#     test.py                                                    ♥           	  #
#                                                                 ¨/\_/\ ♥    	  #
#     By: zkerriga                                                 >^,^<     	  #
#                                                                   / \     	  #
#     Created: 2020-04-25 10:11:47 by zkerriga                     (___)__  	  #
#     Updated: 2020-04-25 13:07:05 by zkerriga                              	  #
#                                                                             	  #
# ******************************************************************************* #

from telethon import TelegramClient, events
from config import api_id, api_hash

TEST_BOT = 1103314091
BACK = 'Вернуться'
GOTIT = 'Понятно'
want_to_help = [ BACK, 'Поддержать НКО и местные инициативы',
				'Распространить полезную информацию',
				'Стать волонтером', 'Обратная связь']
become_a_volunteer = [	 BACK, 'У меня есть медицинские навыки',
						'Хочу помочь нуждающимся']

client = TelegramClient('zkerriga', api_id, api_hash)

@client.on(events.NewMessage(outgoing=True, pattern=r'/start'))
async def handler(event):
	print('[+] Bot started')
	await client.send_message(TEST_BOT, 'Хочу помочь')

@client.on(events.NewMessage(pattern=r'Отлично! Вот несколько вариантов\.'))
async def handler(event):
	print('[+] Want to help started')
	await client.send_message(TEST_BOT, want_to_help.pop())

@client.on(events.NewMessage(pattern=r'Напишите здесь, что вы хотели бы мне передать\.'))
async def handler(event):
	print('[+] Want to help -> Feedback')
	await client.send_message(TEST_BOT, "[+] Zkerriga's test feedback")

@client.on(events.NewMessage(pattern=r'Спасибо за ваше сообщение, оно передано разработчикам!.*'))
async def handler(event):
	print('[+] Want to help -> Feedback -> Send')
	await client.send_message(TEST_BOT, BACK)

@client.on(events.NewMessage())
async def handler(event):
	if event.forward and event.text.find('test feedback') > 0:
		print('[+] Want to help -> Feedback -> Send -> Ok')

@client.on(events.NewMessage(pattern=r'Какая форма волонтерства вам подходит.*'))
async def handler(event):
	print('[+] Want to help -> Voluntier')
	await client.send_message(TEST_BOT, become_a_volunteer.pop())

@client.on(events.NewMessage(pattern=r'.*волонтеры фонда помогают.*'))
async def handler(event):
	print('[+] Want to help -> Voluntier -> I want -> Ok')
	await client.send_message(TEST_BOT, GOTIT)

@client.on(events.NewMessage(pattern=r'.*главной больницы Москвы.*'))
async def handler(event):
	print('[+] Want to help -> Voluntier -> I have -> Ok')
	await client.send_message(TEST_BOT, GOTIT)


client.start()
client.run_until_disconnected()