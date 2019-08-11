# !/bin/python
# coding: utf-8

class RTFReader(object):
	"""docstring for RTFReader"""
	def __init__(self, arg):
		super(RTFReader, self).__init__()
		self.arg = arg

	@property
	def builder(self):
		return self._builder
	
	def ParseRTF(self, context):
		for x in context:
			if x.type == CHAR:
				self._builder.ConvertCharacter(x.Char)