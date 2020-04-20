from shapely.geometry import Polygon, Point, LinearRing
from geopy import distance
import paho.mqtt.client as mqtt
#import socket, time, netifaces,random
import time, json, string, time
import paho.mqtt.publish as publish

print("=>","God is the one who give us prosper, all credit shall be for his behalf. Thank to wimbuh_adi the one who orchestarted this access point, that so i can help you today :)")

def getPhysicalnetworkIP():
    return socket.gethostname()
def encodeGmap(destination):
	return "https://www.google.com/maps/dir/?api=1&destination=%s"%destination
def colorCode(distance):
	if distance <= 0.5:
		return "yellow"
	elif distance > 0.5 and distance < 1.5:
		return "orange"
	elif distance >= 1.5:
		return "red"
#HOST = getPhysicalnetworkIP()  # Standard loopback interface address (localhost)
#PORT = 1234        # Port to listen on (non-privileged ports are > 1023)

def talkToMe_Son(coordinate):
	coordinate = '{"lat":-7.662103, "lng":109.653015}'
	print("==========PAKAI WRITTEN TELEMETRI=========")
	coorDict = json.loads(coordinate)
	strCoordinate = coorDict["lat"],coorDict["lng"]
	strCoordinate = coordinate.replace(" ","")
	print(type(coorDict))
	#coorStr =  (coorDict["lat"],",",coorDict["lng"])
	#coorStr = (coorDict["lat"]+","+coorDict["lng"])
	#print(coorStr)
	#coordinate = input("geoLoc : ")
	#print("hallo my son")
	
	
	#strCoordinate = coordinate.replace(" ","")
	#coordinate = coordinate.split(",")
	#lat,lon = float(coordinate[0]),float(coordinate[1])
	lat,lon = float(coorDict["lat"]),float(coorDict["lng"])
	
	
	'''
	print(type(coordinate))
	print(type(coorDict))
	lat = coorDict["lat"]
	lon = coorDict["lng"]
	'''

	point = Point(lat,lon)
	polygon = Polygon([(-7.765825, 110.378119),(-7.766006, 110.378752),(-7.776038, 110.374696),(-7.775900, 110.374171)])
	pol_ext = LinearRing(polygon.exterior.coords)
	if polygon.contains(point) == True:
		print("=>","He's on the correct path\n")
	else :
		print("=>","Allert Rised")
		d = pol_ext.project(point)
		p = pol_ext.interpolate(d)
		closest_point_coords = list(p.coords)[0]
		dstn = distance.distance((closest_point_coords[0],closest_point_coords[1]), (lat, lon)).kilometers
		print("=>","hiker at" ,"%.2f" %dstn, "KM offet from save heaven")
		print("=>","Now broadcasting DISTRESS SIGNAL to all Stakeholders")
		theCollor = colorCode(dstn)
		
		url = encodeGmap(strCoordinate)

		theMessage = "Code %s is declared. Hiker is detected %.3f KM off from safe haven. All personals is advised to review the possible rescue route. %s"%(theCollor, dstn,url)
		print("=>","\""+theMessage+"\"")
		
		#s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#s.connect((HOST, PORT))
		try :
			print("connecting to WHATSAPP server")
			time.sleep(1)
			message = theMessage
			publish.single("GuardianAngel/Distress", payload=message, hostname="localhost", port=1883)
			#print(message)
			#s.sendall(message.encode('utf-8'))
			#data = s.recv(1024)
			#print('Reply : ', repr(data))
			print("=>","\"Wish they can be there on time\"")
		except ConnectionAbortedError: 
			pass
		except OSError:
			pass
		except KeyboardInterrupt:
			print("quiting by KeyboardInterrupt")
			s.close()
			pass
		finally :
			print("=>","broadcast message is sended to broker\n")
			#time.sleep(1.5)

def printData(data):
	print("=>","coordinate: "+data)
	print("=>","sending data to angel")
	print(type(data))
	talkToMe_Son(data)
	
def on_subscribe(client, userdata, mid, granted_qos):
	print("=>","MQTT Subscribed: "+str(mid)+" "+str(granted_qos),"\n\n")
	
def on_connect(client, userdata, flags, rc):
	#print ("Connected with result code "+str(rc))
	'''client.subscribe("topic/test")'''
	client.subscribe("GuardianAngel", qos=2)
	print("=>","Now that I can hear from my servant, you -my sons, can restasure")
	#client.subscribe("kucing", qos=1)
	#client.subscribe("aaa", qos=1)
	
def on_message(client, userdata, msg):
	'''on_printJson(msg)'''
	'''if msg.payload.decode() == "hello world!":'''
	'''print "Yes!"'''
	#print(datetime.now()+timedelta(hours=7))
	printData(msg.payload.decode())
	#print(datetime.now())
	'''client.disconnect()'''

client = mqtt.Client()
#client.connect("10.33.109.82",1883,60)
client.connect("localhost",1883,60)
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_message = on_message
client.loop_forever()
		
