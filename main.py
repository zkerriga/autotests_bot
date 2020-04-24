# ******************************************************************************* #
#                                                                             	  #
#     main.py                                                    ♥           	  #
#                                                                 ¨/\_/\ ♥    	  #
#     By: zkerriga                                                 >^,^<     	  #
#                                                                   / \     	  #
#     Created: 2020-04-24 12:22:22 by zkerriga                     (___)__  	  #
#     Updated: 2020-04-24 12:45:45 by zkerriga                              	  #
#                                                                             	  #
# ******************************************************************************* #

from pyrogram import Client
from config import api_id, api_hash

with Client("my_account", api_id, api_hash) as app:
	app.send_message("me", "Братииииишка, я тебе покушать принёс!")
