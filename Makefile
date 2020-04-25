# ******************************************************************************* #
#                                                                             	  #
#     Makefile                                                   ♥           	  #
#                                                                 ¨/\_/\ ♥    	  #
#     By: zkerriga                                                 >^,^<     	  #
#                                                                   / \     	  #
#     Created: 2020-04-25 10:43:28 by zkerriga                     (___)__  	  #
#     Updated: 2020-04-25 22:20:21 by zkerriga                              	  #
#                                                                             	  #
# ******************************************************************************* #

all: backup know want need
	@echo -e "\n\033[32m[+] All tests complite! Check out log.\033[0m"

backup:
	@touch log
	@rm -f log_backup
	@mv log log_backup 

want:
	@echo -e "\n\033[32m[+] Start want test!\033[0m"
	@python3 want.py
	@echo -e "\n\033[32m[+] Test0 comlite!\033[0m"

know:
	@echo -e "\n\033[32m[+] Start know test!\033[0m"
	@python3 know.py
	@echo -e "\n\033[32m[+] Test1 comlite!\033[0m"

need:
	@echo -e "\n\033[32m[+] Start need test!\033[0m"
	@python3 need.py
	@echo -e "\n\033[32m[+] Test2 comlite!\033[0m"

clean:
	@rm -f *.session*
	@echo -e "\n\033[32m[+] Cleaned!\033[0m"
