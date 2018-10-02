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
                bloc += 1
            elif todo == "ConditionValues":
                suivant = callMultipleCondition(info[0], info[1], info[2])
                bloc += 1
            elif todo == "EndBloc":
                if bloc == 0:
                    error("NotBlocFound", "Fin de bloc alors que aucun bloc n'est ouvert")
                else:
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
    while ligne < len(text):
        code = text[ligne]
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
                bloc += 1
            elif todo == "ConditionValues":
                suivant = callMultipleCondition(info[0], info[1], info[2])
                bloc += 1
            elif todo == "EndBloc":
                if bloc == 0:
                    error("NotBlocFound", "Fin de bloc alors que aucun bloc n'est ouvert")
                else:
                    bloc -= 1
                    suivant = True
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