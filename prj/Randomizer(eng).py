#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
import pygame
import sys
import math
from operator import itemgetter
import random
from random import randint
#Константы и функции
FPS=60
W=940
H=600
RUN=True
WHITE=(255,255,255)
BLACK=(0,0,0)
PINK=(152, 79, 210)
YELLOW=(255,255,0)
tr=0
#Инициализация, создание объектов
print("_________________________________________________")
print("")
print("████─████─█──█─████──████─█───█─███─████─███─████")
print("█──█─█──█─██─█─█──██─█──█─██─██──█────██─█───█──█")
print("████─████─█─██─█──██─█──█─█─█─█──█───██──███─████")
print("█─█──█──█─█──█─█──██─█──█─█───█──█──██───█───█─█─")
print("█─█──█──█─█──█─████──████─█───█─███─████─███─█─█─")
print("")
print("_________________________________________________")

d=input("Enter the number of participants=")
d=int(d)
name=[]
n=0
while n<d:
    name.append(input(f"Enter the name of the participant №{n+1}:"))
    n+=1
pygame.init()
screen=pygame.display.set_mode((W,H))
clock=pygame.time.Clock()
f = pygame.font.SysFont('serif', 38)
f_small = pygame.font.SysFont('serif', 28)
position=[]
for n in range(360):
    position.append([250*math.cos(n)+300,250*math.sin(n)+300])
position=sorted(position, key=itemgetter(0))
position_left=[]
position_right=[]
n=0
while n<len(position):
    if position[n][1]>300:
        position_right.append(position[n])
    else:
        position_left.append(position[n])
    n+=1
position_left.reverse()
position=position_right+position_left
delinel=len(position)/d
pos=[]
for n in range(d):
    pos.append(n*int(delinel))

position_txt=[]
for n in range(360):
    position_txt.append([150*math.cos(n)+300,150*math.sin(n)+300])
position_txt=sorted(position_txt, key=itemgetter(0))
position_left_txt=[]
position_right_txt=[]
n=0
while n<len(position_txt):
    if position_txt[n][1]>300:
        position_right_txt.append(position_txt[n])
    else:
        position_left_txt.append(position_txt[n])
    n+=1
position_left_txt.reverse()
position_txt=position_right_txt+position_left_txt
pos_txt=[]
for n in range(d):
    pos_txt.append(n*int(delinel)-int(delinel)//2)
v=FPS
press=False
tic=0
R=randint(1,255)
G=randint(1,255)
B=randint(1,255)
while RUN:
    screen.fill(PINK)
    #FPS
    clock.tick(FPS)
    #Цикл обработки событий
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            sys.exit()
    #Изменение объектов
    pygame.draw.circle(screen,WHITE,(300,300),250)
    pressed=pygame.mouse.get_pressed()
    mp=pygame.mouse.get_pos()
    if pressed[0] and mp[0]<=835 and mp[0]>=595 and mp[1]<=455 and mp[1]>=405:
        v=random.randint(1000, 8000)
        tr=random.uniform(0.1, 1)
        press=True
    if press:
        FPS=v
    
    pygame.draw.rect(screen,(255,255,255),(590,400,250,60))
    if tic>30:
        R=randint(1,255)
        G=randint(1,255)
        B=randint(1,255)
        tic=0
    tic+=1
    pygame.draw.polygon(screen,YELLOW,([300,40],[280,10],[320,10]))
    pygame.draw.rect(screen,(R,G,B),(595,405,240,50))
    text_start = f.render("Twist", True, WHITE)
    screen.blit(text_start, text_start.get_rect(center=(715,430)))
    for k in range(d):
        if v!=10:
            pos[k]=0 if pos[k]>=len(position)-1 else pos[k]+1
            pos_txt[k]=0 if pos_txt[k]>=len(position_txt)-1 else pos_txt[k]+1
        pygame.draw.line(screen,PINK,[300,300],[position[pos[k]][1],position[pos[k]][0]],10)
        text_tr2 = f_small.render(name[k], True, BLACK)
        screen.blit(text_tr2, text_tr2.get_rect(center=(position_txt[pos_txt[k]][1],position_txt[pos_txt[k]][0])))
    if v>10:
        v=v-tr
    if v-10<0:
        v=10
    text_v = f.render(f'Speed={round(FPS-10,4)}', True, (255, 255, 255))
    screen.blit(text_v, (590, 60))
    text_tr = f.render(f'Friction={round(tr,4)}', True, (255, 255, 255))
    screen.blit(text_tr, (590, 120))
    #text2 = f.render(str(pygame.mouse.get_pos()), True, (255, 255, 255))
    #screen.blit(text2, (10, 10))
    #Обновление экрана
    #pygame.display.flip()
    pygame.display.update()