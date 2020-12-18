################################################################
#% DataManager - IoTControl
#%
#%       Tool - Insert Random.
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

#Edit the time you want the insertion running
DURATEMPO = 600

#Your statics constants here
Const1 = 0.0

#Start
xstamp = datetime.now() #(2020,7,19,18,47,00)
print ("System started at ", xstamp)
print ("will run till ", DURATEMPO, "seconds.")

#connection string
client = pymongo.MongoClient("mongodb+srv://username:password@add_here_your_mongodb_atlas_cloud?retryWrites=true&w=majority")
print(client.list_database_names())

#Your_db_here
db = client["Your_db_here"]

#Your_collection_here
col= db["Your_collection_here"] 

#Timer loop
Tfim = time.time()+DURATEMPO
Trot = time.time()

while (time.time() < Tfim):
    xstamp = datetime.now()
    ++indkey
    randuvar = random.uniform(0.0, 300.0)
    randvar = random.random()
    #Your_dictionary_here
    dict={"Pos1":indkey,"Pos2":randvar,"Pos3":randuvar,"Pos4":Const1,"Pos5":Const1,"Pos6":Const1,"Pos7":Const1,"Pos8":xstamp
    }
    #data insertion
    x = col.insert_one(dict)
    print(x.inserted_id) 

#end
print(client.list_database_names())
xstamp = datetime.now() 
print ("System ends at ", xstamp)
