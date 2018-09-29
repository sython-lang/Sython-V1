from files.ListObject import variables, variableExist, callFunction
from files.Operations import add, subtract, multiply, divide

def createVariable(type_, name, value):
    var = variableExist(name)
    if not var:
        var = Variable(type_, name)
        if var.verifyVariable()[0]:
            if var.setValue(value)[0]:
                variables.append([name, var])
            else:
                return var.setValue(value)[1]
        else:
            return var.verifyVariable()[1]
    else:
        if var.changeType(type_)[0]:
            if not var.setValue(value)[0]:
                return var.setValue(value)[1]
        else:
            return var.changeType(type_)[1]

def setVariable(name, value):
    var = variableExist(name)
    if not var:
        return "La variable '"+name+"' n'existe pas"
    else:
        result = var.setValue(value)
        if not result[0]:
            return result[1]

class Variable():
    def __init__(self, type_, name):
        self.type_, self.name = type_, name
    
    def verifyVariable(self):
        if self.type_ in ["int","str","float"]:
            return True, self.type_
        else:
            return False, "Type inconnu : "+self.type_

    def changeType(self, type_):
        if type_ in ["int","str","float"]:
            self.type_ = type_
            return True, self.type_
        else:
            return False, "Type inconnu : "+type_

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
                return True, self.name
            elif self.type_ == "int":
                try:
                    self.value = int(callFunction(name, parameters))
                    return True, ""
                except:
                    return False, "Ce n'est pas un entier"
            elif self.type_ == "float":
                try:
                    self.value = float(callFunction(name, parameters))
                    return True, self.name
                except:
                    return False, "Impossible de convertir '"+callFunction(name, parameters)+"' en flottant"
        else:
            var = variableExist(value)
            if not var:
                if len(value) > 0 and (value[0] != '"' or value[-1] != '"'):
                    if " + " in value:
                        values = value.split(" + ")
                        while len(values) > 1:
                            result, info = add(values[0], values[1], self.type_)
                            if result:
                                values[0] = info
                                del values[1]
                            else:
                                return False, info
                        self.value = values[0]
                        return True, self.name
                    elif "+" in value:
                        values = value.split("+")
                        while len(values) > 1:
                            result, info = add(values[0], values[1], self.type_)
                            if result:
                                values[0] = info
                                del values[1]
                            else:
                                return False, info
                        self.value = values[0]
                        return True, self.name
                    if " - " in value:
                        values = value.split(" - ")
                        while len(values) > 1:
                            result, info = subtract(values[0], values[1], self.type_)
                            if result:
                                values[0] = info
                                del values[1]
                            else:
                                return False, info
                        self.value = values[0]
                        return True, self.name
                    elif "-" in value:
                        values = value.split("-")
                        while len(values) > 1:
                            result, info = subtract(values[0], values[1], self.type_)
                            if result:
                                values[0] = info
                                del values[1]
                            else:
                                return False, info
                        self.value = values[0]
                        return True, self.name
                    if " * " in value:
                        values = value.split(" * ")
                        while len(values) > 1:
                            result, info = multiply(values[0], values[1], self.type_)
                            if result:
                                values[0] = info
                                del values[1]
                            else:
                                return False, info
                        self.value = values[0]
                        return True, self.name
                    elif "*" in value:
                        values = value.split("*")
                        while len(values) > 1:
                            result, info = multiply(values[0], values[1], self.type_)
                            if result:
                                values[0] = info
                                del values[1]
                            else:
                                return False, info
                        self.value = values[0]
                        return True, self.name
                    if " / " in value:
                        values = value.split(" / ")
                        while len(values) > 1:
                            result, info = divide(values[0], values[1], self.type_)
                            if result:
                                values[0] = info
                                del values[1]
                            else:
                                return False, info
                        self.value = values[0]
                        return True, self.name
                    elif "/" in value:
                        values = value.split("/")
                        while len(values) > 1:
                            result, info = divide(values[0], values[1], self.type_)
                            if result:
                                values[0] = info
                                del values[1]
                            else:
                                return False, info
                        self.value = values[0]
                        return True, self.name
                    else:
                        if self.type_ == "int":
                            try:
                                self.value = int(value)
                                return True, self.name
                            except:
                                return False, "Impossible de convertir '"+ value +"' en entier"
                        elif self.type_ == "float":
                            try:
                                self.value = float(value)
                                return True, self.name
                            except:
                                return False, "Impossible de convertir '"+value+"' en float"
                        elif self.type_ == "str":
                            if len(value) > 1 and value[0] == '"' and value[-1] == '"':
                                value = value[1:-1]
                                self.value = value
                                return True, self.name
                            else:
                                return False, "Impossible de convertir '"+value+"' en string"
                elif self.type_ == "str":
                        if len(value) > 1 and value[0] == '"' and value[-1] == '"':
                            value = value[1:-1]
                            self.value = value
                            return True, self.name
                        else:
                            return False, "Impossible de convertir '"+value+"' en string"
                else:
                    return False, "Impossible de convertir '"+value+"' en string"
            else:
                if var.type_ == self.type_:
                    self.value = var.value
                    return True, self.name
                else:
                    return False, "Les variables '"+self.name+"' et '"+var.name+"' n'ont pas le même type"