# Archivo: citas_dia.py
# Autor: Jorge Aguirre Andreu
# Descripción: Muestra las citas médicas a las que debe acudir el usuario, previamente
# introducidas por él mismo. 
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

import e32, appuifw, graphics, key_codes, sys, os, keycapture

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
    global canvasCitasDia
    global imCitasDia
    global actDia
    global actMes
    global actAno
    global actPos
    global valor
    colorTexto=[0 for x in range(2)]
    for i in range(2):
        colorTexto[i]=0x000000
    colorTexto[actPos]=0xff0000
    canvasCitasDia.blit(imCitasDia)
    canvasCitasDia.rectangle((20,120,220,225),outline=0xeeeeee,fill=0xeeeeee)
    canvasCitasDia.text((120,85),getLang(u"CITA")+" (%d-%d-%d)"%(actDia,actMes,actAno),0xbbbbbb,font=(u"symbol",27))
    canvasCitasDia.text((119,84),getLang(u"CITA")+" (%d-%d-%d)"%(actDia,actMes,actAno),0x000000,font=(u"symbol",27))
    canvasCitasDia.text((240,410),getLang(u"VOLVER"),0xffffff,font=(u"legend",25,appuifw.STYLE_BOLD))
    
    canvasCitasDia.line((20,120,330,120),0)
    canvasCitasDia.text((40,135),getLang(u"NREG"),colorTexto[0],font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasCitasDia.line((20,155,330,155),0)
    canvasCitasDia.text((40,170),ajustar_texto(valor),0x000000,font=(u"legend",17))
    canvasCitasDia.line((20,190,330,190),0)
    canvasCitasDia.text((40,205),getLang(u"BREG"),colorTexto[1],font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasCitasDia.line((20,225,330,225),0)

def press_select():
    global movimientos
    global actPos
    global valor
    global actDia
    global actMes
    global actAno
    global marcado
    if(movimientos[actPos][2]) == u"nuevo":
        valor = appuifw.query(getLang(u"ESCRIBE TEXTO:"), "text", base_de_datos.obtener_registros_citas(actDia,actMes,actAno))
        if valor == None:
            contenidoDB = base_de_datos.obtener_registros_citas(actDia,actMes,actAno)
            if contenidoDB == 0:
                valor = getLang(u"NADA")
            else:
                valor = contenidoDB
        else:
            base_de_datos.actualizar_registros_citas(actDia,actMes,actAno,valor)
    elif(movimientos[actPos][2]) == u"borra":
        valor = getLang(u"NADA")
        base_de_datos.borrar_registros_citas(actDia,actMes,actAno)
    appuifw.app.body = canvasCitasDia

def moverCursor(pos):
    global actPos
    global movimientos
    actPos+=movimientos[actPos][1][pos]
    appuifw.app.body = canvasCitasDia

def press_up():
    moverCursor(0)

def press_right():
    moverCursor(1)

def press_down():
    moverCursor(2)

def press_left():
    moverCursor(3)

def volverAtras():
    global gvAtras
    gvAtrasEnvio=[0 for x in range(len(gvAtras)-1)]
    for i in range(len(gvAtras)-1):
        gvAtrasEnvio[i]=gvAtras[i]
    gvAtras[len(gvAtras)-1](gvAtrasEnvio)

def ajustar_texto(texto):
    maximo=13
    grupos=[
        [u"aábdeéghnñoópquúü",float(13)/float(20)],
        [u"cçsvy",float(13)/float(26)],
        [u"fiíjl",float(13)/float(36)],
        [u"kxz",float(13)/float(23)],
        [u"rt",float(13)/float(30)],
        [u"m",float(13)/float(13)],
        [u"w",float(13)/float(14)],
        [u" .,:;",float(13)/float(44)],
    ]
    total=float(0)
    numero=0
    if texto == None:
        texto = getLang(u"NADA")
    for i in texto:
        for j in grupos:
            if i in j[0] and total<maximo:
                if total+j[1]<maximo:
                    total=total+j[1]
                    numero=numero+1
    if numero+1<len(texto):
        return texto[:numero-2]+"..."
    return texto    

def mostrar_citas_dia_aux(vAtras):
    global actDia
    global actMes
    global actAno
    mostrar_citas_dia(actDia,actMes,actAno,vAtras)

def mostrar_citas_dia(dia,mes,ano,vAtras):
    global actDia
    actDia=dia
    global actMes
    actMes=mes
    global actAno
    actAno=ano
    global movimientos
    movimientos=[
        [0,[0,0,1,0],u"nuevo"],
        [1,[-1,0,0,0],u"borra"]        
        ]  
    global valor
    valor = base_de_datos.obtener_registros_citas(actDia,actMes,actAno)
    if valor == None:
        valor = getLang(u"NADA")
    global actPos
    actPos=0
    global actMod
    actMod=False    
    ruta = unidad+':\\python\\resources\\ui\\'
    global imCitasDia
    imCitasDia = graphics.Image.open(ruta+'fondo01.png')
    global canvasCitasDia
    canvasCitasDia = appuifw.Canvas(redraw_callback = handle_redraw)
    canvasCitasDia.blit(imCitasDia)
    appuifw.app.body = canvasCitasDia
    appuifw.app.screen = 'full'
    appuifw.app.title = u"Citas_dia"
    canvasCitasDia.bind(key_codes.EKeySelect, press_select)
    canvasCitasDia.bind(key_codes.EKeyUpArrow, press_up)
    canvasCitasDia.bind(key_codes.EKeyRightArrow, press_right)
    canvasCitasDia.bind(key_codes.EKeyDownArrow, press_down)
    canvasCitasDia.bind(key_codes.EKeyLeftArrow, press_left) 
    global gvAtras
    gvAtras=vAtras
    if len(vAtras)==1:
        appuifw.app.exit_key_handler=gvAtras[0]
    else:
        appuifw.app.exit_key_handler=volverAtras