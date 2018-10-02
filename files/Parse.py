def parser(code, bloc, suivant):
    if "}" in code:
        if bloc == 0:
            if "    "*(bloc)+"}" == code:
                return "EndBloc", []
            else:
                return "Erreur", ["BadEnd", "La fin du bloc est mal placé (indentation ou non seul)"]
        else:
            if "    "*(bloc-1)+"}" == code:
                return "EndBloc", []
            else:
                return "Erreur", ["BadEnd", "La fin du bloc est mal placé (indentation ou non seul)"]
    elif suivant:
        if code[:4*bloc] == "    "*bloc:
            code = code[4*bloc:]
        else:
            return "Erreur", ["BadIndentation", "L'indentation ne correspond pas avec le nombre de bloc ouvert"]
        if len(code) > 3 and code[:3] == "if " and code[-2:] == " {":
            if " == " in code[3:-2]:
                value1, value2 = code[3:-2].split(" == ")
                return "ConditionValues", [value1, value2, "="]
            elif "==" in code[3:-2]:
                value1, value2 = code[3:-2].split("==")
                return "ConditionValues", [value1, value2, "="]
            elif " < " in code[3:-2]:
                value1, value2 = code[3:-2].split(" < ")
                return "ConditionValues", [value1, value2, "<"]
            elif "<" in code[3:-2]:
                value1, value2 = code[3:-2].split("<")
                return "ConditionValues", [value1, value2, "<"]
            elif " <= " in code[3:-2]:
                value1, value2 = code[3:-2].split(" <= ")
                return "ConditionValues", [value1, value2, "<="]
            elif "<=" in code[3:-2]:
                value1, value2 = code[3:-2].split("<=")
                return "ConditionValues", [value1, value2, "<="]
            elif " > " in code[3:-2]:
                value1, value2 = code[3:-2].split(" > ")
                return "ConditionValues", [value1, value2, ">"]
            elif ">" in code[3:-2]:
                value1, value2 = code[3:-2].split(">")
                return "ConditionValues", [value1, value2, ">"]
            elif " >= " in code[3:-2]:
                value1, value2 = code[3:-2].split(" >= ")
                return "ConditionValues", [value1, value2, ">="]
            elif ">=" in code[3:-2]:
                value1, value2 = code[3:-2].split(">=")
                return "ConditionValues", [value1, value2, ">="]
            else:
                return "ConditionValue", [code[3:-2]]
        elif " = " in code:
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
    else:
        return "X", []
