#%% Task 4.1 
#Create a Python file object
fileObj = open(file='data/raw/transshipment_vessels_20180723.csv',mode='r')

#Read the entire contents into a list object
lineList = fileObj.readlines()

#Release the link to the file objects
fileObj.close() #Close the file

#Assign the contents of the first line in, the header, to a variable
headerLineString = lineList[0]

#Print the contents of the header line
print(headerLineString)
#%% Task 4.2

#Split the headerLineString into a list of header items
headerItems = headerLineString.split(",")

#Capture the index values of the mmsi, shipname, and fleet_name values with variables
mmsi_idx = headerItems.index("mmsi")
name_idx = headerItems.index("shipname")
fleet_idx = headerItems.index("fleet_name")

#Print the index values
print(mmsi_idx,name_idx,fleet_idx)

#%% Task 4.3
#Create an empty dictionary
vesselDict = {}
#Iterate through all lines (except the header) in the data file:
for line in lineList[1:]:
#Split the data into values
   values = line.split(",")
#Extract the mmsi value from the list using the mmsi_idx value
   mmsi = values[mmsi_idx]
#Extract the fleet value
   fleet = values[fleet_idx]
#Adds info to the vesselDict dictionary; mmsi #s are the keys and the fleet country is the value
   vesselDict[mmsi] = fleet

#%% Task 4.4 Using the dictionary
#Assigning 258799000 to a "vesselID" variable
vesselID = "258799000"

#Using the vesselDict dictionary to lookup the fleet value for the vessel with the MMSI equal to the vesselID value.
print(vesselDict["258799000"])

#Creating statement
if vesselID in vesselDict:
    print(f"Vessel # {vesselID} flies the flag of {vesselDict[vesselID]}.")

#%% Task 5 Scripting Task
#Reading in Loitering Events csv file
fileObj2 = open(file='data/raw/loitering_events_20180723.csv',mode='r')

#Read the entire contents into a list object
loiterlineList = fileObj2.readlines()

#Closing the csv file
fileObj2.close()

#For loop that will iterate through all lines from the loitering csv file
for items in loiterlineList[1:]:
    #Creating boolean variables for use in the latitude and longitude rules
    equator_cross = False
    long_rule = False
    
    #Splitting lines from csv files into separate string entrys, delineating by ","
    entries = items.split(",")
    
    #Telling python where to look for the values for each variable
    t_mmsi = entries[0]
    start_lat = float(entries[1])
    start_long = float(entries[2])
    end_lat = float(entries[3])
    end_long = float(entries[4])
   
    #Creating equator cross rule
    if start_lat < 0 and end_lat > 0:
        equator_cross = True
   
    #Creating rule for longitude parameter
    if start_long >= 165 and start_long <= 170:
        long_rule = True
    
    #If latitude and longitude rules are met, printing statement using t_mmsi vlaue and vesselDict
    if equator_cross and long_rule:
        print(f"Vessel #{t_mmsi} flies the flag of {vesselDict[t_mmsi]}.")

# %%
