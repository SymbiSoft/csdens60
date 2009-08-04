import e32, appuifw

# Archivo: est.py
# Autor: Jorge Aguirre Andreu
# Descripción: Realiza promedios a petición de análisis de glucosa que estén almacenados en el diario.
# Promedios de después de todas las comidas, a intervalos de tiempo que quiera.
# También es capaz de avisar con antelación de cuando se puede quedar sin tiras reactivas(usadas para los análisis).
# Aspecto configurable por el usuario.
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

def mostrarEst():
    appuifw.note(u"Estadisticas", "info")