import json

d = {'course_name':'python','fess':15000}
f = json.dumps(d)
print(f)
print(type(f))


print("Converting json data into python")

x = '{"cname":"python","fees":12200,"duration":"2 months"}'
y = json.loads(x)
print(type(y))
print(y)