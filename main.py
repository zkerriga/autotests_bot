# ******************************************************************************* #
#                                                                             	  #
#     main.py                                                    ♥           	  #
#                                                                 ¨/\_/\ ♥    	  #
#     By: zkerriga                                                 >^,^<     	  #
#                                                                   / \     	  #
#     Created: 2020-04-24 12:22:22 by zkerriga                     (___)__  	  #
#     Updated: 2020-04-27 17:18:17 by zkerriga                              	  #
#                                                                             	  #
# ******************************************************************************* #

from pyrogram import Client, MessageHandler, Filters
from config import api_id, api_hash
from time import sleep
import os

TEST_BOT = 1103314091

# api_id and api_hash located in the file config.ini
app = Client("main", api_id, api_hash)
app.start()
app.send_message(TEST_BOT, "/start")
os.system("make know")
print("#1")

app.stop()