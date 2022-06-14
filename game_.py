import sys
import random
import pygame
import time
import math
from tkinter import *
from tkinter import messagebox
from pygame.locals import QUIT,KEYDOWN,K_LEFT,K_RIGHT,K_UP,K_DOWN,Rect,MOUSEBUTTONDOWN,K_SPACE,MOUSEBUTTONUP
def blockadd():
    ru=2
    for i in range(10):
        ryt=random.randint(1,3)
        if ryt!=3:
            block[0][i]=stage
        else:
            ry=random.randint(1,ru)
            if ry==2:block[0][i]=-1;ru+=2
        
    for i in range(14,-1,-1):
        for g in range(10):
            block[i+1][g]=block[i][g]
            block[i][g]=0
    #print(block)
def checkcircle(a,b,c,d,e,f):#x,y,반지름
    if math.sqrt(abs(a-d)**2+abs(b-e)**2)<=c+f:return 1
    else:return 0
def showw():
        #show.append(["text",pygame.font.SysFont(None,30),"+"+str(gbcnt),(80,188,223),(lastx,530),0])
        #font1=pygame.font.SysFont(None,30)
        #text_Title=myFont.render("+"+str(gbcnt), True,(80,188,223))
        #SURFACE.blit(text_Title,(lastx,530))
    zcc=0
    for iw in range(len(show)):
        i=iw-zcc
        if show[i][0]=="text":
            if show[i][5]<20:
                show[i][5]+=1
                font1=show[i][1]
                text_Title=font1.render(show[i][2], True,show[i][3])
                SURFACE.blit(text_Title,show[i][4])
            else:
                show.pop()
                zcc+=1
def blockdraw():
    for g in range(16):
        for i in range(10):
            if block[g][i]>0:
                pygame.draw.rect(SURFACE,(255,212,0),[i*80+1,g*50+1,78,48],1)
                text_Title=myFont.render(str(block[g][i]), True, (255,255,255))
                text_Rect=text_Title.get_rect()
                text_Rect.centerx=i*80+40
                text_Rect.centery=g*50+25
                SURFACE.blit(text_Title,text_Rect)
            if block[g][i]==-1:
                pygame.draw.ellipse(SURFACE,(63,232,127),Rect(i*80+25,g*50+10,30,30))
                pygame.draw.circle(SURFACE,(255,255,255),(i*80+40,g*50+25),11,3)
def dse():
    #show.append(["text",pygame.font.SysFont(None,30),"+"+str(gbcnt),(80,188,223),(lastx,530),0])
    font1=pygame.font.SysFont('notosanscjkkrblack',50)
    text_Title=font1.render("stage : "+str(stage), True,(255,255,255))
    SURFACE.blit(text_Title,(30,750))
def ballcnt():
    if nscnt!=0:
        font2=pygame.font.SysFont('notosanscjkkrblack',30)
        text_Title1=font2.render("x"+str(nscnt), True,(62,248,255))
        text_Rect=text_Title1.get_rect()
        text_Rect.centerx=llstx
        text_Rect.centery=730
        SURFACE.blit(text_Title1,text_Rect)
    #(63,232,127)
