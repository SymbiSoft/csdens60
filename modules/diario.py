import e32, appuifw

# Archivo: diario.py
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

def mostrarDiario():
    appuifw.note(u"Diario", "info")