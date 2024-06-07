# FILE CONTAINING, you guessed it, CLASSES!

#-------------------------------------------------------------------------
# Defining the Concepts Class:
class Concept:
	def __init__(self,name,category,probability):
		self.name = name
		self.category = category		
		self.probability = probability

#-------------------------------------------------------------------------
# Defining the SignalBase Class
class SignalBase:
	def __init__(self,name):
	#def __init__(self,name,probability):			
		self.name = name
		# self.probability = probability #It could be given a certain probability to certain Signals, or maybe a cost in complexity? But the pratical % won't be
		# defined here, but somewhere else when we apply the code.
	
#-------------------------------------------------------------------------
# Defining the Individuals' class "concepts", attached to a <> Signal <> that we'are going to use:
class IndividualConcepts:
	def __init__(self,name,sigrep1,sigrep1prob,sigrep2,sigrep2prob,sigrep3,sigrep3prob):
		self.name = name
		self.sigrep1 = sigrep1
		self.sigrep1prob = sigrep1prob
		self.sigrep2 = sigrep2
		self.sigrep2prob = sigrep2prob
		self.sigrep3 = sigrep3
		self.sigrep3prob = sigrep3prob

#-------------------------------------------------------------------------
# Creating each individual

class Individual:
	def __init__(self,name,evltn_points,concepts2signals,signals2concepts):
		self.name = name
		self.evltn_points = evltn_points
		self.concepts2signals = concepts2signals
		self.signals2concepts = signals2concepts

