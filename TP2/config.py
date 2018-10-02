import json

def initialize():
    global p
    with open("parameter.json") as f:
        p=json.load(f)
