import json
dic1 = {'type':'dic1','username':'loleina','age':16.5}
json_dic1 = json.dumps(dic1)
print (json_dic1)
print("=======================================")
json_to_python = json.loads(json_dic1)
print (json_to_python)
print (type(json_to_python['age']))
print(json_to_python['age'])