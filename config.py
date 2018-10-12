import json

def initialize():
    global p
    with open("parameter.json") as f:
        p=json.load(f)

def initializeWator():
    global p
    with open("wator.json") as f:
        p=json.load(f)
