import numpy as np


class Layer():
	def __init__(self, model, activation_function):
		"""
		Parameters:
		----------
		model: class
		    function with a result method which will be applied on the input

		activation_function: function
		    function which convert the model output to a probability
		"""
		self.activation_function = activation_function
		self.model = model

	def think(self, x):
		return self.model.result(x)

	def output(self, x):
		return self.activation_function(self.think(x))


