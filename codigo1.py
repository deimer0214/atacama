from nltk import word_tokenize, ngrams
import json
import  csv

def stopwords (tmp_entrada):
    stop = open("C:/Users/deimer0214/PycharmProjects/tatacoa/stopwords.txt", "r",  encoding="utf8")
    lista_stop=[]
    for st in stop:
        lista_tmp=[]
        st=st[0:st[0].find('\n')]
        lista_stop.append(st)
    for tr in lista_stop:
        tmp_entrada = [x for x in tmp_entrada if x != tr]
    return tmp_entrada

def CargarDiccionarioLemas():
    file = open("C:/Users/deimer0214/PycharmProjects/tatacoa/diccionarioLematizador.txt", "rb")
    lema_d={}
    for line in file:
        bloques = line.split()
        palabra = bloques[0]
        lema = bloques[1]
        lema_d.update({palabra:lema})
    return lema_d

def lematizador(lema_d,palabra):
    palabra=palabra.lower()
    if palabra in lema_d:
        lema = str(lema_d.get(palabra))
    else:
        lema = palabra
    return lema

lema_d = CargarDiccionarioLemas()


with open('C:/Users/deimer0214/PycharmProjects/tatacoa/cien_tweets.json') as f:
    data = json.load(f)
    lista_registros = []
    for l in data["Name"]:
        tmpCampo=l['text']
        if (len(tmpCampo))>0:
            terminos = {}
            lineaSplit = word_tokenize(tmpCampo.lower())
            for palabra in lineaSplit:
                terminos[palabra] = 1
            tmp_salida = stopwords(terminos)
            lista_palabras = []
            for palabra in tmp_salida:
                lista_palabras.append(lematizador(lema_d, palabra))
            #lista_registros = {"Vector": lista_palabras}
            lista_registros.append(lista_palabras)

ponderator= []

with open('ponderador.txt') as inputfile:
    for line in inputfile:
        ponderator.append(line.strip().split(','))


for ponderator2 in ponderator:
    for listaRegistros2 in lista_registros:
        for listaRegistros3 in listaRegistros2:
            #if listaRegistros3 == ponderator2:
            print(listaRegistros3.join(ponderator2))

