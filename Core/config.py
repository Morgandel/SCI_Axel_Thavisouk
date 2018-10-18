import json

def initialize(file):
    global p
    with open(file) as f:
        p=json.load(f)
