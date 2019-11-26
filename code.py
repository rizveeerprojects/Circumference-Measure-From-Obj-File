#an implementation to detect a surface (2D, one coordinate fixed)
#way 1: 
	#take the points, perform angular sort 
	#then interpolate among points to get a perfect curve
	#find length between two points 
#way 2:
	#take the points find two points which will be lying at the furthest point (a)
	#again take the points find two point which are perpendicular two the previous 2 point and will make second best farthest distance (b)
	#result is pi * a * b



class CircumferenceMeasureFromObj:
	#A class to find circumference distance of a surface (2D, one co ordinate fixed other two are variables, ellipsical shape)
	def __init__(self,fixedCoordinate,fixedCoordinateValue):
		#fixed coordinate -> which coordinate is fixed 
		#fixedCoordinateValue -> value of the fixed coordinate 
		self.fixedCoordinate=fixedCoordinate
		self.fixedCoordinateValue = fixedCoordinateValue
		self.considerableVertixes=[] 

	def ReadObjFile(self,filename):
		#filename -> obj file name 
		try:
			with open(filename,'r') as file:
				lines=file.readlines()
				for l in lines:
					sp=l.split(' ')
					if(sp[0] == 'v'):
						#there lies vertex information 
						#line of consideration 
						x=float(sp[1])
						y=float(sp[2])
						z=float(sp[3]) 
						if(self.fixedCoordinate == 'y' and y == self.fixedCoordinateValue):
							self.considerableVertixes.append([x,y,z])
						elif(self.fixedCoordinate == 'z' and z == self.fixedCoordinateValue):
							self.considerableVertixes.append([x,y,z])
						elif(self.fixedCoordinate == 'x' and x == self.fixedCoordinateValue):
							self.considerableVertixes.append([x,y,z])
							

		except Exception as e:
			print(e) 



circumferenceMeasure = CircumferenceMeasureFromObj('y',-1.8604)
circumferenceMeasure.ReadObjFile('Model/Model.obj')
