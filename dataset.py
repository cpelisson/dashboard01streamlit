import json 
import pandas as pd

file = open('dados/vendas.json')#abrir o arquivo em json
data = json.load(file)#transformar ele em database

df = pd.DataFrame.from_dict(data) #usando pandas transformou em dataframes




file.close()
