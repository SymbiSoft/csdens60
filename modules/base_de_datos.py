# Archivo: base_de_datos.py
# Autor: Jorge Aguirre Andreu
# Descripción: Se encarga de la creación de la base de datos entera si no existe y del manejo mediante métodos de
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
from random import randrange
from time import localtime

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
dbconf = e32db.Dbms()
dbvconf = e32db.Db_view()
idiomas = [u'es',
           u'en',
           u'it',
           u'ca',
           u'de',
           u'eu',
           u'fr',
           u'gl',
           u'jp',
           u'pt',
           u'ru',
           u'zh'
           ]
idionombre = [u'Español',
              u'Inglés',
              u'Italiano',
              u'Catalán',
              u'Alemán',
              u'Euskera',
              u'Francés',
              u'Gallego',
              u'Japonés',
              u'Portugués',
              u'Ruso',
              u'Chino'
              ]
# tenemos una bd independiente llamada conf.cfg para almacenar parametros invariables
# que solo se van a modificar muy pocas veces
try:
    dbconf.open(u'%s:\\Python\\resources\\config\\conf.cfg'%(unidad))
except:
    dbconf.create(u'%s:\\Python\\resources\\config\\conf.cfg'%(unidad))
    dbconf.open(u'%s:\\Python\\resources\\config\\conf.cfg'%(unidad))
    # tabla dbproperties para almacenar el idioma(por defecto español) y la bd actual(la primera que genera)
    dbconf.execute(u"create table dbproperties (nombre varchar,valor varchar)")
    dbconf.execute(u"insert into dbproperties(nombre,valor) values('idioma','es')")
    dbconf.execute(u"insert into dbproperties(nombre,valor) values('db','%s')"%(database))
    # guarda los idiomas disponibles para cargar
    dbconf.execute(u"create table idiomas (id integer,const varchar,nombre varchar)")
    for i in range(12):
        dbconf.execute(u"insert into idiomas(id,const,nombre) values(%d,'%s','%s')"%(i,idiomas[i],idionombre[i]))
    # guarda un registro con todas las bds que hemos creado
    dbconf.execute(u"create table dbs (id integer,nombre varchar)")
    dbconf.execute(u"insert into dbs(id,nombre) values(1,'%s')"%(database))
    
try:
    db.open(u'%s:\\Python\\resources\\db\\%s'%(unidad,database))
except:
    db.create(u'%s:\\Python\\resources\\db\\%s'%(unidad,database))
    db.open(u'%s:\\Python\\resources\\db\\%s'%(unidad,database))
    db.execute(u"create table diario (fecha date,tipo varchar,valor bigint)")
    db.execute(u"create table extra (fecha date,tipo varchar,valor varchar)")
    db.execute(u"create table insulinas (tipo varchar,orden integer)")
    db.execute(u"create table ordendiario (tipo varchar,orden integer)")
    db.execute(u"insert into ordendiario(tipo,orden) values('desa',1)")
    db.execute(u"insert into ordendiario(tipo,orden) values('almu',2)")
    db.execute(u"insert into ordendiario(tipo,orden) values('cena',3)")
    db.execute(u"create table registroscitas (fecha date,descripcion varchar)")
    db.execute(u"create table tiposalimentos (tipo varchar, racion integer)")
    db.execute(u"insert into tiposalimentos(tipo,racion) values('vaso de leche o 2 yogures naturales',1)")
    db.execute(u"insert into tiposalimentos(tipo,racion) values('un pan o tazon de cereales o pasta',2)")
    db.execute(u"insert into tiposalimentos(tipo,racion) values('tazon de legumbres o patatas',2)")    
    db.execute(u"insert into tiposalimentos(tipo,racion) values('1 pieza mediana de fruta',2)")
    db.execute(u"insert into tiposalimentos(tipo,racion) values('1 plato de verdura',1)")
    db.execute(u"insert into tiposalimentos(tipo,racion) values('carne o pescado',0)")
    
    #Datos de ejemplo (se insertaran en la base de datos si la siguiente condicion se evalua como verdadera, y no si es falsa):
    if True:
        #fechaValues=[2009,9,18,0,0,0,0,0,1] #dia,mes,año de insersion de los datos
        #fecha=time.mktime(time.struct_time(fechaValues))
        #-1 es que esta introducida en la bd pero no se usa
        db.execute(u"insert into insulinas (tipo,orden) values('%s',%d)"%('Rapida',0))
        db.execute(u"insert into insulinas (tipo,orden) values('%s',%d)"%('Lantus',1))
        #for i in range(1253916000,1297116000,86400):
         #   rDesayunoAntes=randrange(70,240)
         #   rDesayunoDespues=randrange(rDesayunoAntes-20,rDesayunoAntes+20)
         #   rDesayunoRapida=randrange(2,7)
         #   rDesayunoLantus=24
         #   rAlmuerzoAntes=randrange(70,240)
         #   rAlmuerzoDespues=randrange(rDesayunoAntes-20,rDesayunoAntes+20)
         #   rAlmuerzoRapida=randrange(2,7)
         #   rCenaAntes=randrange(70,240)
         #   rCenaDespues=randrange(rDesayunoAntes-20,rDesayunoAntes+20)
         #   rCenaRapida=randrange(2,7)
         #   rCenaLantus=7
         #   db.execute(u"insert into diario (fecha,tipo,valor) values(#%s#,'%s',%d)"%(e32db.format_time(i),'desayunoantes',rDesayunoAntes))
         #   db.execute(u"insert into diario (fecha,tipo,valor) values(#%s#,'%s',%d)"%(e32db.format_time(i),'desayunodespues',rDesayunoDespues))
         #   db.execute(u"insert into diario (fecha,tipo,valor) values(#%s#,'%s',%d)"%(e32db.format_time(i),'desayunoRapidaantes',rDesayunoRapida))
         #   db.execute(u"insert into diario (fecha,tipo,valor) values(#%s#,'%s',%d)"%(e32db.format_time(i),'desayunoLantusantes',rDesayunoLantus))
         #   db.execute(u"insert into diario (fecha,tipo,valor) values(#%s#,'%s',%d)"%(e32db.format_time(i),'almuerzoantes',rAlmuerzoAntes))
         #   db.execute(u"insert into diario (fecha,tipo,valor) values(#%s#,'%s',%d)"%(e32db.format_time(i),'almuerzodespues',rAlmuerzoDespues))
         #   db.execute(u"insert into diario (fecha,tipo,valor) values(#%s#,'%s',%d)"%(e32db.format_time(i),'almuerzoRapidaantes',rAlmuerzoRapida))
         #   db.execute(u"insert into diario (fecha,tipo,valor) values(#%s#,'%s',%d)"%(e32db.format_time(i),'cenaantes',rCenaAntes))
         #   db.execute(u"insert into diario (fecha,tipo,valor) values(#%s#,'%s',%d)"%(e32db.format_time(i),'cenadespues',rCenaDespues))
         #   db.execute(u"insert into diario (fecha,tipo,valor) values(#%s#,'%s',%d)"%(e32db.format_time(i),'cenaRapidaantes',rCenaRapida))
         #   db.execute(u"insert into diario (fecha,tipo,valor) values(#%s#,'%s',%d)"%(e32db.format_time(i),'cenaLantusantes',rCenaLantus))

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

