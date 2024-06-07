# THIS FILE CONTAINS THE TOOLS TO EXTRACT MEANS, STD DEVIATIONS AND STANDARD ERRORS OF THE MEAN
# The first step into carrying the actual statistics later;

#=========================================================================
from numpy import loadtxt, array, zeros, linspace, std, mean, sqrt
from pylab import scatter,plot,show,xlim,ylim,xlabel,ylabel,legend, title, figure
from copy import copy, deepcopy
from scipy import stats

from fileoperators import saving_stats1
#=========================================================================
#-------------------------------------------------------------------------
# First  we just want to gather the data and calculate it's mean, standard error and standard deviation
# We just pass three arguments: scenario = 0 or 1 (0 = scenario 1; 1 = scenario 2/3);
#                               nogens = the number of generations performed for each run
#                               nofruns = the number of runs performed;

def get_means_and_sdev(scenario,nofgens,nofruns):

	normality = []

	#-----------------------------------------------------------------
	# For efficiency
	
	efficiencydata = zeros((nofgens,nofruns),float) # Here we'll store all the information from all the runs to perform the STD AND SEM calcs;
	efficiency_calculated = zeros((nofgens,3),float) #final values that we're going to use;	

	for i in range(0,nofruns):
	
		location = "datafiles/eff_r"+str(i)
		efficiencydata[:,i] = loadtxt(location,float,usecols=(1),delimiter=";")
	
	# Now for the calculations per se
	for i in range(0,nofgens):
		# Mean		
		efficiency_calculated[i,0] = mean(efficiencydata[i,:])
		# Standard Deviation
		efficiency_calculated[i,1] = std(efficiencydata[i,:],ddof=1) 
		# Standard Error of the Mean
		efficiency_calculated[i,2] = (efficiency_calculated[i,1])/sqrt(nofruns)

	normality.append(normalitytest(efficiencydata)) 
	saving_stats1("eff",efficiency_calculated)

	#'''
	figure()
	plot(efficiency_calculated[:,0])
	plot(efficiency_calculated[:,0]+efficiency_calculated[:,2])
	plot(efficiency_calculated[:,0]-efficiency_calculated[:,2])
	#'''

	#-----------------------------------------------------------------
	# For Mean Evolution Points

	evol_pointsdata = zeros((nofgens,nofruns),float) 
	evol_pointscalculated = zeros((nofgens,3),float)

	for i in range(0,nofruns):
	
		location = "datafiles/mep_r"+str(i)
		evol_pointsdata[:,i] = loadtxt(location,float,usecols=(1),delimiter=";")
		
	# Now for the calculations per se
	for i in range(0,nofgens):
		# Mean		
		evol_pointscalculated[i,0] = mean(evol_pointsdata[i,:])
		# Standard Deviation
		evol_pointscalculated[i,1] = std(evol_pointsdata[i,:],ddof=1) 
		# Standard Error of the Mean
		evol_pointscalculated[i,2] = (evol_pointscalculated[i,1])/sqrt(nofruns)

	normality.append(normalitytest(evol_pointsdata))
	saving_stats1("mep",evol_pointscalculated)

	#'''
	figure()
	plot(evol_pointscalculated[:,0])
	plot(evol_pointscalculated[:,0]+evol_pointscalculated[:,2])
	plot(evol_pointscalculated[:,0]-evol_pointscalculated[:,2])
	#'''
	#-----------------------------------------------------------------
	# For Concepts Per Word
	

	cpw_data = zeros((nofgens,nofruns),float) 
	cpw_calculated = zeros((nofgens,3),float)

	for i in range(0,nofruns):
	
		location = "datafiles/cpw_r"+str(i)
		cpw_data[:,i] = loadtxt(location,float,usecols=(1),delimiter=";")
		
	# Now for the calculations per se
	for i in range(0,nofgens):
		# Mean		
		cpw_calculated[i,0] = mean(cpw_data[i,:])
		# Standard Deviation
		cpw_calculated[i,1] = std(cpw_data[i,:],ddof=1) 
		# Standard Error of the Mean
		cpw_calculated[i,2] = (cpw_calculated[i,1])/sqrt(nofruns)

	normality.append(normalitytest(cpw_data))
	saving_stats1("cpw",cpw_calculated)

	#'''
	figure()
	plot(cpw_calculated[:,0])
	plot(cpw_calculated[:,0]+cpw_calculated[:,2])
	plot(cpw_calculated[:,0]-cpw_calculated[:,2])
	#'''

	#-----------------------------------------------------------------
	# For Phrases Length;
	
	# For General

	genlen_data = zeros((nofgens,nofruns),float) 
	genlen_calculated = zeros((nofgens,3),float)

	# For Unsucessfully Transmitted

	ntlen_data = zeros((nofgens,nofruns),float) 
	ntlen_calculated = zeros((nofgens,3),float)


	# For Sucessfully Transmitted
	
	ytlen_data = zeros((nofgens,nofruns),float) 
	ytlen_calculated = zeros((nofgens,3),float)


	for i in range(0,nofruns):
	
		location1 = "datafiles/genlen_r"+str(i)
		location2 = "datafiles/ntlen_r"+str(i)
		location3 = "datafiles/ytlen_r"+str(i)

		genlen_data[:,i] = loadtxt(location1,float,usecols=(1),delimiter=";")
		ntlen_data[:,i] = loadtxt(location2,float,usecols=(1),delimiter=";")
		ytlen_data[:,i] = loadtxt(location3,float,usecols=(1),delimiter=";")

	# Now for the calculations per se
	for i in range(0,nofgens):
		# General		
		genlen_calculated[i,0] = mean(genlen_data[i,:]) # Mean
		genlen_calculated[i,1] = std(genlen_data[i,:],ddof=1) # Standard Deviation
		genlen_calculated[i,2] = (genlen_calculated[i,1])/sqrt(nofruns) # Standard Error of the Mean
		# For Unsuccessfully Transmitted
		ntlen_calculated[i,0] = mean(ntlen_data[i,:]) # Mean
		ntlen_calculated[i,1] = std(ntlen_data[i,:],ddof=1) # Standard Deviation
		ntlen_calculated[i,2] = (ntlen_calculated[i,1])/sqrt(nofruns) # Standard Error of the Mean
		# For Successfully Transmitted		
		ytlen_calculated[i,0] = mean(ytlen_data[i,:]) # Mean
		ytlen_calculated[i,1] = std(ytlen_data[i,:],ddof=1) # Standard Deviation
		ytlen_calculated[i,2] = (ytlen_calculated[i,1])/sqrt(nofruns) # Standard Error of the Mean

	normality.append(normalitytest(genlen_data))
	saving_stats1("genlen",genlen_calculated)

	normality.append(normalitytest(ntlen_data))
	saving_stats1("ntlen",ntlen_calculated)

	normality.append(normalitytest(ytlen_data))
	saving_stats1("ytlen",ytlen_calculated)

	#'''
	figure()
	plot(genlen_calculated[:,0],"g-")
	plot(genlen_calculated[:,0]+genlen_calculated[:,2],"g--")
	plot(genlen_calculated[:,0]-genlen_calculated[:,2],"g--")
	plot(ntlen_calculated[:,0],"r-")
	plot(ntlen_calculated[:,0]+ntlen_calculated[:,2],"r--")
	plot(ntlen_calculated[:,0]-ntlen_calculated[:,2],"r--")
	plot(ytlen_calculated[:,0],"b-")
	plot(ytlen_calculated[:,0]+ytlen_calculated[:,2],"b--")
	plot(ytlen_calculated[:,0]-ytlen_calculated[:,2],"b--")
	#'''
	
	#===============================================================================================================
	# Now for the most complex of the measures;
	# We've to establish a separation by groups; 

	grouping1 = {0:[0,1,2,3,4],1:[5,6]}	
	grouping2 = {0:[0,1,2,3,4],1:[5,6,7,8,9],2:[10,11,12],3:[13,14,15,16,17,18,19],4:[20,21,22,23,24,25,26,27,28,29]}
	
	if scenario == 0:
		grouping = grouping1
	elif scenario == 1:
		grouping = grouping2
	lenofgrouping = len(grouping)

	#=====================================	

	#-----------------------------------------------------------------	
	# For Expressions / Concept (MEAN)
	
	# FIRST FOR EACH INDIVIDUAL GROUP
	npc_dataarray={}
	for i in range(0,lenofgrouping):

		zeta = len(grouping[i])
		cols_to_use = [x+1 for x in grouping[i]] # We'have to add 1 for the cols because col = 0 is for the generations 
							 # in all files from which we extract the data;

		npc_data = zeros((nofgens,nofruns*zeta),float)
	
		for j in range(0,nofruns):
	
			location = "datafiles/npc_r"+str(j)
			npc_data[:,(j*zeta):((j+1)*zeta)] = loadtxt(location,float,usecols=cols_to_use,delimiter=";")
		
		npc_dataarray[i] = deepcopy(npc_data)
	
	npc_calculatedarray = {}
	for i in range(0,lenofgrouping):

		npc_calculated = zeros((nofgens,3),float)

		for j in range(0,nofgens):
			npc_calculated[j,0] = mean(npc_dataarray[i][j,:]) # Mean
			npc_calculated[j,1] = std(npc_dataarray[i][j,:],ddof=1) # Standard Deviation
			npc_calculated[j,2] = (npc_calculated[j,1])/sqrt(nofruns) # Standard Error of the Mean
		#
		
		npc_calculatedarray[i] = deepcopy(npc_calculated)	

	figure()#'''
	for i in range(0,lenofgrouping):

		normality.append(normalitytest(npc_dataarray[i]))
		saving_stats1("npc_gr"+str(i),npc_calculatedarray[i])
		#'''
		plot(npc_calculatedarray[i][:,0])
		plot(npc_calculatedarray[i][:,0]+npc_calculatedarray[i][:,2])
		plot(npc_calculatedarray[i][:,0]-npc_calculatedarray[i][:,2])
		#'''		

		

	# THEN FOR THE MEAN OF THE ENTIRETY (NOT SEPARETED BY GROUPS)

	theta = 0 #getting the number of total columns;
	for i in range(0,lenofgrouping):
		zeta = len(grouping[i])
		theta = theta + zeta

	npc_data_mean = zeros((nofgens,theta*nofruns),float)
	npc_calculated_mean = zeros((nofgens,3),float)

	for i in range(0,nofruns):

		location = "datafiles/npc_r"+str(i)
		npc_data_mean[:,(i*theta):((i+1)*theta)] = loadtxt(location,float,usecols=range(1,theta+1),delimiter=";")

	for i in range(0,nofgens):

		npc_calculated_mean[i,0] = mean(npc_data_mean[i,:]) # Mean
		npc_calculated_mean[i,1] = std(npc_data_mean[i,:],ddof=1) # Standard Deviation 
		npc_calculated_mean[i,2] = (npc_calculated_mean[i,1])/sqrt(nofruns) # Standard Error of the Mean

	normality.append(normalitytest(npc_data_mean))
	saving_stats1("npc_mean",npc_calculated_mean)
	
	#'''
	plot(npc_calculated_mean[:,0],"r-")
	plot(npc_calculated_mean[:,0]+npc_calculated_mean[:,2],"r--")
	plot(npc_calculated_mean[:,0]-npc_calculated_mean[:,2],"r--")
	#'''

	#-----------------------------------------------------------------	
	# For Mean Signal Units Per Concept

	# FIRST FOR EACH INDIVIDUAL GROUP
	supc_dataarray={}
	for i in range(0,lenofgrouping):

		zeta = len(grouping[i])
		cols_to_use = [x+1 for x in grouping[i]] # We'have to add 1 for the cols because col = 0 is for the generations 
							 # in all files from which we extract the data;

		supc_data = zeros((nofgens,nofruns*zeta),float)
	
		for j in range(0,nofruns):
	
			location = "datafiles/supc_r"+str(j)
			supc_data[:,(j*zeta):((j+1)*zeta)] = loadtxt(location,float,usecols=cols_to_use,delimiter=";")
		
		supc_dataarray[i] = deepcopy(supc_data)
	
	supc_calculatedarray = {}
	for i in range(0,lenofgrouping):

		supc_calculated = zeros((nofgens,3),float)

		for j in range(0,nofgens):
			supc_calculated[j,0] = mean(supc_dataarray[i][j,:]) # Mean
			supc_calculated[j,1] = std(supc_dataarray[i][j,:],ddof=1) # Standard Deviation
			supc_calculated[j,2] = (supc_calculated[j,1])/sqrt(nofruns) # Standard Error of the Mean
		#
		
		supc_calculatedarray[i] = deepcopy(supc_calculated)	

	figure()#'''
	for i in range(0,lenofgrouping):

		normality.append(normalitytest(supc_dataarray[i]))
		saving_stats1("supc_gr"+str(i),supc_calculatedarray[i])	
		#'''
		plot(supc_calculatedarray[i][:,0])
		plot(supc_calculatedarray[i][:,0]+supc_calculatedarray[i][:,2])
		plot(supc_calculatedarray[i][:,0]-supc_calculatedarray[i][:,2])
		#'''

	# THEN FOR THE MEAN OF THE ENTIRETY (NOT SEPARETED BY GROUPS)

	theta = 0 #getting the number of total columns;
	for i in range(0,lenofgrouping):
		zeta = len(grouping[i])
		theta = theta + zeta

	supc_data_mean = zeros((nofgens,theta*nofruns),float)
	supc_calculated_mean = zeros((nofgens,3),float)

	for i in range(0,nofruns):

		location = "datafiles/supc_r"+str(i)
		supc_data_mean[:,(i*theta):((i+1)*theta)] = loadtxt(location,float,usecols=range(1,theta+1),delimiter=";")

	for i in range(0,nofgens):

		supc_calculated_mean[i,0] = mean(supc_data_mean[i,:]) # Mean
		supc_calculated_mean[i,1] = std(supc_data_mean[i,:],ddof=1) # Standard Deviation 
		supc_calculated_mean[i,2] = (supc_calculated_mean[i,1])/sqrt(nofruns) # Standard Error of the Mean

	normality.append(normalitytest(supc_data_mean))
	saving_stats1("supc_mean",supc_calculated_mean)

	#'''
	plot(supc_calculated_mean[:,0],"r-")
	plot(supc_calculated_mean[:,0]+supc_calculated_mean[:,2],"r--")
	plot(supc_calculated_mean[:,0]-supc_calculated_mean[:,2],"r--")
	#'''
	
	#-----------------------------------------------------------------	
	# For ENTROPY

	# FIRST FOR EACH INDIVIDUAL GROUP
	ent_dataarray={}
	for i in range(0,lenofgrouping):

		zeta = len(grouping[i])
		cols_to_use = [x+1 for x in grouping[i]] # We'have to add 1 for the cols because col = 0 is for the generations 
							 # in all files from which we extract the data;

		ent_data = zeros((nofgens,nofruns*zeta),float)
	
		for j in range(0,nofruns):
	
			location = "datafiles/ent_r"+str(j)
			ent_data[:,(j*zeta):((j+1)*zeta)] = loadtxt(location,float,usecols=cols_to_use,delimiter=";")
		
		ent_dataarray[i] = deepcopy(ent_data)
	
	ent_calculatedarray = {}
	for i in range(0,lenofgrouping):

		ent_calculated = zeros((nofgens,3),float)

		for j in range(0,nofgens):
			ent_calculated[j,0] = mean(ent_dataarray[i][j,:]) # Mean
			ent_calculated[j,1] = std(ent_dataarray[i][j,:],ddof=1) # Standard Deviation
			ent_calculated[j,2] = (ent_calculated[j,1])/sqrt(nofruns) # Standard Error of the Mean
		#
		
		ent_calculatedarray[i] = deepcopy(ent_calculated)	

	figure()#'''
	for i in range(0,lenofgrouping):

		normality.append(normalitytest(ent_dataarray[i]))
		saving_stats1("ent_gr"+str(i),ent_calculatedarray[i])
		#'''
		plot(ent_calculatedarray[i][:,0])
		plot(ent_calculatedarray[i][:,0]+ent_calculatedarray[i][:,2])
		plot(ent_calculatedarray[i][:,0]-ent_calculatedarray[i][:,2])
		#'''

	# THEN FOR THE MEAN OF THE ENTIRETY (NOT SEPARETED BY GROUPS)

	theta = 0 #getting the number of total columns;
	for i in range(0,lenofgrouping):
		zeta = len(grouping[i])
		theta = theta + zeta

	ent_data_mean = zeros((nofgens,theta*nofruns),float)
	ent_calculated_mean = zeros((nofgens,3),float)

	for i in range(0,nofruns):

		location = "datafiles/ent_r"+str(i)
		ent_data_mean[:,(i*theta):((i+1)*theta)] = loadtxt(location,float,usecols=range(1,theta+1),delimiter=";")

	for i in range(0,nofgens):

		ent_calculated_mean[i,0] = mean(ent_data_mean[i,:]) # Mean
		ent_calculated_mean[i,1] = std(ent_data_mean[i,:],ddof=1) # Standard Deviation 
		ent_calculated_mean[i,2] = (ent_calculated_mean[i,1])/sqrt(nofruns) # Standard Error of the Mean

	normality.append(normalitytest(ent_data_mean))
	saving_stats1("ent_mean",ent_calculated_mean)

	#'''
	plot(ent_calculated_mean[:,0],"r-")
	plot(ent_calculated_mean[:,0]+ent_calculated_mean[:,2],"r--")
	plot(ent_calculated_mean[:,0]-ent_calculated_mean[:,2],"r--")
	#'''

	
	#=====================================	
	show()#''' # ALL THESE COMMENTED LINES WERE CREATED FOR DEBUGGING PURPOSES
	saving_stats1("norm",array(normality))
	#=====================================

#-------------------------------------------------------------------------
# Establishes the normality test function that we'll use;
# Based on SciPy Shapiro-Wilk normality test 
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.shapiro.html
# Threshold = 0.05


def normalitytest(array_):

	rowsofarray = len(array_[:,0])
	isitnormal = zeros((rowsofarray,1),float)

	for i in range(0,rowsofarray):
		result=stats.shapiro(array_[i,:])       #Shapiro-Wilk
		if result.pvalue >= 0.05: # Threshold
			isitnormal[i] = 0.0
		else:
			isitnormal[i] = 1.0
	
	totalnormality = sum(isitnormal[:,0])

	return totalnormality
