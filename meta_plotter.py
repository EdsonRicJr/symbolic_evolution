#=========================================================================
from numpy import loadtxt, array, zeros, linspace
from pylab import scatter,plot,show,xlim,ylim,xlabel,ylabel,legend, title, figure
#=========================================================================

#-------------------------------------------------------------------------
# Plotting Efficiency;

x_gen = loadtxt("datafiles/eff_r0",int,usecols=(0),delimiter=";")
y_eff = loadtxt("datafiles/eff_r0",float,usecols=(1),delimiter=";")

figure()
scatter(x_gen,y_eff)
ylim(0.0,1.0)
xlim(0,1000)
xlabel("Gen")
ylabel("Efficiency (%)")

#-------------------------------------------------------------------------
# Plotting Mean Evolution Points;

x_gen = loadtxt("datafiles/mep_r0",int,usecols=(0),delimiter=";")
y_mep = loadtxt("datafiles/mep_r0",float,usecols=(1),delimiter=";")

figure()
scatter(x_gen,y_mep)
xlim(0,1000)
xlabel("Gen")
ylabel("Mean Evolution Points")


#-------------------------------------------------------------------------
# Plotting Concepts Per Word;

x_gen = loadtxt("datafiles/cpw_r0",int,usecols=(0),delimiter=";")
y_cpw = loadtxt("datafiles/cpw_r0",float,usecols=(1),delimiter=";")
	
figure()
scatter(x_gen,y_cpw)
xlabel("Gen")
ylabel("Concepts/Word")

#-------------------------------------------------------------------------
# Plotting Words / Concept (MEAN)

x_gen = loadtxt("datafiles/npc_r0",int,usecols=(0),delimiter=";")
raw_data = loadtxt("datafiles/npc_r0",float, delimiter=";")

zeta = len(raw_data[0,:])-1
theta = len(raw_data[:,0])

y_namesperconcept = zeros(theta,float)

for i in range(0,theta):
		#print(raw_data[i,1:])	
	y_namesperconcept[i]=sum(raw_data[i,1:])/zeta

# !!!!!!! # <><><><><><><><><><><><><>


group1_values = zeros(theta,float)
group2_values = zeros(theta,float)
group3_values = zeros(theta,float)
group4_values = zeros(theta,float)
group5_values = zeros(theta,float)

for i in range(0,theta):

	group1_values[i]=sum(raw_data[i,1:6])/5.0
	group2_values[i]=sum(raw_data[i,6:11])/5.0
	group3_values[i]=sum(raw_data[i,11:14])/3.0
	group4_values[i]=sum(raw_data[i,14:21])/7.0
	group5_values[i]=sum(raw_data[i,21:31])/10.0

# !!!!!!! # <><><><><><><><><><><><>
	
figure()
plot(x_gen,y_namesperconcept,"g-", label="mean")
plot(x_gen,group1_values,label="group1") # <><><><><>
plot(x_gen,group2_values,label="group2") # <><><><><>
plot(x_gen,group3_values,label="group3") # <><><><><>
plot(x_gen,group4_values,label="group4") # <><><><><>
plot(x_gen,group5_values,label="group5") # <><><><><>
xlabel("Gen")
ylabel("Mean Words / Concept")
legend()

#-------------------------------------------------------------------------
# Plotting Phrases Length;

x_gen = loadtxt("datafiles/genlen_r0",int,usecols=(0),delimiter=";")
y_gen = loadtxt("datafiles/genlen_r0",float,usecols=(1),delimiter=";")
y_unsuc = loadtxt("datafiles/ntlen_r0",float,usecols=(1),delimiter=";")
y_succe = loadtxt("datafiles/ytlen_r0",float,usecols=(1),delimiter=";")

figure()
plot(x_gen,y_gen,"g-",label="general")
plot(x_gen,y_unsuc,"c--",label="unsuccessfull")
plot(x_gen,y_succe,"r--",label="successfull")

xlabel("Gen")
ylabel("Mean Phrase Length (SU)")

title("Phrase's Length")
legend()

#-------------------------------------------------------------------------
# Plotting Mean Signal Units Per Concept

x_gen = loadtxt("datafiles/supc_r0",int,usecols=(0),delimiter=";")
raw_data = loadtxt("datafiles/supc_r0",float, delimiter=";")

zeta = len(raw_data[0,:])-1
theta = len(raw_data[:,0])

y_signunitperconcept = zeros(theta,float)

for i in range(0,theta):
	#print(raw_data[i,1:])	
	y_signunitperconcept[i]=sum(raw_data[i,1:])/zeta

# !!!!!!! # <><><><><><><><><><><><><>


group1_values = zeros(theta,float)
group2_values = zeros(theta,float)
group3_values = zeros(theta,float)
group4_values = zeros(theta,float)
group5_values = zeros(theta,float)

for i in range(0,theta):

	group1_values[i]=sum(raw_data[i,1:6])/5.0
	group2_values[i]=sum(raw_data[i,6:11])/5.0
	group3_values[i]=sum(raw_data[i,11:14])/3.0
	group4_values[i]=sum(raw_data[i,14:21])/7.0
	group5_values[i]=sum(raw_data[i,21:31])/10.0

# !!!!!!! # <><><><><><><><><><><><>

figure()
plot(x_gen,y_signunitperconcept,"r-",label="mean")
plot(x_gen,group1_values,label="group1") # <><><><><>
plot(x_gen,group2_values,label="group2") # <><><><><>
plot(x_gen,group3_values,label="group3") # <><><><><>
plot(x_gen,group4_values,label="group4") # <><><><><>
plot(x_gen,group5_values,label="group5") # <><><><><>
xlabel("Gen")
ylabel("Mean Signal Units/Concept")
legend()

#-------------------------------------------------------------------------
# Plotting MEAN ENTROPY;

x_gen = loadtxt("datafiles/ent_r0",int,usecols=(0),delimiter=";")
raw_data = loadtxt("datafiles/ent_r0",float, delimiter=";")

zeta = len(raw_data[0,:])-1
theta = len(raw_data[:,0])

y_mean_entropy = zeros(theta,float)

for i in range(0,theta):
	#print(raw_data[i,1:])	
	y_mean_entropy[i]=sum(raw_data[i,1:])/zeta

# !!!!!!! # <><><><><><><><><><><><><>


group1_values = zeros(theta,float)
group2_values = zeros(theta,float)
group3_values = zeros(theta,float)
group4_values = zeros(theta,float)
group5_values = zeros(theta,float)

for i in range(0,theta):

	group1_values[i]=sum(raw_data[i,1:6])/5.0
	group2_values[i]=sum(raw_data[i,6:11])/5.0
	group3_values[i]=sum(raw_data[i,11:14])/3.0
	group4_values[i]=sum(raw_data[i,14:21])/7.0
	group5_values[i]=sum(raw_data[i,21:31])/10.0

# !!!!!!! # <><><><><><><><><><><><>

figure()
plot(x_gen,y_mean_entropy,"b-",label="mean")
plot(x_gen,group1_values,label="group1") # <><><><><>
plot(x_gen,group2_values,label="group2") # <><><><><>
plot(x_gen,group3_values,label="group3") # <><><><><>
plot(x_gen,group4_values,label="group4") # <><><><><>
plot(x_gen,group5_values,label="group5") # <><><><><>
xlabel("Gen")
ylabel("Mean Entropy for Concepts")
legend()

#-------------------------------------------------------------------------
# SHOW ALL
show()
#-------------------------------------------------------------------------
