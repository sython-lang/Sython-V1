from files.ListObject import variableExist

def callSimpleCondition(value):
    var = variableExist(value)
    if not var:
        return bool(value)
    else:
        return bool(var.value)

def callMultipleCondition(value1, value2, type_):
    var1 = variableExist(value1)
    var2 = variableExist(value2)
    if not var1 and not var2:
        pass
    elif not var1:
        value2 = var2.value
        if var2.type_ == "int":
            try:
                value1 = int(value1)
            except:
                return False
        elif var2.type_ == "float":
            try:
                value1 = float(value1)
            except:
                return False
    elif not var2:
        value1 = var1.value
        if var1.type_ == "int":
            try:
                value2 = int(value2)
            except:
                return False
        elif var1.type_ == "float":
            try:
                value2 = float(value2)
            except:
                return False
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