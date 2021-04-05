import os
os.system('cls')

import hashlib
from rich import *
import time
               
print("")
print("                                 [green]#####  #  #")
print("                                    [green]#   ##")
print("                                   [green]#    ##    [blue]Team")
print("                                  [green]#     # #")
print("                                 [green]###### #  #")
print(" ")
print(" ------------------------------------------------------------------------------")
print(" ")

print(" [red]Available hash types (md5, sha1, sha384, sha512, sha224, sha256)[/red]")

print("")

hashtype = input(" Enter hash type : ")

if hashtype == "md5":
    from hashtypes import md5
if hashtype == "sha256":
    from hashtypes import sha256
if hashtype == "sha1":
    from hashtypes import sha1
if hashtype == "sha224":
    from hashtypes import sha224
if hashtype == "sha384":
    from hashtypes import sha384
if hashtype == "sha512":
    from hashtypes import sha512
if hashtype == "":
    print("")
    print(" [red]Please enter a hash type (md5, sha1, sha512, sha224, sha256, sha384)[/red]")

time.sleep(10)
os.system('cls')