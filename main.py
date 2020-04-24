# ******************************************************************************* #
#                                                                             	  #
#     main.py                                                    ♥           	  #
#                                                                 ¨/\_/\ ♥    	  #
#     By: zkerriga                                                 >^,^<     	  #
#                                                                   / \     	  #
#     Created: 2020-04-24 12:22:22 by zkerriga                     (___)__  	  #
#     Updated: 2020-04-24 20:28:09 by zkerriga                              	  #
#                                                                             	  #
# ******************************************************************************* #

from pyrogram import Client, MessageHandler, Filters
import time

TEST_BOT = 1103314091
status = 'begin' 
# stack = []
# cache = {}

# api_id and api_hash located in the file config.ini
app = Client("my_account")
app.start()
app.send_message(TEST_BOT, "/start")

@app.on_message(Filters.text)
def begin(client, message):
	global status

	time.sleep(1)
	if status == 'begin':
		print('[+] Bot started')
		status = 'info_start'
		app.send_message(TEST_BOT, "Полезно знать")
		time.sleep(1)
	elif status == 'info_start':
		print('[+] Info')
		status = 'info_profilactic'
		app.send_message(TEST_BOT, "Напомнить меры профилактики")
		time.sleep(1)
	elif status == 'info_profilactic':
		print('[+] Info->Profilactic->1')
		status = 'info_profilactic_1'
		app.send_message(TEST_BOT, "Как не заразиться?")
		time.sleep(1)
	elif status == 'info_profilactic_1':
		print('[+] Info->Profilactic->1->ok')
		status = 'info_profilactic_1_ok'
		app.send_message(TEST_BOT, "Понятно")
		# time.sleep(1)
	elif status == 'info_profilactic_1_ok':
		print('[+] Info->Profilactic->2')
		status = 'info_profilactic_2'
		app.send_message(TEST_BOT, "Как не заразить окружающих?")
		time.sleep(1)
	elif status == 'info_profilactic_2':
		print('[+] Info->Profilactic->2->ok')
		status = 'info_profilactic_2_ok'
		app.send_message(TEST_BOT, "Понятно")
		# time.sleep(1)
	elif status == 'info_profilactic_2_ok':
		print('[+] Info->Profilactic->3')
		status = 'info_profilactic_3'
		app.send_message(TEST_BOT, "Когда стоит вызывать врача?")
		time.sleep(1)
	elif status == 'info_profilactic_3':
		print('[+] Info->Profilactic->3->ok')
		status = 'info_profilactic_3_ok'
		app.send_message(TEST_BOT, "Понятно")
		# time.sleep(1)
	elif status == 'info_profilactic_3_ok':
		print('[+] Info->Profilactic->end')
		status = 'info_profilactic_end'
		app.send_message(TEST_BOT, "Вернуться")
		# time.sleep(1)
	elif status == 'info_profilactic_end':
		print('[+] Info')
		status = 'info_start_2'
		app.send_message(TEST_BOT, "Полезно знать")
		time.sleep(1)
	elif status == 'info_start_2':
		print('[+] Info->Lawyers')
		status = 'info_start_lawyers'
		app.send_message(TEST_BOT, "Советы юристов")
		time.sleep(1)
	elif status == 'info_start_lawyers':
		print('[+] Info->Lawyers->1')
		status = 'info_start_lawyers_1'
		app.send_message(TEST_BOT, "Что будет, если нарушить карантин?")
		time.sleep(1)

	elif status == 'info_start_lawyers_1':
		print('[+] Info->Lawyers->1->ok')
		status = 'info_start_lawyers_1_ok'
		app.send_message(TEST_BOT, "Понятно")
		# time.sleep(1)
	elif status == 'info_start_lawyers_1_ok':
		print('[+] Info->Lawyers->2')
		status = 'info_start_lawyers_2'
		app.send_message(TEST_BOT, "Как вести себя при задержании?")
		time.sleep(1)
	elif status == 'info_start_lawyers_2':
		print('[+] Info->Lawyers->2->ok')
		status = 'info_start_lawyers_2_ok'
		app.send_message(TEST_BOT, "Понятно")
		# time.sleep(1)
	elif status == 'info_start_lawyers_2_ok':
		print('[+] Info->Lawyers->3')
		status = 'info_start_lawyers_3'
		app.send_message(TEST_BOT, "Могут ли меня уволить?")
		time.sleep(1)
	elif status == 'info_start_lawyers_3':
		print('[+] Info->Lawyers->3->ok')
		status = 'info_start_lawyers_3_ok'
		app.send_message(TEST_BOT, "Понятно")
		# time.sleep(1)
	elif status == 'info_start_lawyers_3_ok':
		print('[+] Info->Lawyers->end')
		status = 'end'
		app.send_message(TEST_BOT, "Вернуться")
		# time.sleep(1)
	elif status == 'end':
		print("[+] SUCCESS")
	else:
		print('[-] Error! Stopped status:', status)





# @app.on_message()
# def main_answer(client, message):
# 	global stack
# 	time.sleep(1)
# 	try:
# 		for el in message.reply_markup.keyboard[::-1]:
# 			for btn in el:
# 				# if (btn != 'Вернуться'):
# 				stack.append(btn)
# 				print(stack[-1])
# 		time.sleep(3)
# 	except:
# 		print("Empty keyboard", stack[-1])
# 	run_stack()

# def run_stack():
# 	time.sleep(3)
# 	global stack
# 	global cache
# 	if (stack[-1] == 'Понятно' or stack[-1] == 'Вернуться' or cache.get(stack[-1], 0) == 0):
# 		cache[stack[-1]] = 1
# 		app.send_message(TEST_BOT, stack.pop())
# 		time.sleep(4)
# 	else:
# 		stack.pop()
# 		time.sleep(2)
# 		run_stack()

