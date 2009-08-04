import e32, appuifw

# Archivo: dieta.py
# Autor: Jorge Aguirre Andreu
# Descripci�n: Consulta a a trav�s de un servicio web dietas que te vengan bien, dependiendo de tu peso y tu situaci�n actual.
# Tambi�n puedes calcular la cantidad aproximada de dosis de insulina que necesitas seg�n que alimentos tomes.
# ADVERTENCIA: El c�lculo es una mera aproximaci�n, debe seguir las indicaciones de su endocrino.
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

def mostrarDieta():
    appuifw.note(u"Dieta", "info")