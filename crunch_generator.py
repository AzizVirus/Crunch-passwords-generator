# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys
import os
import time

class bcolors:
	HEADER = '\033[95m' #move
	BLUE = '\033[94m' #blue
	GREEN = '\033[92m' #green
	WARNING = '\033[93m' #orange                                  
	FAIL = '\033[91m' #red
	ENDC = '\033[0m' #end color
	BOLD = '\033[1m' #gras
	UNDERLINE = '\033[4m' #underline
        BLEUCIEL = '\033[1;36m' #bleuciel

prompt = bcolors.FAIL + "PasswordList Generator By Crunch:@ " + bcolors.ENDC
start_time = time.time()

os.system("clear")

print bcolors.FAIL + "   ______                      __       ____                  __    _      __ " 
print bcolors.FAIL + "  / ____/______  ______  _____/ /_     / __ \____ ___________/ /   (_)____/ /_"
print bcolors.FAIL + " / /   / ___/ / / / __ \/ ___/ __ \   / /_/ / __ `/ ___/ ___/ /   / / ___/ __/"
print bcolors.FAIL + "/ /___/ /  / /_/ / / / / /__/ / / /  / ____/ /_/ (__  |__  ) /___/ (__  ) /_  "
print bcolors.FAIL + "\____/_/   \__,_/_/ /_/\___/_/ /_/  /_/    \__,_/____/____/_____/_/____/\__/  "
print bcolors.FAIL + "                                                                              "
print bcolors.GREEN + "   ______                           __                ____       "
print bcolors.GREEN + "  / ____/__  ____  ___  _________ _/ /_____  _____   / __ )__  __"
print bcolors.GREEN + " / / __/ _ \/ __ \/ _ \/ ___/ __ `/ __/ __ \/ ___/  / __  / / / /"
print bcolors.GREEN + "/ /_/ /  __/ / / /  __/ /  / /_/ / /_/ /_/ / /     / /_/ / /_/ / "
print bcolors.GREEN + "\____/\___/_/ /_/\___/_/   \__,_/\__/\____/_/     /_____/\__, /  "
print bcolors.GREEN + "                                                        /____/   "
print bcolors.BLUE + "    ___        _    _    ___                "
print bcolors.BLUE + "   /   |____  (_)__| |  / (_)______  _______"
print bcolors.BLUE + "  / /| /_  / / /_  / | / / / ___/ / / / ___/"
print bcolors.BLUE + " / ___ |/ /_/ / / /| |/ / / /  / /_/ (__  ) "
print bcolors.BLUE + "/_/  |_/___/_/ /___/___/_/_/   \__,_/____/  " + bcolors.ENDC
print ' '
print ' '
                                            
print(""" \033[1;36m
                                      ┌══════════════════════════════════════════════┐
                                      █                                              █ 
                                      █       ツ     Powered By Crunch     ツ        █
                                      █                                              █
                                      └══════════════════════════════════════════════┘     \n \033[1;m""")
print (" ")
print (" ")
passlength = raw_input(prompt + "How Much <min> <max> Character In The Password ? (example: 1 5) :")
print ' '
print (prompt + "<min> <max> Character In The Password Selected ! ==> " )  + passlength
print ' '
keywords = raw_input(prompt + "Select The Keywords / Characters To Generate ! : ")
print ' '
print (prompt + "Keywords / Characters Selected ! ==> ") + keywords
print ' '
choice = raw_input(prompt + "You Want To Save The Keywords In A File ? (y/n) ")

if choice == "y":
 print ' '
 path = raw_input(prompt + "Select The File Path (example: /root/Desktop/rockyou.txt : ")
 print ' '
 print (prompt + "Started ! " )
 print ' '
 print (prompt + "Generating Passwordlist Now ! Wait... ")
 print ' '
 print (prompt + "Passwords Will Be Saved In  ==> ")+path
 print ' '
 os.system("crunch "+passlength+" "+keywords+" -o "+path)
 print ' '
 print (prompt + "Finished ! ")
 print ' '
 print (prompt + "Passwords Saved In ==> "+path)
 print ' '
 print (prompt + "Time Elapsed: "+ str(time.time() - start_time))
 print ' '
 sys.exit(prompt + "Exit ! ")

else:
 print ' '
 print (prompt + "Started ! ")
 print ' '
 os.system("crunch "+passlength+" "+keywords)
print (prompt + "Finished ! ")
print ' '
print (prompt + "Time Elapsed: "+ str(time.time() - start_time))
print ' '
sys.exit(prompt + "Exit ! ")
