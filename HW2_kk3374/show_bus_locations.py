from __future__ import print_function
import os
import sys
import json
import urllib2

#used script from HW2 resources repository: https://github.com/fedhere/UInotebooks/blob/master/dataWrangling/acquiringData.ipynb
url = str("http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + str(sys.argv[1]) + "&VehicleMonitoringDetailLevel=calls&LineRef=" + str(sys.argv[2]))
response = urllib2.urlopen(url)
data = response.read().decode("utf-8")
busData = json.loads(data)

countOfBuses = busData['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
print("Bus Line : " + str(sys.argv[2]))
print("Number of Active Buses : " + str(len(countOfBuses)))   

i = 0
for element in countOfBuses:
    lat = countOfBuses[i]["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
    longitude = countOfBuses[i]["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
    print("Bus " + str(i) + " is at latitude " + str(lat) + " and longitude " + str(longitude))
    i +=1