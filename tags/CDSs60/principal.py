import e32, appuifw, key_codes, graphics, sys

modulospropios = 'c:\\Python\\modules'
sys.path.append(modulospropios)

import diario, dieta, est, citas, config, export

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


#cambiar la unidad de c a e para el movil

ruta = 'c:\\python\\resources\\ui\\'
im = [ graphics.Image.open(ruta+'menuprincipal0.png'), graphics.Image.open(ruta+'menuprincipal1.png'), 
graphics.Image.open(ruta+'menuprincipal2.png'), graphics.Image.open(ruta+'menuprincipal3.png'), 
graphics.Image.open(ruta+'menuprincipal4.png'), graphics.Image.open(ruta+'menuprincipal5.png') ]
photo = 0
    
def press_right():
    #giro a la derecha del menu
    global photo
    if photo == 5:
        photo = 0
    else:
        photo = photo + 1
    canvas.blit(im[photo])
    
def press_left():
    #giro a la izquierda del menu
    global photo
    if photo == 0:
        photo = 5
    else:
        photo = photo - 1
    canvas.blit(im[photo])
    
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
    
def confirma():
    opcion = [u"Si", u"No"]
    test = appuifw.popup_menu(opcion, u"¿Está seguro?")

    if test == 0 :
	    appuifw.note(u"Hasta luego", "conf")
	    app_lock.signal()
        

canvas=appuifw.Canvas(redraw_callback=handle_redraw)
appuifw.app.body=canvas
#acceso con el teclado directamente
canvas.bind(key_codes.EKeySelect, press_select)
canvas.bind(key_codes.EKeyRightArrow, press_right)
canvas.bind(key_codes.EKeyLeftArrow, press_left)
canvas.bind(key_codes.EKey2, press_diario)
canvas.bind(key_codes.EKey6, press_dieta)
canvas.bind(key_codes.EKey9, press_configuracion)
canvas.bind(key_codes.EKey0, press_exportar)
canvas.bind(key_codes.EKey7, press_citas)
canvas.bind(key_codes.EKey4, press_estadisticas)

canvas.blit(im[photo])

appuifw.app.exit_key_handler = confirma
appuifw.app.screen = 'full'
appuifw.app.title = u"CSDs60"
app_lock = e32.Ao_lock()
app_lock.wait()