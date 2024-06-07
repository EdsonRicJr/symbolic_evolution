# THIS FILE CONTAINS THE SIGNAL BASE THAT WE'RE GOING TO USE

#=========================================================================
from classes1 import SignalBase
#=========================================================================

# We are going to use a different signal base depending on the context, so for making it more clear, better than letting it in the main code, with several possibilities
# depending on the scenario that we're using, I've opted for creating this file which can be commented at will to choose which signal base we'll use;

#'''
#-------------------------------------------------------------------------
# SCENARIO 1:
# Namely: Ka, Ke, Ki

def importingSignals():
	#signal1, signal2, signal3, signal4 = SignalBase("Ka"), SignalBase("Ke"), SignalBase("Ki"), SignalBase("Ko")
	signal1, signal2, signal3, signal4, signal5 = SignalBase("Ka"), SignalBase("Ke"), SignalBase("Ki"), SignalBase("Ko"), SignalBase("Ku")
	#return [signal1, signal2, signal3, signal4]
	return [signal1, signal2, signal3, signal4, signal5]

#-------------------------------------------------------------------------
#'''

'''
#-------------------------------------------------------------------------
# SCENARIO 1: with extra signals;
def importingSignals():

	signal1, signal2, signal3, signal4, signal5 = SignalBase("Ka"), SignalBase("Ke"), SignalBase("Ki"), SignalBase("Ko"), SignalBase("Ku") 
	return [signal1, signal2, signal3, signal4, signal5]

#-------------------------------------------------------------------------
'''
'''
#-------------------------------------------------------------------------
# SCENARIO 2:
# Namely: Ka, Ke, Ki, Ko, Ku
#         Ha, He, Hi, Ho, Hu
#         Ta, Te, Ti, To, Tu
#	  Sa, Se, Si, So, Su

def importingSignals():

	signal1, signal2, signal3, signal4, signal5 = SignalBase("Ka"), SignalBase("Ke"), SignalBase("Ki"), SignalBase("Ko"), SignalBase("Ku") 
	signal6, signal7, signal8, signal9, signal10 = SignalBase("Ha"), SignalBase("He"), SignalBase("Hi"), SignalBase("Ho"), SignalBase("Hu")
	#signal6, signal7, signal8= SignalBase("Ha"), SignalBase("He"), SignalBase("Hi")
	#signal11, signal12, signal13, signal14, signal15 = SignalBase("Ta"), SignalBase("Te"), SignalBase("Ti"), SignalBase("To"), SignalBase("Tu")
	#signal16, signal17, signal18, signal19, signal20 = SignalBase("Sa"), SignalBase("Se"), SignalBase("Si"), SignalBase("So"), SignalBase("Su")	
	
	return [signal1, signal2, signal3, signal4, signal5, signal6, signal7, signal8, signal9, signal10]#, signal11, signal12, signal13, signal14, signal15, signal16, signal17, signal18, signal19, signal20]
	#return [signal1, signal2, signal3, signal4, signal5, signal6, signal7, signal8]
#-------------------------------------------------------------------------
'''

