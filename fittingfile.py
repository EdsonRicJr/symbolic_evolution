# This file creates the fits, which we're going to use to do our statistical analysis;
#
# The whole idea behind it is the following:
# [1] Make a fit for every single run;
# [2] Gather all the parameters used for fitting and save then;
# [3] Makes a normality test for each parameter;
# [4] Use these parameters in order to do statistical analysis;

# This file deals with [1], [2]; [3] and [4] is not implemented in an automatic fashion; Unfortunalety it requires a hands-on approach to choose what you're testint against what (see statistical comparison file: XXXX.py);

# OBSERVATION:
# - Much of the code follows the logic and structure from stats1.py, if you've read already it'll make it easier to understand the rationale on this # one;
# - Article from where I've taken the method: 
#  Meredith, M. P., and S. V. Stehman. "Repeated measures experiments in forestry: focus on analysis of response curves." Canadian Journal of Forest Research 21.7 (1991): 957-965.

#=========================================================================
from numpy import loadtxt, array, zeros, linspace, std, mean, sqrt, polyfit, exp
from pylab import scatter,plot,show,xlim,ylim,xlabel,ylabel,legend, title, figure
from copy import copy, deepcopy

from scipy import stats, optimize

from fileoperators import saving_fits
#=========================================================================

#-------------------------------------------------------------------------
# We just pass three arguments: scenario = 0 or 1 (0 = scenario 1; 1 = scenario 2/3);
#                               nogens = the number of generations performed for each run
#                               nofruns = the number of runs performed;

colours_ = ["b+","g-","r.","c*","m--","yo", "k_", "w-."]

nofgens=300
nofruns=25
scenario=0                      

grouping1 = {0:[0,1,2,3,4],1:[5,6]}	
grouping2 = {0:[0,1,2,3,4],1:[5,6,7,8,9],2:[10,11,12],3:[13,14,15,16,17,18,19],4:[20,21,22,23,24,25,26,27,28,29]}

if scenario == 0:
	grouping = grouping1
elif scenario == 1:
	grouping = grouping2
lenofgrouping = len(grouping)

#=========================================================================
#-------------------------------------------------------------------------
# Here we define all the functions that we're going to use with scipy.optimize.curve_fit 
# (https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html)
# For one of the cases we're going to use numpy polynominal fit polyfit();

# For Efficiency:
# https://en.wikipedia.org/wiki/Logistic_function

def eff_func(x,a,b,c):
	return a/(1+exp(-b*(x-c)))
effNparams = 3 # (a,b,c)

# For Mean Evolution Points:
# same as above;

def evol_func(x,a,b,c):
	return a/(1+exp(-b*(x-c)))
evolNparams = 3

# For Concepts Per Word:
#https://stackoverflow.com/questions/21420792/exponential-curve-fitting-in-scipy

def cpw_func(x,a,b,c):
	return a*exp(-b*x)+c
cpwNparams = 3

# For Phrases Length: 
#I've opted for using the polynomyal function from numpy; So it's dynamic is a bit different;

lenNparams = 4
def polyno_fit(y,rowsize,d_of_f,colours):
	
	x=array(range(0,rowsize))
	values = polyfit(x,y,d_of_f)
	
	fitted_curve = zeros(rowsize,float) + values[-1]
	for i in range(0,d_of_f):
		fitted_curve = fitted_curve + (x**(d_of_f-i))*values[i]

	plot(x,fitted_curve,colours) # Must comment, here just for checking if okey during coding;
	
	return values

# For Expressions (names) Per Concept:

def npc_func(x,a,b,c):
	return a*exp(-b*x)+c
npcNparams = 3

# For Mean Signal Units Per Concept

def supc_func(x,a,b,c,d):
	return a*(x**3)+b*(x**2)+c*x+d
	#return a*exp(-b*x)+c for testing;
supcNparams = 4

# For ENTROPY

def ent_func(x,a,b,c):	
	return a*exp(-b*x)+c #return a*(x**2)+b*(x)+c for testing;
entNparams = 3

#=========================================================================

x_axis = array(range(0,nofgens))

#-------------------------------------------------------------------------
# First for Efficiency:

# Stores the raw data
efficiencydata = zeros((nofgens,nofruns),float)

for i in range(0,nofruns):

	location = "datafiles/eff_r"+str(i)
	efficiencydata[:,i] = loadtxt(location,float,usecols=(1),delimiter=";")

# Stores the parameters;
efficiency_param = zeros((effNparams,nofruns),float) # This value depends on the quantity of params used in the function that'll call;

