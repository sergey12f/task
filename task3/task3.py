import json
import sys
for x in range(len(sys.argv)):
	if 'values.json' in sys.argv[x]:
		with open(sys.argv[x],'r') as file:
			value1 = json.load(file)
	if 'tests.json' in sys.argv[x]:
		with open(sys.argv[x],'r') as file:
			tests = json.load(file)



def recursive(obj):
	if isinstance(obj, dict):
		for key, value in obj.items():
			if obj.get('id',False) != False:
				global value1
				for x in range(len(value1['values'])):
					if obj['id']==value1['values'][x]['id']:
						obj['value'] = value1['values'][x]['value']

			recursive(value)

	elif isinstance(obj, list):
		for item in obj:
			recursive(item)

		else:
			pass


print(recursive(tests))
result = json.loads(json.dumps(tests))
for x in range(len(sys.argv)):
	if 'result.json' in sys.argv[x]:
		with open(sys.argv[3],"w") as file:
			json.dump(result,file,indent =2)