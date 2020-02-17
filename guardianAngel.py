from shapely.geometry import Point
from shapely.geometry import Polygon, Point, LinearRing
from geopy import distance

coordinate = input("geoLoc : ")
coordinate = coordinate.split(",")
lat,lon = float(coordinate[0]),float(coordinate[1])
point = Point(lat,lon)
polygon = Polygon([(-7.765825, 110.378119),(-7.766006, 110.378752),(-7.776038, 110.374696),(-7.775900, 110.374171)])
pol_ext = LinearRing(polygon.exterior.coords)
if polygon.contains(point) == True:
	print("Safe")
else :
	print("Allert Rised")
	d = pol_ext.project(point)
	p = pol_ext.interpolate(d)
	closest_point_coords = list(p.coords)[0]
	dstn = distance.distance((closest_point_coords[0],closest_point_coords[1]), (lat, lon)).kilometers
	print("hiker at" ,"%.2f" %dstn, "KM offet from save heaven")
