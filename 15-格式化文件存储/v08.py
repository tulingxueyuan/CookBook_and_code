import json


data = {"name":"hahah", "age":12}


with open("t.json", 'w') as f:
    json.dump(data, f)


with open("t.json", 'r') as f:
    d = json.load( f)
    print(d)

