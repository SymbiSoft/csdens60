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
#from time import localtime



#creacion de la base de datos del mes actual
#actMes = localtime()[1]
#actAno = localtime()[0]
#database = u"csds60"
#database = database +"_"+ str(actMes)+"_"+str(actAno) + ".db" 

#tiene que estar en esta linea, sino falla por los parametros de arriba
from base_de_datos import obtener_idioma_act_conf
from base_de_datos import obtener_db_actual
from base_de_datos import obtener_peso_actual
from base_de_datos import obtener_altura_actual
from base_de_datos import obtener_totalinsu_actual
from base_de_datos import obtener_ratiodesayuno_actual
from base_de_datos import obtener_ratioalmuerzo_actual
from base_de_datos import obtener_ratiocena_actual
from base_de_datos import obtener_alarmatiras_actual
#carga la bd seleccionada
database = obtener_db_actual()
#idioma seleccionado, es especial por recuperar la constante del idioma, no el idioma en si
cfgIdioma = obtener_idioma_act_conf() 

#numero de tiras reactivas minimo para activar la alarma
#alarmaTiras = 5
alarmaTiras = int(obtener_alarmatiras_actual()) 
#numero de dias con antelacion antes de la fecha de la cita 
#alarmaCitas = 3 

#peso de la persona en kg
#peso = 76.00
peso = obtener_peso_actual()
#altura de la persona en cm
#estatura = 175
altura = obtener_altura_actual()

#total de insulinas que se administra diariamente
#totalInsulina = 38 
totalInsulina = obtener_totalinsu_actual()
#cantidad de glucosa que baja una unidad de insulina(parte entera)
factorSensibilidad = int(1800//totalInsulina)

#dosis de insulina recomendada por el medico, ayudara a calcular los ratios
#dosisDesayuno = 4
#dosisAlmuerzo = 3
#dosisCena = 2

#ratio es la necesidad de insulina por racion de hidratos de carbono
#ratios de desayuno, almuerzo y cena; normalmente los ratios del desayuno a cena varian,
#por eso es necesario guardar los 3 tipos
#ratioDesayuno = 0.75
#ratioAlmuerzo = 1.34
#ratioCena = 2
ratioDesayuno = obtener_ratiodesayuno_actual()
ratioAlmuerzo = obtener_ratioalmuerzo_actual()
ratioCena = obtener_ratiocena_actual()

#1 racion de hidratos de carbono -> un vaso de leche o 2 yogures naturales
#2              "                -> un pan o tazon de cereales, legumbres, patatas, pasta
#2              "                -> 1 pieza mediana de fruta
#1              "                -> 1 plato de verdura
#0              "                -> carne o pescado
#para calcular la dosis de insulina, la formula es (cantidad de raciones de hc)/(ratio pertinente) +
#correcion de glucosa si superamos 250 mg, cuya formula es (glucosa actual - 100) / (factor sensibilidad)     


