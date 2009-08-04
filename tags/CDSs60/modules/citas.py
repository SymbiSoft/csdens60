import e32, appuifw

# Archivo: citas.py
# Autor: Jorge Aguirre Andreu
# Descripción: Lleva el control de todas las citas con los distintos médicos del diabético, desde 
# endocrino, podólogo, oculista, análisis de sangre y cualquier otro. 
# También tiene la opción de activar una alarma dias antes para no olvidar dichas citas. 
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

def mostrarCitas():
    appuifw.note(u"Citas", "info")