# 
# 
# All code was designed by Edson Ricardo Junior, contact via edsonricardojr@gmail.com if you need it;
# Sorry in advance for my poor coding style!  (better[optimized] versions of this code are more than welcomed)

#=========================================================================
from classes1 import Concept, SignalBase, IndividualConcepts, Individual

from signal_base import importingSignals

from funcoes1 import randomprob, repres_chooser, map_sig_2_str, signaltocode, creating_individuals, order_of_interactions, interaction_
from funcoes1 import selection_device1, selection_device2, evolves 

from funcoes2 import creating_dict_of_concepts
from funcoes3 import generate_conceptual_phrase

from analysistools import concept_entropy1, conceptsperword, phrase_summary

from fileoperators import saving_variables, saving_variables2, delete_phrases

from stats1 import get_means_and_sdev

#from plotter import plotter_
#=========================================================================

#------------------------------------------------------------------------- 
'''
The variables that we have at our disposal are: (1) number of individuals; (2) number of base signals; (3) number of semantic objects/concepts; (4) frequency variety  or percentage into which a conceptual object appears [interobject relation]; (5) number of possible representations for each concept within each individual (we're using THREE); (6) Probabilities of each of these representations mentioned in #5; (7) Maximum Size of Each "word" (8) number or percentage of individuals duplicated/excluded in each iteration; (9) number of cycles

==>For now we've chose to let as fixed [5,6,7,8]
'''

#-------------------------------------------------------------------------
# STEP 1: CREATING A DICITONARY OF CONCEPTS
# They're of an Abstract nature, as one can see within file funcoes2.py

dictionary_of_concepts = creating_dict_of_concepts()
dofconceptoslength = len(dictionary_of_concepts)

#-------------------------------------------------------------------------
# STEP 2: CREATING THE LIST OF SIGNALS WE'RE GOING TO USE
# SEE THE FILE signal_base.py
# Where we establish which signals we're going to use

'''[RQ] Actually more of a note, here when later computing length, if comparing different phrase sizes one must normalize for the signals size being used.'''
signals=importingSignals()
signal_size_unit = 2 # pay attention to it if changing the dimension of the signals strings (e.g.: ka = 2; chirp = 5)

#-------------------------------------------------------------------------
# STEP 3: CREATING THE ITERATION 0 OF "INDIVIDUALS"
# Here we frist create the individuals, this assemble will interact and evolve in time later;
'''[RQ] It's important to note that not necessarily this concept must be attached to a biological unit, but could, for instance, be attached to a bundle of conceptual interpretation, which itself can evolve or be substituted with time'''
# creating_individuals(NumberOfIndividuals, dictionary_of_concepts, signals_, wordmaxsize)
wordsmaxsize = 4 
nofindividuals_ = 100
individuals = creating_individuals(nofindividuals_,dictionary_of_concepts,signals,wordsmaxsize)

#-------------------------------------------------------------------------
# STEP 4: CYCLES OF INTERACTIONS
# Choosing the amount of generations and no of runs for the algorithm to execute;

nofgenerations = 300
nofruns = 25

# Actual running:
for i in range(0,nofruns):

	print("***** RUN ", i," *****") # Just to show where we're at
	
	# FOR EACH RUN CREATING AN ENTIRELY NEW SET SIMULATION
	if i!=0:
		individuals = creating_individuals(nofindividuals_,dictionary_of_concepts,signals,wordsmaxsize)

	for j in range(0,nofgenerations):

		print("* GENERATION ", j," *") # Just to show where we're at
		
		# Order of Interactions for each generation
		sender,receiver = order_of_interactions(len(individuals))	
		
		for k in range(0,len(sender)):

			interaction_(sender[k],receiver[k], signals, dofconceptoslength, individuals, wordsmaxsize,j,i)
	
		# CHANGES WITHIN EACH ITERATION/GENERATION

		individuals,efficiency, mean_evol_points = evolves(individuals,signals,0.05)
			# It makes the selection and cross-overing; 

		# Making the necessary analyses:	
		entropy,names_per_concept,mean_sigun_len_per_concept=concept_entropy1(individuals,signals,signal_size_unit)
		conceptspword=conceptsperword(individuals)
		general,nottransm,yestransm = phrase_summary(len(individuals),signal_size_unit,j,i)

		# Saving all the necessary variable/values:
		saving_variables(efficiency,mean_evol_points,conceptspword,mean_sigun_len_per_concept,names_per_concept,entropy,j,i)
		saving_variables2(general,nottransm,yestransm,j,i)	
		
		# Deleting all the phrases (if too many runs the phrases folder can get in the order of gigabytes);
		delete_phrases()

get_means_and_sdev(0,nofgenerations,nofruns)
