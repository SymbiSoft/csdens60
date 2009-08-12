# Archivo: principal.py
# Autor: Jorge Aguirre Andreu
# Descripción: Proyecto de fin de carrera, es un sistema de gestión de todos los aspectos
# del control de la diabetes para la plataforma s60, en concreto resolución de 352x416.
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

import e32, appuifw, key_codes, graphics, sys

modulospropios = 'c:\\Python\\modules'
sys.path.append(modulospropios)

import dieta, est, citas, config, export, diario
from idioma import getLang,fijarIdioma

#cambiar la unidad de c a e para el movil

fijarIdioma(u"en")

ruta = 'c:\\python\\resources\\ui\\'
im = [ graphics.Image.open(ruta+'menuprincipal0.png'), graphics.Image.open(ruta+'menuprincipal1.png'), 
graphics.Image.open(ruta+'menuprincipal2.png'), graphics.Image.open(ruta+'menuprincipal3.png'), 
graphics.Image.open(ruta+'menuprincipal4.png'), graphics.Image.open(ruta+'menuprincipal5.png') ]
tx = [u"       Diario",u"       Dieta",u"Configuración",u"    Exportar",u"Citas médicas",u"  Estadísticas"]
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
    appuifw.app.exit_key_handler = mostrarPrincipal
    diario.mostrarDiario()

def press_dieta():
    dieta.mostrarDieta()

def press_configuracion():
    config.mostrarConfig()

def press_exportar():
    export.mostrarExport()

def press_citas():
    citas.mostrarCitas()

def press_estadisticas():
    est.mostrarEst()

def handle_redraw(rect):
    global photo
    canvas.blit(im[photo])
    canvas.text((250,410),getLang(u"SALIR"),0xffffff,font=(u"legend",25,appuifw.STYLE_BOLD))
    canvas.text((80,245),tx[photo],0xaaaaaa,font="title")
    canvas.text((78,243),tx[photo],0x000000,font="title")

def confirma():
    #TODO: ESTO HAY QUE QUITARLO!
    app_lock.signal()
    #TODO: ESTO HA Y QUE QUITARLO!
    return
    opcion = [getLang(u"SÍ"),getLang(u"NO")]
    test = appuifw.popup_menu(opcion,getLang(u"¿ESTÁ SEGURO?"))
    if test == 0 :
	    appuifw.note(getLang(u"HASTA LUEGO"), "conf")
	    app_lock.signal()

def mostrarPrincipal():
    global canvas
    canvas=appuifw.Canvas(redraw_callback=handle_redraw)
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