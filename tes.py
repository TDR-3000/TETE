#!/usr/bin/python2
# coding=utf-8

import os, sys, time

os.system('clear')

logo ='''\033[1;91m
\033[1;91m████████\033[1;97m╗\033[1;91m██\033[1;97m╗  \033[1;91m██\033[1;97m╗\033[1;91m███████\033[1;97m╗\033[1;91m███\033[1;97m╗   \033[1;91m███\033[1;97m╗\033[1;91m███████\033[1;97m╗
\033[1;97m╚══\033[1;91m██\033[1;97m╔══╝\033[1;91m██\033[1;97m║  \033[1;91m██\033[1;97m║\033[1;91m██\033[1;97m╔════╝\033[1;91m████\033[1;97m╗ \033[1;91m████\033[1;97m║\033[1;91m██\033[1;97m╔════╝
\033[1;91m   ██\033[1;97m║   \033[1;91m███████\033[1;97m║\033[1;91m█████\033[1;97m╗  \033[1;91m██\033[1;97m╔\033[1;91m████\033[1;97m╔\033[1;91m██\033[1;97m║\033[1;91m█████\033[1;97m╗  
\033[1;91m   ██\033[1;97m║   \033[1;91m██\033[1;97m╔══\033[1;91m██\033[1;97m║\033[1;91m██\033[1;97m╔══╝  \033[1;91m██\033[1;97m║╚\033[1;91m██\033[1;97m╔╝\033[1;91m██\033[1;97m║\033[1;91m██\033[1;97m╔══╝  
\033[1;91m   ██\033[1;97m║   \033[1;91m██\033[1;97m║  \033[1;91m██\033[1;97m║\033[1;91m███████\033[1;97m╗\033[1;91m██\033[1;97m║ ╚═╝ \033[1;91m██\033[1;97m║\033[1;91m███████\033[1;97m╗
\033[1;97m   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚══════╝

Coding By : Pahrul Aguspriana X 

\033[1;97m[\033[1;91m1\033[1;97m]\033[1;97m change termux appearance
\033[1;97m[\033[1;91m2\033[1;97m]\033[1;97m remove termux appearance
\033[1;97m[\033[1;91m3\033[1;97m]\033[1;97m change termux background
\033[1;97m[\033[1;91m4\033[1;97m]\033[1;97m change termux exstra key
\033[1;97m[\033[1;91m0\033[1;97m]\033[1;97m log out 
'''

def main():
    print logo
    pahrul = raw_input('\033[1;97m[\033[1;91m•\033[1;97m]\033[1;97m choose : ')
    if pahrul == '1':
        os.system('clear')
        ubah()
    elif pahrul == '2':
        os.system('clear')
        delet()
    elif pahrul == '3':
        os.system('clear')
        warna()
    elif pahrul == '4':
        os.system('clear')
        setup()
    elif pahrul == '0':
        exit()
    else:
        exit()

color ='''\033[1;91m
\033[1;91m████████\033[1;97m╗\033[1;91m██\033[1;97m╗  \033[1;91m██\033[1;97m╗\033[1;91m███████\033[1;97m╗\033[1;91m███\033[1;97m╗   \033[1;91m███\033[1;97m╗\033[1;91m███████\033[1;97m╗
\033[1;97m╚══\033[1;91m██\033[1;97m╔══╝\033[1;91m██\033[1;97m║  \033[1;91m██\033[1;97m║\033[1;91m██\033[1;97m╔════╝\033[1;91m████\033[1;97m╗ \033[1;91m████\033[1;97m║\033[1;91m██\033[1;97m╔════╝
\033[1;91m   ██\033[1;97m║   \033[1;91m███████\033[1;97m║\033[1;91m█████\033[1;97m╗  \033[1;91m██\033[1;97m╔\033[1;91m████\033[1;97m╔\033[1;91m██\033[1;97m║\033[1;91m█████\033[1;97m╗  
\033[1;91m   ██\033[1;97m║   \033[1;91m██\033[1;97m╔══\033[1;91m██\033[1;97m║\033[1;91m██\033[1;97m╔══╝  \033[1;91m██\033[1;97m║╚\033[1;91m██\033[1;97m╔╝\033[1;91m██\033[1;97m║\033[1;91m██\033[1;97m╔══╝  
\033[1;91m   ██\033[1;97m║   \033[1;91m██\033[1;97m║  \033[1;91m██\033[1;97m║\033[1;91m███████\033[1;97m╗\033[1;91m██\033[1;97m║ ╚═╝ \033[1;91m██\033[1;97m║\033[1;91m███████\033[1;97m╗
\033[1;97m   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚══════╝

Coding By : Pahrul Aguspriana X 

\033[1;97m[\033[1;91m1\033[1;97m]\033[1;97m color background 1
\033[1;97m[\033[1;91m2\033[1;97m]\033[1;97m color background 2
\033[1;97m[\033[1;91m3\033[1;97m]\033[1;97m color background 3
\033[1;97m[\033[1;91m4\033[1;97m]\033[1;97m default color background 
\033[1;97m[\033[1;91m0\033[1;97m]\033[1;97m Log out 
'''

def warna():
    print color
    pahrul = raw_input('\033[1;97m[\033[1;91m•\033[1;97m]\033[1;97m choose : ')
    if pahrul == '1':
        os.system('clear')
        x()
    elif pahrul == '2':
        os.system('clear')
        xx()
    elif pahrul == '3':
        os.system('clear')
        xxx()
    elif pahrul == '4':
        os.system('clear')
        xxxx()
    elif pahrul == '5':
        os.system('clear')
        xxxxx()
    elif pahrul == '6':
        os.system('clear')
        xxxxxx()
    elif pahrul == '0':
        exit()
    else:
        exit()

