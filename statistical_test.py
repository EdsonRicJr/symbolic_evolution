# This file has the tools to statistically analyse curves; Continuing what we proposed initially at "fittingfile.py" we have:
#
# The whole idea behind it is the following:
# - Make a fit for every single run;
# - Gather all the parameters used for fitting and save then;
# - Makes a normality test for each parameter;
# - Use these parameters in order to do statistical analysis;
#
# Here we deal with the last two objectives, it is important to note that it's not implemented in an automatic fashion; Unfortunalety it requires 
# a hands-on approach to choose what you're testing against what;
#
# We use four tools in order to do the analyses:
# [1] Following the procedures in (*), we've already obtained the parameters which we are going to use, then unlike the cited source, that uses One-# Way ANOVA, we use here the Non-Parametric alternatives which are the Mann Whitney U for pairwise and the Kruskal-Wallis H-test for multiple
# groups, for each individual parameter 
# (https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html)
# (https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kruskal.html)
#  
# [2] In order to test the normality of the data, and before performing the actual Mann Whitney // Kruskal-Wallis, we perform a Shapiro-Wilk test 
# for normality;
# (https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.shapiro.html)
#
# [3] We do a posthoc analysis of the Kruskal-Wallis if needed for the parameters which are different; We use than the Dunn's test, which is the
# adequate tool for a nonparametric posthoc analysis following Kruskal-Wallis;
# (https://scikit-posthocs.readthedocs.io/en/latest/generated/scikit_posthocs.posthoc_dunn.html)
#
# [4] Finally, we also can perform an Spearman's correlation coefficient analyses, which again, takes into account the fact that our data is non- 
# parametric;
# (https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.spearmanr.html)
#
#
# * Meredith, M. P., and S. V. Stehman. "Repeated measures experiments in forestry: focus on analysis of response curves." Canadian Journal of
# Forest Research 21.7 (1991): 957-965. 
# NOTE: Mann-Whitney U test can be performed for only two groups, where we could also perform a KW-H-test;

#=========================================================================
from numpy import loadtxt, array, zeros, linspace, std, mean, sqrt, polyfit, exp, where, nan
from pylab import scatter,plot,show,xlim,ylim,xlabel,ylabel,legend, title, figure
import matplotlib.pyplot as plt 
from copy import copy, deepcopy

from scipy import stats, optimize
import scikit_posthocs as sp
import pandas as pd

#=========================================================================

#-------------------------------------------------------------------------
# First, we must upload the data that we wish to test:
# [I'd recommend getting the files that you wish to test and copy them to a specific folder and run the analysis there]

whichcomparison = 1 # If it's a pairwise comparison ( == 0) or a multiple comparison ( == 1 )
                    # or if a comparison between 3 groups (==2)	     

#pamloc1 = "eff2" #"ent1_gr0"
pamloc1 = "ent1_gr0"
#pamloc2 = "eff3" #"ent1_gr1"
pamloc2 = "ent1_gr1"
pamloc3 = "ent1_gr2"
pamloc4 = "ent1_gr3"
pamloc5 = "ent1_gr4"

#curveloc1 = #"eff2curve" #"ent_gr0"
curveloc1 = "ent_gr0"
#curveloc2 = #"eff3curve" #"ent_gr1"
curveloc2 = "ent_gr1"
curveloc3 = "ent_gr2"
curveloc4 = "ent_gr3"
curveloc5 = "ent_gr4"

if whichcomparison == 0:

	# fist loading the arrays [ remember that dat structure is of the dimensions 
	#                          for param (NofParams,NofSamples)
	#                          for curves (NofGens, 3 ) where columns are MEAN | SD | SEM ]

	pam_array1 = loadtxt(pamloc1,float,delimiter=";")
	pam_array2 = loadtxt(pamloc2,float,delimiter=";")

	curve_array1 = loadtxt(curveloc1,float,delimiter=";")
	curve_array2 = loadtxt(curveloc2,float,delimiter=";")
	
	zeta = len(pam_array1[:,0])
	# Now testing for normality (only for Parameters), for crvs nrmlt was tested bfr point by point;
	
	print("Normality test:		       ")
	print("Parameter    Sample1	              Sample2")
	for i in range(0,zeta):
		
		results_1 = stats.shapiro(pam_array1[i,:])	
		results_2 = stats.shapiro(pam_array2[i,:])
		print(i,"         ",results_1.pvalue,"     ",results_2.pvalue)

	
	# Now making for each parameter a Mann-Whitney U test;
	print("\n")
	print("Statistical test MWU-test:		       ")
	print("Parameter         p-value")
	for i in range(0,zeta):
	
		results = stats.mannwhitneyu(pam_array1[i,:],pam_array2[i,:])
		print(i,"         ",results.pvalue)

	# Now performing a Spearman's  Correlation Coefficient between the CURVES;
	print("\n")
	print("Spearman Coefficient: ")
	print("Correlation               p-value")
	results_ = stats.spearmanr(curve_array1[:,0],curve_array2[:,0])
	print(results_.correlation,"      ",results_.pvalue)
	
