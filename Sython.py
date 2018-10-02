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
    lastIf = False
    isBlock = False
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
            elif todo == "setVariable":
                result = setVariable(info[0], info[1])
            elif todo == "callFunction":
                result = callFunction(info[0], info[1])
            elif todo == "Erreur":
                error(info[0], info[1])
            elif todo == "ConditionValue":
                suivant = callSimpleCondition(info[0])
                lastIf = callSimpleCondition(info[0])
                bloc += 1
                isBlock = suivant
            elif todo == "ConditionValues":
                suivant = callMultipleCondition(info[0], info[1], info[2])
                lastIf = callSimpleCondition(info[0])
                bloc += 1
                isBlock = suivant
            elif todo == "ConditionValueELIF":
                if lastIf:
                    suivant = False
                else:
                    suivant = callSimpleCondition(info[0])
                    bloc += 1
                lastIf = suivant
                isBlock = suivant
            elif todo == "ConditionValuesELIF":
                if lastIf:
                    suivant = False
                else:
                    suivant = callSimpleCondition(info[0])
                    bloc += 1
                lastIf = suivant
                isBlock = suivant
            elif todo == "ConditionELSE":
                if lastIf:
                    suivant = False
                else:
                    suivant = True
                    bloc += 1
                lastIf = suivant
                isBlock = suivant
            elif todo == "EndBloc":
                if bloc == 0 and bloc:
                    error("NotBlocFound", "Fin de bloc alors que aucun bloc n'est ouvert")
                elif isBlock:
                    bloc -= 1
                    suivant = True
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
    suivant = True
    lastIf = [False] * 12
    while ligne < len(text):
        code = text[ligne]
        if len(code) > 1 and code[0] + code[1] == "//":
            pass
        elif code == "":
            pass
        else:
            #print("\n\n", code)
            todo, info = parser(code, bloc, suivant)
            #print("->", todo, ":", info,"\nLast if :",lastIf,"\nBloc :",bloc, "\nSuivant :",suivant,"\n\n")
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
                if info[2]:
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
                    if info[2]:
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