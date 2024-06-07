# THIS FILE CONTAINS SEVERAL FUNCTIONS THAT'LL BE CALLED IN MAIN CODE

# There are some [RQ = RESEARCH QUESTION] in here as well, points noteworthy for future endeavours;

#=========================================================================
# First, importing all that's necessary to our bidding;
from random import randint, random, sample, choice, shuffle
from math import floor
from copy import copy, deepcopy

from classes1 import Concept, SignalBase, IndividualConcepts, Individual
from funcoes3 import generate_conceptual_phrase

from fileoperators import savephrase
#=========================================================================

#-------------------------------------------------------------------------
# Defining a Function which will sum 3 probs to 1:
def randomprob():
	a = random()
	b = 1-a
	c = randint(2,10)
	d = randint(1,c-1)
	e = b*(d/c)
	f = b*((c-d)/c)
	probs = [a, e, f]
	return probs

#-------------------------------------------------------------------------
# Defining a function which will choose between one of three possible representation, given their probabilities

def repres_chooser(A,B,C):

	alpha = random()
	
	if alpha <= A:
		return 1
	elif alpha <= (A+B):
		return 2
	else:
		return 3

#-------------------------------------------------------------------------
# Maps a specific signal, given in it's numerical form, to a string one; So that we can, further, create a proper dictionary of easy access and
# with all it's ambiguities to make the SIGNAL->CONCEPT CODE
def map_sig_2_str(sinal,signalbase):
	temp_string=[]
	for j in range(0,len(sinal)):
		temp_string.append(signalbase[sinal[j]].name)
	temp_string="".join(temp_string)
	return temp_string


#-------------------------------------------------------------------------
# Each individual has 2 important dictionaries attached to it. (1) The c2s [concept to signal] dictionary = which establishes how, given a conceptual
# formulation, it'll be turned into a signal; (2) s2c [signal to code] dictionary = which establishes how, given a signal, it'll be turned into a concept;
# The problem is not of direct transformation, once one realizes that there's ambiguity in it.

# THEN, This function turns a dictionary of conceptual to signal and reverses it; Of the utmost importance to our code;
 
def signaltocode(c2sdic,signals_):
	
	signal2code = {}
	temp_len=len(c2sdic)

	#For each concept in c2s we will get its signal representations and count for concepts, reversing the logic;

	for i in range(0,temp_len):
		
		# We're first getting them from the concept2signal and extracting their signaling;
		temp_1 = map_sig_2_str(c2sdic[i].sigrep1,signals_)
		temp_2 = map_sig_2_str(c2sdic[i].sigrep2,signals_)
		temp_3 = map_sig_2_str(c2sdic[i].sigrep3,signals_)

		if temp_1 in signal2code:
			signal2code[temp_1].append(i)
		else:
			signal2code[temp_1]=[i]

		if temp_2 in signal2code:
			signal2code[temp_2].append(i)
		else:
			signal2code[temp_2]=[i]

		if temp_3 in signal2code:
			signal2code[temp_3].append(i)
		else:
			signal2code[temp_3]=[i]

	return signal2code

#-------------------------------------------------------------------------
# THIS FUNCTION CREATES THE INDIVIDUALS WITH ALL THEIR DICTIONARIES, EVOLUTION POINTS AND PROBABILITES ATTACHED;
# I'd say that this is one of the 2 cores of the code;

def creating_individuals(NumberOfIndividuals, dictionary_of_concepts, signals_, wordmaxsize):

	individuals = {}

	signalslen = len(signals_) # To not recalculate it in every iteration;
	signalslen_ = signalslen - 1

	for i in range(0,NumberOfIndividuals):
	
		evolutionpoints = 0
	
		# CONCEPT TO SIGNAL ------------------
		c2s_dict={}
		for j in range(0,len(dictionary_of_concepts)):
		
			# Defining the probabilities of each represetantion ( Watashi, Boku, Ore)
			s1p,s2p,s3p = randomprob()	
		
			# Creating each Signal representation for each concept: Watashi / Boku / Ore
			lenofsignals = [randint(1,wordmaxsize), randint(1,wordmaxsize), randint(1,wordmaxsize)]	
				#  =! from signalslen, this one establishes the max use of Signals_base per concept (or in other terms, max word size)
			
			sr1,sr2,sr3 = [0]*lenofsignals[0],[0]*lenofsignals[1],[0]*lenofsignals[2]

			for k in range(0,lenofsignals[0]):
				sr1[k] = randint(0,signalslen_)
			for k in range(0,lenofsignals[1]):
				sr2[k] = randint(0,signalslen_)
			for k in range(0,lenofsignals[2]):
				sr3[k] = randint(0,signalslen_)	

			c2s_dict[j] = IndividualConcepts(dictionary_of_concepts[j].name,sr1,s1p,sr2,s2p,sr3,s3p)
	
		# SIGNAL TO CONCEPT  ------------------
		s2c = signaltocode(c2s_dict,signals_)
	
		# ACTUAL CREATION OF THE INDIVIDUAL WITH THEIR CONCEPTUAL-SIGNAL CODE
		individuals[i]=Individual("individual{0}".format(i),evolutionpoints,c2s_dict,s2c)
	
	return individuals	
	
