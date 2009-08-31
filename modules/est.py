# Archivo: est.py
# Autor: Jorge Aguirre Andreu
# Descripción: Realiza promedios a petición de análisis de glucosa que estén almacenados en el diario.
# Promedios de después de todas las comidas, a intervalos de tiempo que quiera.
# También es capaz de avisar con antelación de cuando se puede quedar sin tiras reactivas(usadas para los análisis).
# Aspecto configurable por el usuario.
#
#   Copyright (C) 2009  Jorge Aguirre Andreu
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
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
    global canvasEst
    global imEst
    canvasEst.blit(imEst)
    canvasEst.text((160,85),getLang(u"EST"),0xbbbbbb,font=(u"symbol",27))
    canvasEst.text((159,84),getLang(u"EST"),0x000000,font=(u"symbol",27))
    canvasEst.text((240,410),getLang(u"VOLVER"),0xffffff,font=(u"legend",25,appuifw.STYLE_BOLD))
    canvasEst.text((25,410),getLang(u"OPCIONES"),0xffffff,font=(u"legend",25,appuifw.STYLE_BOLD))

def volverAtras():
    global gvAtras
    gvAtrasEnvio=[0 for x in range(len(gvAtras)-1)]
    for i in range(len(gvAtras)-1):
        gvAtrasEnvio[i]=gvAtras[i]
    gvAtras[len(gvAtras)-1](gvAtrasEnvio)

def mostrarEst(vAtras):
    ruta = unidad+':\\python\\resources\\ui\\'
    global imEst
    imEst = graphics.Image.open(ruta+'fondo11.png')
    global canvasEst
    canvasEst = appuifw.Canvas(redraw_callback = handle_redraw)
    canvasEst.blit(imEst)
    appuifw.app.body = canvasEst
    appuifw.app.screen = 'full'
    appuifw.app.title = u"Estadística"
    global gvAtras
    gvAtras=vAtras
    if len(vAtras)==1:
        appuifw.app.exit_key_handler=gvAtras[0]
    else:
        appuifw.app.exit_key_handler=volverAtras