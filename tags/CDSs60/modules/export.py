# Archivo: export.py
# Autor: Jorge Aguirre Andreu
# Descripción: Puedes exportar todo el diario, las citas médicas, las dietas, las estadisticas a un formato
# (por determinar) mediante conexión(a determinar) con un ordenador(del endocrino), asi se facilitan las revisiones
# y se agiliza el trato entre ambas partes.
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
    global canvasExport
    global imExport
    canvasExport.blit(imExport)
    canvasExport.text((178,85),getLang(u"EXPORTAR"),0xbbbbbb,font=(u"symbol",27))
    canvasExport.text((177,84),getLang(u"EXPORTAR"),0x000000,font=(u"symbol",27))
    canvasExport.text((240,410),getLang(u"VOLVER"),0xffffff,font=(u"legend",25,appuifw.STYLE_BOLD))
    canvasExport.text((25,410),getLang(u"OPCIONES"),0xffffff,font=(u"legend",25,appuifw.STYLE_BOLD))

def volverAtras():
    global gvAtras
    gvAtrasEnvio=[0 for x in range(len(gvAtras)-1)]
    for i in range(len(gvAtras)-1):
        gvAtrasEnvio[i]=gvAtras[i]
    gvAtras[len(gvAtras)-1](gvAtrasEnvio)

def mostrarExport(vAtras):
    ruta = unidad+':\\python\\resources\\ui\\'
    global imExport
    imExport = graphics.Image.open(ruta+'fondo11.png')
    global canvasExport
    canvasExport = appuifw.Canvas(redraw_callback = handle_redraw)
    canvasExport.blit(imExport)
    appuifw.app.body = canvasExport
    appuifw.app.screen = 'full'
    appuifw.app.title = u"Exportar"
    global gvAtras
    gvAtras=vAtras
    if len(vAtras)==1:
        appuifw.app.exit_key_handler=gvAtras[0]
    else:
        appuifw.app.exit_key_handler=volverAtras