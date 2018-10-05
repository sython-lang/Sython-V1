from files.ListObject import variables, variableExist, callFunction
from files.Operations import add, subtract, multiply, divide
from files.FunctionsForSython import error

def createVariable(type_, name, value):
    var = variableExist(name)
    if not var:
        var = Variable(type_, name)
        var.verifyVariable()
        var.setValue(value)
        variables.append([name, var])
    else:
        var.changeType(type_)
        var.setValue(value)

def setVariable(name, value):
    var = variableExist(name)
    if not var:
        return "La variable '"+name+"' n'existe pas"
    else:
        result = var.setValue(value)

class Variable():
    def __init__(self, type_, name):
        self.type_, self.name = type_, name
    
    def verifyVariable(self):
        if not self.type_ in ["int","str","float"]:
            error("UnknownType", "Type inconnu : "+self.type_)

    def changeType(self, type_):
        if type_ in ["int","str","float"]:
            self.type_ = type_
        else:
            error("UnknownType", "Type inconnu : "+self.type_)

    def setValue(self, value):
        if "(" in value and ")" in value:
            if '"' in value:
                temp = value.split("(")
                if len(temp) == 2:
                    name, parametre = temp
                else:
                    name = temp[0]
                    del temp[0]
                    parametre = "(".join(temp)
            else:
                name, parametre = value.split("(")
            if ", " in parametre:
                parameters = parametre[:-1].split(", ")
            else:
                parameters = [parametre[:-1]]
            if self.type_ == "str":
                self.value = str(callFunction(name, parameters))
            elif self.type_ == "int":
                temp = callFunction(name, parameters)
                try:
                    self.value = int(temp)
                except:
                    error("ErrorConversion", "Impossible de convertir '"+temp+"' en entier")
            elif self.type_ == "float":
                temp = callFunction(name, parameters)
                try:
                    self.value = float(temp)
                except:
                    error("ErrorConversion", "Impossible de convertir '"+temp+"' en flottant")
        else:
            var = variableExist(value)
            if not var:
                if len(value) > 1 and value[0] == '"' and value[-1] == '"':
                    if self.type_ == "str":
                        if len(value) > 1 and value[0] == '"' and value[-1] == '"':
                            value = value[1:-1]
                            self.value = value
                        else:
                            error("ErrorConversion", "Impossible de convertir '"+value+"' en string")
                    else:
                        error("ErrorConversion", "Impossible de convertir '"+value+"' en "+self.type_)
                else:
                    if " + " in value:
                        values = value.split(" + ")
                        while len(values) > 1:
                            result, info = add(values[0], values[1], self.type_)
                            if result:
                                values[0] = info
                                del values[1]
                            else:
                                error("ErrorAddition", info)
                                del values[1]
                        self.value = values[0]
                    elif "+" in value:
                        values = value.split("+")
                        while len(values) > 1:
                            result, info = add(values[0], values[1], self.type_)
                            if result:
                                values[0] = info
                                del values[1]
                            else:
                                error("ErrorAddition", info)
                        self.value = values[0]
                    elif " - " in value:
                        values = value.split(" - ")
                        while len(values) > 1:
                            result, info = subtract(values[0], values[1], self.type_)
                            if result:
                                values[0] = info
                                del values[1]
                            else:
                                error("ErrorSubstraction", info)
                        self.value = values[0]
                    elif "-" in value:
                        values = value.split("-")
                        while len(values) > 1:
                            result, info = subtract(values[0], values[1], self.type_)
                            if result:
                                values[0] = info
                                del values[1]
                            else:
                                error("ErrorSubstraction", info)
                        self.value = values[0]
                    elif " * " in value:
                        values = value.split(" * ")
                        while len(values) > 1:
                            result, info = multiply(values[0], values[1], self.type_)
                            if result:
                                values[0] = info
                                del values[1]
                            else:
                                error("ErrorMultiplication", info)
                        self.value = values[0]
                    elif "*" in value:
                        values = value.split("*")
                        while len(values) > 1:
                            result, info = multiply(values[0], values[1], self.type_)
                            if result:
                                values[0] = info
                                del values[1]
                            else:
                                error("ErrorMultiplication", info)
                        self.value = values[0]
                    elif " / " in value:
                        values = value.split(" / ")
                        while len(values) > 1:
                            result, info = divide(values[0], values[1], self.type_)
                            if result:
                                values[0] = info
                                del values[1]
                            else:
                                error("ErrorDivision", info)
                        self.value = values[0]
                    elif "/" in value:
                        values = value.split("/")
                        while len(values) > 1:
                            result, info = divide(values[0], values[1], self.type_)
                            if result:
                                values[0] = info
                                del values[1]
                            else:
                                error("ErrorDivision", info)
                        self.value = values[0]
                    else:
                        if self.type_ == "int":
                            try:
                                self.value = int(value)
                            except:
                                error("ErrorConversion", "Impossible de convertir '"+ value +"' en entier")
                        elif self.type_ == "float":
                            try:
                                self.value = float(value)
                            except:
                                error("ErrorConversion", "Impossible de convertir '"+value+"' en float")
                        elif self.type_ == "str":
                            if len(value) > 1 and value[0] == '"' and value[-1] == '"':
                                value = value[1:-1]
                                self.value = value
                            else:
                                error("ErrorConversion", "Impossible de convertir '"+value+"' en string")
            else:
                if var.type_ == self.type_:
                    self.value = var.value
                else:
                    error("ErrorConversion", "Impossible de convertir '"+var.value+"' en "+self.type_)