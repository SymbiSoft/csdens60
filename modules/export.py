# Archivo: export.py
# Autor: Jorge Aguirre Andreu
# Descripci�n: Puedes exportar todo el diario en un archivo xml para la aplicaci�n
# csds60analyzer, exportar a html para su visionado y enviar dichos datos mediante 
# conexi�n(a determinar) con un ordenador(del endocrino), asi se facilitan las revisiones
# y se agiliza el trato entre ambas partes.
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

import e32, appuifw, sys, os, graphics, codecs, key_codes

sys.setdefaultencoding('utf-8')

try:
    raise Exception
except Exception:
    path = sys.exc_info()[2].tb_frame.f_code.co_filename
if not path:
    path = os.path.join(os.getcwd(), 'default.py')
unidad=path[0]

modulospropios = unidad+':\\Python\\modules'
sys.path.append(modulospropios)
from idioma import getLang
from configuracion import *
from e32socket import *
import base_de_datos


# Sirve para crear un archivo xml del mes para su uso con csds60analyzer
def generar_xml():
    global unidad
    xml=u""
    datos=base_de_datos.obtener_datos_diario()
    fecha=0
    for i in range(datos.count_line()):
        datos.get_line()
        if fecha!=datos.col(1):
            fecha=datos.col(1)
            xml=xml+u"</dia>\n<dia>\n\t<fecha>"+str(fecha)+u"</fecha>\n"
        if str(datos.col(2)) == u"Antes del desayuno":
            texto = u"desayunoantes"
            xml=xml+u"\t<"+texto+u">"+str(datos.col(3))+u"</"+texto+u">\n"
        elif str(datos.col(2)) == u"Despues del desayuno":
            texto = u"desayunodespues"
            xml=xml+u"\t<"+texto+u">"+str(datos.col(3))+u"</"+texto+u">\n"
        elif str(datos.col(2)) == u"Antes del almuerzo":
            texto = u"almuerzoantes"
            xml=xml+u"\t<"+texto+u">"+str(datos.col(3))+u"</"+texto+u">\n"
        elif str(datos.col(2)) == u"Despues del almuerzo":
            texto = u"almuerzodespues"
            xml=xml+u"\t<"+texto+u">"+str(datos.col(3))+u"</"+texto+u">\n"
        elif str(datos.col(2)) == u"Antes de la cena":
            texto = u"cenaantes"
            xml=xml+u"\t<"+texto+u">"+str(datos.col(3))+u"</"+texto+u">\n"
        elif str(datos.col(2)) == u"Despues de la cena":
            texto = u"cenadespues"
            xml=xml+u"\t<"+texto+u">"+str(datos.col(3))+u"</"+texto+u">\n"
        datos.next_line()
    xmlFinal=u"<?xml version=\"1.0\" encoding=\"UTF-8\"?><root>"+xml[6:]+u"</dia></root>"
    fichero=codecs.open(unidad+':\\Python\\resources\\xml\db_'+base_de_datos.obtener_db_actual()+'.xml','w','utf8')
    fichero.write(xmlFinal)

# Sirve para crear un html de un mes para visualizarlo en una pantalla mas grande como un ordenador
def generar_html():
    global unidad
    
    html=u""
    cabecerahtml=u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//ES\"><html><head><title>CSDs60WebAnalyzer</title>"
    #css=u"<style type=\"text/css\">#datosCont{margin:20px auto 0;padding:15px 20px;width:700px}div.dat\
#osDia{margin-bottom:15px}div.datosDiaTitulo{border-bottom:2px solid #97d25d;cursor:pointer;font-we\
#ight:700}div.datosDiaCont{display:none;padding-left:20px}div.datosDiaContAtr{float:left;width:70%}\
#div.datosDiaContVal{float:right;text-align:center;width:30%}</style>"
    #javascript=u"<script type=\"text/javascript\">function mostrar(act){var hijos=act.parentNode.child\
