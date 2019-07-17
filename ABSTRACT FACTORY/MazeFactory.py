# /bin/python
# coding: utf-8


from abc import ABCMeta, abstractmethod

import sys

class Product(metaclass=ABCMeta):
	def __init__(self):
		print("class:", self.__class__.__name__," init")

	@abstractmethod
	def Desc(self):

class RefrigeratorProduct(Product):
	pass

class RefrigeratorFactory():
	



if __name__ == '__main__':
	# 想要一台冰箱
	product=
	# 