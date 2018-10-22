import json

'''
file: le fichier de configuration
Permet de charger les fichiers de config
'''
def initialize(file):
    global p
    with open(file) as f:
        p=json.load(f)
