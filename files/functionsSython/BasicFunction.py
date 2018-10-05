from files.ListObject import functions, variableExist, functionExist
from files.Operations import add, subtract, multiply, divide
from files.FunctionsForSython import is_number, error

class Show():
    def __init__(self):
        self.nbParameters = 1
        self.returnValue = False
    
    def call(self, parameters):
        parameters = parameters[0]
        if " + " in parameters:
            values = parameters.split(" + ")
            while len(values) > 1:
                var1 = variableExist(values[0])
                if not var1:
                    var1 = variableExist(values[1])
                    if not var1:
                        if '"' in values[0] or '"' in values[1]:
                            result, info = add(values[0], values[1], "str")
                        elif '.' in values[0] or '.' in values[1]:
                            result, info = add(values[0], values[1], "float")
                        else:
                            result, info = add(values[0], values[1], "int")
                    else:
                        result, info = add(values[0], values[1], var1.type_)
                else:
                    result, info = add(values[0], values[1], var1.type_)
                if result:
                    values[0] = info
                    del values[1]
                else:
                    error("ErrorAddition", info)
            return values[0]
        elif "+" in parameters:
            values = parameters.split("+")
            while len(values) > 1:
                var1 = variableExist(values[0])
                if not var1:
                    var1 = variableExist(values[1])
                    if not var1:
                        if '"' in values[0] or '"' in values[1]:
                            result, info = add(values[0], values[1], "str")
                        elif '.' in values[0] or '.' in values[1]:
                            result, info = add(values[0], values[1], "float")
                        else:
                            result, info = add(values[0], values[1], "int")
                    else:
                        result, info = add(values[0], values[1], var1.type_)
                else:
                    result, info = add(values[0], values[1], var1.type_)
                if result:
                    values[0] = info
                    del values[1]
                else:
                    error("ErrorAddition", info)
            return values[0]
        elif " - " in parameters:
            values = parameters.split(" - ")
            while len(values) > 1:
                var1 = variableExist(values[0])
                if not var1:
                    var1 = variableExist(values[1])
                    if not var1:
                        if '"' in values[0] or '"' in values[1]:
                            result, info = subtract(values[0], values[1], "str")
                        elif '.' in values[0] or '.' in values[1]:
                            result, info = subtract(values[0], values[1], "float")
                        else:
                            result, info = subtract(values[0], values[1], "int")
                    else:
                        result, info = subtract(values[0], values[1], var1.type_)
                else:
                    result, info = subtract(values[0], values[1], var1.type_)
                if result:
                    values[0] = info
                    del values[1]
                else:
                    error("ErrorSubstraction", info)
            return values[0]
        elif "-" in parameters:
            values = parameters.split("-")
            while len(values) > 1:
                var1 = variableExist(values[0])
                if not var1:
                    var1 = variableExist(values[1])
                    if not var1:
                        if '"' in values[0] or '"' in values[1]:
                            result, info = subtract(values[0], values[1], "str")
                        elif '.' in values[0] or '.' in values[1]:
                            result, info = subtract(values[0], values[1], "float")
                        else:
                            result, info = subtract(values[0], values[1], "int")
                    else:
                        result, info = subtract(values[0], values[1], var1.type_)
                else:
                    result, info = subtract(values[0], values[1], var1.type_)
                if result:
                    values[0] = info
                    del values[1]
                else:
                    error("ErrorSubstraction", info)
            return values[0]
        elif " * " in parameters:
            values = parameters.split(" * ")
            while len(values) > 1:
                var1 = variableExist(values[0])
                if not var1:
                    var1 = variableExist(values[1])
                    if not var1:
                        if '"' in values[0] or '"' in values[1]:
                            result, info = multiply(values[0], values[1], "str")
                        elif '.' in values[0] or '.' in values[1]:
                            result, info = multiply(values[0], values[1], "float")
                        else:
                            result, info = multiply(values[0], values[1], "int")
                    else:
                        result, info = multiply(values[0], values[1], var1.type_)
                else:
                    result, info = multiply(values[0], values[1], var1.type_)
                if result:
                    values[0] = info
                    del values[1]
                else:
                    error("ErrorMultiplication", info)
            return values[0]
        elif "*" in parameters:
            values = parameters.split("*")
            while len(values) > 1:
                var1 = variableExist(values[0])
                if not var1:
                    var1 = variableExist(values[1])
                    if not var1:
                        if '"' in values[0] or '"' in values[1]:
                            result, info = multiply(values[0], values[1], "str")
                        elif '.' in values[0] or '.' in values[1]:
                            result, info = multiply(values[0], values[1], "float")
                        else:
                            result, info = multiply(values[0], values[1], "int")
                    else:
                        result, info = multiply(values[0], values[1], var1.type_)
                else:
                    result, info = multiply(values[0], values[1], var1.type_)
                if result:
                    values[0] = info
                    del values[1]
                else:
                    error("ErrorMultiplication", info)
            return values[0]
        elif " / " in parameters:
            values = parameters.split(" / ")
            while len(values) > 1:
                var1 = variableExist(values[0])
                if not var1:
                    var1 = variableExist(values[1])
                    if not var1:
                        if '"' in values[0] or '"' in values[1]:
                            result, info = divide(values[0], values[1], "str")
                        elif '.' in values[0] or '.' in values[1]:
                            result, info = divide(values[0], values[1], "float")
                        else:
                            result, info = divide(values[0], values[1], "int")
                    else:
                        result, info = divide(values[0], values[1], var1.type_)
                else:
                    result, info = divide(values[0], values[1], var1.type_)
                if result:
                    values[0] = info
                    del values[1]
                else:
                    error("ErrorDivision", info)
            return values[0]
        elif "/" in parameters:
            values = parameters.split("/")
            while len(values) > 1:
                var1 = variableExist(values[0])
                if not var1:
                    var1 = variableExist(values[1])
                    if not var1:
                        if '"' in values[0] or '"' in values[1]:
                            result, info = divide(values[0], values[1], "str")
                        elif '.' in values[0] or '.' in values[1]:
                            result, info = divide(values[0], values[1], "float")
                        else:
                            result, info = divide(values[0], values[1], "int")
                    else:
                        result, info = divide(values[0], values[1], var1.type_)
                else:
                    result, info = divide(values[0], values[1], var1.type_)
                if result:
                    values[0] = info
                    del values[1]
                else:
                    error("ErrorDivision", info)
            return values[0]
        else:
            var = variableExist(parameters)
            if not var:
                if len(parameters) > 1 and parameters[0] == '"' and parameters[-1] == '"':
                    return parameters[1:-1]
                elif is_number(parameters):
                    return parameters
                else:
                    error("ErrorConversion", "Impossible de convertir '"+parameters+"' en string")
            else:
                return var.value

class Pause():
    def __init__(self):
        self.nbParameters = 0
        self.returnValue = False
    
    def call(self):
        input()

class Enter():
    def __init__(self):
        self.nbParameters = 1
        self.returnValue = True
    
    def call(self, parameters):
        result = input(Show().call(parameters))
        return result

class CanConvert():
    def __init__(self):
        self.nbParameters = 2
        self.returnValue = True
    
    def call(self, parameters):
        value, type_ = parameters
        var = variableExist(value)
        if var:
            value = var.value
        if type_ == "int":
            try:
                int(value)
                return True
            except:
                return False
        elif type_ == "float":
            try:
                float(value)
                return True
            except:
                return False
        elif type_ == "str":
            return True
        else:
            return False

def initBasicFunctions():
    show = Show()
    pause = Pause()
    enter = Enter()
    canConvert = CanConvert()
    functions.append(["show", show])
    functions.append(["pause", pause])
    functions.append(["enter", enter])
    functions.append(["canConvert", canConvert])