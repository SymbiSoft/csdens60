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

import e32, appuifw, sys, os, graphics

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
    global canvasCitas
    global imCitas
    canvasCitas.blit(imCitas)
    canvasCitas.text((150,85),getLang(u"CITAS"),0xbbbbbb,font=(u"symbol",27))
    canvasCitas.text((149,84),getLang(u"CITAS"),0x000000,font=(u"symbol",27))
    canvasCitas.text((240,410),getLang(u"VOLVER"),0xffffff,font=(u"legend",25,appuifw.STYLE_BOLD))
    canvasCitas.text((25,410),getLang(u"OPCIONES"),0xffffff,font=(u"legend",25,appuifw.STYLE_BOLD))

def volverAtras():
    global gvAtras
    gvAtrasEnvio=[0 for x in range(len(gvAtras)-1)]
    for i in range(len(gvAtras)-1):
        gvAtrasEnvio[i]=gvAtras[i]
    gvAtras[len(gvAtras)-1](gvAtrasEnvio)

def mostrarCitas(vAtras):
    ruta = unidad+':\\python\\resources\\ui\\'
    global imCitas
    imCitas = graphics.Image.open(ruta+'fondo11.png')
    global canvasCitas
    canvasCitas = appuifw.Canvas(redraw_callback = handle_redraw)
    canvasCitas.blit(imCitas)
    appuifw.app.body = canvasCitas
    appuifw.app.screen = 'full'
    appuifw.app.title = u"Citas"
    global gvAtras
    gvAtras=vAtras
    if len(vAtras)==1:
        appuifw.app.exit_key_handler=gvAtras[0]
    else:
        appuifw.app.exit_key_handler=volverAtras