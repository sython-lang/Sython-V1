from files.FunctionsForSython import error

variables = []
functions = []

def variableExist(name):
    for i in variables:
        if i[0] == name:
            return i[1]
    return False

def callVariable(name):
    var = variableExist(name)
    if not var:
        error("UnknownVariable", "La variable '"+name+"' est inconnu")
    else:
        return var.value

def functionExist(name):
    for i in functions:
        if i[0] == name:
            return i[1]
    return False

def callFunction(name, parameters):
    func = functionExist(name)
    if not func:
        error("UnknownFunction", "La fonction '"+name+"' est inconnu")
    else:
        if func.nbParameters == 0 and parameters[0] == "":
            return func.call()
        if func.nbParameters == len(parameters):
            return func.call(parameters)
        else:
            error("NumberParameters", "Nombre de parametres acceptés : "+str(func.nbParameters)+" - Nombre de parametres donnés : "+str(len(parameters)))