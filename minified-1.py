#!/usr/bin/env python3
from curses import *
import sys
def m(S):
	f=open(sys.argv[1],"r+")
	c=f.read().split("\n")
	p=[0,0]
	while 1:
		S.clear()
		h,w=S.getmaxyx()
		P=[0,p[1]//h*h]
		for i in range(P[1],min(len(c),P[1]+h)):S.addstr(i-P[1],0,c[i])
		S.move(p[1]-P[1],p[0])
		S.refresh()
		k=S.get_wch()
		if k==259:
			p[1]=max(0,p[1]-1)
			p[0]=min(len(c[p[1]]),p[0])
		elif k==258:
			p[1]=min(len(c)-1,p[1]+1)
			p[0]=min(len(c[p[1]]),p[0])
		elif k in(260,261):
			p[0]+=(1 if k%2 else -1)
			if p[0]<0:p=[len(c[p[1]-1]),max(0,p[1]-1)]
			if p[0]>len(c[p[1]]):p=[0,min(len(c)-1,p[1]+1)]
		elif k==263:
			if p[0]:
				t=c[p[1]]
				c[p[1]]=t[:p[0]-1]+t[p[0]:]
				p[0]-=1
			elif p[1]:
				t=len(c[p[1]-1])
				c[p[1]-1]+=c[p[1]]
				del c[p[1]]
				p=[t,max(0,p[1]-1)]
		elif k=="\n":
			c.insert(p[1]+1,c[p[1]][p[0]:])
			c[p[1]]=c[p[1]][:p[0]]
			p=[0,p[1]+1]
		elif type(k)==str:
			if k=="\x18":
				f.truncate(0)
				f.seek(0)
				f.write("\n".join(c))
				break
                        elif ord(k)>31
				t=c[p[1]]
				c[p[1]]=t[:p[0]]+k+t[p[0]:]
				p[0]+=1
wrapper(m)
