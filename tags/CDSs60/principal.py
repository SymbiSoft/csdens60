# Archivo: principal.py
# Autor: Jorge Aguirre Andreu
# Descripción: Proyecto de fin de carrera, es un sistema de gestión de todos los aspectos
# del control de la diabetes para la plataforma s60, en concreto resolución de 352x416.
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


# ------------------------------------------
# INICIO: IMPORTAR
# ------------------------------------------

import e32, appuifw, key_codes, graphics, sys, os

try:
    raise Exception
except Exception:
    path = sys.exc_info()[2].tb_frame.f_code.co_filename
if not path:
    path = os.path.join(os.getcwd(), 'default.py')
unidad=path[0]

modulospropios = unidad+':\\Python\\modules'
sys.path.append(modulospropios)

import dieta, citas, config, export, diario, licencia
from idioma import getLang
from configuracion import *
from base_de_datos import cerrar_bds
from base_de_datos import obtener_db_actual
from base_de_datos import comprobar_db

# ------------------------------------------
# FIN: IMPORTAR
# ------------------------------------------


ruta = unidad+':\\python\\resources\\ui\\'

im=[
    graphics.Image.open(ruta+'menuprincipalDiario.png'),
    graphics.Image.open(ruta+'menuprincipalComidas.png'), 
    graphics.Image.open(ruta+'menuprincipalConfiguracion.png'),
    graphics.Image.open(ruta+'menuprincipalExportar.png'), 
    graphics.Image.open(ruta+'menuprincipalCitas.png')
    ]

tx=[
    getLang(u"MENUDIARIO"),
    getLang(u"MENUDIETA"),
    getLang(u"MENUCONFIGURACIÓN"),
    getLang(u"MENUEXPORTAR"),
    getLang(u"MENUCITASMÉDICAS")
    ]
    
photo = 0

def press_up():
    global photo
    photo = 0
    appuifw.app.body=canvas
    press_diario()
    canvas.blit(im[photo])

def press_down():
    global photo
    photo = 3
    appuifw.app.body=canvas
    press_exportar()
    canvas.blit(im[photo])
    
def press_right():
    global photo
    photo = 1
    appuifw.app.body=canvas
    press_dieta()
    canvas.blit(im[photo])
    
def press_left():
    global photo
    photo = 4
    appuifw.app.body=canvas
    press_citas()
    canvas.blit(im[photo])    
    
def press_select():
    global photo
    photo = 2
    appuifw.app.body=canvas
    press_configuracion()
    canvas.blit(im[photo])

def press_diario():
    global soloLectura
    if soloLectura == False:
        diario.mostrarDiario([mostrarPrincipal])
    else:
        appuifw.note(u"Con la base de datos actual solo puedes exportar","info")

def press_dieta():
    dieta.mostrarDieta([mostrarPrincipal])

def press_configuracion():
    config.mostrarConfig([mostrarPrincipal])

def press_exportar():
    export.mostrarExport([mostrarPrincipal])

def press_citas():
    citas.mostrarCitas([mostrarPrincipal])

# "How to use Canvas"<http://wiki.forum.nokia.com/index.php/How_to_use_Canvas>(5 Agosto 2009)
def handle_redraw(rect):
    global photo
    canvas.blit(im[photo])
    canvas.text((250,410),getLang(u"SALIR"),0xffffff,font=(u"legend",25,appuifw.STYLE_BOLD))
    canvas.text((80,245),tx[photo],0xaaaaaa,font="title")
    canvas.text((78,243),tx[photo],0x000000,font="title")

def confirma():
    opcion = [getLang(u"SÍ"),getLang(u"NO")]
    test = appuifw.popup_menu(opcion,getLang(u"¿ESTÁ SEGURO?"))
    if test == 0 :
        try:
            cerrar_bds()
            appuifw.note(getLang(u"HASTA LUEGO"), "conf")
            app_lock.signal()
        except:
            appuifw.note(getLang(u"HASTA LUEGO"), "conf")
            app_lock.signal()

# "How to detect key presses in Python"<http://wiki.forum.nokia.com/index.php/How_to_detect_key_presses_in_Python>(14 Septiembre 2009)        
def teclaPresionada(key):
    if key['type']==3:
        if key['scancode']==164:
            verLicencia()
            
def verLicencia():
    licencia.mostrar_licencia([mostrarPrincipal])        

def mostrarPrincipal():
    try:
        comprobar_db()
    except:
        print u"Cargando"
    global soloLectura
    soloLectura = False
    try:
        dbAct = obtener_db_actual()
        if dbAct != u"csds60_"+str(actMes)+"_"+str(actAno)+".db":
            soloLectura = True
        else:
            soloLectura = False
    # "How to use keys in PyS60"<http://wiki.forum.nokia.com/index.php/How_to_use_Keys_in_PyS60>(4 Agosto 2009)
    except:
        soloLectura = False
    global canvas
    canvas=appuifw.Canvas(redraw_callback=handle_redraw, event_callback=teclaPresionada)    
    appuifw.app.body=canvas
    canvas.bind(key_codes.EKeySelect, press_select)
    canvas.bind(key_codes.EKeyRightArrow, press_right)
    canvas.bind(key_codes.EKeyLeftArrow, press_left)
    canvas.bind(key_codes.EKeyUpArrow, press_up)
    canvas.bind(key_codes.EKeyDownArrow, press_down)
    canvas.bind(key_codes.EKey2, press_up)
    canvas.bind(key_codes.EKey6, press_right)
    canvas.bind(key_codes.EKey5, press_select)
    canvas.bind(key_codes.EKey4, press_left)
    canvas.bind(key_codes.EKey8, press_down)
    #canvas.bind(key_codes.EKey4, press_estadisticas)
    appuifw.app.exit_key_handler = confirma
    appuifw.app.screen = 'full'
    appuifw.app.title = u"CSDs60"

mostrarPrincipal()
app_lock = e32.Ao_lock()
app_lock.wait()