#-------------------------------------------------------------------------
# Defining a function which will randomize individual encounters, given a # of individual;

"""[RQ] For every iteration, or cycle, of interactions, we want a random order to happen. So that certain
individuals are not preferred in detrimental to others. Certainly this aspect could be further explored
in a later moment. For instance: Individuals who have a better capacity to understand each other (if we are
talking about actual biological individuals) would have an advantage by clustering and would interact more between
themselves. That could lead to 'islands' of code-signal processing. What would be the consequences?""" 

def order_of_interactions(nofindividuals):

	# Everybody must interact with everybody (sending and receiving)
	middle_control = {}
	for i in range(0,nofindividuals):
		inner_control = sample(range(0,nofindividuals),nofindividuals)
		inner_control.remove(i)   
		
		middle_control[i]=inner_control
	
	# After all of it, we have the order from the perspective of each individual, now we must randomize how they'll take turns
	
	list_of_individuals = {}
	for i in range(0,nofindividuals):  # I could have put within the above iteration, but it's clearer this way 	
		list_of_individuals[i]=0
	sender,receiver=[],[]

	while len(list_of_individuals)>0:
	
		key1=choice(list(list_of_individuals.keys()))
		value1=copy(list_of_individuals[key1])		
		if value1 < (nofindividuals-1):
			sender.append(key1)
			receiver.append(middle_control[key1][value1])
			list_of_individuals[key1]= value1 + 1
			
		else:
			del list_of_individuals[key1]
	
	return sender,receiver


#-------------------------------------------------------------------------
# Defining a function which will make the interaction between the individuals
# I'd say that this is the second of the cores of the code;

def interaction_(senderID,receiverID, signals, dofconceptoslength,individuals, wordsmaxsize,generation_,run_): 

	# 1st Point: The Sender & Receiver are already defined by the "order_of_interactions" function.

	# 2nd Point: Now we must define what is going to be transmitted, conceptually.
                                                          
	temporary_phrase = generate_conceptual_phrase()
	c_l_of_phrase = len(temporary_phrase) #conceptual length of phrase	
	
	# 3rd Point: Now we must translate it to our signal base
	translated_phrase = {}
	
	for i in range(0,c_l_of_phrase):
		
		# Here, we must randomize which representation the individual will use [(1,2,3)?]:
		probA = individuals[senderID].concepts2signals[temporary_phrase[i]].sigrep1prob
		probB = individuals[senderID].concepts2signals[temporary_phrase[i]].sigrep2prob
		probC = individuals[senderID].concepts2signals[temporary_phrase[i]].sigrep3prob
		
		choice = repres_chooser(probA,probB,probC) # call to function that defines which one we'll use			

		if choice == 1:
			 # transformar de [1,1] ou [2] p/ "kaka" ou "ki" (respectivamente)
			temp_concept = map_sig_2_str(individuals[senderID].concepts2signals[temporary_phrase[i]].sigrep1,signals)
			translated_phrase[i]=[temp_concept]			

		elif choice == 2:
			temp_concept = map_sig_2_str(individuals[senderID].concepts2signals[temporary_phrase[i]].sigrep2,signals)
			translated_phrase[i]=[temp_concept]

		else:
			temp_concept = map_sig_2_str(individuals[senderID].concepts2signals[temporary_phrase[i]].sigrep3,signals)
			translated_phrase[i]=[temp_concept]
	
		# Here is where the magic happens, from Concept to Signal
		
	# 4th Point: Here we'll bring forth what the Receiver translates from this (must be careful with voids)

	# Basically what we want is getting the translated phrase and doing the reverse process, through the lenses of the receiver;

	what_was_understood =[] 	
	for i in range(0,len(translated_phrase)):
		#print("*****") Uncomment to see why there's a zero, it's a problem with <<<TypeError: unhashable type: 'list'>>>
		#print(translated_phrase[i])
		#print(translated_phrase[i][0])
		if translated_phrase[i][0] in individuals[receiverID].signals2concepts:
			random_int_variable = randint(0,len(individuals[receiverID].signals2concepts[translated_phrase[i][0]])-1) 
			# It's probabilistic for the receiver as well, among the possible interpretations
			temp_meaning = individuals[receiverID].signals2concepts[translated_phrase[i][0]][random_int_variable]
		else:
			temp_meaning = randint(0,dofconceptoslength) 
			# We give the chance for the receiver to give some random meaning to the word and still being able to understand it; 

		what_was_understood.append(temp_meaning)
	
	# 5th Point: Now we check if the message that was transmitted was successfully received, which implies in:
		'''# > altering the probabs for the sender (improv the one sent, decrease the ones not sent)
			this can be one thing that we analyse further as well'''				
	
	# Location for saving the phrase
	location="datafiles/phrases/phr_r"+str(run_)+"g"+str(generation_)	
	# > creating the branching necessary for analysis
			
	if temporary_phrase==what_was_understood:
		# > giving evolution points for both (the whole idea of a genetic algorithm )	
		individuals[senderID].evltn_points = individuals[senderID].evltn_points + 1
		individuals[receiverID].evltn_points = individuals[receiverID].evltn_points + 1
		# Saving the phrase
		savephrase(location,translated_phrase,generation_,1)  #To see the function check it in analysistools.py
	else:
		savephrase(location,translated_phrase,generation_,0)  #To see the function check it in analysistools.py	
		mutation(senderID,individuals,signals,wordsmaxsize,0.005)
	# MUTATION

	#mutation(senderID,individuals,signals,wordsmaxsize,0.005)	

