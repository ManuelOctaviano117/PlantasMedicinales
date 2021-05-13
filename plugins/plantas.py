
import random

def random_planta(malestar,nombre_slot,db):
    """ Dado un malestar regrasa una planta aleatoria """
    opciones=[]
    basededatos=db['plantas']
    for fila in basededatos:
        if fila[0] == malestar:
            opciones.append(fila[1])
    msg = random.choice(opciones)
    return 'set_slot {0} "{1}"'.format(nombre_slot,msg)

def propiedad(planta,nombre_slot,db):
    """ Dado un malestar regrasa una planta aleatoria """
    opciones=[]
    basededatos=db['plantas']
    for fila in basededatos:
        if fila[1] == planta:
            opciones.append(fila[2])
    msg = random.choice(opciones)
    return 'set_slot {0} "{1}"'.format(nombre_slot,msg)

####DAR INFORMACIÓN DE PLANTA


