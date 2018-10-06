def parser(code, bloc, suivant):
    if "}" in code:
        if "    "*(bloc-1)+"}" == code:
            return "EndBloc", []
        else:
            return "Erreur", ["BadEnd", "La fin du bloc est mal placé (indentation ou non seul)"]
    if code[:4*bloc] == "    "*bloc:
        code = code[4*bloc:]
    else:
        return "Erreur", ["BadIndentation", "L'indentation ne correspond pas avec le nombre de bloc ouvert"]
    if len(code) > 6 and code[:6] == "while " and code[-2:] == " {":
        if " == " in code[6:-2]:
            value1, value2 = code[6:-2].split(" == ")
            return "WhileValues", [value1, value2, "=", suivant]
        elif "==" in code[6:-2]:
            value1, value2 = code[6:-2].split("==")
            return "WhileValues", [value1, value2, "=", suivant]
        elif " <= " in code[6:-2]:
            value1, value2 = code[6:-2].split(" <= ")
            return "WhileValues", [value1, value2, "<=", suivant]
        elif "<=" in code[6:-2]:
            value1, value2 = code[6:-2].split("<=")
            return "WhileValues", [value1, value2, "<=", suivant]
        elif " < " in code[6:-2]:
            value1, value2 = code[6:-2].split(" < ")
            return "WhileValues", [value1, value2, "<", suivant]
        elif "<" in code[6:-2]:
            value1, value2 = code[6:-2].split("<")
            return "WhileValues", [value1, value2, "<", suivant]
        elif " >= " in code[6:-2]:
            value1, value2 = code[6:-2].split(" >= ")
            return "WhileValues", [value1, value2, ">=", suivant]
        elif ">=" in code[6:-2]:
            value1, value2 = code[6:-2].split(">=")
            return "WhileValues", [value1, value2, ">=", suivant]
        elif " > " in code[6:-2]:
            value1, value2 = code[6:-2].split(" > ")
            return "WhileValues", [value1, value2, ">", suivant]
        elif ">" in code[6:-2]:
            value1, value2 = code[6:-2].split(">")
            return "WhileValues", [value1, value2, ">", suivant]
        elif " != " in code[6:-2]:
            value1, value2 = code[6:-2].split(" != ")
            return "WhileValues", [value1, value2, "!=", suivant]
        elif "!=" in code[6:-2]:
            value1, value2 = code[6:-2].split("!=")
            return "WhileValues", [value1, value2, "!=", suivant]
        else:
            return "WhileValue", [code[6:-2], suivant]
    elif len(code) > 3 and code[:3] == "if "and code[-2:] == " {":
        if " == " in code[3:-2]:
            value1, value2 = code[3:-2].split(" == ")
            return "ConditionValues", [value1, value2, "=", suivant]
        elif "==" in code[3:-2]:
            value1, value2 = code[3:-2].split("==")
            return "ConditionValues", [value1, value2, "=", suivant]
        elif " < " in code[3:-2]:
            value1, value2 = code[3:-2].split(" < ")
            return "ConditionValues", [value1, value2, "<", suivant]
        elif "<" in code[3:-2]:
            value1, value2 = code[3:-2].split("<")
            return "ConditionValues", [value1, value2, "<", suivant]
        elif " <= " in code[3:-2]:
            value1, value2 = code[3:-2].split(" <= ")
            return "ConditionValues", [value1, value2, "<=", suivant]
        elif "<=" in code[3:-2]:
            value1, value2 = code[3:-2].split("<=")
            return "ConditionValues", [value1, value2, "<=", suivant]
        elif " > " in code[3:-2]:
            value1, value2 = code[3:-2].split(" > ")
            return "ConditionValues", [value1, value2, ">", suivant]
        elif ">" in code[3:-2]:
            value1, value2 = code[3:-2].split(">")
            return "ConditionValues", [value1, value2, ">", suivant]
        elif " >= " in code[3:-2]:
            value1, value2 = code[3:-2].split(" >= ")
            return "ConditionValues", [value1, value2, ">=", suivant]
        elif ">=" in code[3:-2]:
            value1, value2 = code[3:-2].split(">=")
            return "ConditionValues", [value1, value2, ">=", suivant]
        else:
            return "ConditionValue", [code[3:-2], suivant]
    elif len(code) > 5 and code[:5] == "elif "and code[-2:] == " {":
        if " == " in code[5:-2]:
            value1, value2 = code[5:-2].split(" == ")
            return "ConditionValuesELIF", [value1, value2, "=", suivant]
        elif "==" in code[5:-2]:
            value1, value2 = code[5:-2].split("==")
            return "ConditionValuesELIF", [value1, value2, "=", suivant]
        elif " < " in code[5:-2]:
            value1, value2 = code[5:-2].split(" < ")
            return "ConditionValuesELIF", [value1, value2, "<", suivant]
        elif "<" in code[5:-2]:
            value1, value2 = code[5:-2].split("<")
            return "ConditionValuesELIF", [value1, value2, "<", suivant]
        elif " <= " in code[5:-2]:
            value1, value2 = code[5:-2].split(" <= ")
            return "ConditionValuesELIF", [value1, value2, "<=", suivant]
        elif "<=" in code[5:-2]:
            value1, value2 = code[5:-2].split("<=")
            return "ConditionValuesELIF", [value1, value2, "<=", suivant]
        elif " > " in code[5:-2]:
            value1, value2 = code[5:-2].split(" > ")
            return "ConditionValuesELIF", [value1, value2, ">", suivant]
        elif ">" in code[5:-2]:
            value1, value2 = code[5:-2].split(">")
            return "ConditionValuesELIF", [value1, value2, ">", suivant]
        elif " >= " in code[5:-2]:
            value1, value2 = code[5:-2].split(" >= ")
            return "ConditionValuesELIF", [value1, value2, ">=", suivant]
        elif ">=" in code[5:-2]:
            value1, value2 = code[5:-2].split(">=")
            return "ConditionValuesELIF", [value1, value2, ">=", suivant]
        else:
            return "ConditionValueELIF", [code[5:-2], suivant]
    elif "else {" in code:
        return "ConditionELSE", [suivant]
    elif suivant:
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
    else:
        return "X", []
