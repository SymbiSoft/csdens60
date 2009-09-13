# Archivo: base_de_datos.py
# Autor: Jorge Aguirre Andreu
# Descripci�n: Se encarga de la creaci�n de la base de datos entera si no existe y del manejo mediante m�todos de
# las consultas a la base de datos.
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

import e32db,sys,time

try:
    raise Exception
except Exception:
    path = sys.exc_info()[2].tb_frame.f_code.co_filename
if not path:
    path = os.path.join(os.getcwd(), 'default.py')
unidad=path[0]

modulospropios = unidad+':\\Python\\modules'
sys.path.append(modulospropios)
from configuracion import *

db = e32db.Dbms()
dbv = e32db.Db_view()
try:
    db.open(u'%s:\\Python\\resources\\db\\%s'%(unidad,database))
except:
    db.create(u'%s:\\Python\\resources\\db\\%s'%(unidad,database))
    db.open(u'%s:\\Python\\resources\\db\\%s'%(unidad,database))
    db.execute(u"create table diario (fecha date,tipo varchar,valor bigint)")
    db.execute(u"create table extra (fecha date,tipo varchar,valor varchar)")

def obtener_diario_dia(dia,mes,ano,tipo):
    fechaValues=[ano,mes,dia,0,0,0,0,0,1]
    fecha=time.mktime(time.struct_time(fechaValues))
    dbv.prepare(db,u"select * from diario where fecha=#%s# and tipo='%s'"%(e32db.format_time(fecha),tipo))
    if dbv.count_line()!=0:
        dbv.get_line()
        return dbv.col(3)
    return 0

def actualizar_diario_dia(dia,mes,ano,tipo,valor):
    fechaValues=[ano,mes,dia,0,0,0,0,0,1]
    fecha=time.mktime(time.struct_time(fechaValues))
    dbv.prepare(db,u"select * from diario where fecha=#%s# and tipo='%s'"%(e32db.format_time(fecha),tipo))
    if dbv.count_line()!=0:
        db.execute(u"update diario set valor=%d where fecha=#%s# and tipo='%s'"%(valor,e32db.format_time(fecha),tipo))
    else:
        db.execute(u"insert into diario (fecha,tipo,valor) values(#%s#,'%s',%d)"%(e32db.format_time(fecha),tipo,valor))

def obtener_extra_diario(dia,mes,ano,tipo):
    fechaValues=[ano,mes,dia,0,0,0,0,0,1]
    fecha=time.mktime(time.struct_time(fechaValues))
    dbv.prepare(db,u"select * from extra where fecha=#%s# and tipo='%s'"%(e32db.format_time(fecha),tipo))
    if dbv.count_line()!=0:
        dbv.get_line()
        return dbv.col(3)
    return 0
    
def actualizar_extra_diario(dia,mes,ano,tipo,valor):
    fechaValues=[ano,mes,dia,0,0,0,0,0,1]
    fecha=time.mktime(time.struct_time(fechaValues))
    dbv.prepare(db,u"select * from extra where fecha=#%s# and tipo='%s'"%(e32db.format_time(fecha),tipo))
    if dbv.count_line()!=0:
        db.execute(u"update extra set valor='%s' where fecha=#%s# and tipo='%s'"%(valor,e32db.format_time(fecha),tipo))
    else:
        db.execute(u"insert into extra (fecha,tipo,valor) values(#%s#,'%s','%s')"%(e32db.format_time(fecha),tipo,valor))