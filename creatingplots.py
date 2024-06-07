# This is a file created in order to Plot what is necessary;

#=========================================================================
from numpy import loadtxt, array, zeros, linspace, std, mean, sqrt, polyfit, exp, where, nan
from pylab import scatter,plot,show,xlim,ylim,xlabel,ylabel,legend, title, figure
import matplotlib.pyplot as plt 
from copy import copy, deepcopy

from scipy import stats, optimize
import scikit_posthocs as sp
import pandas as pd

#=========================================================================

#curveloc1 = "eff2curve" 
#curveloc2 = "eff3curve" 
curveloc1 = "ent_gr0"
curveloc2 = "ent_gr1"
curveloc3 = "ent_gr2"
curveloc4 = "ent_gr3"
curveloc5 = "ent_gr4"

curveloc6 = "c2ent_gr0"
curveloc7 = "c2ent_gr1"
curveloc8 = "c2ent_gr2"
curveloc9 = "c2ent_gr3"
curveloc10 = "c2ent_gr4"


whichplot = 2 # 0 = pairs being plotted; 1 = groups being plotted simultaneously ; 2 = groups vs groups

if whichplot == 0:

	curve_array1 = loadtxt(curveloc1,float,delimiter=";")
	curve_array2 = loadtxt(curveloc2,float,delimiter=";")

	# Now finally we're plotting the curves with the SD(or)SEM associated with it;
	
	xaxis = array(range(0,len(curve_array1[:,0])))
	
	# Means (change the label for your need):		
	plt.plot(xaxis, curve_array1[:,0], color="darkred",label="sample1")
	plt.plot(xaxis, curve_array2[:,0], color="darkblue",label="sample2")
	
	# Plotting the SEMs together:
	plt.fill_between(xaxis,curve_array1[:,0]-curve_array1[:,2],curve_array1[:,0]+curve_array1[:,2],color="lightcoral", alpha = 0.5)
	plt.fill_between(xaxis,curve_array2[:,0]-curve_array2[:,2],curve_array2[:,0]+curve_array2[:,2],color="cornflowerblue", alpha = 0.5)
	
	# Axis-Naming and showing
	#plt.axes.Axes.set_xlim(0,1000) #only if needed
	#plt.axes.Axes.set_ylim(0,200) #only if needed
	plt.ylabel("Eficiência (%)")	 # you should change according to what you wish to plot
	plt.xlabel("Gerações")
	plt.legend()
	plt.show()

if whichplot == 1:

	curve_array1 = loadtxt(curveloc1,float,delimiter=";")
	curve_array2 = loadtxt(curveloc2,float,delimiter=";")
	curve_array3 = loadtxt(curveloc3,float,delimiter=";")
	curve_array4 = loadtxt(curveloc4,float,delimiter=";")
	curve_array5 = loadtxt(curveloc5,float,delimiter=";")

	# Now finally we're plotting the curves with the SD(or)SEM associated with it;
	
	xaxis = array(range(0,len(curve_array1[:,0])))
	
	# Means (change the label for your need):		
	plt.plot(xaxis, curve_array1[:,0], color="darkred",label="sample1")
	plt.plot(xaxis, curve_array2[:,0], color="darkblue",label="sample2")
	plt.plot(xaxis, curve_array3[:,0], color="darkorange",label="sample3")	
	plt.plot(xaxis, curve_array4[:,0], color="darkgreen",label="sample1")
	plt.plot(xaxis, curve_array5[:,0], color="darkmagenta",label="sample1")

	# Plotting the SEMs together:
	plt.fill_between(xaxis,curve_array1[:,0]-curve_array1[:,2],curve_array1[:,0]+curve_array1[:,2],color="lightcoral", alpha = 0.5)
	plt.fill_between(xaxis,curve_array2[:,0]-curve_array2[:,2],curve_array2[:,0]+curve_array2[:,2],color="cornflowerblue", alpha = 0.5)
	plt.fill_between(xaxis,curve_array3[:,0]-curve_array3[:,2],curve_array3[:,0]+curve_array3[:,2],color="navajowhite", alpha = 0.5)
	plt.fill_between(xaxis,curve_array4[:,0]-curve_array4[:,2],curve_array4[:,0]+curve_array4[:,2],color="lightgreen", alpha = 0.5)
	plt.fill_between(xaxis,curve_array5[:,0]-curve_array5[:,2],curve_array5[:,0]+curve_array5[:,2],color="orchid", alpha = 0.5)	

	# Axis-Naming and showing
	#plt.axes.Axes.set_xlim(0,1000) #only if needed
	#plt.axes.Axes.set_ylim(0,200) #only if needed
	plt.ylabel("Entropia")	 # you should change according to what you wish to plot
	plt.xlabel("Gerações")
	plt.legend()
	plt.show()