figure() 
for i in range(0,nofruns):

	popt, pcov = optimize.curve_fit(eff_func,x_axis,efficiencydata[:,i])
	plot(evol_func(x_axis,popt[0],popt[1],popt[2]))

	for k in range(0,effNparams):
		efficiency_param[k,i]=deepcopy(popt[k])

saving_fits("eff",efficiency_param)
show()
#-------------------------------------------------------------------------
# for Mean Evolution Points:

# Stores the raw data
evol_pointsdata = zeros((nofgens,nofruns),float)

for i in range(0,nofruns):

	location = "datafiles/mep_r"+str(i)
	evol_pointsdata[:,i] = loadtxt(location,float,usecols=(1),delimiter=";")

# Stores the parameters;
evol_points_param = zeros((evolNparams,nofruns),float) # This value depends on the quantity of params used in the function that'll call;

figure() 
for i in range(0,nofruns):

	popt, pcov = optimize.curve_fit(evol_func,x_axis,evol_pointsdata[:,i], p0=(5, 5, 5))
	plot(evol_func(x_axis,popt[0],popt[1],popt[2]))

	for k in range(0,evolNparams):
		evol_points_param[k,i]=deepcopy(popt[k])

saving_fits("mep",evol_points_param)
show()

#-------------------------------------------------------------------------
# for Concepts Per Word:

cpw_data = zeros((nofgens,nofruns),float)

for i in range(0,nofruns):

	location = "datafiles/cpw_r"+str(i)
	cpw_data[:,i] = loadtxt(location,float,usecols=(1),delimiter=";")

# Stores the parameters;
cpw_param = zeros((cpwNparams,nofruns),float) # This value depends on the quantity of params used in the function that'll call;

figure() 
for i in range(0,nofruns):

	popt, pcov = optimize.curve_fit(cpw_func,x_axis,cpw_data[:,i])
	plot(cpw_func(x_axis,popt[0],popt[1],popt[2]))

	for k in range(0,cpwNparams):
		cpw_param[k,i]=deepcopy(popt[k])

saving_fits("cpw",cpw_param)
show()

#-------------------------------------------------------------------------
# for Phrase's Length

	# For General
genlen_data = zeros((nofgens,nofruns),float) 
	# For Unsucessfully Transmitted
ntlen_data = zeros((nofgens,nofruns),float) 
	# For Sucessfully Transmitted
ytlen_data = zeros((nofgens,nofruns),float) 

for i in range(0,nofruns):
	
	location1 = "datafiles/genlen_r"+str(i)
	location2 = "datafiles/ntlen_r"+str(i)
	location3 = "datafiles/ytlen_r"+str(i)

	genlen_data[:,i] = loadtxt(location1,float,usecols=(1),delimiter=";")
	ntlen_data[:,i] = loadtxt(location2,float,usecols=(1),delimiter=";")
	ytlen_data[:,i] = loadtxt(location3,float,usecols=(1),delimiter=";")

# Stores the parameters;
genlen_param = zeros((lenNparams,nofruns),float) 
ntlen_param = zeros((lenNparams,nofruns),float)
ytlen_param = zeros((lenNparams,nofruns),float)

figure() 
for i in range(0,nofruns):

	values_1 = polyno_fit(genlen_data[:,i],nofgens,lenNparams,colours_[0])
	values_2 = polyno_fit(ntlen_data[:,i],nofgens,lenNparams,colours_[1])
	values_3 = polyno_fit(ytlen_data[:,i],nofgens,lenNparams,colours_[2])	

	for k in range(0,lenNparams):
		genlen_param[k,i]=deepcopy(values_1[k])
		ntlen_param[k,i]=deepcopy(values_2[k])
		ytlen_param[k,i]=deepcopy(values_3[k])

saving_fits("genlen",genlen_param)
saving_fits("ntlen",ntlen_param)
saving_fits("ytlen",ytlen_param)

show()

#-------------------------------------------------------------------------
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


figure()	
npc_paramarray = {}
for i in range(0,lenofgrouping):

	zeta = len(grouping[i])
	beta = nofruns*zeta
	npc_param = zeros((npcNparams,beta),float)

	for j in range(0,beta):
		popt, pcov = optimize.curve_fit(npc_func,x_axis,npc_dataarray[i][:,j],p0=(5, 5, 5))
		plot(npc_func(x_axis,popt[0],popt[1],popt[2]),colours_[i])

		for k in range(0,npcNparams):
			npc_param[k,j]=deepcopy(popt[k])
		
	npc_paramarray[i] = deepcopy(npc_param)	

show()

# Saving them;
for i in range(0,lenofgrouping):

	saving_fits("npc_gr"+str(i),npc_paramarray[i])

