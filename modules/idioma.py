import sys, e32, appuifw, string

modulospropios = 'c:\\Python\\modules\\idiomas'
sys.path.append(modulospropios)

idioma=u"es"

def fijarIdioma(id):
    global idioma
    idioma=id

def getLang(palabra):
    global idioma
    exec("from csds60_"+idioma+" import csds60")
    return csds60[palabra]