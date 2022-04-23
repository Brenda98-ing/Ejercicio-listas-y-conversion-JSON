
import json

lista= {
                "target" : {
                    "code": "hola",
                    "name": "hola",
                    "pice" : "hola"
                },
                "tpGrouper_food": "hola"
                
            }
lista2 = {
                "target" : {
                    "code": "hola",
                    "name": "hola",
                    "pice" : "hola"
                },
                "tpGrouper_food": "hola"
                
            }


resultado=[]
resultado.append(lista)
resultado.append(lista2)
print(lista)
response = json.dumps(lista)
print("..............................")
print(resultado)
#print(response['target']['name'])