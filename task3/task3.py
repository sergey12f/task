import json
import os
current_file = os.path.realpath(__file__)
current_directory = os.path.dirname(current_file)
with open(current_directory+'/values.json','r') as file:
	value1 = json.load(file)
with open(current_directory+'/tests.json','r') as file:
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
with open(current_directory+"/result.json","w") as file:
	json.dump(result,file,indent =2)