pygame.init()
FPSCLOCK = pygame.time.Clock()
SURFACE = pygame.display.set_mode((800,800))
SURFACE.fill((0,0,0))
pygame.draw.line(SURFACE,(255,212,0),(0,600),(800,600),5)
pygame.draw.ellipse(SURFACE,(255,255,255),Rect(400,590,10,10))
myFont = pygame.font.Font( None, 30)
pygame.display.update()
ball=[]
bcnt=1
running=0
show=[]
block=[[0 for i in range(10)]for g in range(16)]
stage=1
dt=2
blockadd()
nscnt=0
lastx=400
while 1:
    #if running==1:continue
    SURFACE.fill((0,0,0))
    llstx=lastx
    nscnt=bcnt
    blockdraw()
    showw()
    dse()
    ballcnt()
    #for g in range(20):
    #    for i in range(10):
    #        pygame.draw.rect(SURFACE,(255,212,0),[i*80+3,g*50+3,74,44],3)
    #pygame.draw.rect(SURFACE,(255,212,0),[400,20,80,50],3)
    #pygame.draw.rect(SURFACE,(255,212,0),[400,100,80,50])
    pygame.draw.line(SURFACE,(255,212,0),(0,700),(800,700),5)
    pygame.draw.ellipse(SURFACE,(80,188,223),Rect(lastx,690,10,10))
    #print(pygame.mouse.get_pressed())
    er=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type==MOUSEBUTTONDOWN and event.button==1:
            running=1
    if running==0:
        xp,yp=er[0],er[1]
        if yp>=700:continue
        if xp!=lastx:
            #print(xp,lastx)
            b2=abs(lastx-xp)
            a2=690-yp
            c2=math.sqrt(a2**2+b2**2)
            A=(math.acos((2*(b2**2))/(2*b2*c2)))*(180/math.pi)
            if xp<lastx:ae=270-A
            else:ae=90+A
            wx=lastx
            wy=695
            xd=math.sin(math.radians(ae))
            yd=math.cos(math.radians(ae))
            while 800>wx>0 and 800>wy>0:
                hl=[int(wy+yd*20)//50,int(wx+xd*20)//80]
                #pygame.draw.line(SURFACE,(80,188,223),(wx,wy),(wx+xd*15,wy+yd*15),3)
                #print(hl,block[hl[0]][hl[1]])
                if 0<=hl[0]<=15 and 0<=hl[1]<=9 and block[hl[0]][hl[1]]>0:
                    #adx=wx
                    #ady=wy
                    #wx+=xd*15
                    #wy+=yd*15
                    #wx-=xd*(abs(hl[0]*50+50-(wy+yd*15))/yd)
                    
                    #y11=hl[0]*50+50
                    #a12=(wy+yd*15-5-wy)/(wx+xd*15-5-wx)
                    #b12=wy-a12*wx
                    #wy=y11
                    #wx=(y11-b12)/a12
                    #y12=a12*(x1)+b12
                    #(y11-b12)/a12
                    #y=(wy+yd*15-wy)/(wx+xd*15-wx)*x1+b
                    #pygame.draw.line(SURFACE,(80,188,223),(adx,ady),(wx,wy+5),3)
                    #pygame.draw.ellipse(SURFACE,(80,188,223),Rect(wx-3,wy,10,10))
                    break#(80,188,250)
                pygame.draw.line(SURFACE,(62,248,255),(wx,wy),(wx+xd*15,wy+yd*15),3)
                wx+=xd*20
                wy+=yd*20
    if running==1:
        xpos,ypos=er[0],er[1]
        if ypos>=700:continue
        b2=abs(lastx-xpos)
        a2=690-ypos
        c2=math.sqrt(a2**2+b2**2)
        if b2==0:angle=0
        else:
            A=(math.acos((2*(b2**2))/(2*b2*c2)))*(180/math.pi)
            if xpos<lastx:angle=270-A
            else:angle=90+A
        ball=[[lastx,690,1,1,1]for i in range(bcnt)]
        gball=[]
        gbcnt=0
        nut=bcnt
        delay=0
        #print(bcnt)
        while 1:
            #print(ball)
            SURFACE.fill((0,0,0))
            blockdraw()
            ballcnt()
            dse()
            pygame.draw.line(SURFACE,(255,212,0),(0,700),(800,700),5)
            delay+=1
            for i in range(min(bcnt,delay//13+1)):
                if ball[i][4]==1:
                    x=ball[i][0]
                    y=ball[i][1]
                    if y==690:nscnt-=1
                    dirx=ball[i][2]
                    diry=ball[i][3]
                    xd=math.sin(math.radians(angle))*dt*dirx
                    yd=math.cos(math.radians(angle))*dt*diry
                    x+=xd
                    y+=yd
                    #[i*80+3,g*50+3,74,44]
                    #print((x-1)//80*80,x,zy,y,yd)
                    #print(int(y-1)//50,int(x-1)//80)
                    #if 1<=y//50<=15 and 1<=x//80<=9 and block[int(y)//50][int(x)//80]==1:
                    x-=1
                    y-=1
                    op=[0,0]
                    zy=y//50*50+50
                    xy=(y+10)//50*50
                    zx=x//80*80+80
                    xx=(x+10)//80*80
                    py=[int(y)//50,int(x+5)//80,int(y+10)//50,int(x)//80,int(x+10)//80]
                    #print(py)
                    if 0<=py[0]<=15 and 0<=py[1]<=9 and block[py[0]][py[1]]==-1:
                        if checkcircle(x+5,y+5,10,py[1]*80+40,py[0]*50+25,15)==1:#(i*80+40,g*50+25)
                            block[py[0]][py[1]]=0
                            gbcnt+=1
                            gball.append([py[1]*80+25,py[0]*50+10,1])
                            #print("ASD")
                    if 15>=py[0]>=0 and 0<=py[1]<=9 and (x+5)//80*80<=(x+5)<=(x+5)//80*80+80 and y<=zy and block[py[0]][py[1]]>0:
                        #print("#",y,x)
                        block[py[0]][py[1]]-=1;diry*=-1;y=zy+1
                        op[0]=1
                        #print("#@",y,x)
                    elif 15>=py[2]>=0 and 0<=py[1]<=9 and (x+5)//80*80<=(x+5)<=(x+5)//80*80+80 and y+10>=xy and block[py[2]][py[1]]>0:
                        #print("##")
                        block[py[2]][py[1]]-=1;diry*=-1;y=zy-10-1
                        op[0]=1
                    elif 15>=py[0]>=0 and 0<=py[3]<=9 and (y+5)//50*50<=(y+5)<=(y+5)//50*50+50 and x<=zx and block[py[0]][py[3]]>0:
                        #print("###",y,x)
                        block[py[0]][py[3]]-=1;dirx*=-1;x=zx+1
                        #print("###@",y,x)
                        op[1]=1
                    elif 15>=py[0]>=0 and 0<=py[4]<=9 and (y+5)//50*50<=(y+5)<=(y+5)//50*50+50 and x+10>=xx and block[py[0]][py[4]]>0:
                        #print("####")
                        block[py[0]][py[4]]-=1;dirx*=-1;x=zx-10-1
                        op[1]=1
                    if op[0]==0:y+=1
                    if op[1]==0:x+=1
                    if y<=0:y=0;diry*=-1
                    if x<=10:x=10;dirx*=-1
                    if y>=690:
                        ball[i][1]=690
                        if nut==bcnt:lastx=ball[i][0];ball[i][4]=3;nut-=1
                        else:ball[i][4]=2
                    if x>=795:x=795;dirx*=-1
                    if ball[i][4]==1:
                        pygame.draw.ellipse(SURFACE,(80,188,223),Rect(x,y,10,10))
                        ball[i]=[x,y,dirx,diry,1]
                elif ball[i][4]==2:
                    x=ball[i][0]
                    if x<lastx and x+2>lastx:ball[i][4]=0;nut-=1
                    if x>lastx and x-2<lastx:ball[i][4]=0;nut-=1
                    if x<lastx:x+=2
                    elif x>lastx:x-=2
                    if ball[i][0]==lastx:ball[i][4]=0;nut-=1
                    pygame.draw.ellipse(SURFACE,(80,188,223),Rect(x,ball[i][1],10,10))
                    ball[i][0]=x
                elif ball[i][4]==3:
                    pygame.draw.ellipse(SURFACE,(80,188,223),Rect(lastx,ball[i][1],10,10))
                if nut==0:break
            for i in range(len(gball)):
                if gball[i][1]+1>=690:
                    pygame.draw.ellipse(SURFACE,(63,232,127),Rect(gball[i][0],690,10,10))
                    gball[i][2]=2
                if gball[i][2]==1:
                    gball[i][1]+=2
                    pygame.draw.ellipse(SURFACE,(63,232,127),Rect(gball[i][0],gball[i][1],10,10))
            if nut==0:break
            pygame.display.update()
            #FPSCLOCK.tick(100)
        lnt=gbcnt
        while lnt!=0:
            SURFACE.fill((0,0,0))
            blockdraw()
            dse()
            ballcnt()
            pygame.draw.line(SURFACE,(255,212,0),(0,700),(800,700),5)
            pygame.draw.ellipse(SURFACE,(80,188,223),Rect(lastx,690,10,10))
            for i in range(gbcnt):
                #print(gball[i])
                if gball[i][2]==1:
                    gball[i][1]+=2
                    pygame.draw.ellipse(SURFACE,(63,232,127),Rect(gball[i][0],gball[i][1],10,10))
                    if gball[i][1]>=690:gball[i][2]=2
                elif gball[i][2]==2:
                    if gball[i][0]+2<lastx:gball[i][0]+=2
                    elif gball[i][0]-2>lastx:gball[i][0]-=2
                    if gball[i][0]==lastx:lnt-=1;gball[i][2]=0
                    if gball[i][0]<lastx and gball[i][0]+2>lastx:lnt-=1;gball[i][2]=0
                    if gball[i][0]>lastx and gball[i][0]-2<lastx:lnt-=1;gball[i][2]=0
                    if gball[i][2]!=0:pygame.draw.ellipse(SURFACE,(63,232,127),Rect(gball[i][0],690,10,10))
                pygame.display.update()
        if gbcnt!=0:
            bcnt+=gbcnt
            show.append(["text",pygame.font.SysFont(None,30),"+"+str(gbcnt),(63,232,127),(lastx,650),0])
        #font1=pygame.font.SysFont(None,30)
        #text_Title=myFont.render("+"+str(gbcnt), True,(80,188,223))
        #SURFACE.blit(text_Title,(lastx,530))
        running=0
        stage+=1
        #print(lastx)
        blockadd()
        #print(block)
    pygame.display.update()
    for i in range(10):
        if block[14][i]>0:sys.exit()
    FPSCLOCK.tick(50)