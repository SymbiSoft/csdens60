# Archivo: idioma.py
# Autor: Jorge Aguirre Andreu
# Descripción: Cambia dinamicamente el idioma de la aplicacion, usa las 2 ultimas letras del archivo de idioma.
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

import sys, e32, appuifw, string, os

try:
    raise Exception
except Exception:
    path = sys.exc_info()[2].tb_frame.f_code.co_filename
if not path:
    path = os.path.join(os.getcwd(), 'default.py')
unidad=path[0]

modulospropios = unidad+':\\Python\\modules\\idiomas'
sys.path.append(modulospropios)
from configuracion import *

idioma=cfgIdioma
print u"el idioma es %s"%(idioma)

def fijarIdioma(id):
    global idioma
    idioma=id

def getLang(palabra):
    global idioma
    exec("from csds60_"+idioma+" import csds60")
    return csds60[palabra]