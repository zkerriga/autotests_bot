# ******************************************************************************* #
#                                                                             	  #
#     main.py                                                    ♥           	  #
#                                                                 ¨/\_/\ ♥    	  #
#     By: zkerriga                                                 >^,^<     	  #
#                                                                   / \     	  #
#     Created: 2020-04-24 12:22:22 by zkerriga                     (___)__  	  #
#     Updated: 2020-04-24 15:14:44 by zkerriga                              	  #
#                                                                             	  #
# ******************************************************************************* #

from pyrogram import Client, MessageHandler
import time

TEST_BOT = 1103314091
stack = []

# api_id and api_hash located in the file config.ini
app = Client("my_account")

app.start()
app.send_message(TEST_BOT, "/start")

@app.on_message()
def main_answer(client, message):
	global stack
	try:
		for el in message.reply_markup.keyboard:
			for btn in el:
				if (btn != 'Вернуться'):
					stack.append(btn)
				print(stack)
				time.sleep(2)
	except:
		print("Empty keyboard", stack[-1])
	run_stack()

def run_stack():
	global stack
	app.send_message(TEST_BOT, stack.pop())
	return stack

# if (len(stack) == 0):
# 	print('Все тесты пройдены')
# else:
# 	print(stack)