#Nodes;for(var i=0;i<hijos.length;i++){if(hijos[i].tagName==\"DIV\"&&hijos[i].className==\"datosDia\
#Cont\"){if(hijos[i].style.display==\"block\"){hijos[i].style.display=\"none\"}else{hijos[i].style.\
#display=\"block\"}}}}window.onload=function(){var dias=document.getElementById(\"datosCont\").chil\
#dNodes;for(var i=0;i<dias.length;i++){if(dias[i].tagName==\"DIV\"&&dias[i].className==\"datosDia\"\
#){for(var j=0;j<dias[i].childNodes.length;j++){if(dias[i].childNodes[j].tagName==\"DIV\"&&dias[i].\
#childNodes[j].className==\"datosDiaTitulo\"){var diaValor=dias[i].childNodes[j];var fecha=new Date\
#();fecha.setTime(diaValor.innerHTML*1000);diaValor.innerHTML=fecha.getDate()+\"/\"+(fecha.getMonth(\
#)+1)+\"/\"+fecha.getFullYear();dias[i].childNodes[j].onclick=function(){mostrar(this)}}}}}}</script>"
    datos=base_de_datos.obtener_datos_diario()   
    
    fecha=0
    fechaantigua=-1
    comida = False
    depdesant=u"" 
    depdesdes=u""
    depalmant=u""
    depalmdes=u""
    depcenant=u""
    depcendes=u""
    glucag=u""
    glucdesant=u""
    glucdesdes=u""
    glucalmant=u""
    glucalmdes=u""
    gluccenant=u""
    gluccendes=u""
    orina=u""
    insudesant=u""
    insudesdes=u""
    insualmant=u""
    insualmdes=u""
    insucenant=u""
    insucendes=u""
    acetona=u""
    desayuno=u""
    medman=u""
    almuerzo=u"" 
    merienda=u""
    cena=u""
    resopon=u""
    notas=u""
    medica=u""
    
    html=html+u"/head><body><table border=\"1\" width=\"100%\"><tr><td align=\"center\" rowspan=\"4\">\
Fecha</td><td align=\"center\" colspan=\"6\">Dosis de insulina</td><td align=\"center\" colspan=\"6\">\
Glucosa en sangre</td><td align=\"center\" colspan=\"2\" rowspan=\"2\">Orina</td><td align=\"center\" colspan=\"15\">\
Datos extra</td></tr><tr><td align=\"center\" colspan=\"2\">Desayuno</td><td align=\"center\" colspan=\"2\">\
Almuerzo</td><td align=\"center\" colspan=\"2\">Cena</td><td align=\"center\" colspan=\"2\">Desayuno</td>\
<td align=\"center\" colspan=\"2\">Almuerzo</td><td align=\"center\" colspan=\"2\">Cena</td><td align=\"center\" colspan=\"6\">\
Comidas</td><td align=\"center\" rowspan=\"3\">Medicamentos</td><td align=\"center\" colspan=\"6\">Deporte</td>\
<td align=\"center\" rowspan=\"3\">Notas extra</td><td align=\"center\" rowspan=\"3\">Glucag&oacute;n</td></tr><tr>\
<td align=\"center\" rowspan=\"2\">Antes</td><td align=\"center\" rowspan=\"2\">Despu&eacute;s</td><td align=\"center\" rowspan=\"2\">\
Antes</td><td align=\"center\" rowspan=\"2\">Despu&eacute;s</td><td align=\"center\" rowspan=\"2\">Antes</td>\
<td align=\"center\" rowspan=\"2\">Despu&eacute;s</td><td align=\"center\" rowspan=\"2\">Antes</td><td align=\"center\" rowspan=\"2\">\
Despu&eacute;s</td><td align=\"center\" rowspan=\"2\">Antes</td><td align=\"center\" rowspan=\"2\">Despu&eacute;s</td>\
<td align=\"center\" rowspan=\"2\">Antes</td><td align=\"center\" rowspan=\"2\">Despu&eacute;s</td><td align=\"center\" rowspan=\"2\">\
Glucosa</td><td align=\"center\" rowspan=\"2\">Acetona</td><td align=\"center\" rowspan=\"2\">Desayuno</td>\
<td align=\"center\" rowspan=\"2\">Mediama&ntilde;ana</td><td align=\"center\" rowspan=\"2\">Almuerzo</td>\
<td align=\"center\" rowspan=\"2\">Merienda</td><td align=\"center\" rowspan=\"2\">Cena</td><td align=\"center\" rowspan=\"2\">\
Resop&oacute;n</td><td align=\"center\" colspan=\"2\">Desayuno</td><td align=\"center\" colspan=\"2\">Almuerzo</td>\
<td align=\"center\" colspan=\"2\">Cena</td></tr><tr><td align=\"center\">Antes</td><td align=\"center\">Despu&eacute;s</td>\
<td align=\"center\">Antes</td><td align=\"center\">Despu&eacute;s</td><td align=\"center\">Antes</td><td align=\"center\">\
Despu&eacute;s</td></tr>"

    #sirve para construir la pagina dinamicamente, entraria en el segundo dia, es ahi cuando rellenamos todo lo del dia anterior
    entraunavez=0
    for i in range(datos.count_line()):        
        datos.get_line()
        ord = int(datos.col(5))
        
        if fecha!=datos.col(1):
            fecha=datos.col(1)
            
            if entraunavez==1: 
                #esto es para que dibuje las celdas si estan vacias
                if depdesant==u"":
                    depdesant=u"&nbsp;"
                if depdesdes==u"":   
                    depdesdes=u"&nbsp;"
                if depalmant==u"": 
                    depalmant=u"&nbsp;"
                if depalmdes==u"": 
                    depalmdes=u"&nbsp;"
                if depcenant==u"": 
                    depcenant=u"&nbsp;"
                if depcendes==u"": 
                    depcendes=u"&nbsp;"
                if glucag==u"": 
                    glucag=u"&nbsp;"
                if glucdesant==u"":  
                    glucdesant=u"&nbsp;"
                if glucdesdes==u"": 
                    glucdesdes=u"&nbsp;"
                if glucalmant==u"": 
                    glucalmant=u"&nbsp;"
                if glucalmdes==u"": 
                    glucalmdes=u"&nbsp;"
                if gluccenant==u"": 
                    gluccenant=u"&nbsp;"
                if gluccendes==u"": 
                    gluccendes=u"&nbsp;"
                if orina==u"": 
                    orina=u"&nbsp;"
                if insudesant==u"": 
                    insudesant=u"&nbsp;"
                if insudesdes==u"": 
                    insudesdes=u"&nbsp;"
                if insualmant==u"": 
                    insualmant=u"&nbsp;"
                if insualmdes==u"": 
                    insualmdes=u"&nbsp;"
                if insucenant==u"": 
                    insucenant=u"&nbsp;"
                if insucendes==u"": 
                    insucendes=u"&nbsp;"
                if acetona==u"": 
                    acetona=u"&nbsp;"
                if desayuno==u"": 
                    desayuno=u"&nbsp;"
                if medman==u"": 
                    medman=u"&nbsp;"
                if almuerzo==u"": 
                    almuerzo=u"&nbsp;"
                if merienda==u"": 
                    merienda=u"&nbsp;"
                if cena==u"": 
                    cena=u"&nbsp;"
                if resopon==u"": 
                    resopon=u"&nbsp;"
                if notas==u"": 
                    notas=u"&nbsp;"
                if medica==u"": 
                    medica=u"&nbsp;"            
                         
                #escribir pagina web,al final fuera del buble hay que repetir una vez mas esto, para el ultimo dia del mes
                html=html+u"<tr><td align=\"center\">"+fechaantigua+"</td><td align=\"center\">"+insudesant+"</td><td align=\"center\">"+insudesdes+"</td>\
<td align=\"center\">"+insualmant+"</td><td align=\"center\">"+insualmdes+"</td><td align=\"center\">"+insucenant+"</td><td align=\"center\">\
"+insucendes+"</td><td align=\"center\">"+glucdesant+"</td><td align=\"center\">"+glucdesdes+"</td><td align=\"center\">"+glucalmant+"</td>\
<td align=\"center\">"+glucalmdes+"</td><td align=\"center\">"+gluccenant+"</td><td align=\"center\">"+gluccendes+"</td><td align=\"center\">\
"+orina+"</td><td align=\"center\">"+acetona+"</td><td align=\"center\">"+desayuno+"</td><td align=\"center\">"+medman+"</td><td align=\"center\">\
"+almuerzo+"</td><td align=\"center\">"+merienda+"</td><td align=\"center\">"+cena+"</td><td align=\"center\">"+resopon+"</td><td align=\"center\">\
"+medica+"</td><td align=\"center\">"+depdesant+"</td><td align=\"center\">"+depdesdes+"</td><td align=\"center\">"+depalmant+"\
</td><td align=\"center\">"+depalmdes+"</td><td align=\"center\">"+depcenant+"</td><td align=\"center\">"+depcendes+"</td><td align=\"center\">\
"+notas+"</td><td align=\"center\">"+glucag+"</td></tr>"
                
            entraunavez=1
            
            depdesant=u"" 
            depdesdes=u""
            depalmant=u""
            depalmdes=u""
            depcenant=u""
            depcendes=u""
            glucag=u""
            glucdesant=u""
            glucdesdes=u""
            glucalmant=u""
            glucalmdes=u""
            gluccenant=u""
            gluccendes=u""
            orina=u""
            insudesant=u""
            insudesdes=u""
            insualmant=u""
            insualmdes=u""
            insucenant=u""
            insucendes=u""
            acetona=u""
            desayuno=u""
            medman=u""
            almuerzo=u"" 
            merienda=u""
            cena=u""
            resopon=u""
            notas=u""
            medica=u""
            
            #html=html+u"</div></div><div class=\"datosDia\"><div class=\"datosDiaTitulo\">"+str(fecha)+"</div><div class=\"datosDiaCont\">"            
        
        chk = u""
        term = u""        
        
        if ord == 5 or ord == 6 or ord == 12 or ord == 13 or ord == 19 or ord == 20 or ord == 23:
            if str(datos.col(4)) == u"S":
                chk = u"Si"
            else:
                chk = u"No"
            
            if ord == 5:
                depdesant=chk
            elif ord == 6:
                depdesdes=chk
            elif ord == 12:
                depalmant=chk
            elif ord == 13:
                depalmdes=chk
            elif ord == 19:
                depcenant=chk
            elif ord == 20:
                depcendes=chk
            elif ord == 23:
                glucag=chk
            
        elif ord == 0 or ord == 1 or ord == 7 or ord == 8 or ord == 14 or ord == 15 or ord == 21:
            term = u" mg"
            
            if ord == 0:
                glucdesant=str(datos.col(3))+term
            elif ord == 1:
                glucdesdes=str(datos.col(3))+term
            elif ord == 7:
                glucalmant=str(datos.col(3))+term
            elif ord == 8:
                glucalmdes=str(datos.col(3))+term
            elif ord == 14:
                gluccenant=str(datos.col(3))+term
            elif ord == 15:
                gluccendes=str(datos.col(3))+term
            elif ord == 21:
                orina=str(datos.col(3))+term
                
        elif ord == 3 or ord == 4 or ord == 10 or ord == 11 or ord == 17 or ord == 18:
            term = u" ui"
            
            #las insulinas quedan de la forma nombreinsulina<br>cantidad<br>
            if ord == 3:
                insudesant=insudesant+(str(datos.col(2)))[25:]+"<br/>"+str(datos.col(3))+term+"<br/>"
                #insudesant=insudesant+(str(datos.col(2))).substring(25,(len(str(datos.col(2)))))+"<br/>"+str(datos.col(3))+term+"<br/>"
            elif ord == 4:
                insudesdes=insudesdes+(str(datos.col(2)))[26:]+"<br/>"+str(datos.col(3))+term+"<br/>"
                #insudesdes=insudesdes+(str(datos.col(2))).substring(25,(len(str(datos.col(2)))))+"<br/>"+str(datos.col(3))+term+"<br/>"
            elif ord == 10:
                insualmant=insualmant+(str(datos.col(2)))[25:]+"<br/>"+str(datos.col(3))+term+"<br/>"
                #insualmant=insualmant+(str(datos.col(2))).substring(25,(len(str(datos.col(2)))))+"<br/>"+str(datos.col(3))+term+"<br/>"
            elif ord == 11:
                insualmdes=insualmdes+(str(datos.col(2)))[26:]+"<br/>"+str(datos.col(3))+term+"<br/>"
                #insualmdes=insualmdes+(str(datos.col(2))).substring(25,(len(str(datos.col(2)))))+"<br/>"+str(datos.col(3))+term+"<br/>"
            elif ord == 17:
                insucenant=insucenant+(str(datos.col(2)))[23:]+"<br/>"+str(datos.col(3))+term+"<br/>"
                #insucenant=insucenant+(str(datos.col(2))).substring(23,(len(str(datos.col(2)))))+"<br/>"+str(datos.col(3))+term+"<br/>"
            elif ord == 18:
                insucendes=insucendes+(str(datos.col(2)))[24:]+"<br/>"+str(datos.col(3))+term+"<br/>"
                #insucendes=insucendes+(str(datos.col(2))).substring(23,(len(str(datos.col(2)))))+"<br/>"+str(datos.col(3))+term+"<br/>"
                
        elif ord == 22:
            term = u" +"
            
            acetona=str(datos.col(3))+term
            
        elif ord == 24 or ord == 25 or ord == 26 or ord == 27 or ord == 28 or ord == 29 or ord == 30 or ord == 31:   
            comida = True
        if ord != 2 and ord != 9 and ord != 16:
            #if chk == u"" and comida == False:
             #   html=html+u"<div class=\"datosDiaContAtr\">"+str(datos.col(2))+u"</div><div class=\"datosDiaContVal\">"+str(datos.col(3))+term+u"</div>"
            if chk == u"" and comida == True:
                # Decoding to unicode
                input_s = str(datos.col(4))
                repr(input_s)

                uni = input_s.decode('utf-8')
                repr(uni)

                # cp1252 is the encoding used on my windows-pc,
                #output_s = input_s.encode('utf-8')
                #repr(output_s)

                #value = u""+str(datos.col(4))
                              
                uni = uni.replace('ñ','&ntilde;')
                uni = uni.replace('Ñ','&Ntilde;')
                uni = uni.replace('ç','&ccedil;')
                uni = uni.replace('Ç','&Ccedil;')                
                uni = uni.replace('á','&aacute;')
                uni = uni.replace('Á','&Aacute;')
                uni = uni.replace('é','&eacute;')
                uni = uni.replace('É','&Eacute;')
                uni = uni.replace('í','&iacute;')
                uni = uni.replace('Í','&Iacute;')
                uni = uni.replace('ó','&oacute;')
                uni = uni.replace('Ó','&Oacute;')
                uni = uni.replace('ú','&uacute;')
                uni = uni.replace('Ú','&Uacute;')                
                #uni = uni.replace('£','&pound;')
                #uni = uni.replace('¥','&yen;')
                #uni = uni.replace('¤','&curren;')
                #uni = uni.replace('€','&euro;')
                #uni = uni.replace('¡','&iexcl;')
                #uni = uni.replace('¿','&iquest;')
                #uni = uni.replace('§','&sect;')
                uni = uni.replace('£','')
                uni = uni.replace('¥','')
                uni = uni.replace('¤','')
                uni = uni.replace('€','')
                uni = uni.replace('¡','')
                uni = uni.replace('¿','')
                uni = uni.replace('§','')
                uni = uni.replace('$','')
                uni = uni.replace('=','')
                uni = uni.replace('\'','')
                uni = uni.replace('*','')
                uni = uni.replace('$','')
                uni = uni.replace('?','')
                uni = uni.replace('!','')
                uni = uni.replace('+','')
                uni = uni.replace('-','')
                uni = uni.replace('_','')
                uni = uni.replace(':','')
                uni = uni.replace('(','')
                uni = uni.replace(')','')
                uni = uni.replace('{','')
                uni = uni.replace('}','')
                uni = uni.replace('<','')
                uni = uni.replace('>','')
                uni = uni.replace('"','')
                uni = uni.replace('#','')
                uni = uni.replace('@','')
                uni = uni.replace('|','')
                uni = uni.replace('%','')                

                comd = u""+uni
                if ord == 24:
                    desayuno=comd
                elif ord == 25:
                    medman=comd
                elif ord == 26:
                    almuerzo=comd
                elif ord == 27:
                    merienda=comd
                elif ord == 28:
                    cena=comd
                elif ord == 29:
                    resopon=comd
                elif ord == 30:
                    notas=comd
                elif ord == 31:
                    medica=comd

                #html=html+u"<div class=\"datosDiaContAtr\">"+str(datos.col(2))+u"</div><div class=\"datosDiaContVal\">"+comd+u"</div>"
            #elif chk != u"":
             #   html=html+u"<div class=\"datosDiaContAtr\">"+str(datos.col(2))+u"</div><div class=\"datosDiaContVal\">"+chk+u"</div>"       
        comida = False

        #aqui guardamos la fecha para poder distinguir las filas de la tabla en el html
        fechaantigua=str(fecha)
        datos.next_line()
    if fechaantigua>0:    
        html=html+u"<tr><td align=\"center\">"+fechaantigua+"</td><td align=\"center\">"+insudesant+"</td><td align=\"center\">"+insudesdes+"</td>\
<td align=\"center\">"+insualmant+"</td><td align=\"center\">"+insualmdes+"</td><td align=\"center\">"+insucenant+"</td><td align=\"center\">\
"+insucendes+"</td><td align=\"center\">"+glucdesant+"</td><td align=\"center\">"+glucdesdes+"</td><td align=\"center\">"+glucalmant+"</td>\
<td align=\"center\">"+glucalmdes+"</td><td align=\"center\">"+gluccenant+"</td><td align=\"center\">"+gluccendes+"</td><td align=\"center\">\
"+orina+"</td><td align=\"center\">"+acetona+"</td><td align=\"center\">"+desayuno+"</td><td align=\"center\">"+medman+"</td><td align=\"center\">\
"+almuerzo+"</td><td align=\"center\">"+merienda+"</td><td align=\"center\">"+cena+"</td><td align=\"center\">"+resopon+"</td><td align=\"center\">\
"+medica+"</td><td align=\"center\">"+depdesant+"</td><td align=\"center\">"+depdesdes+"</td><td align=\"center\">"+depalmant+"\
</td><td align=\"center\">"+depalmdes+"</td><td align=\"center\">"+depcenant+"</td><td align=\"center\">"+depcendes+"</td><td align=\"center\">\
"+notas+"</td><td align=\"center\">"+glucag+"</td></tr>"
    
    htmlFinal=cabecerahtml+html[12:]+u"</body></html>"
    #htmlFinal=cabecerahtml+css+javascript+u"</head><body><div id=\"datosCont\">"+html[12:]+u"</div></body></html>"
    fichero=codecs.open(unidad+':\\Python\\resources\\html\datos_'+base_de_datos.obtener_db_actual()+'.html','w','utf8')
    fichero.write(htmlFinal)

