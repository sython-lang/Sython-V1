from files.Parse import parser
from files.Variable import createVariable, setVariable
from files.ListObject import callVariable, callFunction
from files.functionsSython.BasicFunction import initBasicFunctions
from files.FunctionsForSython import error, setInteractif
from files.Conditions import callSimpleCondition, callMultipleCondition
import sys

def interpreter():
    setInteractif(True)
    code = ""
    bloc = 0
    suivant = True
    lastIf = [False] * 12
    while True:
        code = input(">>> ")
        if len(code) > 1 and code[0] + code[1] == "//":
            pass
        elif code == "":
            pass
        else:
            todo, info = parser(code, bloc, suivant)
            if todo == "defVariable":
                result = createVariable(info[0], info[1], info[2])
                if suivant:
                    lastIf[bloc] = False
            elif todo == "setVariable":
                result = setVariable(info[0], info[1])
                if suivant:
                    lastIf[bloc] = False
            elif todo == "callFunction":
                result = callFunction(info[0], info[1])
                if suivant:
                    lastIf[bloc] = False
            elif todo == "Erreur":
                error(info[0], info[1])
                if suivant:
                    lastIf[bloc] = False
            elif todo == "ConditionValue":
                if info[1]:
                    suivant = callSimpleCondition(info[0])
                    lastIf[bloc] = suivant
                bloc += 1
            elif todo == "ConditionValues":
                if info[3]:
                    suivant = callMultipleCondition(info[0], info[1], info[2])
                    lastIf[bloc] = suivant
                bloc += 1
            elif todo == "ConditionValueELIF":
                if lastIf[bloc]:
                    suivant = False
                else:
                    if info[1]:
                        suivant = callSimpleCondition(info[0])
                        lastIf[bloc] = suivant
                bloc += 1
            elif todo == "ConditionValuesELIF":
                if lastIf[bloc]:
                    suivant = False
                else:
                    if info[2]:
                        suivant = callMultipleCondition(info[0], info[1], info[2])
                        lastIf[bloc] = suivant
                bloc += 1
            elif todo == "ConditionELSE":
                if lastIf[bloc]:
                    suivant = False
                else:
                    if bloc - 1 >= 0:
                        if info[0] and lastIf[bloc-1]:
                            suivant = True
                        else:
                            suivant = False
                    else:
                        if info[0]:
                            suivant = True
                        else:
                            suivant = False
                bloc += 1
                lastIf[bloc] = False
            elif todo == "EndBloc":
                bloc -= 1
                if bloc < 0:
                    bloc = 0
                suivant = True
            else:
                if suivant:
                    lastIf[bloc] = False
            try:
                if result is not None:
                    print(result)
                    del result
            except:
                pass