#-------------------------------------------------------------------------
# MUTATION FUNCTION
# This functions creates what we call mutation in the Genetic Algorithm Code (important to try and avoid local maxima);

def mutation(senderID,individuals, signals,wordmaxsize, probofmutation):

	# First we establish if mutation will happen;

	temporary_value = random()
	if temporary_value <= probofmutation:

	# if it so happens to mutate, now we make it happen
		# Choosing which concept will mutate and getting the size of signals;
		beta = len(signals)-1                                  # the -1 is to use randint() below properly
		theta = len(individuals[senderID].concepts2signals)
		which_concept_will_mutate = randint(0,theta-1)	


		# Saving the probabilites:
		probab1 = deepcopy(individuals[senderID].concepts2signals[which_concept_will_mutate].sigrep1prob)
		probab2 = deepcopy(individuals[senderID].concepts2signals[which_concept_will_mutate].sigrep2prob)
		probab3 = deepcopy(individuals[senderID].concepts2signals[which_concept_will_mutate].sigrep3prob)
			
		# Defining which probability permutation will occur
		which_permut = randint(0,4)

		# Making the permutation / mutation
		if which_permut == 0:
			individuals[senderID].concepts2signals[which_concept_will_mutate].sigrep2prob = probab3		
			individuals[senderID].concepts2signals[which_concept_will_mutate].sigrep3prob = probab2
		
		elif which_permut == 1:
			individuals[senderID].concepts2signals[which_concept_will_mutate].sigrep1prob = probab3		
			individuals[senderID].concepts2signals[which_concept_will_mutate].sigrep3prob = probab1			
	
		elif which_permut == 2:
			individuals[senderID].concepts2signals[which_concept_will_mutate].sigrep1prob = probab2		
			individuals[senderID].concepts2signals[which_concept_will_mutate].sigrep2prob = probab3		
			individuals[senderID].concepts2signals[which_concept_will_mutate].sigrep3prob = probab1		

		elif which_permut == 3:
			individuals[senderID].concepts2signals[which_concept_will_mutate].sigrep1prob = probab2		
			individuals[senderID].concepts2signals[which_concept_will_mutate].sigrep2prob = probab1	

		elif which_permut ==4:
			individuals[senderID].concepts2signals[which_concept_will_mutate].sigrep1prob = probab3		
			individuals[senderID].concepts2signals[which_concept_will_mutate].sigrep2prob = probab1		
			individuals[senderID].concepts2signals[which_concept_will_mutate].sigrep3prob = probab2		

		#It is not necessary to redefine the individual signals2concepts;
		#print("!")


#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# These are some functions which are called within **evolves_() [below] **
# Their aim is to help in the selection proccess;

