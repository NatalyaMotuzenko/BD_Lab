import mysql.connector
import json
conn=mysql.connector.connect(user='root',password='candycola1199',host='localhost',database='fruits_and_vegetables_supply')
myCursor=conn.cursor()

myCursor.execute("SELECT * FROM fruits_and_vegetables_supply.fruits_and_vegetables;")
d = myCursor.fetchall()
with open('fruits_and_vegetables.json','w') as f:
    json.dump(d,f)
myCursor.execute("SELECT * FROM fruits_and_vegetables_supply.plantings;")
d = myCursor.fetchall()
with open('plantings.json','w') as f:
    json.dump(d,f)
myCursor.execute("SELECT * FROM fruits_and_vegetables_supply.storehouses;")
d = myCursor.fetchall()
with open('storehouses.json','w') as f:
    json.dump(d,f)
myCursor.execute("SELECT * FROM fruits_and_vegetables_supply.transport;")
d = myCursor.fetchall()
with open('transport.json','w') as f:
    json.dump(d,f)

myCursor.execute("SELECT * FROM fruits_and_vegetables_supply.supply_to_storehouses;")
d = myCursor.fetchall()

for i in range(len(d)):
    d[i]=(d[i][0],d[i][1],d[i][2],d[i][3],d[i][4],d[i][5].strftime('%Y,%m,%d'),d[i][6])
with open('supply_to_storehouses.json','w') as f:
    json.dump(d, f)
