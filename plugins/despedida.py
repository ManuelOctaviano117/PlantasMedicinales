import random

def execute(*args):
    var=args[0]
    opts=args[1]
    msg = random.choice(['Me dio gusto ayudarte','Espero te sirviera mi ayuda','Gracias por dejarme ayudarte']+opts)
    return 'set_slot {0} "{1}"'.format(var,msg)
