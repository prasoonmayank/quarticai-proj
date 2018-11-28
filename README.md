# Quarticai-Proj
The project is a rule engine for signal input json files. Currently the json file it considers is <a href="https://github.com/prasoonmayank/quarticai-proj/blob/master/raw_data.json">raw_data.json</a>.
You can create rules for different signal values and print the ones that dont follow the given rule. For a live demo visit: http://thebrainer.pythonanywhere.com/

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
		ATL1": [
			{
				"value_type": "Integer",
				"value_condition":	"value<=240.00"
			}
		]
	},
	{
		"ATL2": [
			{
				"value_type": "String",
				"value_condition":	"value!='LOW'"
			}
		]
	},
	{
		"ATL3": [
			{
				"value_type": "Datetime",
				"value_condition": "value<=datetime.datetime.now()"
			}
		]
	}
]

This ensures that the rules are properly formatted based on the variable_types they apply to.
The search is really fast in the current saved format, while taking much lower space.

Currently, the worst time complexity of saving the data in the format shown above is O(n x (a+b)) where n is the total number of entered values while a and b are the number of signals and number of values in each data type. We dont know the relation between a and b, and hence they cannot be discarded
The worst case time complexity of getting the signal with wrong info is O(a x c x d x e) where a is the number of signals, c is the number of datatypes for which the signal is present(3 in our case), d is the number of values in each type while e is the number of conditions for each type of variable.

The only bottleneck to the problem is that it takes time to store the input data in the form of the json field. The quering of the data is a lot faster due to the use of hashmaps.

If given more time, we can further generalize the program to consider all different types of conditions possible for the different data types other than the String, Integer or the Datetime that is currently given. Also, unlike right now where each of the data types are accessed differently, the code can be further optimized to consider cases where different variables of different types are linked as well.

Thus, if given more time, I would first try to generalize the code for all different data types. Followed by trying to consider two different variable comparision under the same rule.

## Running the web based rule engine
You can also decide to run the webengine rather than running the python file.

Visit http://thebrainer.pythonanywhere.com/ to see the rule bsed web engine or open it in your local environment following the following steps:

To run the web based rule engine, in the conda environment

git clone https://github.com/prasoonmayank/quarticai-proj

cd webruleengine

conda create -n projenv python=3.7.0

conda install --yes -file requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

Assuming the localhost server to be 8000, go to localhost:8000
There you can add the rules as required.
The format is:
signalId - the signal Id
vartype
var_condition
Eg. for integer var less than 240.00
vartype is Integer and varcondition is "value<=240.00"

For string var not equal to LOW
vartype is String and varcondition is "value!='LOW'"

For datetime var not in future
vartype is datetime and varconditino is "value<=datetime.datetime.now()"

The given code automatically computes the values as required.

## Running the code
To run the program: python main.py raw_data.json rules.json
The program has been made on Python 3.7.0

## Output of the code
The code gives the output in the following format:

"[SIGNAL_CODE] signal is not satisfying the condition [CONDITION] for [VARIABLE TYPE CONSIDERED] variable type when the value is [VARIABLE VALUE]\n"