#------------------------------------------------------
# For those which max_min values are > cut_number:
def selection_device1(cutt_number, n_of_maxormin, tupple_list,max_or_min):

	temporary_list_ = []
	theta = len(tupple_list)
	
	# max_or_min == 0 => we're dealing with minimal values;
	# max_or_min == 1 => we're dealing with maximal values;	
	if max_or_min == 0:

		order = list(range(0,n_of_maxormin))
		shuffle(order)

		for k in range(0,cutt_number):
			temporary_list_.append(tupple_list[theta-1-order[k]][0])
		
		return temporary_list_

	if max_or_min == 1:
	
		order = list(range(0,n_of_maxormin))
		shuffle(order)

		for k in range(0,cutt_number):
			temporary_list_.append(tupple_list[order[k]][0])
		
		return temporary_list_

#------------------------------------------------------
# For those min or max value < cut_number;
def selection_device2(cutt_number, n_of_maxormin, tupple_list,max_or_min):

	temporary_list_ = []
	theta = len(tupple_list)
	
	# max_or_min == 0 => we're dealing with minimal values;
	# max_or_min == 1 => we're dealing with maximal values;	
	if max_or_min == 0:

		for i in range(0,n_of_maxormin):
			temporary_list_.append(tupple_list[theta-1-i][0]) #Appending the minimum indeces
		
		new_sorted_list = tupple_list[:(theta-n_of_maxormin)] # The new list with the minimum indeces out
		#print(temporary_list_) # was here for debugging purposes		
		#print(new_sorted_list)	# was here for debugging purposes
	
		while len(temporary_list_) < cutt_number:
			
			temp_list_for_counting_apex = []		
			for i in range(0,len(new_sorted_list)):
				temp_list_for_counting_apex.append(new_sorted_list[i][1])				
	
			#print(temp_list_for_counting_apex) # was here for debugging purposes
			new_min = min(temp_list_for_counting_apex)			
			n_of_new_min = temp_list_for_counting_apex.count(new_min)
			#print("n_new_min",n_of_new_min) # was here for debugging purposes
			
			alpha = len(temporary_list_)	
			
			if ((len(temporary_list_)+n_of_new_min) <= cutt_number):
				for k in range(0,n_of_new_min):
					temporary_list_.append(new_sorted_list[theta-1-alpha-k][0])
			
				new_sorted_list = new_sorted_list[:(theta-len(temporary_list_))]
				# print("new_sorted_list:",new_sorted_list) # was here for debugging purposes
			else:
				order = list(range(0,n_of_new_min))
				shuffle(order)
				# print("order:",order) # was here for debugging purposes
				
				for k in range(0,(cutt_number-len(temporary_list_))):
					temporary_list_.append(new_sorted_list[theta-1-alpha-order[k]][0])
		
		return temporary_list_				


		

	if max_or_min == 1:
		
		for i in range(0,n_of_maxormin):
			temporary_list_.append(tupple_list[i][0]) #Appending the maximum indeces
		
		new_sorted_list = tupple_list[n_of_maxormin:] # The new list with the maximum indeces out
		#print(temporary_list_) # was here for debugging purposes		
		#print(new_sorted_list)	# was here for debugging purposes
	
		while len(temporary_list_) < cutt_number:
			
			temp_list_for_counting_apex = []		
			for i in range(0,len(new_sorted_list)):
				temp_list_for_counting_apex.append(new_sorted_list[i][1])				
	
			#print(temp_list_for_counting_apex) # was here for debugging purposes
			new_max = max(temp_list_for_counting_apex)			
			n_of_new_max = temp_list_for_counting_apex.count(new_max)
			#print("n_new_max",n_of_new_max) # was here for debugging purposes

			if ((len(temporary_list_)+n_of_new_max) <= cutt_number):
				for k in range(0,n_of_new_max):
					temporary_list_.append(new_sorted_list[k][0])
			
				new_sorted_list = new_sorted_list[n_of_new_max:]
				#print("new_sorted_list:",new_sorted_list) # # was here for debugging purposes
			else:
				order = list(range(0,n_of_new_max))
				shuffle(order)
				#print("order:",order) # was here for debugging purposes
				
				for k in range(0,(cutt_number-len(temporary_list_))):
					temporary_list_.append(new_sorted_list[order[k]][0])
		
		return temporary_list_


#-------------------------------------------------------------------------
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# Defining a function which will make the selection of those who will pass to the next cycle and those who won't
# The first passing variable is the individuals dictionary, the second the cut which we'll use (the percentage of the total individuals
# that'll be substituted);

# This function calls the above functions selection_device1 and selection_device2; Which were separated in order to make the code clearer in it's objective; Both selection_devices functions basically deal with indexing problems and randomizing (to avoid biasing).

