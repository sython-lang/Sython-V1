from files.ListObject import variables, variableExist

def add(value1, value2, type_):
    var1 = variableExist(value1)
    var2 = variableExist(value2)
    if not var1 and not var2:
        if type_ == "int":
            try:
                value = int(value1) + int(value2)
                value = int(value)
                return True, value
            except:
                return False, "Impossible de convertir '"+value1+"' et/ou '"+value2+"' en entier"
        elif type_ == "float":
            try:
                value = float(value1) + float(value2)
                value = float(value)
                return True, value
            except:
                return False, "Impossible de convertir '"+value1+"' et/ou '"+value2+"' en flottant"
        elif type_ == "str":
            if len(value1) > 1 and len(value2) > 1 and value1[0] == '"' and value1[-1] == '"' and value2[0] == '"' and value2[-1] == '"':
                value1 = value1[1:-1]
                value2 = value2[1:-1]
                return True, value1+value2
            elif len(value1) > 1 and value1[0] == '"' and value1[-1] == '"':
                value1 = value1[1:-1]
                return True, value1+value2
            elif len(value2) > 1 and value2[0] == '"' and value2[-1] == '"':
                value2 = value2[1:-1]
                return True, value1+value2
            else:
                return True, value1+value2
    elif not var1:
        if type_ == "int" and var2.type_ == "int":
            try:
                value = int(value1) + var2.value
                value = int(value)
                return True, value
            except:
                return False, "Impossible de convertir '"+value1+"' en entier"
        elif type_ == "float" and var2.type_ == "float":
            try:
                value = float(value1) + var2.value
                value = float(value)
                return True, value
            except:
                return False, "Impossible de convertir '"+value1+"' en flottant"
        elif type_ == "str" and var2.type_ == "str":
            if len(value1) > 1 and value1[0] == '"' and value1[-1] == '"':
                value1 = value1[1:-1]
                value2 = str(var2.value)
                return True, value1+value2
            else:
                value2 = str(var2.value)
                return True, value1+value2
        else:
            return False, "Impossible de convertir la variable '"+ var2.name+"' en '"+type_+"'"
    elif not var2:
        if type_ == "int" and var1.type_ == "int":
            try:
                value = int(value2) + var1.value
                value = int(value)
                return True, value
            except:
                return False, "Impossible de convertir '"+value2+"' en entier"
        elif type_ == "float" and var1.type_ == "float":
            try:
                value = float(value2) + var1.value
                value = float(value)
                return True, value
            except:
                return False, "Impossible de convertir '"+value2+"' en flottant"
        elif type_ == "str" and var1.type_ == "str":
            if len(value2) > 1 and value2[0] == '"' and value2[-1] == '"':
                value1 = value2[1:-1]
                value2 = str(var1.value)
                return True, value2+value1
            else:
                value2 = str(var1.value)
                return True, value2+value1
        else:
            return False, "Impossible de convertir la variable '"+ var1.name+"' en '"+type_+"'"
    else:

        if type_ == "int" and var1.type_ == "int" and var2.type_ == "int":
            value = var2.value + var1.value
            value = int(value)
            return True, value
        elif type_ == "float" and var1.type_ == "float" and var2.type_ == "float":
            value = var2.value + var1.value
            value = float(value)
            return True, value
        elif type_ == "str" and var1.type_ == "str" and var2.type_ == "str":
            value1 = str(var2.value)
            value2 = str(var1.value)
            return True, value2+value1
        else:
            return False, "Impossible de convertir la variable '"+ var1.name+"' et/ou '"+var2.name+"' en '"+type_+"'"
    
def multiply(value1, value2, type_):
    var1 = variableExist(value1)
    var2 = variableExist(value2)
    if not var1 and not var2:
        if type_ == "int":
            try:
                value = int(value1) * int(value2)
                value = int(value)
                return True, value
            except:
                return False, "Impossible de convertir '"+value1+"' et/ou '"+value2+"' en entier"
        elif type_ == "float":
            try:
                value = float(value1) * float(value2)
                value = float(value)
                return True, value
            except:
                return False, "Impossible de convertir '"+value1+"' et/ou '"+value2+"' en flottant"
        elif type_ == "str":
            return False, "Impossible de multiplier des strings"
    elif not var1:
        if type_ == "int" and var2.type_ == "int":
            try:
                value = int(value1) * var2.value
                value = int(value)
                return True, value
            except:
                return False, "Impossible de convertir '"+value1+"' en entier"
        elif type_ == "float" and var2.type_ == "float":
            try:
                value = float(value1) * var2.value
                value = float(value)
                return True, value
            except:
                return False, "Impossible de convertir '"+value1+"' en flottant"
        elif type_ == "str" and var2.type_ == "str":
            return False, "Impossible de multiplier des strings"
        else:
            return False, "Impossible de convertir la variable '"+ var2.name+"' en '"+type_+"'"
    elif not var2:
        if type_ == "int" and var1.type_ == "int":
            try:
                value = int(value2) * var1.value
                value = int(value)
                return True, value
            except:
                return False, "Impossible de convertir '"+value2+"' en entier"
        elif type_ == "float" and var1.type_ == "float":
            try:
                value = float(value2) * var1.value
                value = float(value)
                return True, value
            except:
                return False, "Impossible de convertir '"+value2+"' en flottant"
        elif type_ == "str" and var1.type_ == "str":
            return False, "Impossible de multiplier des strings"
        else:
            return False, "Impossible de convertir la variable '"+ var1.name+"' en '"+type_+"'"
    else:

        if type_ == "int" and var1.type_ == "int" and var2.type_ == "int":
            value = var2.value * var1.value
            value = int(value)
            return True, value
        elif type_ == "float" and var1.type_ == "float" and var2.type_ == "float":
            value = var2.value * var1.value
            value = float(value)
            return True, value
        elif type_ == "str" and var1.type_ == "str" and var2.type_ == "str":
            return False, "Impossible de multiplier des strings"
        else:
            return False, "Impossible de convertir la variable '"+ var1.name+"' et/ou '"+var2.name+"' en '"+type_+"'"

