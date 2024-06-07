# THIS FILE CONTAINS THE DIFFERENT WAYS INTO HOW TO ORGANIZE THE GENERATION OF CONCEPTUAL PHRASES;

# This is important, for it can be of utterly simplicity or extreme complexity (think of the differences between Scenarion 1 and 2 and 3);
# There's ample space for creativity here, and we use one scenario or another by simply letting it as a comment or not (note that it must be used with a proper dictionary of concepts. See the file funcoes2.py for it) 

'''[RQ]: We could use the temporal evolution of concepts and compare their entropy with time; If their temporal series differs for the cases of Higher
probabilites of ocurrence and for those of lower probabilities of ocurrence.'''


from random import randint, random, sample, choice
from copy import deepcopy

#"""
#-------------------------------------------------------------------------
# SCENARIO 1:
# Generating a Conceptual Phrase to be signaled:

def generate_conceptual_phrase():
	
	actual_phrase_size = randint(1,2)
	
	conceptual_phrase=[]

	if actual_phrase_size == 1:
		#conceptual_phrase.append(dictionary_of_concepts[randint(0,6)])
		conceptual_phrase.append(randint(0,6))
	elif actual_phrase_size > 1:
		#conceptual_phrase.append(dictionary_of_concepts[randint(5,6)]) #!!!#
		conceptual_phrase.append(randint(5,6))		
		#conceptual_phrase.append(dictionary_of_concepts[randint(0,4)]) #!!!#
		conceptual_phrase.append(randint(0,4))
	return conceptual_phrase

#-------------------------------------------------------------------------
#"""

'''
#-------------------------------------------------------------------------
# SCENARIO 2:
# Generating a Conceptual Phrase to be signaled, complete randomly and without order:

def generate_conceptual_phrase():
	
	actual_phrase_size = randint(1,5)                        # Max Phrase Size is 5; Okay for small utterances
	
	groups_to_use = []
	conceptual_phrase=[]

	for i in range(0,actual_phrase_size):
		
		groups_to_use.append(randint(0,4)) # It can be one of the five groups

	for x in groups_to_use:
	
		if x == 0:
			conceptual_phrase.append(randint(0,4))
		elif x == 1:
			conceptual_phrase.append(randint(5,9))
		elif x == 2:
			conceptual_phrase.append(randint(10,12))
		elif x == 3:
			conceptual_phrase.append(randint(13,19))
		elif x == 4:
			conceptual_phrase.append(randint(20,29))

	return conceptual_phrase
#-------------------------------------------------------------------------
'''

'''
#-------------------------------------------------------------------------
# SCENARIO 3:
# Generating a Conceptual Phrase to be signaled, and ordering it in a simple manner;

def generate_conceptual_phrase():
	
	actual_phrase_size = randint(1,5)                        # Max Phrase Size is 5; Okay for small utterances

	groups_to_use = []
	conceptual_phrase=[]

	for i in range(0,actual_phrase_size):
		
		groups_to_use.append(randint(0,4)) #It can be one of the five groups, so we first generate the phrase by the groups which'll be used

	#print("Groups original: ",groups_to_use)

	zergrouporder = []          # These are to guarantee that the order within same groups will be the same as the original when later
	onegrouporder = []          # sorting by groups;
	secgrouporder = []
	thigrouporder = []
	forgrouporder = []	

	for x in groups_to_use:

		if x == 0:
			#temp_value = randint(0,7)
			temp_value = randint(0,4)
			#conceptual_phrase.append(deepcopy(temp_value))
			zergrouporder.append(deepcopy(temp_value))

		elif x == 1:
			#temp_value = randint(8,15)
			temp_value = randint(5,9)
			#conceptual_phrase.append(deepcopy(temp_value))
			onegrouporder.append(deepcopy(temp_value))

		elif x == 2:
			#temp_value = randint(16,19)
			temp_value = randint(10,12)
			#conceptual_phrase.append(deepcopy(temp_value))
			secgrouporder.append(deepcopy(temp_value))

		elif x == 3:
			#temp_value = randint(20,27)
			temp_value = randint(13,19)
			#conceptual_phrase.append(deepcopy(temp_value))
			thigrouporder.append(deepcopy(temp_value))

		elif x == 4:
			#temp_value = randint(28,39)
			temp_value = randint(20,29)			
			#conceptual_phrase.append(deepcopy(temp_value))
			forgrouporder.append(deepcopy(temp_value))

	#print("CPhrase: ",conceptual_phrase)
	
	# MAMBO JAMBO

	# Savint the indexes from the 4th group
	fourthgroup_indexes = []
	for i in range(0,actual_phrase_size):
		if groups_to_use[i] == 4:
			fourthgroup_indexes.append(i)
	#print("4th index:", fourthgroup_indexes)

	# Excluding all the elements of the 4th group
	new_group_to_use = deepcopy(groups_to_use)      # What to say, I like to be safe;
	if len(fourthgroup_indexes) != 0:	
		new_group_to_use = list(filter(lambda x: x!= 4, new_group_to_use))
	new_group_to_use.sort()                         # Now Sorting the Elements
	
	# Now Reinserting the values of 4 in their original Positions;
	if len(fourthgroup_indexes) != 0:
		for i in range(0,len(fourthgroup_indexes)):
			new_group_to_use.insert(fourthgroup_indexes[i], 4)	 	

	#print("new group: ",new_group_to_use)

	# NOW WE'RE GOING TO CREATE THE ACTUAL PHRASE WITH THE CONCEPT IN ORDERS THAT WE HAVE AT OUR DISPOSAL
	#conceptual_phrase_ =[]	
	index0,index1,index2,index3,index4=0,0,0,0,0

	for i in range(0,actual_phrase_size):
		if new_group_to_use[i] == 0:
			conceptual_phrase.append(zergrouporder[index0])
			index0 = index0 + 1			

		elif new_group_to_use[i] == 1:
			conceptual_phrase.append(onegrouporder[index1])
			index1= index1 + 1			

		elif new_group_to_use[i] == 2:
			conceptual_phrase.append(secgrouporder[index2])
			index2 = index2 + 1			

		elif new_group_to_use[i] == 3:
			conceptual_phrase.append(thigrouporder[index3])
			index3 = index3 + 1			

		elif new_group_to_use[i] == 4:
			conceptual_phrase.append(forgrouporder[index4])
			index4 = index4+ 1			

	#print("new Cphrase: ",conceptual_phrase_)
	return conceptual_phrase
'''
