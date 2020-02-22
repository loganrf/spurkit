import numpy as np

class response:
	freqs = []
	levels = []
	
	def __init__(self, freqs, levels):
		self.freqs = freqs
		self.levels = levels
	
	@classmethod
	def singlePointResponse(freq, level):
		return response([freq],[level])
	
	def getClosestResponse(freq):
		freqLen = len(self.freqs)
		distance = []
		for j in range(freqLen):
			
			
	
	