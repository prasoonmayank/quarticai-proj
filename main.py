import json
import argparse
import datetime

parser = argparse.ArgumentParser()
parser.add_argument('file_location', help="enter json file location", type=str)
parser.add_argument('rules_txt', help="enter rules file", type=str)
args = parser.parse_args()

input_json = {}

def set_data(data, input_json):
	# The function is used to locally get the input json field
	each_entry = {}
	each_entry["value_type"] = each_input["value_type"]
	each_entry["value"] = each_input["value"]
	if(each_input["signal"] in input_json):
		input_json[each_input["signal"]].append(each_entry)
	else:
		input_json[each_input["signal"]] = []
		input_json[each_input["signal"]].append(each_entry)

with open(args.file_location) as json_file:
	# The command is used to get the input signal json file
	data = json.load(json_file)
	for each_input in data:
		set_data(each_input, input_json)

def checkcondition(case, reqd_val, given_signal):
	# The function is used to check the given value condition
	if(case["value_type"]=="Integer" and reqd_val["value_type"]=="Integer"):
		given_value = reqd_val["value"]
		newval = 'float(reqd_val["value"])'
		for given_condition in case["value_conditions"]:
			unchanged_condition = given_condition
			given_condition = given_condition.replace("value",newval)
			if(not eval(given_condition)):
				notsatisfying(case, unchanged_condition, given_signal, given_value)

	elif(case["value_type"]=="String" and reqd_val["value_type"]=="String"):
		given_value = reqd_val["value"]
		newval = 'reqd_val["value"]'
		for given_condition in case["value_conditions"]:
			unchanged_condition = given_condition
			given_condition = given_condition.replace("value", newval)
			if(not eval(given_condition)):
				notsatisfying(case, unchanged_condition, given_signal, given_value)

	elif(case["value_type"]=="Datetime" and reqd_val["value_type"]=="Datetime"):
		given_value = reqd_val["value"]
		f = "%Y-%m-%d %H:%M:%S"
		newval = 'datetime.datetime.strptime(reqd_val["value"],f)'
		for given_condition in case["value_conditions"]:
			unchanged_condition = given_condition
			given_condition = given_condition.replace("value", newval)
			if(not eval(given_condition)):
				notsatisfying(case, unchanged_condition, given_signal, given_value)

def notsatisfying(case, old_val, given_signal, given_value):
	# The function is used to print the values that dont satisfy the given output
	print("%s signal is not satisfying the condition %s for %s variable type when the value is %s\n" % (given_signal, old_val, case["value_type"], given_value))

with open(args.rules_txt) as json_file:
	# The command is used to get the input rules file
	data = json.load(json_file)
	for each_rule in data:
		given_signal = each_rule["signal"]
		reqd_vals = input_json[given_signal]
		for reqd_val in reqd_vals:
			for condition in each_rule["conditions"]:
				checkcondition(condition, reqd_val, given_signal)

