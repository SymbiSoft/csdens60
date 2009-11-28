# Archivo: diario_dia.py
# Autor: Jorge Aguirre Andreu
# Descripción: Muestra un diario de diabetico digital, donde llevar desde las dosis de insulina y análisis de glucosa
# hasta el deporte que realizas. 
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
import extra_diario
import base_de_datos


def handle_redraw(rect):
    global actDia
    global actMes
    global actAno
    global actPos
    global canvasDiarioDia
    global imDiarioDia
    global datos
    global movimientos
    flechaIzquierdaX=127
    flechaIzquierdaY=124
    flechaIzquierda=[(10,0),(0,5),(10,10)]
    flechaDerechaX=196
    flechaDerechaY=124
    flechaDerecha=[(0,0),(10,5),(0,10)]
    desp=130
    canvasDiarioDia.blit(imDiarioDia)
    colorTexto=[0 for x in range(24)]
    colorRelleno=[0 for x in range(24)]
    canvasDiarioDia.rectangle((20,120,120,380),outline=0xeeeeee,fill=0xeeeeee)
    for i in range(11):
        if i!=2 and i!=5 and i!=8 and actMod==True:
            if movimientos[actPos][2]==u"%di"%i:
                canvasDiarioDia.polygon([(flechaIzquierdaX+dx,flechaIzquierdaY+dy) for dx,dy in flechaIzquierda],0xff0000,0xff0000)
                canvasDiarioDia.polygon([(flechaDerechaX+dx,flechaDerechaY+dy) for dx,dy in flechaDerecha],0xff0000,0xff0000)
            elif movimientos[actPos][2]==u"%dd"%i:
                canvasDiarioDia.polygon([(flechaIzquierdaX+dx+desp,flechaIzquierdaY+dy) for dx,dy in flechaIzquierda],0xff0000,0xff0000)
                canvasDiarioDia.polygon([(flechaDerechaX+dx+desp,flechaDerechaY+dy) for dx,dy in flechaDerecha],0xff0000,0xff0000)
            elif movimientos[actPos][2]==u"%dt"%i:
                canvasDiarioDia.polygon([(flechaIzquierdaX+dx-105,flechaIzquierdaY+dy) for dx,dy in flechaIzquierda],0xff0000,0xff0000)
                canvasDiarioDia.polygon([(flechaDerechaX+dx-90,flechaDerechaY+dy) for dx,dy in flechaDerecha],0xff0000,0xff0000)
        flechaIzquierdaY+=20
        flechaDerechaY+=20
    for i in range(24):
        colorTexto[i]=0x000000
    for i in range(24):
        if movimientos[i][2]==u"sb":
            if datos[i]==1:
                colorRelleno[i]=0xdddddd
            else:
                colorRelleno[i]=0xffffff
    colorTexto[actPos]=0xff0000
    canvasDiarioDia.text((240,410),getLang(u"VOLVER"),0xffffff,font=(u"legend",25,appuifw.STYLE_BOLD))
    canvasDiarioDia.text((44,410),getLang(u"EXTRA"),0xffffff,font=(u"legend",25,appuifw.STYLE_BOLD))
    canvasDiarioDia.text((120,85),getLang(u"DIARIO")+" (%d-%d-%d)"%(actDia,actMes,actAno),0xbbbbbb,font=(u"symbol",27))
    canvasDiarioDia.text((119,84),getLang(u"DIARIO")+" (%d-%d-%d)"%(actDia,actMes,actAno),0x000000,font=(u"symbol",27))
    canvasDiarioDia.text((145,115),getLang(u"ANTES"),0x000000,font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasDiarioDia.text((265,115),getLang(u"DESPUES"),0x000000,font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasDiarioDia.line((20,120,330,120),0)
    canvasDiarioDia.text((30,135),getLang(u"DESAYUNO"),0x000000,font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasDiarioDia.text((140,135),u"%03d mg"%datos[0],colorTexto[0],font=(u"legend",17))
    canvasDiarioDia.text((270,135),u"%03d mg"%datos[1],colorTexto[1],font=(u"legend",17))
    canvasDiarioDia.text((40,155),base_de_datos.obtener_insulina(datos[2]),colorTexto[2],font=(u"legend",17))
    canvasDiarioDia.text((149,155),u"%02d ml"%datos[3],colorTexto[3],font=(u"legend",17))
    canvasDiarioDia.text((279,155),u"%02d ml"%datos[4],colorTexto[4],font=(u"legend",17))
    canvasDiarioDia.text((40,175),getLang(u"DEPORTE"),0x000000,font=(u"legend",17))
    canvasDiarioDia.rectangle((151,162,166,177),outline=colorTexto[5],fill=colorRelleno[5])
    canvasDiarioDia.rectangle((281,162,296,177),outline=colorTexto[6],fill=colorRelleno[6])
    canvasDiarioDia.line((20,180,330,180),0)
    canvasDiarioDia.text((30,195),getLang(u"ALMUERZO"),0x000000,font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasDiarioDia.text((140,195),u"%03d mg"%datos[7],colorTexto[7],font=(u"legend",17))
    canvasDiarioDia.text((270,195),u"%03d mg"%datos[8],colorTexto[8],font=(u"legend",17))
    canvasDiarioDia.text((40,215),base_de_datos.obtener_insulina(datos[9]),colorTexto[9],font=(u"legend",17))
    canvasDiarioDia.text((149,215),u"%02d ml"%datos[10],colorTexto[10],font=(u"legend",17))
    canvasDiarioDia.text((279,215),u"%02d ml"%datos[11],colorTexto[11],font=(u"legend",17))
    canvasDiarioDia.text((40,235),getLang(u"DEPORTE"),0x000000,font=(u"legend",17))
    canvasDiarioDia.rectangle((151,222,166,237),outline=colorTexto[12],fill=colorRelleno[12])
    canvasDiarioDia.rectangle((281,222,296,237),outline=colorTexto[13],fill=colorRelleno[13])
    canvasDiarioDia.line((20,240,330,240),0)
    canvasDiarioDia.text((30,255),getLang(u"CENA"),0x000000,font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasDiarioDia.text((140,255),u"%03d mg"%datos[14],colorTexto[14],font=(u"legend",17))
    canvasDiarioDia.text((270,255),u"%03d mg"%datos[15],colorTexto[15],font=(u"legend",17))
    canvasDiarioDia.text((40,275),base_de_datos.obtener_insulina(datos[16]),colorTexto[16],font=(u"legend",17))
    canvasDiarioDia.text((149,275),u"%02d ml"%datos[17],colorTexto[17],font=(u"legend",17))
    canvasDiarioDia.text((279,275),u"%02d ml"%datos[18],colorTexto[18],font=(u"legend",17))
    canvasDiarioDia.text((40,295),getLang(u"DEPORTE"),0x000000,font=(u"legend",17))
    canvasDiarioDia.rectangle((151,282,166,297),outline=colorTexto[19],fill=colorRelleno[19])
    canvasDiarioDia.rectangle((281,282,296,297),outline=colorTexto[20],fill=colorRelleno[20])
    canvasDiarioDia.line((20,300,330,300),0)
    canvasDiarioDia.text((30,315),getLang(u"ORINA"),0x000000,font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasDiarioDia.text((140,315),u"%03d mg"%datos[21],colorTexto[21],font=(u"legend",17))
    canvasDiarioDia.text((40,335),getLang(u"ACETONA"),0x000000,font=(u"legend",17))
    canvasDiarioDia.text((158,335),u"%d +"%datos[22],colorTexto[22],font=(u"legend",17))
    canvasDiarioDia.line((20,340,330,340),0)
    canvasDiarioDia.text((30,365),getLang(u"GLUCAGON"),0x000000,font=(u"legend",17))
    canvasDiarioDia.rectangle((151,352,166,367),outline=colorTexto[23],fill=colorRelleno[23])

def press_select():
    global actMod
    global movimientos
    global actPos
    global datos
    if actMod==True:
        global actDia
        global actMes
        global actAno
        base_de_datos.actualizar_diario_dia(actDia,actMes,actAno,movimientos[actPos][4],datos[actPos])
        actMod=False
    else:
        if movimientos[actPos][2]==u"sb":
            if datos[actPos]==0:
                datos[actPos]=1
            else:
                datos[actPos]=0
            base_de_datos.actualizar_diario_dia(actDia,actMes,actAno,movimientos[actPos][4],datos[actPos])
        else:
            actMod=True
    appuifw.app.body = canvasDiarioDia

def moverCursor(desp,pos):
    global actPos
    global movimientos
    global datos
    global actDia
    global actMes
    global actAno
    if actMod==True:
        datos[actPos]+=desp
        if desp>0:
            if datos[actPos]>movimientos[actPos][3]:
                datos[actPos]=movimientos[actPos][3]
        else:
            if datos[actPos]<0:
                datos[actPos]=0
    else:
        actPos+=movimientos[actPos][1][pos]
    if movimientos[actPos][2][1]==u"t":
        comida=u"cena"
        if actPos==2:
            comida=u"desayuno"
        elif actPos==9:
            comida=u"almuerzo"
        movimientos[actPos+1][4]=u""+comida+base_de_datos.obtener_insulina(datos[actPos])+"antes"
        movimientos[actPos+2][4]=u""+comida+base_de_datos.obtener_insulina(datos[actPos])+"despues"
        datos[actPos+1]=base_de_datos.obtener_diario_dia(actDia,actMes,actAno,movimientos[actPos+1][4])
        datos[actPos+2]=base_de_datos.obtener_diario_dia(actDia,actMes,actAno,movimientos[actPos+2][4])
    appuifw.app.body = canvasDiarioDia

def press_up():
    moverCursor(50,0)

def press_right():
    moverCursor(1,1)

def press_down():
    moverCursor(-50,2)

def press_left():
    moverCursor(-1,3)

def volverAtras():
    global gvAtras
    gvAtrasEnvio=[0 for x in range(len(gvAtras)-1)]
    for i in range(len(gvAtras)-1):
        gvAtrasEnvio[i]=gvAtras[i]
    gvAtras[len(gvAtras)-1](gvAtrasEnvio)

def teclaPresionada(key):
    if key['type']==3:
        if key['scancode']==164:
            diarioExtra()

def diarioExtra():
    global gvAtras
    global actDia
    global actMes
    global actAno
    gvAtrasEnvio=[0 for x in range(len(gvAtras)+1)]
    for i in range(len(gvAtras)):
        gvAtrasEnvio[i]=gvAtras[i]
    gvAtrasEnvio[len(gvAtras)]=mostrar_diario_dia_aux
    extra_diario.mostrar_extra(actDia,actMes,actAno,gvAtrasEnvio)

def mostrar_diario_dia_aux(vAtras):
    global actDia
    global actMes
    global actAno
    mostrar_diario_dia(actDia,actMes,actAno,vAtras)

def mostrar_diario_dia(dia,mes,ano,vAtras):
    global actDia
    actDia=dia
    global actMes
    actMes=mes
    global actAno
    actAno=ano
    global movimientos
    movimientos=[
        [0,[0,1,3,0],u"0i",500,u"desayunoantes"],
        [1,[0,0,3,-1],u"0d",500,u"desayunodespues"],
        [2,[0,1,7,0],u"1t",base_de_datos.obtener_numero_insulinas(),u"desayunodosis"],
        [3,[-3,1,2,-1],u"1i",99,u"desayuno"+base_de_datos.obtener_insulina(0)+"antes"],
        [4,[-3,0,2,-1],u"1d",99,u"desayuno"+base_de_datos.obtener_insulina(0)+"despues"],
        [5,[-2,1,2,0],u"sb",0,u"desayunodeporteantes"],
        [6,[-2,0,2,-1],u"sb",0,u"desayunodeportedespues"],
        [7,[-2,1,3,0],u"3i",500,u"almuerzoantes"],
        [8,[-2,0,3,-1],u"3d",500,u"almuerzodespues"],
        [9,[-7,1,7,0],u"4t",base_de_datos.obtener_numero_insulinas(),u"almuerzodosis"],
        [10,[-3,1,2,-1],u"4i",99,u"almuerzo"+base_de_datos.obtener_insulina(0)+"antes"],
        [11,[-3,0,2,-1],u"4d",99,u"almuerzo"+base_de_datos.obtener_insulina(0)+"despues"],
        [12,[-2,1,2,0],u"sb",0,u"almuerzodeporteantes"],
        [13,[-2,0,2,-1],u"sb",0,u"almuerzodeportedespues"],
        [14,[-2,1,3,0],u"6i",500,u"cenaantes"],
        [15,[-2,0,3,-1],u"6d",500,u"cenadespues"],
        [16,[-7,1,0,0],u"7t",base_de_datos.obtener_numero_insulinas(),u"cenadosis"],
        [17,[-3,1,2,-1],u"7i",99,u"cena"+base_de_datos.obtener_insulina(0)+"antes"],
        [18,[-3,0,2,-1],u"7d",99,u"cena"+base_de_datos.obtener_insulina(0)+"despues"],
        [19,[-2,1,2,0],u"sb",0,u"cenadeporteantes"],
        [20,[-2,0,2,-1],u"sb",0,u"cenadeportedespues"],
        [21,[-2,0,1,0],u"9i",500,u"orina"],
        [22,[-1,0,1,0],u"10i",4,u"acetona"],
        [23,[-1,0,0,0],u"sb",0,u"glucagon"],
        ]
    global datos
    datos=[0 for x in range(24)]
    for i in range(24):
        datos[i]=base_de_datos.obtener_diario_dia(actDia,actMes,actAno,movimientos[i][4])
    global actPos
    actPos=0
    global actMod
    actMod=False
    ruta = unidad+':\\python\\resources\\ui\\'
    global imDiarioDia
    imDiarioDia = graphics.Image.open(ruta+'fondo11.png')
    global canvasDiarioDia
    canvasDiarioDia = appuifw.Canvas(redraw_callback = handle_redraw,event_callback=teclaPresionada)
    canvasDiarioDia.blit(imDiarioDia)
    appuifw.app.body = canvasDiarioDia
    appuifw.app.screen = 'full'
    appuifw.app.title = u"Diario_dia"
    canvasDiarioDia.bind(key_codes.EKeySelect, press_select)
    canvasDiarioDia.bind(key_codes.EKeyUpArrow, press_up)
    canvasDiarioDia.bind(key_codes.EKeyRightArrow, press_right)
    canvasDiarioDia.bind(key_codes.EKeyDownArrow, press_down)
    canvasDiarioDia.bind(key_codes.EKeyLeftArrow, press_left) 
    global gvAtras
    gvAtras=vAtras
    if len(vAtras)==1:
        appuifw.app.exit_key_handler=gvAtras[0]
    else:
        appuifw.app.exit_key_handler=volverAtras