# THEN FOR THE MEAN OF THE ENTIRETY (NOT SEPARETED BY GROUPS)

theta = 0 #getting the number of total columns;
for i in range(0,lenofgrouping):
	zeta = len(grouping[i])
	theta = theta + zeta

npc_data_mean = zeros((nofgens,theta*nofruns),float)
npc_param_mean = zeros((npcNparams,theta*nofruns),float)

for i in range(0,nofruns):

	location = "datafiles/npc_r"+str(i)
	npc_data_mean[:,(i*theta):((i+1)*theta)] = loadtxt(location,float,usecols=range(1,theta+1),delimiter=";")

figure()
for i in range(0,theta*nofruns):

	popt, pcov = optimize.curve_fit(npc_func,x_axis,npc_data_mean[:,i],p0=(5, 5, 5))
	plot(npc_func(x_axis,popt[0],popt[1],popt[2]))

	for k in range(0,npcNparams):
		npc_param_mean[k,i]=deepcopy(popt[k])
show()

saving_fits("npc_mean",npc_param_mean)


#-------------------------------------------------------------------------
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


figure()	
supc_paramarray = {}
for i in range(0,lenofgrouping):

	zeta = len(grouping[i])
	beta = nofruns*zeta
	supc_param = zeros((supcNparams,beta),float)

	for j in range(0,beta):
		popt, pcov = optimize.curve_fit(supc_func,x_axis,supc_dataarray[i][:,j])
		plot(supc_func(x_axis,popt[0],popt[1],popt[2],popt[3]),colours_[i])

		for k in range(0,supcNparams):
			supc_param[k,j]=deepcopy(popt[k])
		
	supc_paramarray[i] = deepcopy(supc_param)	

show()

# Saving them;
for i in range(0,lenofgrouping):

	saving_fits("supc_gr"+str(i),supc_paramarray[i])

# THEN FOR THE MEAN OF THE ENTIRETY (NOT SEPARETED BY GROUPS)

theta = 0 #getting the number of total columns;
for i in range(0,lenofgrouping):
	zeta = len(grouping[i])
	theta = theta + zeta

supc_data_mean = zeros((nofgens,theta*nofruns),float)
supc_param_mean = zeros((supcNparams,theta*nofruns),float)

for i in range(0,nofruns):

	location = "datafiles/supc_r"+str(i)
	supc_data_mean[:,(i*theta):((i+1)*theta)] = loadtxt(location,float,usecols=range(1,theta+1),delimiter=";")

figure()
for i in range(0,theta*nofruns):

	popt, pcov = optimize.curve_fit(supc_func,x_axis,supc_data_mean[:,i])
	plot(supc_func(x_axis,popt[0],popt[1],popt[2],popt[3]))

	for k in range(0,supcNparams):
		supc_param_mean[k,i]=deepcopy(popt[k])
show()

saving_fits("supc_mean",supc_param_mean)

#-------------------------------------------------------------------------
# For Entropy

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


figure()	
ent_paramarray = {}
for i in range(0,lenofgrouping):

	zeta = len(grouping[i])
	beta = nofruns*zeta
	ent_param = zeros((entNparams,beta),float)

	for j in range(0,beta):
		popt, pcov = optimize.curve_fit(ent_func,x_axis,ent_dataarray[i][:,j])
		plot(ent_func(x_axis,popt[0],popt[1],popt[2]),colours_[i])

		for k in range(0,entNparams):
			ent_param[k,j]=deepcopy(popt[k])
		
	ent_paramarray[i] = deepcopy(ent_param)	

show()

# Saving them;
for i in range(0,lenofgrouping):

	saving_fits("ent_gr"+str(i),ent_paramarray[i])

# THEN FOR THE MEAN OF THE ENTIRETY (NOT SEPARETED BY GROUPS)

theta = 0 #getting the number of total columns;
for i in range(0,lenofgrouping):
	zeta = len(grouping[i])
	theta = theta + zeta

ent_data_mean = zeros((nofgens,theta*nofruns),float)
ent_param_mean = zeros((entNparams,theta*nofruns),float)

for i in range(0,nofruns):

	location = "datafiles/ent_r"+str(i)
	ent_data_mean[:,(i*theta):((i+1)*theta)] = loadtxt(location,float,usecols=range(1,theta+1),delimiter=";")

figure()
for i in range(0,theta*nofruns):

	popt, pcov = optimize.curve_fit(ent_func,x_axis,ent_data_mean[:,i])
	plot(ent_func(x_axis,popt[0],popt[1],popt[2]))

	for k in range(0,entNparams):
		ent_param_mean[k,i]=deepcopy(popt[k])
show()

saving_fits("ent_mean",ent_param_mean)