elif whichcomparison == 1:		

	# loading the Arrays

	pam_array1 = loadtxt(pamloc1,float,delimiter=";")
	pam_array2 = loadtxt(pamloc2,float,delimiter=";")
	pam_array3 = loadtxt(pamloc3,float,delimiter=";")
	pam_array4 = loadtxt(pamloc4,float,delimiter=";")
	pam_array5 = loadtxt(pamloc5,float,delimiter=";")


	curve_array1 = loadtxt(curveloc1,float,delimiter=";")
	curve_array2 = loadtxt(curveloc2,float,delimiter=";")
	curve_array3 = loadtxt(curveloc3,float,delimiter=";")
	curve_array4 = loadtxt(curveloc4,float,delimiter=";")
	curve_array5 = loadtxt(curveloc5,float,delimiter=";")

	zeta = len(pam_array1[:,0])
	# Now testing for normality (only for Parameters), for crvs nrmlt was tested bfr point by point;
	
	print("Normality test:		       ")
	print("Parameter  /  Sample1 / Sample2 / Sample 3 / Sample 4 / Sample 5")
	for i in range(0,zeta):
		
		results_1 = stats.shapiro(pam_array1[i,:])	
		results_2 = stats.shapiro(pam_array2[i,:])
		results_3 = stats.shapiro(pam_array3[i,:])
		results_4 = stats.shapiro(pam_array4[i,:])
		results_5 = stats.shapiro(pam_array5[i,:])
		print(i,"/",results_1.pvalue,"/",results_2.pvalue,"/",results_3.pvalue,"/",results_4.pvalue,"/",results_5.pvalue)

	# Now making for each parameter a Kruskal-Wallis H test;
	which_to_posthoc = []	# This list will withhold which parameters are significantly different and will go to a post-hoc analysis
	
	print("\n")
	print("Statistical test KWH-test:		       ")
	print("Parameter         p-value")
	for i in range(0,zeta):
	
		results = stats.kruskal(pam_array1[i,:],pam_array2[i,:],pam_array3[i,:],pam_array4[i,:],pam_array5[i,:])
		print(i,"         ",results.pvalue)
		
		if results.pvalue < 0.05:
			which_to_posthoc.append(i)
	
	# Now if there're differences, let's see which groups differ from one another with the post hoc analysis;
	print("\n Which to Post-Hoc:", which_to_posthoc)
	if len(which_to_posthoc)!=0:

		for x in which_to_posthoc:
			
			# First we must organize the data; Scikit Dunn's Test needs a specific arrangement of the data;
			# For that I'm going first to see which array has the greatest size so we can create the data_array adequately;

			sizes_ = {0:len(pam_array1[x,:]),1:len(pam_array2[x,:]),2:len(pam_array3[x,:]),3:len(pam_array4[x,:]),4:len(pam_array5[x,:])}
			size_to_use = sizes_[0]
			for j in range(0,5):
				if sizes_[j]>=size_to_use:
					size_to_use = sizes_[j]
			
			dunn_array = zeros((5,size_to_use),float) # Now it has the proper dimension
			dunn_array = where(dunn_array==0, nan, dunn_array) # Turning all values into NaN, for later passing to the test;

			# Finally creating the array
			dunn_array[0,0:sizes_[0]]=pam_array1[x,:]
			dunn_array[1,0:sizes_[1]]=pam_array2[x,:]			
			dunn_array[2,0:sizes_[2]]=pam_array3[x,:]
			dunn_array[3,0:sizes_[3]]=pam_array4[x,:]			
			dunn_array[4,0:sizes_[4]]=pam_array5[x,:]

			#print(dunn_array)
					
			print("\n")
			print("Statistical test Dunn Post-Hoc Test:		       ")
			print("Parameter ", x,":")
			p_values_ = sp.posthoc_dunn(dunn_array,p_adjust="bonferroni")
			print(p_values_)
			print("\n")
			print(p_values_ < 0.05)
			
			
	# Now performing a Spearman's  Correlation Coefficient between the CURVES;

	# First we gather all curves into a single array:
	
	curve_big_array = zeros((len(curve_array1[:,0]),5) , float)
	curve_big_array[:,0]= curve_array1[:,0]
	curve_big_array[:,1]= curve_array2[:,0]
	curve_big_array[:,2]= curve_array3[:,0]
	curve_big_array[:,3]= curve_array4[:,0]
	curve_big_array[:,4]= curve_array5[:,0]	

	print("\n")
	print("Spearman Coefficient: ")
	print("Correlation               p-value")
	results_ = stats.spearmanr(curve_big_array,axis=0)
	#print(results_.correlation,"      ",results_.pvalue)
	print(results_.pvalue)			
		
