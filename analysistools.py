#=========================================================================
from classes1 import Concept, SignalBase, IndividualConcepts, Individual

from random import randint, random, sample, choice, shuffle
from math import floor, log
from copy import copy, deepcopy

from funcoes1 import randomprob, repres_chooser, map_sig_2_str

import numpy as np
#=========================================================================

#-------------------------------------------------------------------------
# EFFICIENCY is obtained directly from the Evolve function (funcoes1) once that in every iteration that function will
# set evol_points to zero, so we need to get that mid function;


#-------------------------------------------------------------------------
# Here we create the function which will calculate the entropy in each generation for each concept;
# It also yields the quantity of names per concept and the average number of


def concept_entropy1(individuals,signals_,signal_size_unit):

	lofindividuals = len(individuals)
	lofconcepts = len(individuals[0].concepts2signals)

	entropy_array = {}
	namesperconceptarray = {}
	mean_sigun_array = {}
	
	for i in range(0,lofconcepts):
		
		to_sum_array = {}
		
		for j in range(0,lofindividuals):

			temp_1 = map_sig_2_str(individuals[j].concepts2signals[i].sigrep1,signals_)
			temp_2 = map_sig_2_str(individuals[j].concepts2signals[i].sigrep2,signals_)
			temp_3 = map_sig_2_str(individuals[j].concepts2signals[i].sigrep3,signals_)	

			if temp_1 in to_sum_array:
				to_sum_array[temp_1] = to_sum_array[temp_1] + (1/lofindividuals)*individuals[j].concepts2signals[i].sigrep1prob  
			else:
				to_sum_array[temp_1] = (1/lofindividuals)*individuals[j].concepts2signals[i].sigrep1prob
				
			if temp_2 in to_sum_array:
				to_sum_array[temp_2] = to_sum_array[temp_2] + (1/lofindividuals)*individuals[j].concepts2signals[i].sigrep2prob  
			else:
				to_sum_array[temp_2] = (1/lofindividuals)*individuals[j].concepts2signals[i].sigrep2prob

			if temp_3 in to_sum_array:
				to_sum_array[temp_3] = to_sum_array[temp_3] + (1/lofindividuals)*individuals[j].concepts2signals[i].sigrep3prob  
			else:
				to_sum_array[temp_3] = (1/lofindividuals)*individuals[j].concepts2signals[i].sigrep3prob
		
		#print(to_sum_array)			 # just for checking purposes
		temp_list_ = list(to_sum_array.values()) # Now we can store the dictionary VALUES into a list, for adequate operating below
		#print(temp_list_)                       # just for checking purposes
		
		# NUMBER OF NAMES / CONCEPT
		names_per_concept=len(to_sum_array)  #Simple as that
		namesperconceptarray[i]=names_per_concept #putting in the array for each concept

		# MEAN SIGNAL UNIT LENGTH
		mean_sigun_len_per_concept = signal_unit_retriever(to_sum_array,signal_size_unit) # The number is for the SIGNALUNIT SIZE;
		mean_sigun_array[i]=mean_sigun_len_per_concept

		# DE FACTO CALCULATING THE ENTROPY FOR EACH CONCEPT:
		entropy = 0
		for j in range(0,len(temp_list_)):
			entropy = entropy - temp_list_[j]*(log(temp_list_[j],2)) # Base 2
		
		entropy_array[i]=entropy			

	return entropy_array, namesperconceptarray, mean_sigun_array

#-------------------------------------------------------------------------
# This function is called within concept_entropy in order to get the various possible wordings for a concept and
# retrive the mean length in SIGNAL UNIT LENGTH for that concept
# we must pass the dictionary and the signal unit size (e.g.: ka,ke,ki => 2; CHIRP, SNORE, QUARK => 5)

def signal_unit_retriever(dictionary_of_words,sigunitsize):

	words_ = list(dictionary_of_words.keys())# Getting the KEYS from the dictionary;
	words_length = []
	zeta = len(words_)
	
	for i in range(0,zeta):
		words_length.append( (len(words_[i])/sigunitsize) )
	
	mean_words_length = sum(words_length)/zeta
	return mean_words_length

#-------------------------------------------------------------------------
# Here we have the function that allows us to evaluate what is the average meanings / per "WORD"
# So the inverse of Numbers/Concept; But averaged;

def conceptsperword(individuals):

	words = {}

	for i in range(0,len(individuals)):

		nofwords = len(individuals[i].signals2concepts) # Extracting how many different words there are per individual
		for j in individuals[i].signals2concepts:
			
			if j in words:     # if it already is added to words dict we just append the concepts attached to it;
				sizeoflist = len(individuals[i].signals2concepts[j])
				for k in range(0,sizeoflist):
					if (individuals[i].signals2concepts[j][k]) not in (words[j]): # excluding redundancy;
						words[j].append(individuals[i].signals2concepts[j][k])

			else:              # if it isn't already added to words dict we create the adequate instance for it;
				sizeoflist = len(individuals[i].signals2concepts[j])
				words[j]=[]				
				words[j].append(individuals[i].signals2concepts[j][0])				
				for k in range(1,sizeoflist):
					if (individuals[i].signals2concepts[j][k]) not in (words[j]): # excluding redundancy;
						words[j].append(individuals[i].signals2concepts[j][k])	
	#print(words)	
	
	# Averaging:
	avg_means_p_word = []
	for j in words:
		avg_means_p_word.append(len(words[j]))
	
	avrg = sum(avg_means_p_word)/len(avg_means_p_word)
	
	return avrg # Finally returning the average number of Meaning per Word;

#-------------------------------------------------------------------------
# This function is used to go through the phrases raw files (as they're were created) and return
# three informations:
# - MEAN LENGTH (IN SIGNAL UNITS) OF PHRASES BY GENERATION
# - MEAN LENGTH FOR PHRASES THAT WERE SUCCESSFULLY TRANSMITTED
# - MEAN LENGTH FOR PHRASES THAT WERE UNSUCCESSFULLY TRNASMITTED
# for this function we pass the length of INDIVIDUALS, total number of generations per run, which generation we're in


def phrase_summary(lenofindividuals,signal_unit_size,generation_,run_):
	
	per_generation_interactions = lenofindividuals*(lenofindividuals-1) # Getting the size of interactions per generation

	origin_file = "datafiles/phrases/phr_r"+str(run_)+"g"+str(generation_)
	
	# Loading the Data (they'll all have the same indexing)	
	phrases = np.genfromtxt(origin_file,dtype="str",usecols=(2),delimiter=";")
	gen = np.loadtxt(origin_file,usecols=(0),delimiter=";")                            # This is a redundant information; gomenasai
	transmitted = np.loadtxt(origin_file,usecols=(1),delimiter=";") 
	correctionfactor = np.loadtxt(origin_file,usecols=(3),delimiter=";")
	
	# Analysing for each generation:
	general_ = []
	nottransm_ = []
	yestransm_ = []

	for i in range(0,per_generation_interactions):
		temp_size = (len(phrases[i])-correctionfactor[i])/signal_unit_size
		general_.append(temp_size)		
		if transmitted[i]==1. :
			yestransm_.append(temp_size)
		else:
			nottransm_.append(temp_size)

	# Getting the means
	general = sum(general_)/len(general_)
	
	if len(nottransm_) != 0:  
		nottransm = sum(nottransm_)/len(nottransm_)
	else:
		nottransm = 0

	if len(yestransm_) != 0:
		yestransm = sum(yestransm_)/len(yestransm_)
	else:
		yestransm = 0
	
	return general,nottransm,yestransm
