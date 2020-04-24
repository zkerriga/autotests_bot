# ******************************************************************************* #
#                                                                             	  #
#     main.py                                                    ♥           	  #
#                                                                 ¨/\_/\ ♥    	  #
#     By: zkerriga                                                 >^,^<     	  #
#                                                                   / \     	  #
#     Created: 2020-04-24 12:22:22 by zkerriga                     (___)__  	  #
#     Updated: 2020-04-24 21:33:33 by zkerriga                              	  #
#                                                                             	  #
# ******************************************************************************* #

from pyrogram import Client, MessageHandler, Filters
import time

TEST_BOT = 1103314091
status = [
			'begin', 'info_start', 'info_profilactic', 'info_profilactic_1',
			'info_profilactic_1_ok', 'info_profilactic_2', 'info_profilactic_2_ok',
			'info_profilactic_3', 'info_profilactic_3_ok', 'info_profilactic_end',
			'info_start_2', 'info_start_lawyers', 'info_start_lawyers_1', 
			'info_start_lawyers_1_ok', 'info_start_lawyers_2', 'info_start_lawyers_2_ok',
			'info_start_lawyers_3', 'info_start_lawyers_3_ok', 'end'
		 ]
i = 0

# api_id and api_hash located in the file config.ini
app = Client("my_account")
app.start()
app.send_message(TEST_BOT, "/start")

@app.on_message(Filters.text)
def begin(client, message):
	global status
	global i

	if status[i] == 'begin':
		print('[+] Bot started')
		i += 1
		app.send_message(TEST_BOT, "Полезно знать")
	elif status[i] == 'info_start':
		print('[+] Info')
		i += 1
		app.send_message(TEST_BOT, "Напомнить меры профилактики")
	elif status[i] == 'info_profilactic':
		print('[+] Info->Profilactic->1')
		i += 1
		app.send_message(TEST_BOT, "Как не заразиться?")
	elif status[i] == 'info_profilactic_1':
		print('[+] Info->Profilactic->1->ok')
		i += 1
		app.send_message(TEST_BOT, "Понятно")
	elif status[i] == 'info_profilactic_1_ok':
		print('[+] Info->Profilactic->2')
		i += 1
		app.send_message(TEST_BOT, "Как не заразить окружающих?")
	elif status[i] == 'info_profilactic_2':
		print('[+] Info->Profilactic->2->ok')
		i += 1
		app.send_message(TEST_BOT, "Понятно")
	elif status[i] == 'info_profilactic_2_ok':
		print('[+] Info->Profilactic->3')
		i += 1
		app.send_message(TEST_BOT, "Когда стоит вызывать врача?")
	elif status[i] == 'info_profilactic_3':
		print('[+] Info->Profilactic->3->ok')
		i += 1
		app.send_message(TEST_BOT, "Понятно")
	elif status[i] == 'info_profilactic_3_ok':
		print('[+] Info->Profilactic->end')
		i += 1
		app.send_message(TEST_BOT, "Вернуться")
	elif status[i] == 'info_profilactic_end':
		print('[+] Info')
		i += 1
		app.send_message(TEST_BOT, "Полезно знать")
	elif status[i] == 'info_start_2':
		print('[+] Info->Lawyers')
		i += 1
		app.send_message(TEST_BOT, "Советы юристов")
	elif status[i] == 'info_start_lawyers':
		print('[+] Info->Lawyers->1')
		i += 1
		app.send_message(TEST_BOT, "Что будет, если нарушить карантин?")
	elif status[i] == 'info_start_lawyers_1':
		print('[+] Info->Lawyers->1->ok')
		i += 1
		app.send_message(TEST_BOT, "Понятно")
	elif status[i] == 'info_start_lawyers_1_ok':
		print('[+] Info->Lawyers->2')
		i += 1
		app.send_message(TEST_BOT, "Как вести себя при задержании?")
	elif status[i] == 'info_start_lawyers_2':
		print('[+] Info->Lawyers->2->ok')
		i += 1
		app.send_message(TEST_BOT, "Понятно")
	elif status[i] == 'info_start_lawyers_2_ok':
		print('[+] Info->Lawyers->3')
		i += 1
		app.send_message(TEST_BOT, "Могут ли меня уволить?")
	elif status[i] == 'info_start_lawyers_3':
		print('[+] Info->Lawyers->3->ok')
		i += 1
		app.send_message(TEST_BOT, "Понятно")
	elif status[i] == 'info_start_lawyers_3_ok':
		print('[+] Info->Lawyers->end')
		i += 1
		app.send_message(TEST_BOT, "Вернуться")
	elif status[i] == 'end':
		print("[+] SUCCESS")

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

