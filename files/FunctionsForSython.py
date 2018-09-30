import sys

def setInteractif(boole = False):
    global interactif
    interactif = boole

def getInteractif():
    global interactif
    return interactif

def is_number(s):
    """ Returns True is string is a number. """
    try:
        float(s)
        return True
    except ValueError:
        return False

def error(type_, message):
    print(type_, ":", message)
    if not getInteractif():
        sys.exit()
