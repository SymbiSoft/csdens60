# Archivo: selecAlarm.py
# Autor: Jorge Aguirre Andreu
# Descripción: Sirve para seleccionar cuando se activaran las alarmas disponibles 
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

import e32, appuifw, graphics, key_codes, sys, os

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
import base_de_datos

def handle_redraw(rect):
    global canvasSelecAlarm
    global imSelecAlarm
    global actPos
    global datos
    global qactual
    flechaIzquierdaX=230
    flechaIzquierdaY=125
    flechaIzquierda=[(10,0),(0,5),(10,10)]
    flechaDerechaX=320
    flechaDerechaY=125
    flechaDerecha=[(0,0),(10,5),(0,10)]
    desplaz = 70
    desplaz1 = 105
    colorTexto=[0 for x in range(4)]    
    canvasSelecAlarm.blit(imSelecAlarm)
    canvasSelecAlarm.rectangle((20,120,220,295),outline=0xeeeeee,fill=0xeeeeee)
    canvasSelecAlarm.rectangle((243,262,319,277),outline=0x000000,fill=0x0000ff)
    if actPos == 3:
        canvasSelecAlarm.rectangle((243,262,319,277),outline=0x000000,fill=0xff0000)
    for i in range(3):
        if actMod == True and i == actPos:
            if i == 1:
                canvasSelecAlarm.polygon([(flechaIzquierdaX+dx,flechaIzquierdaY+dy+desplaz) for dx,dy in flechaIzquierda],0xff0000,0xff0000)
                canvasSelecAlarm.polygon([(flechaDerechaX+dx,flechaDerechaY+dy+desplaz) for dx,dy in flechaDerecha],0xff0000,0xff0000)
            elif i == 2:
                canvasSelecAlarm.polygon([(flechaIzquierdaX+dx,flechaIzquierdaY+dy+desplaz1) for dx,dy in flechaIzquierda],0xff0000,0xff0000)
                canvasSelecAlarm.polygon([(flechaDerechaX+dx,flechaDerechaY+dy+desplaz1) for dx,dy in flechaDerecha],0xff0000,0xff0000)
            else:
                canvasSelecAlarm.polygon([(flechaIzquierdaX+dx,flechaIzquierdaY+dy) for dx,dy in flechaIzquierda],0xff0000,0xff0000)
                canvasSelecAlarm.polygon([(flechaDerechaX+dx,flechaDerechaY+dy) for dx,dy in flechaDerecha],0xff0000,0xff0000)
    for i in range(4):
        colorTexto[i]=0x000000    
    colorTexto[actPos]=0xff0000
    canvasSelecAlarm.line((20,120,330,120),0)
    canvasSelecAlarm.text((30,135),getLang(u"ALARMATIRAS"),0x000000,font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasSelecAlarm.text((250,135),u"%03d tiras"%datos[0],colorTexto[0],font=(u"legend",17))
    canvasSelecAlarm.line((20,155,330,155),0)
    canvasSelecAlarm.text((30,170),getLang(u"QTIRASACT"),0x000000,font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasSelecAlarm.text((250,170),u"%03d tiras"%qactual,0x000000,font=(u"legend",17))
    canvasSelecAlarm.text((30,205),getLang(u"QTIRASRESTA"),0x000000,font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasSelecAlarm.text((250,205),u"%03d tiras"%datos[1],colorTexto[1],font=(u"legend",17))
    canvasSelecAlarm.line((20,225,330,225),0)
    canvasSelecAlarm.text((30,240),getLang(u"QTIRASTOTAL"),0x000000,font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasSelecAlarm.text((250,240),u"%03d tiras"%datos[2],colorTexto[2],font=(u"legend",17))
    canvasSelecAlarm.line((20,260,330,260),0)
    canvasSelecAlarm.text((30,275),getLang(u"RESETTIRAS"),colorTexto[3],font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasSelecAlarm.line((20,295,330,295),0)
    canvasSelecAlarm.text((240,410),getLang(u"VOLVER"),0xffffff,font=(u"legend",25,appuifw.STYLE_BOLD))
    canvasSelecAlarm.text((122,85),getLang(u"ALARMA"),0xbbbbbb,font=(u"symbol",27))
    canvasSelecAlarm.text((121,84),getLang(u"ALARMA"),0x000000,font=(u"symbol",27))

def volverAtras():
    global gvAtras
    gvAtrasEnvio=[0 for x in range(len(gvAtras)-1)]
    for i in range(len(gvAtras)-1):
        gvAtrasEnvio[i]=gvAtras[i]
    gvAtras[len(gvAtras)-1](gvAtrasEnvio)
    
def press_select():
    global actMod
    global movimientos
    global actPos
    global datos
    global qactual
    if actMod==True:
        if movimientos[actPos][2] == u"alarmatiras":
            base_de_datos.actualizar_alarmatiras(datos[actPos])
            actMod=False
            appuifw.app.body = canvasSelecAlarm
        elif movimientos[actPos][2] == u"qtirasactual":
            base_de_datos.actualizar_qtirasactual(datos[actPos])
            qactual = int(base_de_datos.obtener_qtirasactual_actual())
            actMod=False
            appuifw.app.body = canvasSelecAlarm
        elif movimientos[actPos][2] == u"qtirastotal":
            base_de_datos.actualizar_qtirastotal(datos[actPos])
            actMod=False
            appuifw.app.body = canvasSelecAlarm
        actMod=False
    else:
        if movimientos[actPos][2] == u"resettiras":
            base_de_datos.reset_qtirasactual()
            qactual = int(base_de_datos.obtener_qtirasactual_actual())            
            appuifw.app.body = canvasSelecAlarm
        else:    
            actMod=True
            appuifw.app.body = canvasSelecAlarm
    
def moverCursor(desp,pos):
    global actPos
    global movimientos
    global datos
    if actMod==True:
        if actPos != 3:
            datos[actPos]+=desp          
            if desp>0:
                if datos[actPos]>movimientos[actPos][3]:
                    datos[actPos]=movimientos[actPos][3]
            else:
                if datos[actPos]<0:
                    datos[actPos]=0            
    else:
        actPos+=movimientos[actPos][1][pos]
    appuifw.app.body = canvasSelecAlarm
    
def press_up():
    moverCursor(25,0)

def press_right():
    moverCursor(1,1)

def press_down():
    moverCursor(-25,2)

def press_left():
    moverCursor(-1,3)

def mostrar_selecAlarm(vAtras):
    qtirastotal = base_de_datos.obtener_qtirastotal()
    global movimientos
    movimientos=[
        [0,[0,0,1,0],u"alarmatiras",qtirastotal-1],
        [1,[-1,0,1,0],u"qtirasactual",999],
        [2,[-1,0,1,0],u"qtirastotal",999],
        [3,[-1,0,0,0],u"resettiras",0]        
        ]
    global datos
    datos=[0 for x in range(3)]
    for i in range(3):
        if i == 0:
            # alarma de tiras reacticas
            datos[i] = base_de_datos.obtener_alarmatiras_actual()
        elif i == 1:
            datos[i] = 0
        elif i == 2:
            datos[i] = base_de_datos.obtener_qtirastotal()
    global actPos
    actPos = 0
    global actMod
    actMod=False
    global qactual
    qactual = base_de_datos.obtener_qtirasactual_actual()
    ruta = unidad+':\\python\\resources\\ui\\'
    global imSelecAlarm
    imSelecAlarm = graphics.Image.open(ruta+'fondo01.png')
    global canvasSelecAlarm
    canvasSelecAlarm = appuifw.Canvas(redraw_callback = handle_redraw)
    canvasSelecAlarm.blit(imSelecAlarm)
    appuifw.app.body = canvasSelecAlarm
    appuifw.app.screen = 'full'
    appuifw.app.title = u"selecAlarm"
    canvasSelecAlarm.bind(key_codes.EKeySelect, press_select)
    canvasSelecAlarm.bind(key_codes.EKeyUpArrow, press_up)
    canvasSelecAlarm.bind(key_codes.EKeyRightArrow, press_right)
    canvasSelecAlarm.bind(key_codes.EKeyDownArrow, press_down)
    canvasSelecAlarm.bind(key_codes.EKeyLeftArrow, press_left) 
    global gvAtras
    gvAtras=vAtras
    if len(vAtras)==1:
        appuifw.app.exit_key_handler=gvAtras[0]
    else:
        appuifw.app.exit_key_handler=volverAtras
    