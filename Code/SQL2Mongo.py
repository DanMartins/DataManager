################################################################
#% DataManager - IoTControl
#%
#%       Tool - Interface.
#%       DanMartins
#%       Implemented by Danilo Martins
#%       IoTControl reasearch project 
#%       São Paulo, 2020. 
#%
#%################################################################
import random, sys, time
import pymongo
import pprint
from datetime import datetime
import datetime as dt

#init
xstamp = datetime.now() #(2020,7,25,22,43,00)
print ("System started at ", xstamp)
count=0

#connection string
client = pymongo.MongoClient("mongodb+srv://username:password@add_here_your_mongodb_atlas_cloud?retryWrites=true&w=majority")
print(client.list_database_names())

#file handler
file = open("your_drive_here:\your_drive_here\your_file.sql", "rt")
if file:
    pass
else:
    raise NameError('Error - File not found') 

#db selection
db = client["Your_db_here"]

#loop - read SQL file to push data to MongoDB server
for x in file:
  count+=1
  #parse the file for SQL INSERT to MONGO insert_one
  y = "INSERT" in x
  if y:
    #identified SQL insertion then manipulate string to fit MongoDB insertOne
    x = x.replace("\"admin\".", "")
    x = x.replace("INSERT INTO", "")
    x = x.replace("VALUES", "")
    x = x.replace("(", "")
    x = x.replace(")", "")
    x = x.replace(";", "")
    x = x.replace("','", "\" \"")
    x = x.replace(", ", " ")
    x = x.replace(",", ".")
    x = x.replace("'", "\"")
    x = x.replace(" \"", "\"")
    x = x.replace(" \"", "\"")
    x = x.replace("\"\"", "\"")
    x = x.split('\"')
    
    #accomodate the string to fit
    del x[0]
    len_t = len(x)
    del x[len_t-1]
    
    #look for missing values in the manipulation - error
    if ((len(x) - 1)% 2 != 0):
       print ("Error - Value Not found")
       break
    
    #determine the aument of values to convert
    vars = int((len(x)-1)/2)
    
    #table name to collection name
    col= db[x[0]]
    
    #init the dictionarie for MongoDB insertion
    dict = {}
    for i in range(1, vars+1):
        y = x[i]
        y = y.strip(".")
        dtype = 0
        try:
           #check if the datatype is number
           z = float(x[i+vars])
        except ValueError:
           dtype = 1
        
        if dtype == 1:
           #check if the datatype is datetime
           try:
              date_time_obj = dt.datetime.strptime(x[i+vars], '%d/%m/%Y %H:%M:%S')
              z = date_time_obj
           except ValueError:
              #datatype is string
              z = x[i+vars]
        dict.update({y:z})

    #dictionarie ready push the data to MongoDB by command insert_one - print (dict)
    x = col.insert_one(dict)
    #print(x.inserted_id)
  
  #Parse the file for SQL CREATE TABLE to MONGO collection name - this is just proforma, not really needed.
  else:
    y = "CREATE TABLE" in x
    if y:
      x = x.split()
      x = x[2]
      x = x.replace("\"admin\".", "")
      x = x.strip("\"")
      col= db[x]
  print(count)

#As output print the list of databases and collections names in the MongoDB
print(client.list_database_names())
print(db.list_collection_names())

#end the file handler
file.close()

#end of the code.
xstamp = datetime.now() 
print ("System ends at ", xstamp)