#=========================================================================
from numpy import loadtxt, savetxt, array, zeros, linspace, std, mean, sqrt
from copy import copy, deepcopy

import os
import glob
#=========================================================================

#-------------------------------------------------------------------------
# Here we establish the function that will save the translated phrases as they are, for each run;
# To see how we create the data structure of the passing arguments I'd ask you to refer to the function interaction_ in file funcoes1.py
# There's where we use this function;

# The phrases are of the form:
# PHRASE = {0:['AMAZING'],1:['WATERMELON']}
# understood = 1 WAS UNDERSTOOD; = 0 WASN'T UNDERSTOOD;

def savephrase(location,phrase,generation_,understood):

	zeta = len(phrase)
	temp_string = []
	for i in range(0,zeta):
		temp_string.append(phrase[i][0])
	phrase_to_register =" ".join(temp_string)

	text_file=open(location,"a")
	text_file.write("%s;%s;%s;%s;\n"%(generation_,understood,phrase_to_register,(zeta-1)))
	text_file.close()
	
	
#-------------------------------------------------------------------------
# Here we're going to save all the obtained variables into files for each run and then later retrieve it all and do some stats over it;

def saving_variables(efficiency,mean_evol_points,conceptspword,mean_sigun_len_per_concept,names_per_concept,entropy,generation_,run_):

	# FOR EFFICIENCY
	location="datafiles/eff_r"+str(run_)
	eff_file=open(location,"a")
	eff_file.write("%s;%s;\n"%(generation_,efficiency))
	eff_file.close()

	# FOR MEAN EVOLUTION POINTS
	location="datafiles/mep_r"+str(run_)
	mep_file=open(location,"a")
	mep_file.write("%s;%s;\n"%(generation_,mean_evol_points))
	mep_file.close()

	# FOR THE CONCEPTS PER WORDS
	location="datafiles/cpw_r"+str(run_)
	cpw_file=open(location,"a")
	cpw_file.write("%s;%s;\n"%(generation_,conceptspword))
	cpw_file.close()

	# FOR THE MEAN SIGNAL UNITS PER CONCEPT (SUPC)
	location="datafiles/supc_r"+str(run_)
	#print(mean_sigun_len_per_concept)

	zeta = len(mean_sigun_len_per_concept)
	temp_string = [str(generation_)]	
	for i in range(0,zeta):
		temp_string.append(str(mean_sigun_len_per_concept[i]))
	phrase =";".join(temp_string)
	phrase_ = phrase +"\n"
	
	supc_file=open(location,"a")
	supc_file.write(phrase_)			
	supc_file.close()

	# FOR THE NAMES PER CONCEPT (NPC)
	location="datafiles/npc_r"+str(run_)	
	#print(names_per_concept)

	zeta = len(names_per_concept)
	temp_string = [str(generation_)]	
	for i in range(0,zeta):
		temp_string.append(str(names_per_concept[i]))
	phrase =";".join(temp_string)
	phrase_ = phrase +"\n"
	
	npc_file=open(location,"a")
	npc_file.write(phrase_)			
	npc_file.close()

	# FOR THE ENTROPY (ENT)
	location="datafiles/ent_r"+str(run_)	
	#print(entropy)

	zeta = len(entropy)
	temp_string = [str(generation_)]	
	for i in range(0,zeta):
		temp_string.append(str(entropy[i]))
	phrase =";".join(temp_string)
	phrase_ = phrase +"\n"
	
	ent_file=open(location,"a")
	ent_file.write(phrase_)			
	ent_file.close()

#-------------------------------------------------------------------------
# Here we continue tosave all the obtained variables into files for each run and then later retrieve it all and do some stats over it;

def saving_variables2(general,nottransm,yestransm,generation_,run_):

	# FOR GENERAL LENGTH
	location="datafiles/genlen_r"+str(run_)
	genlen_file=open(location,"a")
	genlen_file.write("%s;%s;\n"%(generation_,general))
	genlen_file.close()

	# FOR NOT TRANSMITTED PHRASES LENGTH
	location="datafiles/ntlen_r"+str(run_)
	ntlen_file=open(location,"a")
	ntlen_file.write("%s;%s;\n"%(generation_,nottransm))
	ntlen_file.close()

	# FOR SUCCESSF TRANSMITTED PHRASES LENGTH
	location="datafiles/ytlen_r"+str(run_)
	ytlen_file=open(location,"a")
	ytlen_file.write("%s;%s;\n"%(generation_,yestransm))
	ytlen_file.close()
	
#-------------------------------------------------------------------------
# This function is called within in the stats1.py file, in order to save the means and standard deviations and standard error of the mean 
# obtained with the function get_means_and_sdev

def saving_stats1(name_radical,array_to_save):

	location_ = "datafiles/stats/"+ name_radical
	savetxt(location_,array_to_save,fmt='%.6f',delimiter=";")

#-------------------------------------------------------------------------
# This function is called within in the fittingfile.py file, in order to save fitting parameters that we obtain;

def saving_fits(name_radical,array_to_save):

	location_ = "datafiles/fits/"+ name_radical
	savetxt(location_,array_to_save,delimiter=";")

#-------------------------------------------------------------------------
# This function is called within in main_code.py file, in order to delete all phrases already used, otherwise we'll generate folders with
# gigabytes into it;

def delete_phrases():

	files = glob.glob('datafiles/phrases/*')
	for f in files:
    		os.remove(f)
