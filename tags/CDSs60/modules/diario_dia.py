# Archivo: diario_dia.py
# Autor: Jorge Aguirre Andreu
# Descripción: Muestra un diario de diabetico digital, donde llevar desde las dosis de insulina y análisis de glucosa
# hasta las comidas que comes, el deporte que realizas, medicamentos que tomas, enfermedad que padezcas y 
# si has tenido hipoglucemias o hiperglucemias. 
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

import e32, appuifw, graphics, key_codes

def handle_redraw(rect):
    global actDia
    global actMes
    global actAno
    global actPos
    global canvasDiarioDia
    global imDiarioDia
    global datos
    flechaIzquierdaX=127
    flechaIzquierdaY=124
    flechaIzquierda=[(10,0),(0,5),(10,10)]
    flechaDerechaX=196
    flechaDerechaY=124
    flechaDerecha=[(0,0),(10,5),(0,10)]
    desp=130
    canvasDiarioDia.blit(imDiarioDia)
    for i in range(11):
        if i!=2 and i!=5 and i!=8 and actMod==True:
            if movimientos[actPos][2]==u"%di"%i:
                canvasDiarioDia.polygon([(flechaIzquierdaX+dx,flechaIzquierdaY+dy) for dx,dy in flechaIzquierda],0xff0000,0xff0000)
                canvasDiarioDia.polygon([(flechaDerechaX+dx,flechaDerechaY+dy) for dx,dy in flechaDerecha],0xff0000,0xff0000)
            elif movimientos[actPos][2]==u"%dd"%i:
                canvasDiarioDia.polygon([(flechaIzquierdaX+dx+desp,flechaIzquierdaY+dy) for dx,dy in flechaIzquierda],0xff0000,0xff0000)
                canvasDiarioDia.polygon([(flechaDerechaX+dx+desp,flechaDerechaY+dy) for dx,dy in flechaDerecha],0xff0000,0xff0000)
        flechaIzquierdaY+=20
        flechaDerechaY+=20
    colorTexto=[0 for x in range(26)]
    for i in range(26):
        colorTexto[i]=0x000000
    colorTexto[actPos]=0xff0000
    canvasDiarioDia.text((120,85),u"Diario (%d-%d-%d)"%(actDia,actMes,actAno),0xbbbbbb,font=(u"symbol",27))
    canvasDiarioDia.text((119,84),u"Diario (%d-%d-%d)"%(actDia,actMes,actAno),0x000000,font=(u"symbol",27))
    canvasDiarioDia.text((145,115),u"Antes",0x000000,font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasDiarioDia.text((265,115),u"Después",0x000000,font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasDiarioDia.rectangle((20,120,120,340),outline=0xeeeeee,fill=0xeeeeee)
    canvasDiarioDia.line((20,120,330,120),0)
    canvasDiarioDia.text((30,135),u"Desayuno",0x000000,font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasDiarioDia.text((140,135),u"%03d mg"%datos[0],colorTexto[0],font=(u"legend",17))
    canvasDiarioDia.text((270,135),u"%03d mg"%datos[1],colorTexto[1],font=(u"legend",17))
    canvasDiarioDia.text((40,155),u"Dosis",colorTexto[2],font=(u"legend",17))
    canvasDiarioDia.text((149,155),u"%02d ml"%datos[3],colorTexto[3],font=(u"legend",17))
    canvasDiarioDia.text((279,155),u"%02d ml"%datos[4],colorTexto[4],font=(u"legend",17))
    canvasDiarioDia.text((40,175),u"Deporte",0x000000,font=(u"legend",17))
    canvasDiarioDia.rectangle((151,162,166,177),outline=colorTexto[5],fill=0xffffff)
    canvasDiarioDia.rectangle((281,162,296,177),outline=colorTexto[6],fill=0xffffff)
    canvasDiarioDia.line((20,180,330,180),0)
    canvasDiarioDia.text((30,195),u"Almuerzo",0x000000,font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasDiarioDia.text((140,195),u"%03d mg"%datos[7],colorTexto[7],font=(u"legend",17))
    canvasDiarioDia.text((270,195),u"%03d mg"%datos[8],colorTexto[8],font=(u"legend",17))
    canvasDiarioDia.text((40,215),u"Dosis",colorTexto[9],font=(u"legend",17))
    canvasDiarioDia.text((149,215),u"%02d ml"%datos[10],colorTexto[10],font=(u"legend",17))
    canvasDiarioDia.text((279,215),u"%02d ml"%datos[11],colorTexto[11],font=(u"legend",17))
    canvasDiarioDia.text((40,235),u"Deporte",0x000000,font=(u"legend",17))
    canvasDiarioDia.rectangle((151,222,166,237),outline=colorTexto[12],fill=0xffffff)
    canvasDiarioDia.rectangle((281,222,296,237),outline=colorTexto[13],fill=0xffffff)
    canvasDiarioDia.line((20,240,330,240),0)
    canvasDiarioDia.text((30,255),u"Cena",0x000000,font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasDiarioDia.text((140,255),u"%03d mg"%datos[14],colorTexto[14],font=(u"legend",17))
    canvasDiarioDia.text((270,255),u"%03d mg"%datos[15],colorTexto[15],font=(u"legend",17))
    canvasDiarioDia.text((40,275),u"Dosis",colorTexto[16],font=(u"legend",17))
    canvasDiarioDia.text((149,275),u"%02d ml"%datos[17],colorTexto[17],font=(u"legend",17))
    canvasDiarioDia.text((279,275),u"%02d ml"%datos[18],colorTexto[18],font=(u"legend",17))
    canvasDiarioDia.text((40,295),u"Deporte",0x000000,font=(u"legend",17))
    canvasDiarioDia.rectangle((151,282,166,297),outline=colorTexto[19],fill=0xffffff)
    canvasDiarioDia.rectangle((281,282,296,297),outline=colorTexto[20],fill=0xffffff)
    canvasDiarioDia.line((20,300,330,300),0)
    canvasDiarioDia.text((30,315),u"Orina",0x000000,font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasDiarioDia.text((140,315),u"%03d mg"%datos[21],colorTexto[21],font=(u"legend",17))
    canvasDiarioDia.text((270,315),u"%03d mg"%datos[22],colorTexto[22],font=(u"legend",17))
    canvasDiarioDia.text((40,335),u"Acetona",0x000000,font=(u"legend",17))
    canvasDiarioDia.text((140,335),u"%03d mg"%datos[23],colorTexto[23],font=(u"legend",17))
    canvasDiarioDia.text((270,335),u"%03d mg"%datos[24],colorTexto[24],font=(u"legend",17))
    canvasDiarioDia.line((20,340,330,340),0)
    canvasDiarioDia.text((30,365),u"Glucagón",0x000000,font=(u"legend",17))
    canvasDiarioDia.rectangle((151,352,166,367),outline=colorTexto[25],fill=0xffffff)

def press_select():
    global actMod
    if actMod==True:
        actMod=False
    else:
        actMod=True
    appuifw.app.body = canvasDiarioDia

def press_up():
    global actPos
    if actMod==True:
        global datos
        datos[actPos]+=50
    else:
        global movimientos
        actPos+=movimientos[actPos][1][0]
    appuifw.app.body = canvasDiarioDia

def press_right():
    global actPos
    if actMod==True:
        global datos
        datos[actPos]+=1
    else:
        global movimientos
        actPos+=movimientos[actPos][1][1]
    appuifw.app.body = canvasDiarioDia

def press_down():
    global actPos
    if actMod==True:
        global datos
        datos[actPos]-=50
    else:
        global movimientos
        actPos+=movimientos[actPos][1][2]
    appuifw.app.body = canvasDiarioDia

def press_left():
    global actPos
    if actMod==True:
        global datos
        datos[actPos]-=1
    else:
        global movimientos
        actPos+=movimientos[actPos][1][3]
    appuifw.app.body = canvasDiarioDia

def mostrar_diario_dia(dia,mes,ano):
    global actDia
    actDia=dia
    global actMes
    actMes=mes
    global actAno
    actAno=ano
    global datos
    datos=[0 for x in range(26)]
    for i in range(26):
        datos[i]=0
    global movimientos
    movimientos=[
        [0,[0,1,3,0],u"0i"],
        [1,[0,0,3,-1],u"0d"],
        [2,[0,1,7,0],u"--"],
        [3,[-3,1,2,-1],u"1i"],
        [4,[-3,0,2,-1],u"1d"],
        [5,[-2,1,2,0],u"--"],
        [6,[-2,0,2,-1],u"--"],
        [7,[-2,1,3,0],u"3i"],
        [8,[-2,0,3,-1],u"3d"],
        [9,[-7,1,7,0],u"--"],
        [10,[-3,1,2,-1],u"4i"],
        [11,[-3,0,2,-1],u"4d"],
        [12,[-2,1,2,0],u"--"],
        [13,[-2,0,2,-1],u"--"],
        [14,[-2,1,3,0],u"6i"],
        [15,[-2,0,3,-1],u"6d"],
        [16,[-7,1,0,0],u"--"],
        [17,[-3,1,2,-1],u"7i"],
        [18,[-3,0,2,-1],u"7d"],
        [19,[-2,1,2,0],u"--"],
        [20,[-2,0,2,-1],u"--"],
        [21,[-2,1,2,0],u"9i"],
        [22,[-2,0,2,-1],u"9d"],
        [23,[-2,1,2,0],u"10i"],
        [24,[-2,0,0,-1],u"10d"],
        [25,[-2,0,0,0],u"--"]
        ]
    global actPos
    actPos=0
    global actMod
    actMod=False
    ruta = 'c:\\python\\resources\\ui\\'
    global imDiarioDia
    imDiarioDia = graphics.Image.open(ruta+'fondo11.png')
    global canvasDiarioDia
    canvasDiarioDia = appuifw.Canvas(redraw_callback = handle_redraw)
    canvasDiarioDia.blit(imDiarioDia)
    appuifw.app.body = canvasDiarioDia
    appuifw.app.screen = 'full'
    appuifw.app.title = u"Diario_dia"
    canvasDiarioDia.bind(key_codes.EKeySelect, press_select)
    canvasDiarioDia.bind(key_codes.EKeyUpArrow, press_up)
    canvasDiarioDia.bind(key_codes.EKeyRightArrow, press_right)
    canvasDiarioDia.bind(key_codes.EKeyDownArrow, press_down)
    canvasDiarioDia.bind(key_codes.EKeyLeftArrow, press_left)