if whichplot == 2:

	curve_array1 = loadtxt(curveloc1,float,delimiter=";")
	curve_array2 = loadtxt(curveloc2,float,delimiter=";")
	curve_array3 = loadtxt(curveloc3,float,delimiter=";")
	curve_array4 = loadtxt(curveloc4,float,delimiter=";")
	curve_array5 = loadtxt(curveloc5,float,delimiter=";")

	curve_array6 = loadtxt(curveloc6,float,delimiter=";")
	curve_array7 = loadtxt(curveloc7,float,delimiter=";")
	curve_array8 = loadtxt(curveloc8,float,delimiter=";")
	curve_array9 = loadtxt(curveloc9,float,delimiter=";")
	curve_array10 = loadtxt(curveloc10,float,delimiter=";")



	# Now finally we're plotting the curves with the SD(or)SEM associated with it;
	
	xaxis = array(range(0,len(curve_array1[:,0])))
	
	# Means (change the label for your need):		
	plt.plot(xaxis, curve_array1[:,0], color="darkred",label="C3 / sample1")
	plt.plot(xaxis, curve_array2[:,0], color="darkblue",label="C3 / sample2")
	plt.plot(xaxis, curve_array3[:,0], color="darkorange",label="C3 / sample3")	
	plt.plot(xaxis, curve_array4[:,0], color="darkgreen",label="C3 / sample4")
	plt.plot(xaxis, curve_array5[:,0], color="darkmagenta",label="C3 / sample5")

	plt.plot(xaxis, curve_array6[:,0], color="darkred",label="C2 / sample1")
	plt.plot(xaxis, curve_array7[:,0], color="darkblue",label="C2 / sample2")
	plt.plot(xaxis, curve_array8[:,0], color="darkorange",label="C2 / sample3")	
	plt.plot(xaxis, curve_array9[:,0], color="darkgreen",label="C2 / sample4")
	plt.plot(xaxis, curve_array10[:,0], color="darkmagenta",label="C2 / sample5")



	# Plotting the SEMs together:
	plt.fill_between(xaxis,curve_array1[:,0]-curve_array1[:,2],curve_array1[:,0]+curve_array1[:,2],color="lightcoral", alpha = 0.5)
	plt.fill_between(xaxis,curve_array2[:,0]-curve_array2[:,2],curve_array2[:,0]+curve_array2[:,2],color="cornflowerblue", alpha = 0.5)
	plt.fill_between(xaxis,curve_array3[:,0]-curve_array3[:,2],curve_array3[:,0]+curve_array3[:,2],color="navajowhite", alpha = 0.5)
	plt.fill_between(xaxis,curve_array4[:,0]-curve_array4[:,2],curve_array4[:,0]+curve_array4[:,2],color="lightgreen", alpha = 0.5)
	plt.fill_between(xaxis,curve_array5[:,0]-curve_array5[:,2],curve_array5[:,0]+curve_array5[:,2],color="orchid", alpha = 0.5)	

	plt.fill_between(xaxis,curve_array6[:,0]-curve_array6[:,2],curve_array6[:,0]+curve_array6[:,2],color="lightcoral", alpha = 0.5)
	plt.fill_between(xaxis,curve_array7[:,0]-curve_array7[:,2],curve_array7[:,0]+curve_array7[:,2],color="cornflowerblue", alpha = 0.5)
	plt.fill_between(xaxis,curve_array8[:,0]-curve_array8[:,2],curve_array8[:,0]+curve_array8[:,2],color="navajowhite", alpha = 0.5)
	plt.fill_between(xaxis,curve_array9[:,0]-curve_array9[:,2],curve_array9[:,0]+curve_array9[:,2],color="lightgreen", alpha = 0.5)
	plt.fill_between(xaxis,curve_array10[:,0]-curve_array10[:,2],curve_array10[:,0]+curve_array10[:,2],color="orchid", alpha = 0.5)	


	# Axis-Naming and showing
	#plt.axes.Axes.set_xlim(0,1000) #only if needed
	#plt.axes.Axes.set_ylim(0,200) #only if needed
	plt.ylabel("Entropia")	 # you should change according to what you wish to plot
	plt.xlabel("Gerações")
	plt.legend()
	plt.show()



