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

def handle_redraw(rect):
    global canvasSelecInsu
    global imSelecInsu
    
    canvasSelecInsu.blit(imSelecInsu)
    canvasSelecInsu.text((240,410),getLang(u"VOLVER"),0xffffff,font=(u"legend",25,appuifw.STYLE_BOLD))
    canvasSelecInsu.text((125,85),getLang(u"INSU"),0xbbbbbb,font=(u"symbol",27))
    canvasSelecInsu.text((124,84),getLang(u"INSU"),0x000000,font=(u"symbol",27))

def volverAtras():
    global gvAtras
    gvAtrasEnvio=[0 for x in range(len(gvAtras)-1)]
    for i in range(len(gvAtras)-1):
        gvAtrasEnvio[i]=gvAtras[i]
    gvAtras[len(gvAtras)-1](gvAtrasEnvio)

def mostrar_selecInsu(vAtras):
    ruta = unidad+':\\python\\resources\\ui\\'
    global imSelecInsu
    imSelecInsu = graphics.Image.open(ruta+'fondo01.png')
    global canvasSelecInsu
    canvasSelecInsu = appuifw.Canvas(redraw_callback = handle_redraw)
    canvasSelecInsu.blit(imSelecInsu)
    appuifw.app.body = canvasSelecInsu
    appuifw.app.screen = 'full'
    appuifw.app.title = u"selecInsu"
    #canvasSelecInsu.bind(key_codes.EKeySelect, press_select)
    #canvasSelecInsu.bind(key_codes.EKeyUpArrow, press_up)
    #canvasSelecInsu.bind(key_codes.EKeyRightArrow, press_right)
    #canvasSelecInsu.bind(key_codes.EKeyDownArrow, press_down)
    #canvasSelecInsu.bind(key_codes.EKeyLeftArrow, press_left) 
    global gvAtras
    gvAtras=vAtras
    if len(vAtras)==1:
        appuifw.app.exit_key_handler=gvAtras[0]
    else:
        appuifw.app.exit_key_handler=volverAtras
    