# Archivo: selecIdioma.py
# Autor: Jorge Aguirre Andreu
# Descripción: Sirve para seleccionar el idioma deseado cargado de los .py existentes 
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
    global canvasSelecIdioma
    global imSelecIdioma
    global colorTexto
    global datos
    colorTexto = 0x000000
    flechaIzquierdaX=80
    flechaIzquierdaY=190
    flechaIzquierda=[(10,0),(0,5),(10,10)]
    flechaDerechaX=260
    flechaDerechaY=190
    flechaDerecha=[(0,0),(10,5),(0,10)]
    canvasSelecIdioma.blit(imSelecIdioma)
    canvasSelecIdioma.text((240,410),getLang(u"VOLVER"),0xffffff,font=(u"legend",25,appuifw.STYLE_BOLD))
    canvasSelecIdioma.text((110,85),getLang(u"IDIOMA"),0xbbbbbb,font=(u"symbol",27))
    canvasSelecIdioma.text((109,84),getLang(u"IDIOMA"),0x000000,font=(u"symbol",27))
    if actMod == True:
        colorTexto = 0xff0000
        canvasSelecIdioma.polygon([(flechaIzquierdaX+dx,flechaIzquierdaY+dy) for dx,dy in flechaIzquierda],0xff0000,0xff0000)
        canvasSelecIdioma.polygon([(flechaDerechaX+dx,flechaDerechaY+dy) for dx,dy in flechaDerecha],0xff0000,0xff0000)    
    
    canvasSelecIdioma.text((75,140),getLang(u"SIDIOMA"),0x000000,font=(u"symbol",22))
    
    # recuperamos la cadena de texto asociada al idioma
    canvasSelecIdioma.text((145,200),base_de_datos.obtener_idioma_actual(),colorTexto,font=(u"symbol",20))
    canvasSelecIdioma.text((30,300),getLang(u"REINICIA"),0x000000,font=(u"symbol",18,appuifw.STYLE_BOLD))
    canvasSelecIdioma.text((30,320),getLang(u"REINICIA1"),0x000000,font=(u"symbol",18,appuifw.STYLE_BOLD))
    print base_de_datos.obtener_idioma_actual()
    
def press_select():
    global actMod
    global actPos
    global datos
    if actMod == True:
        print u"pulsado"
        base_de_datos.actualizar_idioma(datos[actPos][0]) # actualizamos con el valor de la constante
        actMod = False 
    else:
        print u"sin pulsar"        
        actMod = True
    appuifw.app.body = canvasSelecIdioma
    
def moverCursor(desp,pos):
    global actPos
    global datos
    if actMod == True:        
        if actPos == 0 and pos == 1: # si estamos en la posicion 0 y queremos ir a la izquierda, no avanza
            desp = 0
            print u"entra en if"
        elif actPos == len(datos)-1 and pos == 0: # si estamos en la posicion ultima y queremos ir a la derecha, no avanza
            desp = 0
            print u"entra en elif"
        actPos += desp # avanza por los idiomas
        datos[actPos] = base_de_datos.obtener_idiomas(actPos) # recupera el valor para dicha posicion
        print u"actpos es: %d"%(actPos)

    appuifw.app.body = canvasSelecIdioma
    

def volverAtras():
    global gvAtras
    gvAtrasEnvio=[0 for x in range(len(gvAtras)-1)]
    for i in range(len(gvAtras)-1):
        gvAtrasEnvio[i]=gvAtras[i]
    gvAtras[len(gvAtras)-1](gvAtrasEnvio)
    
def press_right():
    moverCursor(1,0)

def press_left():
    moverCursor(-1,1)

def mostrar_idioma(vAtras):    
    global actPos
    actPos=0
    global actMod
    actMod=False
    global datos
    datos=[0 for x in range(base_de_datos.obtener_numero_idiomas())]
    for i in range(len(datos)):
        datos[i] = base_de_datos.obtener_idiomas(i) #datos[0] = [u'es',u'Español'], tenemos los idiomas de esa forma
    ruta = unidad+':\\python\\resources\\ui\\'
    global imSelecIdioma
    imSelecIdioma = graphics.Image.open(ruta+'fondo01.png')
    global canvasSelecIdioma
    canvasSelecIdioma = appuifw.Canvas(redraw_callback = handle_redraw)
    canvasSelecIdioma.blit(imSelecIdioma)
    appuifw.app.body = canvasSelecIdioma
    appuifw.app.screen = 'full'
    appuifw.app.title = u"selecIdioma"    
    canvasSelecIdioma.bind(key_codes.EKeySelect, press_select)
    canvasSelecIdioma.bind(key_codes.EKeyRightArrow, press_right)
    canvasSelecIdioma.bind(key_codes.EKeyLeftArrow, press_left)   
    global gvAtras
    gvAtras=vAtras
    if len(vAtras)==1:
        appuifw.app.exit_key_handler=gvAtras[0]
    else:
        appuifw.app.exit_key_handler=volverAtras
    