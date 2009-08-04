import e32, appuifw

# Archivo: config.py
# Autor: Jorge Aguirre Andreu
# Descripción: Lleva todo lo relacionado con el perfil del usuario, como su peso, la activación de servicios de aviso
# para citas médicas o cantidad de tiras reactivas.
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

def mostrarConfig():
    appuifw.note(u"Configuración", "info")