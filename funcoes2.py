# THIS FILE CONTAINS THE POSSIBILITIES ON HOW TO ORGANIZE CONCEPTS

# Creating a function that establishes a specified number of concepts to be utilized and also how they're going to be organized;

from classes1 import Concept
#"""
#-------------------------------------------------------------------------
# SCENARIO 1:
# Simple possibilites, the conceptual arrays comprises 7 possibilites, one could think of it as representing LOCATIONS [here, North, South, East, West] and a simple Ideia attach to the location [FOOD, DANGER]; That'd be a reasonable possibility for a group of individuals;

def creating_dict_of_concepts():

	dictionary_of_concepts={}

	for i in range(0,7):

		if i<5:
			category=1
			probability = 0.1 # Despite the fact that we're declaring explicitly the probability, pragmatically it deppends on #!!!# (see below)
			dictionary_of_concepts[i]=Concept("concept{0}".format(i),category,probability)

		else:
			category=2
			probability = 0.25 # Despite the fact that we're declaring explicitly the probability, pragmatically it deppends on #!!!# (see below)
			dictionary_of_concepts[i]=Concept("concept{0}".format(i),category,probability)
	
	return dictionary_of_concepts

# !!! # = > It depends on how we generate the conceptual phrases, thats all up to generate_conceptual_phrase() in funcoes3.py
#-------------------------------------------------------------------------
#"""

'''
#-------------------------------------------------------------------------
# SCENARIO 2/3:
# FIVE GROUPS OF CONCEPTS; WITH ARBITRARY VALUES BETWEEN THEM;
# GROUP 1(0) - 5 CONCEPTS            1/5 PROB 1/8 = 0.2*     = 0.025      probs per concept 
# GROUP 2(1) - 5 CONCEPTS            1/5 PROB 1/8   0.2*     = 0.025
# GROUP 3(2) - 3 CONCEPTS            1/5 PROB 1/4   0.2*     = 0.05
# GROUP 4(3) - 7 CONCEPTS            1/5 PROB 1/8   0.2*     = 0.025
# GROUP 5(4) - 10 CONCEPTS           1/5 PROB 1/12  0.2*     = 0.016

def creating_dict_of_concepts():

	dictionary_of_concepts={}

	for i in range(0,5):
			category = 0
			probability = 0.025 #not useful for our purposes ; might clean it later;
			dictionary_of_concepts[i]=Concept("concept{0}".format(i),category,probability)

	for i in range(5,10):
			category = 1
			probability = 0.025 #not useful for our purposes ; might clean it later;
			dictionary_of_concepts[i]=Concept("concept{0}".format(i),category,probability)

	for i in range(10,13):
			category = 2
			probability = 0.05 #not useful for our purposes ; might clean it later;
			dictionary_of_concepts[i]=Concept("concept{0}".format(i),category,probability)

	for i in range(13,20):
			category = 3
			probability = 0.025 #not useful for our purposes ; might clean it later;
			dictionary_of_concepts[i]=Concept("concept{0}".format(i),category,probability)

	for i in range(20,30):
			category = 4
			probability = 0.001 #not useful for our purposes ; might clean it later;
			dictionary_of_concepts[i]=Concept("concept{0}".format(i),category,probability)

	return dictionary_of_concepts

#-------------------------------------------------------------------------
'''
