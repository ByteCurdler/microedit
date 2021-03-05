#!/usr/bin/env python3
from curses import *
import sys

logf = open("microedit.log", "w+")

def log(msg):
    logf.write(str(msg) + "\n")
    logf.flush()

def main(stdscr):

    file = open(sys.argv[1], "r+")
    log(f"Opening {file}...")

    content = file.read().split("\n")

    pos = [0,0]
    while True:
        #Render
        stdscr.clear()
        h,w = stdscr.getmaxyx()
        rpos = [0, pos[1]//h * h]
        for i in range(rpos[1], min(len(content), rpos[1]+h)):
            stdscr.addstr(i-rpos[1], 0, content[i])
        stdscr.move(pos[1]-rpos[1], pos[0])
        stdscr.refresh()
        #Control
        k = stdscr.get_wch()
        size = (len(content[pos[1]]), len(content))
        if k==KEY_UP:
            pos[1]=max(0,pos[1]-1)
            pos[0]=min(len(content[pos[1]]), pos[0])
        elif k==KEY_DOWN:
            pos[1]=min(len(content)-1,pos[1]+1)
            pos[0]=min(len(content[pos[1]]), pos[0])
        elif k in (KEY_LEFT, KEY_RIGHT):
            pos[0]+=(-1 if k == KEY_LEFT else 1)
            if pos[0] < 0:
                pos = [len(content[pos[1]-1]),max(0,pos[1]-1)]
            if pos[0] > len(content[pos[1]]):
                pos = [0,min(len(content)-1,pos[1]+1)]
        elif k==KEY_BACKSPACE:
            if pos[0]:
                tmp=content[pos[1]]
                content[pos[1]] = tmp[:pos[0]-1] + tmp[pos[0]:]
                pos[0] -= 1
            elif pos[1]:
                tmp=len(content[pos[1]-1])
                content[pos[1]-1] += content[pos[1]]
                del content[pos[1]]
                pos = [tmp,max(0,pos[1]-1)]
        elif k=="\n":
            content.insert(pos[1]+1, content[pos[1]][pos[0]:])
            content[pos[1]] = content[pos[1]][:pos[0]]
            pos = [0, pos[1]+1]
        elif type(k)==str:
            if k=="\x18":
                file.truncate(0)
                file.seek(0)
                file.write("\n".join(content))
                return
            elif ord(k)>31:
                tmp=content[pos[1]]
                content[pos[1]] = tmp[:pos[0]] + k + tmp[pos[0]:]
                pos[0] += 1
        #log(f"key {repr(k)}")
            
        
wrapper(main)