def evolves(individuals,signals_,percentage):
	
	zeta = len(individuals)
	beta = len(individuals[0].concepts2signals)
	beta2 = floor(beta/2)
	cut_number = floor(zeta*percentage) # getting how many individuals will'be selected;

	# First getting the index and the corresponding evltn_points;

	ind_index = []
	ind_evol_points = []
		
	for i in range(0,zeta):

		ind_index.append(i)
		ind_evol_points.append(individuals[i].evltn_points)
		# We can use this moment to already set the value of the evltn_points to zero (for the next cycle)
		individuals[i].evltn_points = 0 	
	
	# Calculating Efficiency & Mean Evol_Points;---------------------
	
	successfulinteractions = sum(ind_evol_points)/2
	efficiency = float(successfulinteractions)/(zeta*(zeta-1))	
	#print(efficiency) # for Checking purposes

	mean_evol_points = sum(ind_evol_points)/(len(ind_evol_points))
	#----------------------------------------------------------------


	tupled_list = list(zip(ind_index,ind_evol_points))	
	sorted_list = sorted(tupled_list, key = lambda t: t[1], reverse= True) #Descending order, that's why reverse=True

	# HERE WE HAVE A PROBLEM: I can't just choose the first and the last individuals from this sorted list; If we proceeded like that
        # we'd have created a bias towards the first index and against the last ones (for similar evol_points); So once ordered we must randomize,
	# among similar values, which ones will replicate and which ones will be excluded;
	
	# Getting the max and min values
	max_value = sorted_list[0][1]	         # I could have called max() and min() but I guess? it's faster this way? 
	min_value = sorted_list[zeta-1][1]	 # Not that the code is fully optimized, but at least we try;

	# Counting how many of the max and min values occur (I don't necessarily need the indeces now)
	n_of_max = ind_evol_points.count(max_value)
	n_of_min = ind_evol_points.count(min_value)
	

	#-----------------------------------------------
	# Now actually doing the selection:
	# In the proccess we'll call some auxiliary functions designed specifically for this (selectiondevice 1 & 2)

	those_out = []	
	willduplicate = []
	
	if (n_of_max == cut_number) and (n_of_min == cut_number):
		for i in range(0,cut_number):
			willduplicate.append(sorted_list[i][0])
			those_out.append(sorted_list[zeta-1-i][0])	
	
	elif (n_of_max == cut_number) and (n_of_min != cut_number):
		for i in range(0,cut_number):
			willduplicate.append(sorted_list[i][0])
		if (n_of_min>cut_number):
			those_out=selection_device1(cut_number, n_of_min, sorted_list,0)	
		else:
			those_out=selection_device2(cut_number, n_of_min, sorted_list,0)

	elif (n_of_max != cut_number) and (n_of_min == cut_number):
		for i in range(0,cut_number):
			those_out.append(sorted_list[zeta-1-i][0])
		if (n_of_max > cut_number):
			willduplicate=selection_device1(cut_number,n_of_max,sorted_list,1)
		else:
			willduplicate=selection_device2(cut_number,n_of_max,sorted_list,1)

	elif (n_of_max > cut_number) and (n_of_min != cut_number):
		willduplicate = selection_device1(cut_number,n_of_max,sorted_list,1)
		if (n_of_min>cut_number):
			those_out=selection_device1(cut_number, n_of_min, sorted_list,0)	
		else:
			those_out=selection_device2(cut_number, n_of_min, sorted_list,0)

	elif (n_of_max < cut_number) and (n_of_min != cut_number):
		willduplicate = selection_device2(cut_number,n_of_max,sorted_list,1)
		if (n_of_min>cut_number):
			those_out=selection_device1(cut_number, n_of_min, sorted_list,0)	
		else:
			those_out=selection_device2(cut_number, n_of_min, sorted_list,0)	
	
	#print(those_out)
	#print(willduplicate)

	# CROSS-OVER and subsequently substitution into the individuals dictionary

	for i in range(0,cut_number):
		
		crossoveringlist = sorted(sample(list(range(0,beta)),beta2))	
		#print(crossoveringlist)	just for checking purposes
		
		for j in range(0,beta2):
			individuals[those_out[i]].concepts2signals[crossoveringlist[j]] = individuals[willduplicate[i]].concepts2signals[crossoveringlist[j]]		

		# Reestablishing the interpretation capacity of the thouse_out individuals		
		individuals[those_out[i]].signals2concepts = signaltocode(individuals[those_out[i]].concepts2signals,signals_)		
	
	return individuals, efficiency, mean_evol_points
