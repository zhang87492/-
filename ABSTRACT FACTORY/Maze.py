# /bin/python
# coding: utf-8

from abc import ABCMeta, abstractmethod

from enum import Enum, unique
import math

Direction = Enum('Direction',('North', 'South','East', 'West'))


class MapSite(metaclass=ABCMeta):
	@property
	def type(self):
		return self._type
	
class Door(MapSite):
	def __init__(self, r1 = 0, r2 = 0):
		self._type = 'd'
		self._r1 = r1
		self._r2 = r2

	@property
	def r1(self):
		return self._r1
	
	@property
	def r2(self):
		return self._r2
	
class Wall(MapSite):
	def __init__(self):
		self._type = 'w'

class Room(MapSite):
		"""docstring for Room"""
		def __init__(self, roomNO):
			super(Room, self).__init__()
			self._roomNumber = roomNO
			self._sides = {}
			self._type = roomNO

		@property
		def roomNumber(self):
			return self._roomNumber
		
		def getSide(self, Direction):
			return self._sides[Direction]

		def setSide(self, Direction, MapSite):
			self._sides[Direction] = MapSite

# __GLOBAL_REPLACE__ = '#'
__GLOBAL_REPLACE__ = ' '
class Maze():
	"""docstring for Maze"""
	def __init__(self, width, height):
		super(Maze, self).__init__()
		self._width = width
		self._height = height
		self._sz = [ [__GLOBAL_REPLACE__ for x in range(width * 2 + 1)] for x in range(height * 2 + 1)]


	def __str__(self):
		s=""
		for x in self._sz:
		 	for y in x:
		 		s=s+str(y)+" "
		 	s=s+"\n"
		return s

	__repr__ = __str__

	def AddRoom(self, room, north = Wall(), east = Wall(), south = Wall(), west = Wall()):
		n = room.roomNumber

		rh = math.floor(n/self._width) * 2 + 1
		rw = int(n%self._width) * 2 +1
		self._sz[rh][rw] = room.type
		if north :
		 	self._sz[rh-1][rw]= north.type
		if east:
		 	self._sz[rh][rw+1] = east.type
		if south :
			self._sz[rh+1][rw] = south.type
		if west :
			self._sz[rh][rw-1] = west.type

if __name__ == '__main__':
	# 1 x 2 迷宫
	m = Maze(2,1)
	r1 = Room(0)
	r2 = Room(1)
	d = Door(r1, r2)
	m.AddRoom(r1, east = d)
	m.AddRoom(r2, west = d)
	print(m)
