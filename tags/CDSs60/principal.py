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

import dieta, est, citas, config, export, diario, licencia
from idioma import getLang
from configuracion import *
from base_de_datos import cerrar_bds

# ------------------------------------------
# FIN: IMPORTAR
# ------------------------------------------


ruta = unidad+':\\python\\resources\\ui\\'

im=[
    graphics.Image.open(ruta+'menuprincipal0.png'),
    graphics.Image.open(ruta+'menuprincipal1.png'), 
    graphics.Image.open(ruta+'menuprincipal2.png'),
    graphics.Image.open(ruta+'menuprincipal3.png'), 
    graphics.Image.open(ruta+'menuprincipal4.png'),
    graphics.Image.open(ruta+'menuprincipal5.png')
    ]
    
tx=[
    getLang(u"MENUDIARIO"),
    getLang(u"MENUDIETA"),
    getLang(u"MENUCONFIGURACIÓN"),
    getLang(u"MENUEXPORTAR"),
    getLang(u"MENUCITASMÉDICAS"),
    getLang(u"MENUESTADÍSTICAS")
    ]
    
photo = 0
    
def press_right():
    #giro a la derecha del menu
    global photo
    if photo == 5:
        photo = 0
    else:
        photo = photo + 1
    appuifw.app.body=canvas
    
def press_left():
    #giro a la izquierda del menu
    global photo
    if photo == 0:
        photo = 5
    else:
        photo = photo - 1
    appuifw.app.body=canvas
    
def press_select():
	#en python no existe la sentencia switch, para seleccionar opciones
    global photo
    if photo == 0:
        press_diario()
    elif photo == 1:
        press_dieta()
    elif photo == 2:
        press_configuracion()
    elif photo == 3:
        press_exportar()
    elif photo == 4:
        press_citas()
    elif photo == 5:
        press_estadisticas()
    canvas.blit(im[photo])

def press_diario():
    diario.mostrarDiario([mostrarPrincipal])

def press_dieta():
    dieta.mostrarDieta([mostrarPrincipal])

def press_configuracion():
    config.mostrarConfig([mostrarPrincipal])

def press_exportar():
    export.mostrarExport([mostrarPrincipal])

def press_citas():
    citas.mostrarCitas([mostrarPrincipal])

def press_estadisticas():
    est.mostrarEst([mostrarPrincipal])

def handle_redraw(rect):
    global photo
    canvas.blit(im[photo])
    canvas.text((250,410),getLang(u"SALIR"),0xffffff,font=(u"legend",25,appuifw.STYLE_BOLD))
    canvas.text((80,245),tx[photo],0xaaaaaa,font="title")
    canvas.text((78,243),tx[photo],0x000000,font="title")

def confirma():
    #TODO: ESTO HAY QUE QUITARLO!
    #cerrar_bds()
    app_lock.signal()
    #TODO: ESTO HAY QUE QUITARLO!
    return
    opcion = [getLang(u"SÍ"),getLang(u"NO")]
    test = appuifw.popup_menu(opcion,getLang(u"¿ESTÁ SEGURO?"))
    if test == 0 :
        cerrar_bds()
        appuifw.note(getLang(u"HASTA LUEGO"), "conf")
        app_lock.signal()
        
def teclaPresionada(key):
    if key['type']==3:
        if key['scancode']==164:
            verLicencia()
            
def verLicencia():
    licencia.mostrar_licencia([mostrarPrincipal])

def mostrarPrincipal():
    global canvas
    canvas=appuifw.Canvas(redraw_callback=handle_redraw, event_callback=teclaPresionada)
    appuifw.app.body=canvas
    canvas.bind(key_codes.EKeySelect, press_select)
    canvas.bind(key_codes.EKeyRightArrow, press_right)
    canvas.bind(key_codes.EKeyLeftArrow, press_left)
    canvas.bind(key_codes.EKey2, press_diario)
    canvas.bind(key_codes.EKey6, press_dieta)
    canvas.bind(key_codes.EKey9, press_configuracion)
    canvas.bind(key_codes.EKey0, press_exportar)
    canvas.bind(key_codes.EKey7, press_citas)
    canvas.bind(key_codes.EKey4, press_estadisticas)
    appuifw.app.exit_key_handler = confirma
    appuifw.app.screen = 'full'
    appuifw.app.title = u"CSDs60"

mostrarPrincipal()
app_lock = e32.Ao_lock()
app_lock.wait()