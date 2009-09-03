# Archivo: citas.py
# Autor: Jorge Aguirre Andreu
# Descripción: Lleva el control de todas las citas con los distintos médicos del diabético, desde 
# endocrino, podólogo, oculista, análisis de sangre y cualquier otro. 
# También tiene la opción de activar una alarma dias antes para no olvidar dichas citas. 
#
#   Copyright (C) 2009  Jorge Aguirre Andreu
#
#   This file is part of CSDs60.
#   CSDs60 is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   CSDs60 is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import e32, appuifw, sys, os, graphics, key_codes

from time import localtime

try:
    raise Exception
except Exception:
    path = sys.exc_info()[2].tb_frame.f_code.co_filename
if not path:
    path = os.path.join(os.getcwd(), 'default.py')
unidad=path[0]

modulospropios = unidad+':\\Python\\modules'
sys.path.append(modulospropios)
from idioma import getLang

def esBisiesto(ano):
    return ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0

def diaInicio(mes,ano):
    mods=[[0,3,3,6,1,4,6,2,5,0,3,5],[0,3,4,0,2,5,0,3,6,1,4,6]]
    bi=esBisiesto(ano)
    v1=(ano-1)%7
    v2=((ano-1)/4-(3*(((ano-1)/100+1)/4)))%7
    v3=(v1+v2+mods[bi][mes-1]+1)%7-1
    if v3==-1:
        v3=6
    return v3

def numDias(mes,ano):
    dias=[31,28,31,30,31,30,31,31,30,31,30,31]
    num=dias[mes-1]
    if mes==2 and esBisiesto(ano):
        num+=1
    return num

def dibujarCalendario():
    meses=[getLang(u"ENERO"),getLang(u"FEBRERO"),getLang(u"MARZO"),getLang(u"ABRIL"),getLang(u"MAYO"),getLang(u"JUNIO"),getLang(u"JULIO"),getLang(u"AGOSTO"),getLang(u"SEPTIEMBRE"),getLang(u"OCTUBRE"),getLang(u"NOVIEMBRE"),getLang(u"DICIEMBRE")]
    global actDia
    global actMes
    global actAno
    global actPos
    actIni=diaInicio(actMes,actAno)
    global canvasCitas
    calInicioX=22
    calInicioY=165
    calAncho=45
    calAlto=35
    numerar=False
    contador=0
    canvasCitas.rectangle((19,105,340,380),outline=0xaaaaaa,fill=0xaaaaaa)
    canvasCitas.rectangle((16,102,337,377),outline=0x000000,fill=0xffffff)
    canvasCitas.text((110,125),u"%s %d" % (meses[actMes-1],actAno),0x000000,font=(u"annotation",20))
    canvasCitas.text((40,155),getLang(u"DIAS"),0x555555,font=(u"annotation",20))
    for i in range(6):
        for j in range(7):
            x = calInicioX+j*calAncho-j
            y = calInicioY+i*calAlto-i
            relleno=0xffffff
            if j==5 or j==6:
                relleno=0xd9ddf4
            if i==0 and j==actIni:
                numerar=True
            rellenoLetra=0x000000
            if contador==actDia and actMes==localtime()[1] and actAno==localtime()[0]:
                rellenoLetra=0xff0000
                if actPos==-1:
                    actPos=contador
            if actPos==contador and numerar:
                relleno=0xaaccff
            canvasCitas.rectangle((x,y,x+calAncho,y+calAlto),outline=0x000000,fill=relleno)
            if numerar and numDias(actMes,actAno) > contador:
                contador+=1
                canvasCitas.text((x+7,y+28),u"%2d" % contador,rellenoLetra,font=(u"dense",30))

def press_up():
   global actPos
   global actMes
   global actAno
   actPos-=7
   if actPos<=-1:
        actMes-=1
        if actMes==0:
            actMes=12
            actAno-=1
        actPos=numDias(actMes,actAno)-1
   appuifw.app.body=canvasCitas

def press_right():
    global actPos
    global actMes
    global actAno
    actPos+=1
    if actPos==numDias(actMes,actAno):
        actMes+=1
        if actMes==13:
            actMes=1
            actAno+=1
        actPos=0
    appuifw.app.body=canvasCitas

def press_down():
    global actPos
    global actMes
    global actAno
    actPos+=7
    if actPos>=numDias(actMes,actAno):
        actMes+=1
        if actMes==13:
            actMes=1
            actAno+=1
        actPos=0
    appuifw.app.body=canvasCitas

def press_left():
    global actPos
    global actMes
    global actAno
    actPos-=1
    if actPos==-1:
        actMes-=1
        if actMes==0:
            actMes=12
            actAno-=1
        actPos=numDias(actMes,actAno)-1
    appuifw.app.body=canvasCitas

def press_select():
    global actPos
    global actMes
    global actAno
    global gvAtras
    gvAtrasEnvio=[0 for x in range(len(gvAtras)+1)]
    for i in range(len(gvAtras)):
        gvAtrasEnvio[i]=gvAtras[i]
    gvAtrasEnvio[len(gvAtras)]=mostrarCitas
    
def handle_redraw(rect):
    global canvasCitas
    global imCitas
    canvasCitas.blit(imCitas)
    canvasCitas.text((150,85),getLang(u"CITAS"),0xbbbbbb,font=(u"symbol",27))
    canvasCitas.text((149,84),getLang(u"CITAS"),0x000000,font=(u"symbol",27))
    canvasCitas.text((240,410),getLang(u"VOLVER"),0xffffff,font=(u"legend",25,appuifw.STYLE_BOLD))
    canvasCitas.text((25,410),getLang(u"OPCIONES"),0xffffff,font=(u"legend",25,appuifw.STYLE_BOLD))
    dibujarCalendario()

def volverAtras():
    global gvAtras
    gvAtrasEnvio=[0 for x in range(len(gvAtras)-1)]
    for i in range(len(gvAtras)-1):
        gvAtrasEnvio[i]=gvAtras[i]
    gvAtras[len(gvAtras)-1](gvAtrasEnvio)

def mostrarCitas(vAtras):
    global actDia
    actDia=(localtime()[2])-1
    global actMes
    actMes=localtime()[1]
    global actAno
    actAno=localtime()[0]
    global actPos
    actPos=-1
    ruta = unidad+':\\python\\resources\\ui\\'
    global imCitas
    imCitas = graphics.Image.open(ruta+'fondo01.png')
    global canvasCitas
    canvasCitas = appuifw.Canvas(redraw_callback = handle_redraw)
    canvasCitas.blit(imCitas)
    appuifw.app.body = canvasCitas
    appuifw.app.screen = 'full'
    appuifw.app.title = u"Citas"
    canvasCitas.bind(key_codes.EKeySelect, press_select)
    canvasCitas.bind(key_codes.EKeyUpArrow, press_up)
    canvasCitas.bind(key_codes.EKeyRightArrow, press_right)
    canvasCitas.bind(key_codes.EKeyDownArrow, press_down)
    canvasCitas.bind(key_codes.EKeyLeftArrow, press_left)
    global gvAtras
    gvAtras=vAtras
    if len(vAtras)==1:
        appuifw.app.exit_key_handler=gvAtras[0]
    else:
        appuifw.app.exit_key_handler=volverAtras