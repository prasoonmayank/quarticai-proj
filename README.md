# Quarticai-Proj

## Approach:
The rules file is such that one can add multiple conditions for the different data types that are present within the signal. Thus, the different rules for the signals will be put in the json. At the same time the input is also stored in a different dictionary format locally. It is stored as :

{
	"ATL1": {"String":["HIGH","LOW"...],"Integer":["13.64","3.3"...],"Datetime":["2017-05-13 06:22:35", "2017-08-20 07:25:29"...]},
	"ATL2": {"String":["HIGH","LOW"...],"Integer":["13.64","3.3"...],"Datetime":["2017-05-13 06:22:35", "2017-08-20 07:25:29"...],
	"ATL3": {"String":["HIGH","LOW"...],"Integer":["13.64","3.3"...],"Datetime":["2017-05-13 06:22:35", "2017-08-20 07:25:29"...],
	...
	...
	...
}

The rules are stored as :

[
	{
		"signal": "ATL1",
		"conditions": [
			{
				"value_type": "Integer",
				"value_conditions": [
					"value<=240.00"
				]
			}
		]
	},
	{
		"signal": "ATL2",
		"conditions": [
			{
				"value_type": "String",
				"value_conditions": [
					"value!='LOW'"
				]
			}
		]
	},
	{
		"signal": "ATL3",
		"conditions": [
			{
				"value_type": "Datetime",
				"value_conditions": [
					"value<=datetime.datetime.now()"
				]
			}
		]
	}
]

This ensures that the rules are properly formatted based on the variable_types they apply to.
The search is really fast in the current saved format, while taking much lower space.

Currently, the worst time complexity of saving the data in the format shown above is O(n x (a+b)) where n is the total number of entered values while a and b are the number of signals and number of values in each data type.
The worst case time complexity of getting the signal with wrong info is O(a x c x d x e) where a is the number of signals, c is the number of datatypes for which the signal is present(3 in our case), d is the number of values in each type while e is the number of conditions for each type of variable.

There are no bottlenecks to the program. Although, the rules need to be always in the format specified.

If given more time, we can further generalize the program to consider all different types of conditions possible for the different data types other than the String, Integer or the Datetime that is currently given. Also, unlike right now where each of the data types are accessed differently, the code can be further optimized to consider cases where different variables of different types are linked as well.

Thus, if given more time, I would first try to generalize the code for all different data types. Followed by trying to consider two different variable comparision under the same rule.

## Running the code
To run the program: python main.py raw_data.json rules.json
The program has been made on Python 3.7.0

## Output of the code
The code gives the output in the following format:

"[SIGNAL_CODE] signal is not satisfying the condition [CONDITION] for [VARIABLE TYPE CONSIDERED] variable type when the value is [VARIABLE VALUE]\n"
