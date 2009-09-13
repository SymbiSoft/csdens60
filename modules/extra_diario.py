# Archivo: extra_diario.py
# Autor: Jorge Aguirre Andreu
# Descripción: Muestra las opciones extra del diario de diabetico, medicamentos que tomas, enfermedad que padezcas y 
# las comidas que comes.
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

import e32, appuifw, graphics, sys, os, key_codes

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
    global canvasExtra
    global imExtra
    global actPos
    global valor
    colorTexto=[0 for x in range(8)]
    colorRelleno=[0 for x in range(8)]
    for i in range(8):
        colorTexto[i]=0x000000
    colorTexto[actPos]=0xff0000    
    canvasExtra.blit(imExtra)
    canvasExtra.text((190,85),getLang(u"EXTRA"),0xbbbbbb,font=(u"symbol",27))
    canvasExtra.text((189,84),getLang(u"EXTRA"),0x000000,font=(u"symbol",27))
    canvasExtra.text((240,410),getLang(u"VOLVER"),0xffffff,font=(u"legend",25,appuifw.STYLE_BOLD))    
    canvasExtra.text((30,115),getLang(u"COMIDAS"),0x000000,font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasExtra.rectangle((20,120,150,340),outline=0xeeeeee,fill=0xeeeeee)
    canvasExtra.line((20,120,330,120),0)
    canvasExtra.text((40,135),getLang(u"DESAYUNO"),0x000000,font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasExtra.text((220,135),valor[0],colorTexto[0],font=(u"legend",17))
    canvasExtra.text((40,155),getLang(u"MEDIAMAÑANA"),0x000000,font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasExtra.text((220,155),valor[1],colorTexto[1],font=(u"legend",17))
    canvasExtra.text((40,175),getLang(u"ALMUERZO"),0x000000,font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasExtra.text((220,175),valor[2],colorTexto[2],font=(u"legend",17))
    canvasExtra.text((40,195),getLang(u"MERIENDA"),0x000000,font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasExtra.text((220,195),valor[3],colorTexto[3],font=(u"legend",17))
    canvasExtra.text((40,215),getLang(u"CENA"),0x000000,font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasExtra.text((220,215),valor[4],colorTexto[4],font=(u"legend",17))
    canvasExtra.text((40,235),getLang(u"RESOPON"),0x000000,font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasExtra.text((220,235),valor[5],colorTexto[5],font=(u"legend",17))
    canvasExtra.line((20,240,330,240),0)
    canvasExtra.text((30,255),getLang(u"ENFERMEDADES"),0x000000,font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasExtra.text((220,255),valor[6],colorTexto[6],font=(u"legend",17))
    canvasExtra.line((20,280,330,280),0)
    canvasExtra.text((30,295),getLang(u"MEDICAMENTOS"),0x000000,font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasExtra.text((220,295),valor[7],colorTexto[7],font=(u"legend",17))

def volverAtras():
    global gvAtras
    gvAtrasEnvio=[0 for x in range(len(gvAtras)-1)]
    for i in range(len(gvAtras)-1):
        gvAtrasEnvio[i]=gvAtras[i]
    gvAtras[len(gvAtras)-1](gvAtrasEnvio)
    
def press_select():
    global movimientos
    global actPos
    global valor
    valor[actPos]=appuifw.query(getLang(u"ESCRIBE TEXTO:"), "text")
    base_de_datos.actualizar_extra_diario(actDia,actMes,actAno,movimientos[actPos][3],valor[actPos])
    if valor[actPos]==None:
        valor[actPos]=getLang(u"NADA")
    appuifw.app.body = canvasExtra
    
def moverCursor(pos):
    global actPos
    global movimientos
    actPos+=movimientos[actPos][1][pos]
    appuifw.app.body = canvasExtra
    
def press_up():
    moverCursor(0)

def press_right():
    moverCursor(1)

def press_down():
    moverCursor(2)

def press_left():
    moverCursor(3)

def mostrar_extra(dia,mes,ano,vAtras):
    global actDia
    actDia=dia
    global actMes
    actMes=mes
    global actAno
    actAno=ano    
    global movimientos
    movimientos=[
        [0,[0,0,1,0],u"--",u"desayuno"],
        [1,[-1,0,1,0],u"--",u"mediamanana"],
        [2,[-1,0,1,0],u"--",u"almuerzo"],
        [3,[-1,0,1,0],u"--",u"merienda"],
        [4,[-1,0,1,0],u"--",u"cena"],
        [5,[-1,0,1,0],u"--",u"resopon"],
        [6,[-1,0,1,0],u"--",u"enfermedades"],
        [7,[-1,0,0,0],u"--",u"medicamentos"],
        ]
    global valor
    valor=[0 for x in range(8)]
    #for i in range(8):
        #valor[i]=getLang(u"NADA")
    for i in range(8):
        valor[i]=base_de_datos.obtener_extra_diario(actDia,actMes,actAno,movimientos[i][3])
        if valor[i]==0:
            valor[i]=getLang(u"NADA")
    global actPos
    actPos=0
    ruta = unidad+':\\python\\resources\\ui\\'
    global imExtra
    imExtra = graphics.Image.open(ruta+'fondo01.png')
    global canvasExtra
    canvasExtra = appuifw.Canvas(redraw_callback = handle_redraw)
    canvasExtra.blit(imExtra)
    appuifw.app.body = canvasExtra
    appuifw.app.screen = 'full'
    appuifw.app.title = u"Extra_diario"
    canvasExtra.bind(key_codes.EKeySelect, press_select)
    canvasExtra.bind(key_codes.EKeyUpArrow, press_up)
    canvasExtra.bind(key_codes.EKeyRightArrow, press_right)
    canvasExtra.bind(key_codes.EKeyDownArrow, press_down)
    canvasExtra.bind(key_codes.EKeyLeftArrow, press_left)
    global gvAtras
    gvAtras=vAtras
    if len(vAtras)==1:
        appuifw.app.exit_key_handler=gvAtras[0]
    else:
        appuifw.app.exit_key_handler=volverAtras