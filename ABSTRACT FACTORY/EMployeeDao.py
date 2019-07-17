# /bin/python
# coding: utf-8

from abc import ABCMeta, abstractmethod

import sys

class IDBConnection(metaclass=ABCMeta):
	"""docstring for IDB"""
	def __init__(self):
		print("class:", self.__class__.__name__," init")

	def connect(self):
		print("class:", self.__class__.__name__," func:", sys._getframe().f_code.co_name)

class IDBReader(metaclass=ABCMeta):
	def __init__(self):
		print("class:", self.__class__.__name__," init")

	def executeReador(self):
		print("class:", self.__class__.__name__," func:", sys._getframe().f_code.co_name)

class IDBCommand(metaclass=ABCMeta):
	def __init__(self):
		print("class:", self.__class__.__name__," init")

	def doCommand(self):
		print("class:", self.__class__.__name__," func:", sys._getframe().f_code.co_name)

class IDBFactory(metaclass=ABCMeta):
	def __init__(self):
		print("class:", self.__class__.__name__," func:", sys._getframe().f_code.co_name)


	@abstractmethod
	def createConnect(self):
		pass

	@abstractmethod
	def createReader(self):
		pass

	@abstractmethod
	def createCommand(self):
		pass

# -------------------Mysql的工厂-----------------------------

class MysqlConnect(IDBConnection):
	pass

class MysqlReader(IDBReader):
	pass

class MysqlCommand(IDBCommand):
	pass		

class MysqlDBFactory(IDBFactory):
	def createConnect(self):
		print("class:", self.__class__.__name__," func:", sys._getframe().f_code.co_name)
		return MysqlConnect()

	def createReader(self):
		print("class:", self.__class__.__name__," func:", sys._getframe().f_code.co_name)
		return MysqlReader()

	def createCommand(self):
		print("class:", self.__class__.__name__," func:", sys._getframe().f_code.co_name)
		return MysqlCommand()


# -------------------Oracl的工厂-----------------------------
class OraclConnect(IDBConnection):
	pass

class OraclReader(IDBReader):
	pass

class OraclCommand(IDBCommand):
	pass		

class OraclDBFactory(IDBFactory):
	def createConnect(self):
		print("class:", self.__class__.__name__," func:", sys._getframe().f_code.co_name)
		return OraclConnect()

	def createReader(self):
		print("class:", self.__class__.__name__," func:", sys._getframe().f_code.co_name)
		return OraclReader()

	def createCommand(self):
		print("class:", self.__class__.__name__," func:", sys._getframe().f_code.co_name)
		return OraclCommand()

if __name__ == '__main__':
	print("aaa")
	# factory = MysqlDBFactory()
	factory = OraclDBFactory()
	con = factory.createConnect()
	con.connect()
	com = factory.createCommand()
	com.doCommand()
	reader = factory.createReader()
	reader.executeReador()