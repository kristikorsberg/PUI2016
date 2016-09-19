from __future__ import print_function
import os
import json
import sys
import urllib2

url = str("http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + str(sys.argv[1]) + "&VehicleMonitoringDetailLevel=calls&LineRef=" + str(sys.argv[2]))
response = urllib2.urlopen(url)
data = response.read().decode("utf-8")
busData = json.loads(data)

i = 0
#print(json.dumps(busInfo, sort_keys=True, indent=2))

print('Latitude, Longitude, Stop Name, Stop Status')

countOfBuses = busData['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
for elem in countOfBuses:
    lat = countOfBuses[i]["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
    longitude = countOfBuses[i]["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
    closestStop = countOfBuses[i]["MonitoredVehicleJourney"]["OnwardCalls"]
    if len(closestStop) is 0:
        stopName="N/A"
        proximity="N/A"
    else:
        stopName = closestStop["OnwardCall"][0]["StopPointName"]
        proximity = closestStop["OnwardCall"][0]["Extensions"]["Distances"]["PresentableDistance"]
    print(str(lat) + ", " + str(longitude) + ", " + str(stopName) + ", " + str(proximity))
    i +=1