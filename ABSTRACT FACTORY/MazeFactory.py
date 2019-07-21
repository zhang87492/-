# /bin/python
# coding: utf-8

import sys
from Maze import Maze, Door, Room, Wall
	

class MazeFactory(object):
	"""docstring for MazeF"""
	def __init__(self):
		super(MazeFactory, self).__init__()
	
	def MakeMaze(self,w,h):
		return Maze(w,h)

	def MakeWall(self):
		return Wall()

	def MakeDoor(self, r1, r2):
		return Door(r1,r2)

	def MakeRoom(self, r1):
		return Room(r1)

class EnchantedRoom(Room):
	def __init__(self, roomNo):
		super(EnchantedRoom, self).__init__(roomNo)
		self._type = 'E'

class DoorNeedingSpell(Door):
	def __init__(self, r1, r2):
		super(DoorNeedingSpell, self).__init__(r1,r2)
		self._type = 'S'
		

class EnchantedMazeFactory(MazeFactory):
	"""docstring for EnchantedMazeFactory"""
	def __init__(self):
		super(EnchantedMazeFactory, self).__init__()

	def MakeRoom(self, no):
		return EnchantedRoom(no)

	def MakeDoor(self, r1, r2):
		return DoorNeedingSpell(r1,r2)

if __name__ == '__main__':
	factory = MazeFactory()
	factory = EnchantedMazeFactory()
	aMaze = factory.MakeMaze(2,1)
	r1 = factory.MakeRoom(0)
	r2 = factory.MakeRoom(1)
	d = factory.MakeDoor(r1, r2)
	aMaze.AddRoom(r1, east = d)
	aMaze.AddRoom(r2, west = d)
	print(aMaze)