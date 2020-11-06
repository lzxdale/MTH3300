#******************************************************************************
# aubergine.py
#******************************************************************************
# Name: Zexiang Lin
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#https://www.igismap.com/haversine-formula-calculate-geographic-distance-earth/ earth equation
#
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#
import math
office_lat = 40.740230
office_lon = -73.983766
car1lat = float(input("Enter Latitude of car 1: "))
car1lon = float(input("Enter Longitude of car 1: "))
car1 = input("Car 1 occupied (y/n): ")
print("")
car2lat = float(input("Enter Latitude of car 2: "))
car2lon = float(input("Enter Longitude of car 2: "))
car2 = input("Car 2 occupied (y/n): ")
print("")
lat1diff = (office_lat - car1lat)*111.048
lat2diff = (office_lat - car2lat)*111.048
lon1diff = (office_lon - car1lon)*84.515
lon2diff = (office_lon - car2lon)*84.515
    # flat earth distance
dis1 = math.sqrt(lat1diff**2 + lon1diff**2) # distance from car 1
dis2 = math.sqrt(lat2diff**2 + lon2diff**2) # distance from car 2
print("Car 1 distance =", dis1)
print("Car 2 distance =", dis2)
if car1 == "y" and car2 == "n": # assuming the user will enter the correct symbol
    print("Car 1 should pick you up")
elif car1 == "n" and car2 == "y":
    print("Car 2 should pick you up")
elif car1 == "y" and car2 == "y":
    print("no car available")
else:
    if dis1 > dis2:
        print("Car 2 should pick you up")
    elif dis2 > dis1:
        print("Car 1 should pick you up")
    else:
        print("They are about the same distance, pick on u like")

##challenge## #use spherical geometry#
#info from:  https://www.igismap.com/haversine-formula-calculate-geographic-distance-earth/
#cos a = cos b * cos c + sin b * sin c * cos A
#One can derive Haversine formula to calculate distance between two as:
#a = sin²(ΔlatDifference/2) + cos(lat1).cos(lt2).sin²(ΔlonDifference/2)
#c = 2.atan2(√a, √(1−a))
#d = R.c
#ΔlatDifference = lat1 – lat2 (difference of latitude)
#ΔlonDifference = lon1 – lon2 (difference of longitude)
#R is radius of earth i.e 6371 KM or 3961 miles
#and d is the distance computed between two points.


def find_dis(latdiff, lat1, lat2, londiff):
    s1 = (math.sin(latdiff/2/180*math.pi))**2
    s2 = math.cos(lat1/180*math.pi)
    s3 = math.cos(lat2/180*math.pi)
    s4 = (math.sin(londiff/2/180*math.pi))**2
    a = s1 + s2*s3*s4
    a1 = math.sqrt(a)
    a2 = math.sqrt(1-a)
    c = 2*math.atan2(a1,a2)
    dis = c*6371
    return dis


lat1diff = (office_lat - car1lat) #the difference should remain in degree instead of distance
lat2diff = (office_lat - car2lat)
lon1diff = (office_lon - car1lon)
lon2diff = (office_lon - car2lon)

dis1 = find_dis(lat1diff, office_lat, car1lat, lon1diff)
dis2 = find_dis(lat2diff, office_lat, car2lat, lon2diff)
print("")
print("Below is calculated by spherical geometry")
print("Car 1 distance =", dis1)
print("Car 2 distance =", dis2)
if car1 == "y" and car2 == "n": # assuming the user will enter the correct symbol
    print("Car 1 should pick you up")
elif car1 == "n" and car2 == "y":
    print("Car 2 should pick you up")
elif car1 == "y" and car2 == "y":
    print("no car available")
else:
    if dis1 > dis2:
        print("Car 2 should pick you up")
    elif dis2 > dis1:
        print("Car 1 should pick you up")
    else:
        print("They are about the same distance, pick on u like")
