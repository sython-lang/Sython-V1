from files.ListObject import variableExist, callFunction

def callSimpleCondition(value):
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
        temp = callFunction(name, parameters)
        return bool(temp)
    else:
        var = variableExist(value)
        if not var:
            return bool(value)
        else:
            return bool(var.value)

def callMultipleCondition(value1, value2, type_):
    if "(" in value1 and ")" in value1 and "(" in value2 and ")" in value2:
        if '"' in value1:
            temp = value1.split("(")
            if len(temp) == 2:
                name, parametre = temp
            else:
                name = temp[0]
                del temp[0]
                parametre = "(".join(temp)
        else:
            name, parametre = value1.split("(")
        if ", " in parametre:
            parameters = parametre[:-1].split(", ")
        else:
            parameters = [parametre[:-1]]
        temp = callFunction(name, parameters)
        value1 = temp
        if '"' in value2:
            temp = value2.split("(")
            if len(temp) == 2:
                name, parametre = temp
            else:
                name = temp[0]
                del temp[0]
                parametre = "(".join(temp)
        else:
            name, parametre = value2.split("(")
        if ", " in parametre:
            parameters = parametre[:-1].split(", ")
        else:
            parameters = [parametre[:-1]]
        temp = callFunction(name, parameters)
        value2 = temp
    if "(" in value1 and ")" in value1:
        if '"' in value1:
            temp = value1.split("(")
            if len(temp) == 2:
                name, parametre = temp
            else:
                name = temp[0]
                del temp[0]
                parametre = "(".join(temp)
        else:
            name, parametre = value1.split("(")
        if ", " in parametre:
            parameters = parametre[:-1].split(", ")
        else:
            parameters = [parametre[:-1]]
        temp = callFunction(name, parameters)
        value1 = temp
        var2 = variableExist(value2)
        if not var2:
            pass
        else:
            value2 = var2.value
    if "(" in value2 and ")" in value2:
        if '"' in value2:
            temp = value2.split("(")
            if len(temp) == 2:
                name, parametre = temp
            else:
                name = temp[0]
                del temp[0]
                parametre = "(".join(temp)
        else:
            name, parametre = value2.split("(")
        if ", " in parametre:
            parameters = parametre[:-1].split(", ")
        else:
            parameters = [parametre[:-1]]
        temp = callFunction(name, parameters)
        value2 = temp
        var1 = variableExist(value1)
        if not var1:
            pass
        else:
            value1 = var1.value
    else:
        var1 = variableExist(value1)
        var2 = variableExist(value2)
        if not var1 and not var2:
            pass
        elif not var1:
            value2 = var2.value
        elif not var2:
            value1 = var1.value
        else:
            value1 = var1.value
            value2 = var2.value
    
    if type_ == "=":
        return value1 == value2
    elif type_ == "<":
        return value1 < value2
    elif type_ == "<=":
        return value1 <= value2
    elif type_ == ">":
        return value1 > value2
    elif type_ == ">=":
        return value1 >= value2