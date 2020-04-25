# ******************************************************************************* #
#                                                                             	  #
#     Makefile                                                   ♥           	  #
#                                                                 ¨/\_/\ ♥    	  #
#     By: zkerriga                                                 >^,^<     	  #
#                                                                   / \     	  #
#     Created: 2020-04-25 10:43:28 by zkerriga                     (___)__  	  #
#     Updated: 2020-04-25 22:06:51 by zkerriga                              	  #
#                                                                             	  #
# ******************************************************************************* #

TEST0 = test.py
TEST1 = test1.py

all: backup 0 1 2
	@echo -e "\n\033[32m[+] All tests complite! Check out log.\033[0m"

backup:
	@touch log
	@mv log log_backup 

0:
	@echo -e "\n\033[32m[+] Start test0!\033[0m"
	@python3 $(TEST0)
	@echo -e "\n\033[32m[+] Test0 comlite!\033[0m"

1:
	@echo -e "\n\033[32m[+] Start test1!\033[0m"
	@python3 $(TEST1)
	@echo -e "\n\033[32m[+] Test1 comlite!\033[0m"

2:
	@echo -e "\n\033[32m[+] Start test1!\033[0m"
	
clean:
	@rm -f *.session*
	@echo -e "\n\033[32m[+] Cleaned!\033[0m"
