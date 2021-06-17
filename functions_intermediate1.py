# Practice using default parameter values
# Practice passing in named arguments
# Become familiar with Python's random module

# import random
# def randInt(min=0, max=100):
#     num = random.random()
#     return num


    import random
def rand_num(min=0, max=100):
    num = random.random()*(max-min)+min
    return round(num)
rand_num()
rand_num(max=80)
rand_num(min=7)
rand_num(min=50,max=500)



#print(randInt()) 		    # should print a random integer between 0 to 100
#print(randInt(max=50)) 	    # should print a random integer between 0 to 50
#print(randInt(min=50)) 	    # should print a random integer between 50 to 100
#print(randInt(min=50, max=500))   

# example: 

# def beCheerful(name='', repeat=2):		# set defaults when declaring the parameters
# 	print(f"good morning {name}\n" * repeat)
# beCheerful()				# output: good morning (repeated on 2 lines)
# beCheerful("tim")		        # output: good morning tim (repeated on 2 lines)
# beCheerful(name="john")			# output: good morning john (repeated on 2 lines)
# beCheerful(repeat=6)			# output: good morning (repeated on 6 lines)
# beCheerful(name="michael", repeat=5)	# output: good morning michael (repeated on 5 lines)
# # NOTE: argument order doesn't matter if we are explicit when sending in our arguments!
# beCheerful(repeat=3, name="kb")		# output: good morning kb (repeated on 3 lines)




