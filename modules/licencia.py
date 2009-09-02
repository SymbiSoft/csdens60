# Archivo: licencia.py
# Autor: Jorge Aguirre Andreu
# Descripción: Muestra la licencia de la aplicacion. 
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

import e32, appuifw, graphics, sys, os, imp

try:
    raise Exception
except Exception:
    path = sys.exc_info()[2].tb_frame.f_code.co_filename
if not path:
    path = os.path.join(os.getcwd(), 'default.py')
unidad=path[0]

#_akntextutils = imp.load_dynamic('_akntextutils', unidad+':\\Python\\modules\\_akntextutils.pyd')

modulospropios = unidad+':\\Python\\modules'
sys.path.append(modulospropios)
from idioma import getLang
#from _akntextutils import wrap_text_to_array

def handle_redraw(rect):
    global canvasLic
    global imLic
    canvasLic.blit(imLic)
    canvasLic.text((190,85),getLang(u"LIC"),0xbbbbbb,font=(u"symbol",27))
    canvasLic.text((189,84),getLang(u"LIC"),0x000000,font=(u"symbol",27))
    canvasLic.text((240,410),getLang(u"VOLVER"),0xffffff,font=(u"legend",25,appuifw.STYLE_BOLD))
    
    titulo=u"CSDs60  Copyright (C) 2009"
    autor=u"Jorge Aguirre Andreu"
    t=getLang(u"T")
    t1=getLang(u"T1") 
    t2=getLang(u"T2")
    t3=getLang(u"T3")
    t4=getLang(u"T4")
    t5=u"http://www.gnu.org/licenses/gpl.html"

    #lines = wrap_text_to_array(long_str, 'dense', 176)

    #x, y = 2, 0
    #for line in lines:
     #   y += 14
      #  canvas.text((x, y), line, font='dense')
    canvasLic.text((2,110),titulo,0x000000,font=(u"legend",19))
    canvasLic.text((2,130),autor,0x000000,font=(u"legend",19))
    canvasLic.line((4,140,350,140),0)
    canvasLic.text((2,160),t,0x000000,font=(u"legend",19))
    canvasLic.text((2,180),t1,0x000000,font=(u"legend",19))
    canvasLic.text((2,200),t2,0x000000,font=(u"legend",19))
    canvasLic.text((2,220),t3,0x000000,font=(u"legend",19))
    canvasLic.text((2,240),t4,0x000000,font=(u"legend",19))
    canvasLic.text((2,260),t5,0x0000FF,font=(u"legend",19))
    
def volverAtras():
    global gvAtras
    gvAtrasEnvio=[0 for x in range(len(gvAtras)-1)]
    for i in range(len(gvAtras)-1):
        gvAtrasEnvio[i]=gvAtras[i]
    gvAtras[len(gvAtras)-1](gvAtrasEnvio)
    
def mostrar_licencia(vAtras):
    ruta = unidad+':\\python\\resources\\ui\\'
    global imLic
    imLic = graphics.Image.open(ruta+'fondo01.png')
    global canvasLic
    canvasLic = appuifw.Canvas(redraw_callback = handle_redraw)
    canvasLic.blit(imLic)
    appuifw.app.body = canvasLic
    appuifw.app.screen = 'full'
    appuifw.app.title = u"Licencia"
    global gvAtras
    gvAtras=vAtras
    if len(vAtras)==1:
        appuifw.app.exit_key_handler=gvAtras[0]
    else:
        appuifw.app.exit_key_handler=volverAtras