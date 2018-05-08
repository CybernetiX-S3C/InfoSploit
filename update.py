#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
# author : John Modica @ CybernetiX S3C 
# Tested on Kali Linux / Parrot Os / Ubuntu/ Arco Linux / Archman 
# Simple script for install InfoSploitploit

__author__ = "John Modica @ CybernetiX S3C"

import os
import pip

banner = '''
             
\033[92m 

                                                                                             
        #####  #            /##           #######             ###                             
     ######  /            #/ ###        /       ###            ###               #            
    /#   /  /            ##   ###      /         ##             ##              ###     #     
   /    /  /             ##            ##        #              ##               #     ##     
       /  /              ##             ###                     ##                     ##     
      ## ## ###  /###    ###### /###   ## ###           /###    ##      /###   ###   ######## 
      ## ##  ###/ #### / ##### / ###  / ### ###        / ###  / ##     / ###  / ### ########  
    /### ##   ##   ###/  ##   /   ###/    ### ###     /   ###/  ##    /   ###/   ##    ##     
   / ### ##   ##    ##   ##  ##    ##       ### /##  ##    ##   ##   ##    ##    ##    ##     
      ## ##   ##    ##   ##  ##    ##         #/ /## ##    ##   ##   ##    ##    ##    ##     
 ##   ## ##   ##    ##   ##  ##    ##          #/ ## ##    ##   ##   ##    ##    ##    ##     
###   #  /    ##    ##   ##  ##    ##           # /  ##    ##   ##   ##    ##    ##    ##     
 ###    /     ##    ##   ##  ##    ## /##        /   ##    ##   ##   ##    ##    ##    ##     
  #####/      ###   ###  ##   ###### /  ########/    #######    ### / ######     ### / ##     
    ###        ###   ###  ##   #### /     #####      ######      ##/   ####       ##/   ##    
                                    |                ##                                       
                                     \)              ##                                       
                                                     ##                                       
                                                      ##    v1.0 
          		      Update Script for InfoSploit
          		 Created by John Modica [CybernetiX S3C] 

'''
print banner

content = """
#!/bin/bash

cd /usr/share/Infosploit
python Infosploit "$@"
"""

def main():
	if os.name != "nt":
		if os.getuid() == 0:
			os.system("git clone https://github.com/CybernetiX-S3C/InfoSploit /usr/share/Infosploit")
			for i in ["requests", "bs4"]:
				pip.main(["install", i])
			
			file = open("/usr/bin/Infosploit", "w")
			file.write(content)
			file.close()
			
			os.system("chmod +x /usr/bin/Infosploit")

			print "\n\n[+] Update finished, Run \033[91m'Infosploit'\033[92m In Terminal!"
		else:
			print "Run as root!"
	else:
		print "This script doesn't work on Windows!"

if __name__ == "__main__":
	main()
