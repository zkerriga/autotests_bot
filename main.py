# ******************************************************************************* #
#                                                                             	  #
#     main.py                                                    ♥           	  #
#                                                                 ¨/\_/\ ♥    	  #
#     By: zkerriga                                                 >^,^<     	  #
#                                                                   / \     	  #
#     Created: 2020-04-24 12:22:22 by zkerriga                     (___)__  	  #
#     Updated: 2020-04-24 15:26:32 by zkerriga                              	  #
#                                                                             	  #
# ******************************************************************************* #

from pyrogram import Client, MessageHandler
import time

TEST_BOT = 1103314091
stack = []
cache = {}

# api_id and api_hash located in the file config.ini
app = Client("my_account")

app.start()
app.send_message(TEST_BOT, "/start")

@app.on_message()
def main_answer(client, message):
	global stack
	try:
		for el in message.reply_markup.keyboard[::-1]:
			for btn in el:
				if (btn != 'Вернуться'):
					stack.append(btn)
				print(stack)
				time.sleep(2)
	except:
		print("Empty keyboard", stack[-1])
	run_stack()

def run_stack():
	time.sleep(1)
	global stack
	global cache
	if (cache.get(stack[-1], 0) == 0):
		cache[stack[-1]] = 1
		app.send_message(TEST_BOT, stack.pop())
	else:
		stack.pop()
		run_stack()

# if (len(stack) == 0):
# 	print('Все тесты пройдены')
# else:
# 	print(stack)