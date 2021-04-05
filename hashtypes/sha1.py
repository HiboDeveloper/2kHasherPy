import os
os.system("cls")

from rich import *

print("")
print("                                 [green]#####  #  #")
print("                                    [green]#   ##")
print("                                   [green]#    ##    [blue]Team")
print("                                  [green]#     # #")
print("                                 [green]###### #  #")
print(" ")
print(" ------------------------------------------------------------------------------")
print(" ")

import hashlib
import getpass
import time

password1 = input(" Enter your string : ")

hash1 = hashlib.sha1(str.encode(password1)).hexdigest()

print(hash1)

time.sleep(15)