def obtener_insulina(posicion):
    dbv.prepare(db,u"select * from insulinas where orden=%d"%(posicion));
    if dbv.count_line()!=0:
        dbv.get_line()
        return dbv.col(1)
    return None

def obtener_numero_insulinas():
    dbv.prepare(db,u"select * from insulinas where orden>=0")
    return dbv.count_line()-1

def obtener_datos_diario():
    dbv.prepare(db,u"select * from diario order by fecha,tipo")
    return dbv
    
def actualizar_registros_citas(dia,mes,ano,descripcion):
    fechaValues=[ano,mes,dia,0,0,0,0,0,1]
    fecha=time.mktime(time.struct_time(fechaValues))
    dbv.prepare(db,u"select * from registroscitas where fecha=#%s#"%(e32db.format_time(fecha)))
    if dbv.count_line()!=0:
        db.execute(u"update registroscitas set descripcion='%s' where fecha=#%s#"%(descripcion,e32db.format_time(fecha)))
    else:
        db.execute(u"insert into registroscitas (fecha,descripcion) values(#%s#,'%s')"%(e32db.format_time(fecha),descripcion))
    
def obtener_registros_citas(dia,mes,ano):
    fechaValues=[ano,mes,dia,0,0,0,0,0,1]
    fecha=time.mktime(time.struct_time(fechaValues))
    dbv.prepare(db,u"select * from registroscitas where fecha=#%s#"%(e32db.format_time(fecha)))
    if dbv.count_line()!=0:
        dbv.get_line()
        return dbv.col(2)
    return None
    
def borrar_registros_citas(dia,mes,ano):
    fechaValues=[ano,mes,dia,0,0,0,0,0,1]
    fecha=time.mktime(time.struct_time(fechaValues))
    dbv.prepare(db,u"select * from registroscitas where fecha=#%s#"%(e32db.format_time(fecha)))
    if dbv.count_line()!=0:
        db.execute(u"delete from registroscitas where fecha=#%s#"%(e32db.format_time(fecha)))
        
def obtener_idiomas(posicion):
    dbvconf.prepare(dbconf,u"select * from idiomas where id = %d"%(posicion))
    if dbvconf.count_line()!=0:
        dbvconf.get_line()
        idArray = [dbvconf.col(2),dbvconf.col(3)]
        return idArray
    return None
    
def obtener_numero_idiomas():
    dbvconf.prepare(dbconf,u"select * from idiomas")
    return dbvconf.count_line()-1
    
def obtener_dbs():
    dbvconf.prepare(dbconf,u"select * from dbs")
    return dbvconf
    
def obtener_numero_dbs():
    dbvconf.prepare(dbconf,u"select * from dbs")
    return dbvconf.count_line()-1
    
def actualizar_idioma(idiom):
    dbconf.execute(u"update dbproperties set valor='%s' where nombre='idioma'"%(idiom))
    
def obtener_idioma_actual():
    dbvconf.prepare(dbconf,u"select * from dbproperties where nombre='idioma'")
    if dbvconf.count_line()!=0:
        dbvconf.get_line()
        temp = dbvconf.col(2)
        dbvconf.prepare(dbconf,u"select * from idiomas where const='%s'"%(temp))
        if dbvconf.count_line()!=0:
            dbvconf.get_line()            
            return dbvconf.col(3)
    return None
    
def obtener_idioma_act_conf():
    dbvconf.prepare(dbconf,u"select valor from dbproperties where nombre='idioma'")
    if dbvconf.count_line()!=0:
        dbvconf.get_line()
        return dbvconf.col(1)
    return None
    
def actualizar_db(datab):
    dbconf.execute(u"update dbproperties set valor='%s' where nombre='db'"%(datab))
    
def obtener_db_actual():
    dbvconf.prepare(dbconf,u"select * from dbproperties where nombre='db'")
    if dbvconf.count_line()!=0:
        dbvconf.get_line()
        return dbvconf.col(2)
    return None