# PUI2016

The tasks associated with Homework One are itemized below. I describe what I did to personally
contribute, and explain who I worked with.

#PUI2016 Homework 2 comprised of five separate assignments inclusive of extra credit. The 
#first was to read Appendix A in Allen Downey's "Think Python" book; the second was to 
#create a .csv file entitled  'show_bus_locations_kk3374', capturing the number of active 
#vehicles in a specified bus line and their respective current locations; the third 
#assignment was to create another .csv file entitled 'get_bus_info_kk3374', itemizing the 
#bus location, next bus stop, and distance from that next stop; the fourth assignment 
#required that I upload and modify a dataset from the CUSP DF in Compute; and the extra
#credit work built off of Assignment 3 in CUSP DF to plot a numerical value column
#against the dataset's date/time column. 

#I completed the reading independently.

#Initially, I wrote both Assignments 1 and 2 inside a .ipynb notebook. On Friday, September
#16, 2016, I copied everything to a text editor on my computer and saved the files as
#.csv. Jonathan Pichot told me to use the sys.argv as variables inside the file.
#I then replaced the raw_input() string variables I initially had as placeholders for
#MTA API Key and Bus Line Number with the sys.argv[<index number>], which worked. 
#so that the scripts could be run from the terminal. 
#Additionally, I used print statements a lot while doing this, and found a line of script 
#on Stack #Overflow, which indented everything in a more readable fashion. The line of 
# code that I modified for use on this file can be found here: 
#http://stackoverflow.com/questions/3229419/pretty-printing-nested-dictionaries-in-python

#For Assignment 1, I created a Python script entitled 'show_bus_locations_kk3374.csv', 
#which takes two arguments from the command line, <MTA API Key> and <Bus Number> and outputs
#the bus line number, the number of active buses, and each active bus' location with the
#formatting required in the homework instructions. Please see Figure 1 for a screenshot
#reference of the terminal commands and associated results for Assignment 1. 
#In order to complete Assignment 1, I used the acquiringdata.ipynb file inside the UINotebooks
#of the PUI2016 repository. Initially, I forgot to include the line to 'decode('utf-8'), which 
#initially made it impossible to locate certain nested dictionary values. Once I realized
#that I forgot that line of code, I added it and was able to call every value necessary to complete the
#assignment. I learned how to isolate different nested dictionaries and lists inside the
#JSON file by Google searching 'call nested dictionaries JSON Python', which produced a number
#of helpful StackOverflow discussions, such as 
#http://stackoverflow.com/questions/14227561/find-a-value-within-nested-json-dictionary-in-python.
#By trial and error, I learned that I had to call lists by index numbers and dictionaries
#by the key names. As I walked through the JSON file, I created variable names associated
#with the dictionary key I was currently looking at so that I could keep track of where I was
#inside the file. After viewing the 'Vehicle History' contents, I determined that each bus 
#was identifiable by calling a nested list index number inside the 'Vehicle History' dictionary. 
#I saved a variable named 'countOfBuses', which opened the file to the values of 'Vehicle
#History' and wrote a for loop to count 'i' number of lists (AKA number of buses) inside
#the 'Vehicle History' dictionary. I knew that the index identified each bus because nested
#inside each list was the dictionary called 'Monitored Vehicle Journey', whose label 
#sounded like a description of each vehicle's progress through the bus route. I confirmed
#this hunch by reading the MTA API guide here: 
#http://bustime.mta.info/wiki/Developers/SIRIMonitoredVehicleJourney
#At this point, I wasn't sure how to continue so I spoke with 
#Jonathan Pichot about what to do next. He confirmed that I was on the right track, by 
#diving into the file via nested dictionaries and lists and explained that I should 
#continue doing what I had been doing, but just use the for loop already created to find
#the latitude and longitude for each bus. At this point, I created two variables, 'lat'
#and 'longitude', and used the 'i' iterator to grab the location data for each active bus. 
#I then used a print statement to capture the bus line, the number of active buses, and
#each active bus' respective latitude and longitude. 

#On Friday, while I was at CUSP I was working in one of the conference rooms with 
#Alex Kalinin. He had a hard time getting started with Assignment 1, so I spent some time
#explaining the structure of a JSON file, and how to best navigate it. I also bounced
#some coding ideas off of Hrafnkell Hjorleifsson. We discussed the best ways to 
#iterate through the bus lists. 

#Assignment 2 felt straightforward after navigating the JSON file during Assignment 1.
#The process for navigating the JSON file didn't change, however it did require going
#deeper into the file to determine each bus' next stop and its 'PresentableDistance'
#inside the 'OnwardCall' dictionary. I determined the next stop by selecting the first
#element of the 'OnwardCalls' dictionary, and retrieving the 'StopPointName' of that first
#element. I also printed the 'PresentableDistance' value to show how far away the bus
#was from the next stop. The most challenging part of this assignment was eliminating
#the runtime errors, which occurred when either 'PresentableDistance' or 'StopPointName'
#were empty. To fix this error, I wrote an if statement, which replaced the empty
#values with 'N/A'. At this point, the code ran smoothly. 


#References for Assignment 3:
#In order to complete Assignment 3, I used Mohit Sharma's Pandas tutorial, and some this
#online reference: 
#http://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.DataFrame.plot.scatter.html
#I wasn't sure how to open the CUSP Data Facility inside Compute so I spoke with Graham
#Henke, who showed me how to access datafiles from the DF on the command line. 
#Once I had the DF accessible, I followed the directions for how to use Pandas from the
#UI Notesbooks. I worked on this independently. 
