# Archivo: dieta.py
# Autor: Jorge Aguirre Andreu
# Descripción: Consulta a a través de un servicio web dietas que te vengan bien, dependiendo de tu peso y tu situación actual.
# También puedes calcular la cantidad aproximada de dosis de insulina que necesitas según que alimentos tomes.
# ADVERTENCIA: El cálculo es una mera aproximación, debe seguir las indicaciones de su endocrino.
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
    global canvasDieta
    global imDieta
    canvasDieta.blit(imDieta)
    canvasDieta.text((190,85),getLang(u"DIETA"),0xbbbbbb,font=(u"symbol",27))
    canvasDieta.text((189,84),getLang(u"DIETA"),0x000000,font=(u"symbol",27))
    canvasDieta.text((240,410),getLang(u"VOLVER"),0xffffff,font=(u"legend",25,appuifw.STYLE_BOLD))
    canvasDieta.text((25,410),getLang(u"OPCIONES"),0xffffff,font=(u"legend",25,appuifw.STYLE_BOLD))

def volverAtras():
    global gvAtras
    gvAtrasEnvio=[0 for x in range(len(gvAtras)-1)]
    for i in range(len(gvAtras)-1):
        gvAtrasEnvio[i]=gvAtras[i]
    gvAtras[len(gvAtras)-1](gvAtrasEnvio)

def mostrarDieta(vAtras):
    ruta = unidad+':\\python\\resources\\ui\\'
    global imDieta
    imDieta = graphics.Image.open(ruta+'fondo11.png')
    global canvasDieta
    canvasDieta = appuifw.Canvas(redraw_callback = handle_redraw)
    canvasDieta.blit(imDieta)
    appuifw.app.body = canvasDieta
    appuifw.app.screen = 'full'
    appuifw.app.title = u"Dieta"
    global gvAtras
    gvAtras=vAtras
    if len(vAtras)==1:
        appuifw.app.exit_key_handler=gvAtras[0]
    else:
        appuifw.app.exit_key_handler=volverAtras