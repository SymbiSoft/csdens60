# Archivo: export.py
# Autor: Jorge Aguirre Andreu
# Descripci�n: Puedes exportar todo el diario en un archivo xml para la aplicaci�n
# csds60analyzer mediante conexi�n(a determinar) con un ordenador(del endocrino), asi se facilitan las revisiones
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

import e32, appuifw, sys, os, graphics, codecs

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


def generar_xml():
    global unidad
    xml=u""
    datos=base_de_datos.obtener_datos_diario()
    fecha=0
    for i in range(datos.count_line()):
        datos.get_line()
        if fecha!=datos.col(1):
            fecha=datos.col(1)
            xml=xml+u"</dia>\n<dia>\n\t<fecha>"+str(fecha)+u"</fecha>\n"
        xml=xml+u"\t<"+str(datos.col(2))+u">"+str(datos.col(3))+u"</"+str(datos.col(2))+u">\n"
        datos.next_line()
    xmlFinal=u"<?xml version=\"1.0\" encoding=\"UTF-8\"?><root>"+xml[6:]+u"</dia></root>"
    fichero=codecs.open(unidad+':\\Python\\resources\db\db.xml','w','utf8')
    fichero.write(xmlFinal)

def generar_html():
    global unidad
    
    html=u""
    cabecerahtml=u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\"><html><head><title>CSDs60WebAnalyzer</title>"
    css=u"<style type=\"text/css\">#datosCont{margin:20px auto 0;padding:15px 20px;width:700px}div.dat\
osDia{margin-bottom:15px}div.datosDiaTitulo{border-bottom:2px solid #97d25d;cursor:pointer;font-we\
ight:700}div.datosDiaCont{display:none;padding-left:20px}div.datosDiaContAtr{float:left;width:70%}\
div.datosDiaContVal{float:right;text-align:center;width:30%}</style>"
    javascript=u"<script type=\"text/javascript\">function mostrar(act){var hijos=act.parentNode.child\
Nodes;for(var i=0;i<hijos.length;i++){if(hijos[i].tagName==\"DIV\"&&hijos[i].className==\"datosDia\
Cont\"){if(hijos[i].style.display==\"block\"){hijos[i].style.display=\"none\"}else{hijos[i].style.\
display=\"block\"}}}}window.onload=function(){var dias=document.getElementById(\"datosCont\").chil\
dNodes;for(var i=0;i<dias.length;i++){if(dias[i].tagName==\"DIV\"&&dias[i].className==\"datosDia\"\
){for(var j=0;j<dias[i].childNodes.length;j++){if(dias[i].childNodes[j].tagName==\"DIV\"&&dias[i].\
childNodes[j].className==\"datosDiaTitulo\"){var diaValor=dias[i].childNodes[j];var fecha=new Date\
();fecha.setTime(diaValor.innerHTML*1000);diaValor.innerHTML=fecha.getDate()+\"/\"+(fecha.getMonth(\
)+1)+\"/\"+fecha.getFullYear();dias[i].childNodes[j].onclick=function(){mostrar(this)}}}}}}</script>"
    datos=base_de_datos.obtener_datos_diario()
    fecha=0
    for i in range(datos.count_line()):
        datos.get_line()
        if fecha!=datos.col(1):
            fecha=datos.col(1)
            html=html+u"</div></div><div class=\"datosDia\"><div class=\"datosDiaTitulo\">"+str(fecha)+"</div><div class=\"datosDiaCont\">"
        html=html+u"<div class=\"datosDiaContAtr\">"+str(datos.col(2))+u"</div><div class=\"datosDiaContVal\">"+str(datos.col(3))+u"</div>"
        datos.next_line()
    htmlFinal=cabecerahtml+css+javascript+u"</head><body><div id=\"datosCont\">"+html[12:]+u"</div></body></html>"
    fichero=codecs.open(unidad+':\\Python\\resources\db\datos.html','w','utf8')
    fichero.write(htmlFinal)

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
    generar_xml()
    generar_html()