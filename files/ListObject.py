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
        return "Variable inconnue : "+name
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
        return "Fonction inconnue : "+name
    else:
        if func.nbParameters == 0 and parameters[0] == "":
            return func.call()
        if func.nbParameters == len(parameters):
            return func.call(parameters)
        else:
            return "Nombre de parametres acceptés : "+str(func.nbParameters)+" - Nombre de parametres donnés : "+str(len(parameters))