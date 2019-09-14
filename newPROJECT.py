import sys
import os
import random
import time
from time import sleep

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2.0 / 90)

def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush() # <- add this
        time.sleep(0.2)

print ('\033[97mLoading...')
slowprint('(>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>)√')
sleep(2)
os.system('clear')

mengetik('Masukan user dan password nya')
slowprint('kalo ga tau pm Mr4R13F wa 085755494099')
username = 'Mr4R13F'
password = 'MASTAHCYBER'

def restart():
        ngulang = sys.executable
        os.execl(ngulang, ngulang, *sys.argv)

def main():
        uname = input ('username : ')
        if uname == username:

                pwd = input ('password : ')
                if pwd == password:
                      		   slowprint('hello selamat datang di tools Mr.4R13F')

                else:
                        mengetik('sory invalid password!!!')
                        slowprint('back to login')
                        restart()
        else:
                mengetik('sory invalid username!!!')
                slowprint('back to login')
                restart()

main()

def gambar():
    os.system('clear')
    slowprint('################################################')
    slowprint("##                                            ##")
    slowprint("##      ==>  author   : Mr.4R13F              ##")
    slowprint("##   Team DevlinCyberTeam                     ##")
    slowprint("##      ==>  Team Jr  : AloneSecurity         ##")
    slowprint("##                                            ##")
    slowprint("##   IG     : Unic_Nation101                  ##")
    slowprint("##   chanel : R133F GANZ / Mr 4R13F           ##")
    slowprint("##                                            ##")
    slowprint("################################################")

def pilihan():
    os.system('clear')
    print ('Loading...')
    slowprint('(>>>>>>>>>>>>>>>>>>>>>>>>)√')
    gambar()
    print ('[1]spam')
    print ('[2]Ddos')
    print ('[3]Daface')
    print ('[0]keluar')
    print ('')
def membaca():
    nomor = input ('╰━⋗ pilih nomor : ')
    if nomor == '1':
                    os.system('clear')
                    gambar()
                    mengetik('welcome to Spam Mr4R13F')
                    os.system('php 1.php')

    else:
         print ('invalid!!!')

    if nomor == '2':
                    os.system('clear')
                    gambar()
                    mengetik('welcome to Ddos Mr4R13F')
                    sleep(2)
                    os.system('python3 andromeda.py')

    else:
         print ('invalid!!!')

    if nomor == '3':
                    os.system('clear')
                    gambar()
                    mengetik('welcome to Daface Mr4R13F')
                    sleep(2)
                    os.system('sh R133FDAFACE.sh')
    else:
         print ('invalid!!!')
pilihan()
membaca()
