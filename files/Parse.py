def parser(code):
    if " = " in code:
        if '"' in code:
            temp = code.split(" = ")
            if len(temp) == 2:
                name, value = temp
            else:
                name = temp[0]
                del temp[0]
                value = " = ".join(temp)
        else:
            name, value = code.split(" = ")
        if " " in name:
            type_, name = name.split(" ")
            return "defVariable", [type_, name, value]
        else:
            return "setVariable", [name, value]
    elif "=" in code:
        if '"' in code:
            temp = code.split("=")
            if len(temp) == 2:
                name, value = temp
            else:
                name = temp[0]
                del temp[0]
                value = "=".join(temp)
        else:
            name, value = code.split("=")
        if " " in name:
            type_, name = name.split(" ")
            return "defVariable", [type_, name, value]
        else:
            return "setVariable", [name, value]
    elif "(" in code and ")" in code:
        if '"' in code:
            temp = code.split("(")
            if len(temp) == 2:
                name, parametre = temp
            else:
                name = temp[0]
                del temp[0]
                parametre = "(".join(temp)
        else:
            name, parametre = code.split("(")
        if ", " in parametre:
            parameters = parametre[:-1].split(", ")
        else:
            parameters = [parametre[:-1]]
        return "callFunction", [name, parameters]
    else:
        return "Erreur", ["UnknownCode", "Code inconnu : "+code]
    