elif whichcomparison == 2:

	# loading the Arrays

	pam_array1 = loadtxt(pamloc1,float,delimiter=";")
	pam_array2 = loadtxt(pamloc2,float,delimiter=";")
	pam_array3 = loadtxt(pamloc3,float,delimiter=";")



	curve_array1 = loadtxt(curveloc1,float,delimiter=";")
	curve_array2 = loadtxt(curveloc2,float,delimiter=";")
	curve_array3 = loadtxt(curveloc3,float,delimiter=";")

	zeta = len(pam_array1[:,0])
	# Now testing for normality (only for Parameters), for crvs nrmlt was tested bfr point by point;
	
	print("Normality test:		       ")
	print("Parameter  /  Sample1 / Sample2 / Sample 3 / Sample 4 / Sample 5")
	for i in range(0,zeta):
		
		results_1 = stats.shapiro(pam_array1[i,:])	
		results_2 = stats.shapiro(pam_array2[i,:])
		results_3 = stats.shapiro(pam_array3[i,:])

		print(i,"/",results_1.pvalue,"/",results_2.pvalue,"/",results_3.pvalue)

	# Now making for each parameter a Kruskal-Wallis H test;
	which_to_posthoc = []	# This list will withhold which parameters are significantly different and will go to a post-hoc analysis
	
	print("\n")
	print("Statistical test KWH-test:		       ")
	print("Parameter         p-value")
	for i in range(0,zeta):
	
		results = stats.kruskal(pam_array1[i,:],pam_array2[i,:],pam_array3[i,:])
		print(i,"         ",results.pvalue)
		
		if results.pvalue < 0.05:
			which_to_posthoc.append(i)
	
	# Now if there're differences, let's see which groups differ from one another with the post hoc analysis;
	print("\n Which to Post-Hoc:", which_to_posthoc)
	if len(which_to_posthoc)!=0:

		for x in which_to_posthoc:
			
			# First we must organize the data; Scikit Dunn's Test needs a specific arrangement of the data;
			# For that I'm going first to see which array has the greatest size so we can create the data_array adequately;

			sizes_ = {0:len(pam_array1[x,:]),1:len(pam_array2[x,:]),2:len(pam_array3[x,:])}
			size_to_use = sizes_[0]
			for j in range(0,3):
				if sizes_[j]>=size_to_use:
					size_to_use = sizes_[j]
			
			dunn_array = zeros((3,size_to_use),float) # Now it has the proper dimension
			dunn_array = where(dunn_array==0, nan, dunn_array) # Turning all values into NaN, for later passing to the test;

			# Finally creating the array
			dunn_array[0,0:sizes_[0]]=pam_array1[x,:]
			dunn_array[1,0:sizes_[1]]=pam_array2[x,:]			
			dunn_array[2,0:sizes_[2]]=pam_array3[x,:]

			#print(dunn_array)
					
			print("\n")
			print("Statistical test Dunn Post-Hoc Test:		       ")
			print("Parameter ", x,":")
			p_values_ = sp.posthoc_dunn(dunn_array,p_adjust="bonferroni")
			print(p_values_)
			print("\n")
			print(p_values_ < 0.05)
			
			
	# Now performing a Spearman's  Correlation Coefficient between the CURVES;

	# First we gather all curves into a single array:
	
	curve_big_array = zeros((len(curve_array1[:,0]),3) , float)
	curve_big_array[:,0]= curve_array1[:,0]
	curve_big_array[:,1]= curve_array2[:,0]
	curve_big_array[:,2]= curve_array3[:,0]

	print("\n")
	print("Spearman Coefficient: ")
	print("Correlation               p-value")
	results_ = stats.spearmanr(curve_big_array,axis=0)
	#print(results_.correlation,"      ",results_.pvalue)
	print(results_.pvalue)			

