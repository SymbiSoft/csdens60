# Archivo: personal.py
# Autor: Jorge Aguirre Andreu
# Descripción: Sirve para configurar los datos personales del usuario 
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
from configuracion import *
import base_de_datos

def handle_redraw(rect):
    global canvasPersonal
    global imPersonal
    global datos
    global actPos
    flechaIzquierdaX=230
    flechaIzquierdaY=125
    flechaIzquierda=[(10,0),(0,5),(10,10)]
    flechaDerechaX=320
    flechaDerechaY=125
    flechaDerecha=[(0,0),(10,5),(0,10)]
    colorTexto=[0 for x in range(6)]
    canvasPersonal.blit(imPersonal)    
    canvasPersonal.rectangle((20,120,220,330),outline=0xeeeeee,fill=0xeeeeee)
    for i in range(6):
        if actMod == True and i == actPos:
            canvasPersonal.polygon([(flechaIzquierdaX+dx,flechaIzquierdaY+dy) for dx,dy in flechaIzquierda],0xff0000,0xff0000)
            canvasPersonal.polygon([(flechaDerechaX+dx,flechaDerechaY+dy) for dx,dy in flechaDerecha],0xff0000,0xff0000)
        flechaIzquierdaY+=35
        flechaDerechaY+=35
    for i in range(6):
        colorTexto[i]=0x000000    
    colorTexto[actPos]=0xff0000    
    canvasPersonal.text((240,410),getLang(u"VOLVER"),0xffffff,font=(u"legend",25,appuifw.STYLE_BOLD))
    canvasPersonal.text((120,85),getLang(u"PERSONAL"),0xbbbbbb,font=(u"symbol",27))
    canvasPersonal.text((119,84),getLang(u"PERSONAL"),0x000000,font=(u"symbol",27))
    canvasPersonal.line((20,120,330,120),0)
    canvasPersonal.text((30,135),getLang(u"PESO"),0x000000,font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasPersonal.text((250,135),u"%03.2f kg"%datos[0],colorTexto[0],font=(u"legend",17))
    canvasPersonal.line((20,155,330,155),0)
    canvasPersonal.text((30,170),getLang(u"ALTURA"),0x000000,font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasPersonal.text((250,170),u"%03d cm"%datos[1],colorTexto[1],font=(u"legend",17))
    canvasPersonal.line((20,190,330,190),0)
    canvasPersonal.text((30,205),getLang(u"TOTALINSU"),0x000000,font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasPersonal.text((250,205),u"%03d u"%datos[2],colorTexto[2],font=(u"legend",17))
    canvasPersonal.line((20,225,330,225),0)
    canvasPersonal.text((30,240),getLang(u"RATD"),0x000000,font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasPersonal.text((250,240),u"%02.2f"%datos[3],colorTexto[3],font=(u"legend",17))
    canvasPersonal.line((20,260,330,260),0)
    canvasPersonal.text((30,275),getLang(u"RATA"),0x000000,font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasPersonal.text((250,275),u"%02.2f"%datos[4],colorTexto[4],font=(u"legend",17))
    canvasPersonal.line((20,295,330,295),0)
    canvasPersonal.text((30,310),getLang(u"RATC"),0x000000,font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasPersonal.text((250,310),u"%02.2f"%datos[5],colorTexto[5],font=(u"legend",17))
    canvasPersonal.line((20,330,330,330),0)

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
    if actMod==True:
        if movimientos[actPos][2] == u"peso":
            base_de_datos.actualizar_peso(datos[actPos])
        elif movimientos[actPos][2] == u"altura":
            base_de_datos.actualizar_altura(datos[actPos])
        elif movimientos[actPos][2] == u"totalinsu":
            base_de_datos.actualizar_totalinsu(datos[actPos])
        elif movimientos[actPos][2] == u"ratd":
            base_de_datos.actualizar_ratiodesayuno(datos[actPos])
        elif movimientos[actPos][2] == u"rata":
            base_de_datos.actualizar_ratioalmuerzo(datos[actPos])
        else:
            base_de_datos.actualizar_ratiocena(datos[actPos])
        #print datos[actPos]
        actMod=False
    else:        
        actMod=True
    appuifw.app.body = canvasPersonal
    
def moverCursor(desppeso,desp,despfloat,pos):
    global actPos
    global movimientos
    global datos
    if actMod==True:
        # si estamos en peso
        if actPos == 0:
            datos[actPos]+=desppeso
        # si estamos en altura o totalinsu
        elif actPos == 1 or actPos == 2:
            datos[actPos]+=desp
        # si estamos en algun ratio
        else:
            datos[actPos]+=despfloat
        # control de limites superiores depende del caso    
        if desp>0:
            if datos[actPos]>movimientos[actPos][3]:
                datos[actPos]=movimientos[actPos][3]
        else:
            # control de limites inferiores depende del caso
            if actPos == 0 or actPos == 1:
                if datos[actPos]<0:
                    datos[actPos]=0
            elif actPos == 2:
                if datos[actPos]<1:
                    datos[actPos]=1
            else:
                if datos[actPos]<0.01:
                    datos[actPos]=0.01
    else:
        actPos+=movimientos[actPos][1][pos]
    appuifw.app.body = canvasPersonal
    
def press_up():
    moverCursor(5,50,1,0)

def press_right():
    moverCursor(0.01,1,0.01,1)

def press_down():
    moverCursor(-5,-50,-1,2)

def press_left():
    moverCursor(-0.01,-1,-0.01,3)

def mostrar_personal(vAtras):
    global movimientos
    movimientos=[
        [0,[0,0,1,0],u"peso",400.00],
        [1,[-1,0,1,0],u"altura",250],
        [2,[-1,0,1,0],u"totalinsu",200],
        [3,[-1,0,1,0],u"ratd",10.00],
        [4,[-1,0,1,0],u"rata",10.00],
        [5,[-1,0,0,0],u"ratc",10.00]
        ]
    global datos
    datos=[0 for x in range(6)]
    # recupera los parametros de configuracion.py
    for i in range(6):
        if i == 0:
            # peso de la persona en kg 76.00
            datos[i] = base_de_datos.obtener_peso_actual()
        elif i == 1:
            # altura de la persona en cm 175
            datos[i] = base_de_datos.obtener_altura_actual()
        elif i == 2:
            # total de insulinas que se administra diariamente 38
            datos[i] = base_de_datos.obtener_totalinsu_actual()
        #ratio es la necesidad de insulina por racion de hidratos de carbono
        #ratios de desayuno, almuerzo y cena; normalmente los ratios del desayuno a cena varian,
        #por eso es necesario guardar los 3 tipos
        #ratioDesayuno = 0.75
        #ratioAlmuerzo = 1.34
        #ratioCena = 2
        elif i == 3:            
            datos[i] = base_de_datos.obtener_ratiodesayuno_actual()
        elif i == 4:
            datos[i] = base_de_datos.obtener_ratioalmuerzo_actual()
        else:
            datos[i] = base_de_datos.obtener_ratiocena_actual()
    global actPos
    actPos=0
    global actMod
    actMod=False
    ruta = unidad+':\\python\\resources\\ui\\'
    global imPersonal
    imPersonal = graphics.Image.open(ruta+'fondo01.png')
    global canvasPersonal
    canvasPersonal = appuifw.Canvas(redraw_callback = handle_redraw)
    canvasPersonal.blit(imPersonal)
    appuifw.app.body = canvasPersonal
    appuifw.app.screen = 'full'
    appuifw.app.title = u"personal"
    canvasPersonal.bind(key_codes.EKeySelect, press_select)
    canvasPersonal.bind(key_codes.EKeyUpArrow, press_up)
    canvasPersonal.bind(key_codes.EKeyRightArrow, press_right)
    canvasPersonal.bind(key_codes.EKeyDownArrow, press_down)
    canvasPersonal.bind(key_codes.EKeyLeftArrow, press_left) 
    global gvAtras
    gvAtras=vAtras
    if len(vAtras)==1:
        appuifw.app.exit_key_handler=gvAtras[0]
    else:
        appuifw.app.exit_key_handler=volverAtras
    