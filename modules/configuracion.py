# Archivo: configuracion.py
# Autor: Jorge Aguirre Andreu
# Descripción: Encargado de recoger todos los parametros de configuracion de la aplicacion. 
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
from time import localtime
actMes = localtime()[1]
actAno = localtime()[0]

#tiene que estar en esta linea, sino falla por los parametros de arriba
from base_de_datos import obtener_idioma_act_conf
from base_de_datos import obtener_db_actual
#carga la bd seleccionada
database = obtener_db_actual()
#idioma seleccionado, es especial por recuperar la constante del idioma, no el idioma en si
cfgIdioma = obtener_idioma_act_conf()

    


