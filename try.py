import json

"""
given_signal = ["ATL1", "ATL2", "ATL3"]
given_vartypes = ["Integer", "String", "Datetime"]
given_varconditions = ["value<=240.00", "value!='LOW'", "value<datetime.datetime.now()"]

given_conditions = ["ATL1 Integer value<=240.00", "ATL2 String value!='LOw'", "ATL3 Datetime value<datetime.datetime.now()"]

rules_json = {}

for i in range(len(given_signal)):
	
	signal_id = given_signal[i]
	vartype = given_vartypes[i]
	varcondition = given_varconditions[i]
	condition = {"value_type": vartype, "value_condition": varcondition}
	if signal_id in rules_json:
		rules_json[signal_id].append(condition)
	else:
		rules_json[signal_id] = []
		rules_json[signal_id].append(condition)

for key in rules_json:
	print(key)
"""

with open('webruleengine/checkfolder/try.json', 'r') as textfile:
	data = json.load(textfile)
	print(data["abc"])
