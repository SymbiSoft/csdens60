# Archivo: config.py
# Autor: Jorge Aguirre Andreu
# Descripción: Lleva todo lo relacionado con el perfil del usuario, como su peso, la activación de servicios de aviso
# para citas médicas o cantidad de tiras reactivas.
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
import selecIdioma, personal, selecBD, selecAlarm

def handle_redraw(rect):
    global canvasConf
    global imConf
    global actPos
    colorTexto=[0 for x in range(4)]
    for i in range(4):
        colorTexto[i]=0x000000
    colorTexto[actPos]=0xff0000
    canvasConf.blit(imConf)
    canvasConf.text((150,85),getLang(u"CONFIGURACION"),0xbbbbbb,font=(u"symbol",27))
    canvasConf.text((149,84),getLang(u"CONFIGURACION"),0x000000,font=(u"symbol",27))
    canvasConf.text((240,410),getLang(u"VOLVER"),0xffffff,font=(u"legend",25,appuifw.STYLE_BOLD))
    
    canvasConf.line((20,120,330,120),0)
    canvasConf.text((40,135),getLang(u"IDIOMA"),colorTexto[0],font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasConf.line((20,155,330,155),0)
    canvasConf.text((40,170),getLang(u"PERSONAL"),colorTexto[1],font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasConf.line((20,190,330,190),0)
    canvasConf.text((40,205),getLang(u"BD"),colorTexto[2],font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasConf.line((20,225,330,225),0)
    canvasConf.text((40,240),getLang(u"ALARMA"),colorTexto[3],font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasConf.line((20,260,330,260),0)
    
def config_idioma():
    global actPos
    global gvAtras
    gvAtrasEnvio=[0 for x in range(len(gvAtras)+1)]
    for i in range(len(gvAtras)):
        gvAtrasEnvio[i]=gvAtras[i]
    gvAtrasEnvio[len(gvAtras)]=mostrarConfig
    selecIdioma.mostrar_idioma(gvAtrasEnvio)
    
def config_personal():
    global actPos
    global gvAtras
    gvAtrasEnvio=[0 for x in range(len(gvAtras)+1)]
    for i in range(len(gvAtras)):
        gvAtrasEnvio[i]=gvAtras[i]
    gvAtrasEnvio[len(gvAtras)]=mostrarConfig
    personal.mostrar_personal(gvAtrasEnvio)
    
def config_bd():
    global actPos
    global gvAtras
    gvAtrasEnvio=[0 for x in range(len(gvAtras)+1)]
    for i in range(len(gvAtras)):
        gvAtrasEnvio[i]=gvAtras[i]
    gvAtrasEnvio[len(gvAtras)]=mostrarConfig
    selecBD.mostrar_selecBD(gvAtrasEnvio)
    
def config_alarma():
    global actPos
    global gvAtras
    gvAtrasEnvio=[0 for x in range(len(gvAtras)+1)]
    for i in range(len(gvAtras)):
        gvAtrasEnvio[i]=gvAtras[i]
    gvAtrasEnvio[len(gvAtras)]=mostrarConfig
    selecAlarm.mostrar_selecAlarm(gvAtrasEnvio)
    
def volverAtras():
    global gvAtras
    gvAtrasEnvio=[0 for x in range(len(gvAtras)-1)]
    for i in range(len(gvAtras)-1):
        gvAtrasEnvio[i]=gvAtras[i]
    gvAtras[len(gvAtras)-1](gvAtrasEnvio)
    
def moverCursor(pos):
    global actPos
    global movimientos
    actPos+=movimientos[actPos][1][pos]
    appuifw.app.body = canvasConf
    
def press_select():
    global movimientos
    global actPos
    if(movimientos[actPos][3]) == u"IDIOMA":
        config_idioma()        
    elif(movimientos[actPos][3]) == u"PERSONAL":
        config_personal()        
    elif(movimientos[actPos][3]) == u"BD":
        config_bd()        
    elif(movimientos[actPos][3]) == u"ALARMA":
        config_alarma()
    
def press_up():
    moverCursor(0)

def press_right():
    moverCursor(1)

def press_down():
    moverCursor(2)

def press_left():
    moverCursor(3)

def mostrarConfig(vAtras):
    global movimientos
    movimientos=[
        [0,[0,0,1,0],u"--",u"IDIOMA"],
        [1,[-1,0,1,0],u"--",u"PERSONAL"],
        [2,[-1,0,1,0],u"--",u"BD"],
        [3,[-1,0,0,0],u"--",u"ALARMA"],
        ]
    global actPos
    actPos=0
    ruta = unidad+':\\python\\resources\\ui\\'
    global imConf
    imConf = graphics.Image.open(ruta+'fondo01.png')
    global canvasConf
    canvasConf = appuifw.Canvas(redraw_callback = handle_redraw)
    canvasConf.blit(imConf)
    appuifw.app.body = canvasConf
    appuifw.app.screen = 'full'
    appuifw.app.title = u"Configuracion"
    canvasConf.bind(key_codes.EKeySelect, press_select)
    canvasConf.bind(key_codes.EKeyUpArrow, press_up)
    canvasConf.bind(key_codes.EKeyRightArrow, press_right)
    canvasConf.bind(key_codes.EKeyDownArrow, press_down)
    canvasConf.bind(key_codes.EKeyLeftArrow, press_left)
    global gvAtras
    gvAtras=vAtras
    if len(vAtras)==1:
        appuifw.app.exit_key_handler=gvAtras[0]
    else:
        appuifw.app.exit_key_handler=volverAtras