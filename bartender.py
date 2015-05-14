

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

def ask():

	print "Welcome to the coolest command line bar"
	print "What kind of drink can I pour for you? "
	#answer = raw_input("What kind of drink would you like?")	

	questions = {
	    "strong": "Do ye like yer drinks strong? If so, say 'strong' ",
	    "salty": "Do ye like it with a salty tang? If so, say 'salty' ",
	    "bitter": "Are ye a lubber who likes it bitter? If so, say 'bitter' ",
	    "sweet": "Would ye like a bit of sweetness with yer poison? If so, say 'sweet' ",
	    "fruity": "Are ye one for a fruity finish? If so, say 'fruity' "
	}

	for key in questions:
		print questions[key]


	drink_order = {}	
	drink_order['customer_order'] = raw_input("So, what will ye have?")
	#print drink_order

	if drink_order['customer_order'] == "strong": 
		print "You entered strong"
	elif drink_order['customer_order'] == "salty": 
		print "You entered salty"
	elif drink_order['customer_order'] == "bitter": 
		print "You entered bitter"
	elif drink_order['customer_order'] == "sweet": 
		print "You entered sweet"
	elif drink_order['customer_order'] == "fruity": 
		print "You entered fruity"
	else: 
		print "Please enter your order again."
		ask()

# I guess I am trying to get to this, where one of them is true and the rest is false??
	# drink_order = {
	# 	"strong": False, 
	# 	"salty": True, 
	# 	"bitter": False, 
	# 	"sweet": False, 
	# 	"fruity": False
	# }

	

ask()





