from files.Parse import parser
from files.Variable import createVariable, setVariable
from files.ListObject import callVariable, callFunction
from files.functionsSython.BasicFunction import initBasicFunctions
import sys

def interpreter():
    code = ""
    while True:
        code = input(">>> ")
        if len(code) > 1 and code[0] + code[1] == "//":
            pass
        elif code == "":
            pass
        else:
            todo, info = parser(code)
            if todo == "defVariable":
                result = createVariable(info[0], info[1], info[2])
            elif todo == "setVariable":
                result = setVariable(info[0], info[1])
            elif todo == "callFunction":
                result = callFunction(info[0], info[1])
            elif todo == "Erreur":
                result = info
            if result is not None:
                print(result)
                del result

def interpreter_on_script(text):
    code = ""
    ligne = 0
    while ligne < len(text):
        code = text[ligne]
        if len(code) > 1 and code[0] + code[1] == "//":
            pass
        elif code == "":
            pass
        else:
            todo, info = parser(code)
            if todo == "defVariable":
                result = createVariable(info[0], info[1], info[2])
            elif todo == "setVariable":
                result = setVariable(info[0], info[1])
            elif todo == "callFunction":
                result = callFunction(info[0], info[1])
            elif todo == "Erreur":
                result = info
            if result is not None:
                print(result)
                del result
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