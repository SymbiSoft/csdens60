# Archivo: dieta.py
# Autor: Jorge Aguirre Andreu
# Descripción: Puedes calcular la cantidad aproximada de dosis de insulina que necesitas según que alimentos tomes.
# ADVERTENCIA: EL CALCULO ES UNA MERA APROXIMACION, DEBE SEGUIR LAS INDICACIONES DE SU MEDICO ENDOCRINO, ASI COMO
# CONFIGURAR CORRECTAMENTE LOS PARAMETROS NECESARIOS DE INSULINAS SIGUIENDO CONSEJO MEDICO.
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

import e32, appuifw, sys, os, graphics, key_codes

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
    global canvasDieta
    global imDieta
    global datos
    global actPos
    global momentos
    global resultado
    global j
    flechaIzquierdaX=195
    flechaIzquierdaY=107
    flechaIzquierda=[(10,0),(0,5),(10,10)]
    flechaDerechaX=303
    flechaDerechaY=107
    flechaDerecha=[(0,0),(10,5),(0,10)]
    colorTexto=[0 for x in range(8)]
    canvasDieta.blit(imDieta)
    canvasDieta.rectangle((20,105,190,350),outline=0xeeeeee,fill=0xeeeeee)
    for i in range(8):
        if actMod == True and i == actPos:
            if actPos == 0:
                canvasDieta.polygon([(flechaIzquierdaX+dx,flechaIzquierdaY+dy) for dx,dy in flechaIzquierda],0xff0000,0xff0000)
                canvasDieta.polygon([(flechaDerechaX+dx,flechaDerechaY+dy) for dx,dy in flechaDerecha],0xff0000,0xff0000)
            elif actPos == 1:
                flechaIzquierdaY+=20
                flechaDerechaY+=20
                canvasDieta.polygon([(flechaIzquierdaX+dx,flechaIzquierdaY+dy) for dx,dy in flechaIzquierda],0xff0000,0xff0000)
                canvasDieta.polygon([(flechaDerechaX+dx,flechaDerechaY+dy) for dx,dy in flechaDerecha],0xff0000,0xff0000)
            elif actPos == 2:
                flechaIzquierdaY+=37
                flechaDerechaY+=37
                canvasDieta.polygon([(flechaIzquierdaX+dx,flechaIzquierdaY+dy) for dx,dy in flechaIzquierda],0xff0000,0xff0000)
                canvasDieta.polygon([(flechaDerechaX+dx,flechaDerechaY+dy) for dx,dy in flechaDerecha],0xff0000,0xff0000)
            elif actPos == 3:
                flechaIzquierdaY+=72
                flechaDerechaY+=72
                canvasDieta.polygon([(flechaIzquierdaX+dx,flechaIzquierdaY+dy) for dx,dy in flechaIzquierda],0xff0000,0xff0000)
                canvasDieta.polygon([(flechaDerechaX+dx,flechaDerechaY+dy) for dx,dy in flechaDerecha],0xff0000,0xff0000)
            elif actPos == 4:
                flechaIzquierdaY+=107
                flechaDerechaY+=107
                canvasDieta.polygon([(flechaIzquierdaX+dx,flechaIzquierdaY+dy) for dx,dy in flechaIzquierda],0xff0000,0xff0000)
                canvasDieta.polygon([(flechaDerechaX+dx,flechaDerechaY+dy) for dx,dy in flechaDerecha],0xff0000,0xff0000)
            elif actPos == 5:
                flechaIzquierdaY+=142
                flechaDerechaY+=142
                canvasDieta.polygon([(flechaIzquierdaX+dx,flechaIzquierdaY+dy) for dx,dy in flechaIzquierda],0xff0000,0xff0000)
                canvasDieta.polygon([(flechaDerechaX+dx,flechaDerechaY+dy) for dx,dy in flechaDerecha],0xff0000,0xff0000)
            elif actPos == 6:
                flechaIzquierdaY+=177
                flechaDerechaY+=177
                canvasDieta.polygon([(flechaIzquierdaX+dx,flechaIzquierdaY+dy) for dx,dy in flechaIzquierda],0xff0000,0xff0000)
                canvasDieta.polygon([(flechaDerechaX+dx,flechaDerechaY+dy) for dx,dy in flechaDerecha],0xff0000,0xff0000)
            elif actPos == 7:
                flechaIzquierdaY+=212
                flechaDerechaY+=212
                canvasDieta.polygon([(flechaIzquierdaX+dx,flechaIzquierdaY+dy) for dx,dy in flechaIzquierda],0xff0000,0xff0000)
                canvasDieta.polygon([(flechaDerechaX+dx,flechaDerechaY+dy) for dx,dy in flechaDerecha],0xff0000,0xff0000)

    for i in range(8):
        colorTexto[i]=0x000000
    colorTexto[actPos]=0xff0000    
    canvasDieta.line((20,105,330,105),0)
    canvasDieta.text((30,118),getLang(u"GLUCACTUAL"),0x000000,font=(u"legend",17,appuifw.STYLE_BOLD))    
    canvasDieta.text((225,118),u"%03d mg"%datos[0],colorTexto[0],font=(u"legend",17))
    canvasDieta.text((30,137),getLang(u"MOMENTO"),0x000000,font=(u"legend",17,appuifw.STYLE_BOLD))    
    canvasDieta.text((215,137),u"%s"%momentos[j],colorTexto[1],font=(u"legend",17))
    canvasDieta.line((20,140,330,140),0)
    canvasDieta.text((30,155),getLang(u"TIPO1"),0x000000,font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasDieta.text((210,155),u"%02d "%datos[2]+getLang(u"VASO"),colorTexto[2],font=(u"legend",17))
    canvasDieta.line((20,175,330,175),0)
    canvasDieta.text((30,190),getLang(u"TIPO2"),0x000000,font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasDieta.text((210,190),u"%02d "%datos[3]+getLang(u"PLATO"),colorTexto[3],font=(u"legend",17))
    canvasDieta.line((20,210,330,210),0)
    canvasDieta.text((30,225),getLang(u"TIPO3"),0x000000,font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasDieta.text((210,225),u"%02d "%datos[4]+getLang(u"PLATO"),colorTexto[4],font=(u"legend",17))
    canvasDieta.line((20,245,330,245),0)
    canvasDieta.text((30,260),getLang(u"TIPO4"),0x000000,font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasDieta.text((210,260),u"%02d "%datos[5]+getLang(u"PIEZA"),colorTexto[5],font=(u"legend",17))
    canvasDieta.line((20,280,330,280),0)
    canvasDieta.text((30,295),getLang(u"TIPO5"),0x000000,font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasDieta.text((210,295),u"%02d "%datos[6]+getLang(u"PLATO"),colorTexto[6],font=(u"legend",17))
    canvasDieta.line((20,315,330,315),0)
    canvasDieta.text((30,330),getLang(u"TIPO6"),0x000000,font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasDieta.text((210,330),u"%02d "%datos[7]+getLang(u"PLATO"),colorTexto[7],font=(u"legend",17))
    canvasDieta.line((20,350,330,350),0)
    canvasDieta.text((30,365),getLang(u"CALCINSU"),0x000000,font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasDieta.text((250,365),u"%02d ui"%resultado,0x0000ff,font=(u"legend",17))
    canvasDieta.text((140,85),getLang(u"DIETA"),0xbbbbbb,font=(u"symbol",27))
    canvasDieta.text((139,84),getLang(u"DIETA"),0x000000,font=(u"symbol",27))
    canvasDieta.text((240,410),getLang(u"VOLVER"),0xffffff,font=(u"legend",25,appuifw.STYLE_BOLD))
    canvasDieta.text((25,410),getLang(u"CALCULODOSIS"),0xffffff,font=(u"legend",25,appuifw.STYLE_BOLD))

def volverAtras():
    global gvAtras
    gvAtrasEnvio=[0 for x in range(len(gvAtras)-1)]
    for i in range(len(gvAtras)-1):
        gvAtrasEnvio[i]=gvAtras[i]
    gvAtras[len(gvAtras)-1](gvAtrasEnvio)

#1 racion de hidratos de carbono -> un vaso de leche o 2 yogures naturales
#2 racion de hidratos de carbono -> un pan o tazon de cereales, legumbres, patatas, pasta
#2 racion de hidratos de carbono -> 1 pieza mediana de fruta
#1 racion de hidratos de carbono -> 1 plato de verdura
#0 racion de hidratos de carbono -> carne o pescado
#para calcular la dosis de insulina, la formula es (cantidad de raciones de hc)*(ratio pertinente) +
#correcion de glucosa si superamos 180 mg, cuya formula es (glucosa actual - 100) / (factor sensibilidad)
#mis datos, total = 36 mañana = 4 mediodia = 3 cena = 2
    
def calculo_dosis(glucos,raciones,rat):
    totalInsulina = int(base_de_datos.obtener_totalinsu_actual())
    res = 0
    lact = int(base_de_datos.obtener_lacteos())
    farin = int(base_de_datos.obtener_farinaceos())
    legumb = int(base_de_datos.obtener_legumbres())
    fruta = int(base_de_datos.obtener_frutas())
    verdura = int(base_de_datos.obtener_verduras())
    protein = int(base_de_datos.obtener_proteinicos())
    res += lact*raciones[0]
    res += farin*raciones[1]
    res += legumb*raciones[2]
    res += fruta*raciones[3]
    res += verdura*raciones[4]
    res += protein*raciones[5]
    # formula de hidratos de carbono por ratio actual
    res = res * rat
    # sirve para redondear la cantidad de insulina
    if res - int(res) >= 0.5:
        res += 1
    # si supera los 180, aplicamos la formula del bolo corrector
    if glucos >= 180:
        factorSensibilidad = int(1800//totalInsulina)
        boloCorrector = (glucos - 100)//factorSensibilidad
        res += boloCorrector
    # si estamos entre 100 y 70, restamos una unidad a la dosis de insulina para evitar hipoglucemias
    elif glucos < 100 and glucos >= 70:
        res -= 1
    # si estamos por debajo de 70, informar de hipoglucemia 
    elif glucos < 70:
        res = 0        
    return res    
    
def press_select():
    global actMod
    global movimientos
    global actPos
    global datos
    global contadorraciones
    global rati
    global gluc
    if actMod==True:
        if movimientos[actPos][2] == u"glucosaactual":
            gluc = datos[actPos]
        elif movimientos[actPos][2] == u"momentos":
            if j == 0:
                rati = base_de_datos.obtener_ratiodesayuno_actual()
            elif j == 1:
                rati = base_de_datos.obtener_ratioalmuerzo_actual()
            else:
                rati = base_de_datos.obtener_ratiocena_actual()
        elif movimientos[actPos][2] == u"lacteos":
            contadorraciones[0] = datos[actPos]
        elif movimientos[actPos][2] == u"farinaceos":
            contadorraciones[1] = datos[actPos]
        elif movimientos[actPos][2] == u"legumbrespatatas":
            contadorraciones[2] = datos[actPos]
        elif movimientos[actPos][2] == u"frutas":
            contadorraciones[3] = datos[actPos]
        elif movimientos[actPos][2] == u"verduras":
            contadorraciones[4] = datos[actPos]
        elif movimientos[actPos][2] == u"proteinicos":
            contadorraciones[5] = datos[actPos]
        actMod=False
    else:        
        actMod=True
    appuifw.app.body = canvasDieta
    
def moverCursor(despmomento,desp,despracion,pos):
    global actPos
    global movimientos
    global datos
    global j
    if actMod==True:
        # si estamos en glucosa actual
        if movimientos[actPos][2] == u"glucosaactual":
            datos[actPos]+=desp
        # si estamos en momentos
        elif movimientos[actPos][2] == u"momentos":
            if despmomento>0:
                if j>2:
                    j=2
                else:
                    j+=despmomento
                    if j>2:
                        j=2
            elif despmomento<0:
                if j<0:
                    j=0
                else:
                    j+=despmomento
                    if j<0:
                        j=0
        # si estamos en alguna opcion de raciones
        else:
            datos[actPos]+=despracion
        # control de limites superiores depende del caso    
        if desp>0:
            if datos[actPos]>movimientos[actPos][3]:
                datos[actPos]=movimientos[actPos][3] 
        else:
            # control de limites inferiores depende del caso
            if actPos == 0:
                if datos[actPos]<movimientos[actPos][4]:
                    datos[actPos]=movimientos[actPos][4]               
            elif datos[actPos]<0:
                datos[actPos]=0
    else:        
        actPos+=movimientos[actPos][1][pos]
    appuifw.app.body = canvasDieta
    
def press_up():
    moverCursor(0,50,5,0)

def press_right():
    moverCursor(1,1,1,1)

def press_down():
    moverCursor(0,-50,-5,2)

def press_left():
    moverCursor(-1,-1,-1,3)
    
def teclaPresionada(key):
    global contadorraciones
    global rati
    global gluc
    global resultado
    if key['type']==3:
        if key['scancode']==164:
            resultado = calculo_dosis(gluc,contadorraciones,rati)
            appuifw.app.body = canvasDieta

def mostrarDieta(vAtras):
    global movimientos
    movimientos=[
        [0,[0,0,1,0],u"glucosaactual",600,30],
        [1,[-1,0,1,0],u"momentos",0],
        [2,[-1,0,1,0],u"lacteos",10],
        [3,[-1,0,1,0],u"farinaceos",10],
        [4,[-1,0,1,0],u"legumbrespatatas",10],
        [5,[-1,0,1,0],u"frutas",10],
        [6,[-1,0,1,0],u"verduras",10],
        [7,[-1,0,0,0],u"proteinicos",10]
        ]       
    global datos
    datos=[0 for x in range(8)]
    datos[0] = 100
    global contadorraciones
    contadorraciones =[0 for x in range(6)]
    global actPos
    actPos=0
    global actMod
    actMod=False
    global resultado
    resultado = 0
    global momentos
    momentos = [getLang(u"DESAYUNO"),getLang(u"ALMUERZO"),getLang(u"CENA")]
    global j
    j = 0
    global rati
    rati = base_de_datos.obtener_ratiodesayuno_actual()
    # por defecto 100 mg de glucosa por ser la medida optima
    global gluc
    gluc = 100
    ruta = unidad+':\\python\\resources\\ui\\'
    global imDieta
    imDieta = graphics.Image.open(ruta+'fondo11.png')
    global canvasDieta
    canvasDieta = appuifw.Canvas(redraw_callback = handle_redraw, event_callback=teclaPresionada)
    canvasDieta.blit(imDieta)
    appuifw.app.body = canvasDieta
    appuifw.app.screen = 'full'
    appuifw.app.title = u"Dieta"
    canvasDieta.bind(key_codes.EKeySelect, press_select)
    canvasDieta.bind(key_codes.EKeyUpArrow, press_up)
    canvasDieta.bind(key_codes.EKeyRightArrow, press_right)
    canvasDieta.bind(key_codes.EKeyDownArrow, press_down)
    canvasDieta.bind(key_codes.EKeyLeftArrow, press_left)
    global gvAtras
    gvAtras=vAtras
    if len(vAtras)==1:
        appuifw.app.exit_key_handler=gvAtras[0]
    else:
        appuifw.app.exit_key_handler=volverAtras