# Envia por bluetooth los dos archivos anteriores    
def enviarBluetooth():
    global unidad
    generar_xml()
    generar_html()
    try:
        xmlpath = u''
        htmlpath = u''
        xmlpath = xmlpath + unidad+':\\Python\\resources\\xml\db_'+base_de_datos.obtener_db_actual()+'.xml'
        htmlpath = htmlpath + unidad+':\\Python\\resources\\html\datos_'+base_de_datos.obtener_db_actual()+'.html'
        # "How to send files using bluetooth"<http://wiki.forum.nokia.com/index.php/How_to_send_files_using_bluetooth>(2 Noviembre 2009)
        #encuentra dispositivos con Bluetooth
        phone = bt_obex_discover()
        #direccion mac del dispositivo
        addr=phone[0]
        #puerto del dispositivo
        port=phone[1].values()[0]
        file = appuifw.query(getLang(u'XML CARGA'),'text',xmlpath)
        bt_obex_send_file(addr, port , file)
        file = appuifw.query(getLang(u'HTML CARGA'),'text',htmlpath)
        bt_obex_send_file(addr, port , file)
        appuifw.note(getLang(u"ARCH ENVIADOS"), 'conf')
    except Exception, error:
        appuifw.note(unicode(error), 'error') 

def handle_redraw(rect):
    global canvasExport
    global imExport
    global actPos
    colorTexto=[0 for x in range(3)]
    for i in range(3):
        colorTexto[i]=0x000000
    colorTexto[actPos]=0xff0000
    canvasExport.blit(imExport)
    canvasExport.rectangle((20,120,250,225),outline=0xeeeeee,fill=0xeeeeee)
    canvasExport.text((178,85),getLang(u"EXPORTAR"),0xbbbbbb,font=(u"symbol",27))
    canvasExport.text((177,84),getLang(u"EXPORTAR"),0x000000,font=(u"symbol",27))
    canvasExport.text((240,410),getLang(u"VOLVER"),0xffffff,font=(u"legend",25,appuifw.STYLE_BOLD))
    canvasExport.text((25,410),getLang(u"OPCIONES"),0xffffff,font=(u"legend",25,appuifw.STYLE_BOLD))
    
    canvasExport.line((20,120,330,120),0)
    canvasExport.text((40,135),getLang(u"XML"),colorTexto[0],font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasExport.line((20,155,330,155),0)
    canvasExport.text((40,170),getLang(u"HTML"),colorTexto[1],font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasExport.line((20,190,330,190),0)
    canvasExport.text((40,205),getLang(u"BLUET"),colorTexto[2],font=(u"legend",17,appuifw.STYLE_BOLD))
    canvasExport.line((20,225,330,225),0)

def volverAtras():
    global gvAtras
    gvAtrasEnvio=[0 for x in range(len(gvAtras)-1)]
    for i in range(len(gvAtras)-1):
        gvAtrasEnvio[i]=gvAtras[i]
    gvAtras[len(gvAtras)-1](gvAtrasEnvio)
    
def moverCursor(pos):
    global actPos
    global movimientos
    actPos+=movimientos[actPos][1][pos]
    appuifw.app.body = canvasExport
    
def press_select():
    global movimientos
    global actPos
    if(movimientos[actPos][3]) == u"XML":
        generar_xml()
        appuifw.note(getLang(u"XML GEN"), "conf")
    elif(movimientos[actPos][3]) == u"HTML":
        generar_html()
        appuifw.note(getLang(u"HTML GEN"), "conf")
    elif(movimientos[actPos][3]) == u"BLUET":
        enviarBluetooth()
    appuifw.app.body = canvasExport    
    
def press_up():
    moverCursor(0)

def press_right():
    moverCursor(1)

def press_down():
    moverCursor(2)

def press_left():
    moverCursor(3)

def mostrarExport(vAtras):
    global movimientos
    movimientos=[
        [0,[0,0,1,0],u"--",u"XML"],
        [1,[-1,0,1,0],u"--",u"HTML"],
        [2,[-1,0,0,0],u"--",u"BLUET"],
        ]
    global actPos
    actPos=0
    ruta = unidad+':\\python\\resources\\ui\\'
    global imExport
    imExport = graphics.Image.open(ruta+'fondo01.png')
    global canvasExport
    canvasExport = appuifw.Canvas(redraw_callback = handle_redraw)
    canvasExport.blit(imExport)
    appuifw.app.body = canvasExport
    appuifw.app.screen = 'full'
    appuifw.app.title = u"Exportar"
    canvasExport.bind(key_codes.EKeySelect, press_select)
    canvasExport.bind(key_codes.EKeyUpArrow, press_up)
    canvasExport.bind(key_codes.EKeyRightArrow, press_right)
    canvasExport.bind(key_codes.EKeyDownArrow, press_down)
    canvasExport.bind(key_codes.EKeyLeftArrow, press_left)
    global gvAtras
    gvAtras=vAtras
    if len(vAtras)==1:
        appuifw.app.exit_key_handler=gvAtras[0]
    else:
        appuifw.app.exit_key_handler=volverAtras    