def divide(value1, value2, type_):
    var1 = variableExist(value1)
    var2 = variableExist(value2)
    if not var1 and not var2:
        if type_ == "int":
            try:
                value = int(value1) / int(value2)
                try:
                    value = int(value)
                    return True, value
                except:
                    return False, "Le résultat n'est pas un entier"
            except:
                return False, "Impossible de convertir '"+value1+"' et/ou '"+value2+"' en entier"
        elif type_ == "float":
            try:
                value = float(value1) / float(value2)
                value = float(value)
                return True, value
            except:
                return False, "Impossible de convertir '"+value1+"' et/ou '"+value2+"' en flottant"
        elif type_ == "str":
            return False, "Impossible de diviser des strings"
    elif not var1:
        if type_ == "int" and var2.type_ == "int":
            try:
                value = int(value1) / var2.value
                try:
                    value = int(value)
                    return True, value
                except:
                    return False, "Le résultat n'est pas un entier"
            except:
                return False, "Impossible de convertir '"+value1+"' en entier"
        elif type_ == "float" and var2.type_ == "float":
            try:
                value = float(value1) / var2.value
                value = float(value)
                return True, value
            except:
                return False, "Impossible de convertir '"+value1+"' en flottant"
        elif type_ == "str" and var2.type_ == "str":
            return False, "Impossible de diviser des strings"
        else:
            return False, "Impossible de convertir la variable '"+ var2.name+"' en '"+type_+"'"
    elif not var2:
        if type_ == "int" and var1.type_ == "int":
            try:
                value = var1.value / int(value2)
                try:
                    value = int(value)
                    return True, value
                except:
                    return False, "Le résultat n'est pas un entier"
            except:
                return False, "Impossible de convertir '"+value2+"' en entier"
        elif type_ == "float" and var1.type_ == "float":
            try:
                value = var1.value / float(value2)
                value = float(value)
                return True, value
            except:
                return False, "Impossible de convertir '"+value2+"' en flottant"
        elif type_ == "str" and var1.type_ == "str":
            return False, "Impossible de diviser des strings"
        else:
            return False, "Impossible de convertir la variable '"+ var1.name+"' en '"+type_+"'"
    else:

        if type_ == "int" and var1.type_ == "int" and var2.type_ == "int":
            value = var1.value / var2.value
            try:
                value = int(value)
                return True, value
            except:
                return False, "Le résultat n'est pas un entier"
            return True, value
        elif type_ == "float" and var1.type_ == "float" and var2.type_ == "float":
            value = var1.value / var2.value
            value = float(value)
            return True, value
        elif type_ == "str" and var1.type_ == "str" and var2.type_ == "str":
            return False, "Impossible de diviser des strings"
        else:
            return False, "Impossible de convertir la variable '"+ var1.name+"' et/ou '"+var2.name+"' en '"+type_+"'"

def subtract(value1, value2, type_):
    var1 = variableExist(value1)
    var2 = variableExist(value2)
    if not var1 and not var2:
        if type_ == "int":
            try:
                value = int(value1) - int(value2)
                value = int(value)
                return True, value
            except:
                return False, "Impossible de convertir '"+value1+"' et/ou '"+value2+"' en entier"
        elif type_ == "float":
            try:
                value = float(value1) - float(value2)
                value = float(value)
                return True, value
            except:
                return False, "Impossible de convertir '"+value1+"' et/ou '"+value2+"' en flottant"
        elif type_ == "str":
            return False, "Impossible de soustraire des strings"
    elif not var1:
        if type_ == "int" and var2.type_ == "int":
            try:
                value = int(value1) - var2.value
                value = int(value)
                return True, value
            except:
                return False, "Impossible de convertir '"+value1+"' en entier"
        elif type_ == "float" and var2.type_ == "float":
            try:
                value = float(value1) - var2.value
                value = float(value)
                return True, value
            except:
                return False, "Impossible de convertir '"+value1+"' en flottant"
        elif type_ == "str" and var2.type_ == "str":
            return False, "Impossible de soustraire des strings"
        else:
            return False, "Impossible de convertir la variable '"+ var2.name+"' en '"+type_+"'"
    elif not var2:
        if type_ == "int" and var1.type_ == "int":
            try:
                value = var1.value - int(value2)
                value = int(value)
                return True, value
            except:
                return False, "Impossible de convertir '"+value2+"' en entier"
        elif type_ == "float" and var1.type_ == "float":
            try:
                value = var1.value - float(value2)
                value = float(value)
                return True, value
            except:
                return False, "Impossible de convertir '"+value2+"' en flottant"
        elif type_ == "str" and var1.type_ == "str":
            return False, "Impossible de soustraire des strings"
        else:
            return False, "Impossible de convertir la variable '"+ var1.name+"' en '"+type_+"'"
    else:

        if type_ == "int" and var1.type_ == "int" and var2.type_ == "int":
            value = var1.value - var2.value
            value = int(value)
            return True, value
        elif type_ == "float" and var1.type_ == "float" and var2.type_ == "float":
            value = var1.value - var2.value
            value = float(value)
            return True, value
        elif type_ == "str" and var1.type_ == "str" and var2.type_ == "str":
            return False, "Impossible de soustraire des strings"
        else:
            return False, "Impossible de convertir la variable '"+ var1.name+"' et/ou '"+var2.name+"' en '"+type_+"'"