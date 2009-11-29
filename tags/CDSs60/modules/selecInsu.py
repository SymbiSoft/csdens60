# Archivo: selecInsu.py
# Autor: Jorge Aguirre Andreu
# Descripción: Sirve para insertar o borrar insulinas 
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
    global canvasSelecInsu
    global imSelecInsu
    global valor
    global datos
    global actPos
    global ind
    flechaIzquierdaX=50
    flechaIzquierdaY=216
    flechaIzquierda=[(10,0),(0,5),(10,10)]
    flechaDerechaX=290
    flechaDerechaY=216
    flechaDerecha=[(0,0),(10,5),(0,10)]
    colorTexto=[0 for x in range(2)]
    for i in range(2):
        colorTexto[i]=0x000000
    colorTexto[actPos]=0xff0000
    canvasSelecInsu.blit(imSelecInsu)
    canvasSelecInsu.rectangle((20,120,330,245),outline=0xeeeeee,fill=0xeeeeee)
    canvasSelecInsu.line((20,120,330,120),0)
    canvasSelecInsu.text((40,135),getLang(u"ADDINSULINA"),colorTexto[0],font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasSelecInsu.line((20,155,330,155),0)
    if actPos == 1:
        canvasSelecInsu.polygon([(flechaIzquierdaX+dx,flechaIzquierdaY+dy) for dx,dy in flechaIzquierda],0xff0000,0xff0000)
        canvasSelecInsu.polygon([(flechaDerechaX+dx,flechaDerechaY+dy) for dx,dy in flechaDerecha],0xff0000,0xff0000)
    canvasSelecInsu.text((40,170),getLang(u"ELIMINSULINA"),colorTexto[1],font=(u"legend",17,appuifw.STYLE_BOLD))    
    canvasSelecInsu.text((150,225),datos[ind],colorTexto[1],font=(u"legend",17))
    #canvasSelecInsu.text((150,225),base_de_datos.obtener_insulina(ind),colorTexto[1],font=(u"legend",17))
    canvasSelecInsu.line((20,245,330,245),0)
    #canvasSelecInsu.text((30,285),getLang(u"BORRAINSU"),0x000000,font=(u"symbol",18,appuifw.STYLE_BOLD))
    #canvasSelecInsu.text((30,305),getLang(u"BORRAINSU1"),0x000000,font=(u"symbol",18,appuifw.STYLE_BOLD))
    #canvasSelecInsu.text((30,325),getLang(u"BORRAINSU2"),0x000000,font=(u"symbol",18,appuifw.STYLE_BOLD))
    canvasSelecInsu.text((240,410),getLang(u"VOLVER"),0xffffff,font=(u"legend",25,appuifw.STYLE_BOLD))
    canvasSelecInsu.text((125,85),getLang(u"INSU"),0xbbbbbb,font=(u"symbol",27))
    canvasSelecInsu.text((124,84),getLang(u"INSU"),0x000000,font=(u"symbol",27))

def volverAtras():
    global gvAtras
    gvAtrasEnvio=[0 for x in range(len(gvAtras)-1)]
    for i in range(len(gvAtras)-1):
        gvAtrasEnvio[i]=gvAtras[i]
    gvAtras[len(gvAtras)-1](gvAtrasEnvio)
    
def press_select():
    global movimientos
    global valor
    global actPos
    global actMod
    global datos
    global ind
    if movimientos[actPos][2] == u"inserta":
        valor=appuifw.query(getLang(u"ESCRIBE TEXTO:"), "text")
        if valor != None:
            print valor
            base_de_datos.actualizar_insulina(valor)
            volverAtras()
    elif movimientos[actPos][2] == u"desahb":
        if actMod == False:
            #base_de_datos.deshabilita_insulina(ind)
            #appuifw.note(u"Insulina borrada","info")
            actMod = True
            #volverAtras()
            appuifw.app.body = canvasSelecInsu
        else:
            actMod = False
            appuifw.app.body = canvasSelecInsu
    
def moverCursor(desp,pos):
    global actPos
    global ind
    global movimientos
    global datos
    if movimientos[actPos][2] == u"desahb":
        if desp == 1 or desp == -1:
            ind += desp
        if ind > len(datos)-1:
            ind = len(datos)-1
        elif ind < 0:
            ind = 0
    actPos+=movimientos[actPos][1][pos]
    appuifw.app.body = canvasSelecInsu
    
def press_up():
    moverCursor(0,0)

def press_right():
    moverCursor(1,1)

def press_down():
    moverCursor(0,2)

def press_left():
    moverCursor(-1,3)

def mostrar_selecInsu(vAtras):
    global movimientos
    movimientos=[
        [0,[0,0,1,0],u"inserta"],
        [1,[-1,0,0,0],u"desahb"]
        ]
    global actMod
    actMod=False
    global valor
    global datos
    datos=[0 for x in range(base_de_datos.obtener_numero_insulinas()+1)]
    for i in range(len(datos)):
        datos[i] = base_de_datos.obtener_insulina(i)
    # actPos se mueve por el menu
    global actPos
    actPos=0
    # ind se mueve por los tipos de insulina en la tabla insulinas
    global ind
    ind = 0
    ruta = unidad+':\\python\\resources\\ui\\'
    global imSelecInsu
    imSelecInsu = graphics.Image.open(ruta+'fondo01.png')
    global canvasSelecInsu
    canvasSelecInsu = appuifw.Canvas(redraw_callback = handle_redraw)
    canvasSelecInsu.blit(imSelecInsu)
    appuifw.app.body = canvasSelecInsu
    appuifw.app.screen = 'full'
    appuifw.app.title = u"selecInsu"
    canvasSelecInsu.bind(key_codes.EKeySelect, press_select)
    canvasSelecInsu.bind(key_codes.EKeyUpArrow, press_up)
    canvasSelecInsu.bind(key_codes.EKeyRightArrow, press_right)
    canvasSelecInsu.bind(key_codes.EKeyDownArrow, press_down)
    canvasSelecInsu.bind(key_codes.EKeyLeftArrow, press_left) 
    global gvAtras
    gvAtras=vAtras
    if len(vAtras)==1:
        appuifw.app.exit_key_handler=gvAtras[0]
    else:
        appuifw.app.exit_key_handler=volverAtras
    