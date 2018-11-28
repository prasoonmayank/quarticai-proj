
# Importing the standard libraries
import json
import datetime

def set_data(each_input, input_json):
	# The function is used to locally get the input json field
	if each_input["signal"] in input_json:
		each_entry = input_json[each_input["signal"]]
	else:
		each_entry = {}
	if(not each_input["value_type"] in each_entry):
		each_entry[each_input["value_type"]] = []
	each_entry[each_input["value_type"]].append(each_input["value"])
	input_json[each_input["signal"]] = each_entry


def checkcondition(given_signal, valtype, eachtypevalue, given_val_condition):
	# This part of the code is used to check the different values for the given conditions
	old_condition = given_val_condition
	if(valtype=="Integer"):
		val_condition = given_val_condition.replace("value","float(eachtypevalue)")
		if(not eval(val_condition)):
			return notsatisfying(given_signal, old_condition, valtype, eachtypevalue)

	elif(valtype=="String"):
		val_condition = given_val_condition.replace("value","eachtypevalue")
		if(not eval(val_condition)):
			return notsatisfying(given_signal, old_condition, valtype, eachtypevalue)

	elif(valtype=="Datetime"):
		f = "%Y-%m-%d %H:%M:%S"
		eachtypevalue = datetime.datetime.strptime(eachtypevalue,f)
		val_condition = given_val_condition.replace("value","eachtypevalue")
		if(not eval(val_condition)):
			return notsatisfying(given_signal, old_condition, valtype, eachtypevalue)

def notsatisfying(given_signal, old_condition, valtype, eachtypevalue):
	# The function is used to print the values that dont satisfy the given output
	return ("%s signal is not satisfying the condition %s for %s variable type when the value is %s<br><br>" % (given_signal, old_condition, valtype, eachtypevalue))

def get_string_result(data):

	input_json = {}
	ansstring = ""

	with open('ruleengine/static/ruleengine/raw_data.json') as json_file:
		# The command is used to get the input signal json file
		rawdata = json.load(json_file)
		for each_input in rawdata:
			set_data(each_input, input_json)
	print(type(input_json))

	for key in data:
		reqd_vals = input_json[key]
		conditions = data[key]
		for condition in conditions:
			given_valtype = condition["value_type"]
			given_value_condition = condition["value_condition"]
			for eachtypevalue in reqd_vals[given_valtype]:
				string = checkcondition(key, given_valtype, eachtypevalue, given_value_condition)
				if(string != None):
					ansstring = ansstring+"\n"+string
				# ansstring = ansstring+"\n"+checkcondition(key, given_valtype, eachtypevalue, given_value_condition)

	return ansstring

def convertIntoRules(signals, vartypes, varconditions):
	rules_json = {}

	for i in range(len(signals)):
		
		signal_id = signals[i]
		vartype = vartypes[i]
		varcondition = varconditions[i]
		condition = {"value_type": vartype, "value_condition": varcondition}
		if signal_id in rules_json:
			rules_json[signal_id].append(condition)
		else:
			rules_json[signal_id] = []
			rules_json[signal_id].append(condition)

	return rules_json