def x():
    os.system('clear')
    os.chdir('color')
    os.system('cp background-1 ~/.termux/colors.properties')
    os.system('termux-reload-settings')

def xx():
    os.system('clear')
    os.chdir('color')
    os.system('cp background-2 ~/.termux/colors.properties')
    os.system('termux-reload-settings')

def xxx():
    os.system('clear')
    os.chdir('color')
    os.system('cp background-3 ~/.termux/colors.properties')
    os.system('termux-reload-settings')

def xxxx():
    os.system('clear')
    os.chdir('color')
    os.system('cp default ~/.termux/colors.properties')
    os.system('termux-reload-settings')


def ubah():
    os.system('clear')
    prompt = str(raw_input('\033[1;97m[\033[1;91m×\033[1;97m]\033[1;97m masukan nama kalian : '))
    ugex = open('bash.bashrc', 'w')
    ugex.write('clear')
    ugex.write("\necho '\x1b[1;97m                    .:::!~!!!!!:.'")
    ugex.write("\necho '                 .xUHWH!! !!?M88WHX:.'")
    ugex.write("\necho '               .X*#M@&!!  !X!M&&&&&&WWx:.'")
    ugex.write("\necho '              :!!!!!!?H! :!&!&&&&&&&&&&8X:'")
    ugex.write("\necho '             !!~  ~:~!! :~!&!#&&&&&&&&&&8X:'")
    ugex.write("\necho '            :!~::!H!<   ~.U&X!?R&&&&&&&&MM!'")
    ugex.write("\necho '            ~!~!!!!~~ .:XW&&&U!!?&&&&&&RMM!'")
    ugex.write("\necho '              !:~~~ .:!MST#&&&&WX??#MRRMMM!'")
    ugex.write("\necho '              ~?WuxiW*`   `\xe2\x88\x9a#&&&&8!!!!??!!!'")
    ugex.write("\necho '            :X- M&&&&       `rT#&T~!8&WUXU~'")
    ugex.write("\necho '           :%`  ~#&&&m:    \x1b[1;91m\xe2\x9c\xaa   \x1b[1;97m~!~ ?&&&&&&'")
    ugex.write("\necho '         :!`.-   ~T&&&&8xx.  .xWW- ~x&&&&&'")
    ugex.write("\necho '.....   -~~:<` !    ~?T#&&@@W@*?&&   \x1b[1;91m\xe2\x9c\xaa  \x1b[1;97m/`'")
    ugex.write("\necho 'W&@@M!!! .!~~ !!     .:XUW&W!~ `&~:    :'")
    ugex.write("\necho '#&~~`.:x%`!!  !H:   !WM&&&&Ti.: .!WUn+!`'")
    ugex.write("\necho ':::~:!!`:X~ .: ?H.!u \xc2\xb0&&&B&&&!W:U!T&&M~'")
    ugex.write("\necho '.~~   :X@!.-~   ?@WTWo(`*&&&W&TH&! `'")
    ugex.write("\necho 'Wi.~!X$?!-~    / ?&&&B&Wu(`**&RM!'")
    ugex.write("\necho '.....         /   ~&&&&&B&&en:``'")
    ugex.write("\necho '\x1b[1;791m                  ~`##*&&&&M~'")
    ugex.write('\necho')
    ugex.write('\necho')
    ugex.write("\n\nPS1='\x1b[1;34m\\]\xe2\x95\xad\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\\[\x1b[1;31m\\][\\[\x1b[1;33m\\]" + prompt + '\\[\x1b[1;34m\\]\\[\x1b[1;31m\\]]\\[\x1b[1;31m\\]\\[\x1b[1;34m\\]\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\\[\x1b[1;31m\\][\\[\x1b[1;30m\\]\\w\\[\x1b[1;31m\\]] ')
    ugex.write("\n\\[\x1b[1;34m\\]\xe2\x95\xb0\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\\[\x1b[1;31m\\]\xe2\x9f\xa9\xe2\x9f\xa9\xe2\x9f\xa9\\[\x1b[1;32m\\] '")
    ugex.close()
    os.system('rm $HOME/../usr/etc/bash.bashrc')
    os.system('cp -f bash.bashrc $HOME/../usr/etc')
    os.system('termux-reload-settings')
    os.system('login')


def delet():
    os.chdir('delet')
    os.system('rm $HOME/../usr/etc/bash.bashrc')
    os.system('cp -f bash.bashrc $HOME/../usr/etc')
    os.system('clear')
    os.system('termux-reload-settings')
    os.system('login')

def setup():
    try:
        os.mkdir('/data/data/com.termux/files/home/.termux')
    except:
        pass

    key = "extra-keys = [['CTRL','END','HOME','UP','cd /sdcard ','pkg install ',' pip install '],['python ','python2 ','LEFT','DOWN','RIGHT','/','pip2 install ']]"
    open('/data/data/com.termux/files/home/.termux/termux.properties', 'w').write(key)
    os.system('termux-reload-settings')
    os.system('clear')
    print '\n\033[1;97m[\033[1;91m•\033[1;97m]\033[1;97m Terima Kasih Telah Menggunakan Script Saya !!!'


if __name__ == '__main__':
    main()