def interpreter_on_script(text):
    setInteractif(False)
    code = ""
    ligne = 0
    bloc = 0
    suivant = [False] * 12
    suivant[0] = True
    lastIf = [False] * 12
    While = [""] * 12
    while ligne < len(text):
        code = text[ligne]
        #print("\n\n",code)
        #print("Bloc ->", bloc, ": Suivant -> ", suivant,"\n\n")
        if len(code) > 1 and code[0] + code[1] == "//":
            pass
        elif code == "":
            pass
        else:
            todo, info = parser(code, bloc, suivant[bloc])
            if todo == "defVariable":
                result = createVariable(info[0], info[1], info[2])
                if suivant:
                    lastIf[bloc] = False
            elif todo == "setVariable":
                result = setVariable(info[0], info[1])
                if suivant:
                    lastIf[bloc] = False
            elif todo == "callFunction":
                result = callFunction(info[0], info[1])
                if suivant:
                    lastIf[bloc] = False
            elif todo == "Erreur":
                error(info[0], info[1])
                if suivant:
                    lastIf[bloc] = False
            elif todo == "WhileValue":
                bloc += 1
                if bloc > 0 and suivant[bloc-1]:
                    suivant[bloc] = callSimpleCondition(info[0])
                    if suivant[bloc]:
                        While[bloc] = ligne
                    else:
                        While[bloc] = ""
                elif suivant[bloc]:
                    suivant[bloc] = callSimpleCondition(info[0])
                    if suivant[bloc]:
                        While[bloc] = ligne
                    else:
                        While[bloc] = ""
            elif todo == "WhileValues":
                bloc += 1
                if bloc > 0 and suivant[bloc-1]:
                    suivant[bloc] = callMultipleCondition(info[0], info[1], info[2])
                    if suivant[bloc]:
                        While[bloc] = ligne
                    else:
                        While[bloc] = ""
                elif suivant[bloc]:
                    suivant[bloc] = callMultipleCondition(info[0], info[1], info[2])
                    if suivant[bloc]:
                        While[bloc] = ligne
                    else:
                        While[bloc] = ""
            elif todo == "ConditionValue":
                bloc += 1
                if bloc > 0 and suivant[bloc-1]:
                    suivant[bloc] = callSimpleCondition(info[0])
                    lastIf[bloc] = suivant[bloc]
                elif suivant[bloc]:
                    suivant[bloc] = callSimpleCondition(info[0])
                    lastIf[bloc] = suivant[bloc]
            elif todo == "ConditionValues":
                bloc += 1
                if bloc > 0 and suivant[bloc-1]:
                    suivant[bloc] = callMultipleCondition(info[0], info[1], info[2])
                    lastIf[bloc] = suivant[bloc]
                elif suivant[bloc]:
                    suivant[bloc] = callMultipleCondition(info[0], info[1], info[2])
                    lastIf[bloc] = suivant[bloc]
            elif todo == "ConditionValueELIF":
                bloc += 1
                if lastIf[bloc]:
                    suivant[bloc] = False
                else:
                    if bloc > 0 and suivant[bloc-1]:
                        suivant[bloc] = callSimpleCondition(info[0])
                        lastIf[bloc] = suivant[bloc]
                    elif suivant[bloc]:
                        suivant[bloc] = callSimpleCondition(info[0])
                        lastIf[bloc] = suivant[bloc]
            elif todo == "ConditionValuesELIF":
                bloc += 1
                if lastIf[bloc]:
                    suivant[bloc] = False
                else:
                    if bloc > 0 and suivant[bloc-1]:
                        suivant[bloc] = callMultipleCondition(info[0], info[1], info[2])
                        lastIf[bloc] = suivant[bloc]
                    elif suivant[bloc]:
                        suivant[bloc] = callMultipleCondition(info[0], info[1], info[2])
                        lastIf[bloc] = suivant[bloc]
            elif todo == "ConditionELSE":
                bloc += 1
                if lastIf[bloc]:
                    suivant[bloc] = False
                else:
                    if bloc - 1 >= 0:
                        if suivant[bloc - 1] and lastIf[bloc-1]:
                            suivant[bloc] = True
                        else:
                            suivant[bloc] = False
                    else:
                        if suivant[bloc]:
                            suivant[bloc] = True
                        else:
                            suivant[bloc] = False
                lastIf[bloc] = False
            elif todo == "EndBloc":
                bloc -= 1
                if bloc < 0:
                    bloc = 0
                if While[bloc+1] != "":
                    ligne = While[bloc+1] - 1
                    While[bloc+1] = ""
                elif bloc == 0:
                    suivant[bloc] = True
            else:
                if suivant[bloc]:
                    lastIf[bloc] = False
            try:
                if result is not None:
                    print(result)
                    del result
            except:
                pass
        ligne += 1

if __name__ == "__main__":
    initBasicFunctions()
    arguments = []
    try:
        arguments = sys.argv[1:]
        script = arguments[0]
        if ".sy" in script:
            with open(script, 'r') as code_:
                interpreter_on_script(code_.read().split("\n"))
        else:
            print("ERREUR : Votre programme n'a pas la bonne extention (.sy)")
            input()
    except IndexError:
        pass

    if not arguments:
        interpreter()