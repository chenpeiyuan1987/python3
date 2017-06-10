# json编码和解码

import json;

yuan = {
    "name": "glede",
    "birthday": "1987-03-14",
    "married": True,
    "children": None,
    "sex": 1, # 1男,2女
    "height": 184,
    "weight": 136.0
};

#print(json);

jsonStr = json.dumps(yuan);
print(jsonStr);

jsonObj = json.loads(jsonStr);
print(jsonObj);
