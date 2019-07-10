from datetime import datetime

def log(message):
	""" Logs ouput

		Args:
			message (str): Message information that will be logged

		Results:
			out.log is appended to with new log message
	"""
	with open('out.log', 'a+') as f:
		f.write(message + '\n' + "-"*50 + '\n')

def error_log(message):
	""" Logs error ouput

		Args:
			message (str): Message information that will be logged

		Results:
			error.log is appended to with new log message
	"""
	with open('error.log', 'a+') as f:
		f.write(message + '\n' + "-"*50 + '\n')

def customer_parse(query):

	""" This function parses customers by which state they are in

		Args:
			query (list): List of customers information

		Returns:
			tx (List): Cusomters in Texas
			non_tx (List): Cusomters in not in Texas
	"""
	tx = []
	non_tx = []

	for row in query:
		new_customer = Customer(row[0],row[1],row[2],row[3],\
							row[4],row[5],row[6],row[7], row[8])

		#Seperates Texans and Non - # Texans into their own list
		if(new_customer.state == "TX"):
			tx.append(new_customer)
		else:
			non_tx.append(new_customer)

	return tx, non_tx

def print_customer_list(cust_list):
	""" Prints customers information to terminal

		Args:
			cust_list (List): Customers objects from Texas/Not Texas

		Returns:
			results (str): string of contacts information
	"""
	str=''
	for item in cust_list:
		str += item.__str__()

	return str

def object_sanitizer(obj):
    """ Recurssively converts objects into a dictionary

        Args:
            obj ():

        Returns:
            result (dict):
    """

    if not  hasattr(obj,"__dict__"):
        return obj
    result = {}
    for key, val in obj.__dict__.items():

        if key.startswith("_"):
            continue

        element = []
        if isinstance(val, list):
            for item in val:
                element.append(object_sanitizer(item))
        else:
            element = object_sanitizer(val)

        result[key] = element
    return result
