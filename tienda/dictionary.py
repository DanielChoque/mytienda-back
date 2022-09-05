
def EmpresaDictionary(empresa):
    salida = {}
    salida["id"] = empresa.id
    salida["nombre"] = empresa.nombre
    salida["elaboradopor"] = empresa.elaboradopor
    salida["modificado"] = empresa.modificado
    return salida

def EnvaseDictionary(envase):
    salida = {}
    salida["id"] = envase.id
    salida["nombre"] = envase.nombre 
    salida["modificado"] = envase.modificado
    return salida

def UnidadDictionary(unidad):
    salida = {}
    salida["id"] = unidad.id
    salida["nombre"] = unidad.nombre 
    salida["modificado"] = unidad.modificado
    return salida

def MedidaDictionary(medida):
    salida = {}
    salida["id"] = medida.id
    salida["nombre"] = medida.nombre 
    salida["modificado"] = medida.modificado
    return salida
