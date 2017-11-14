import mysql.connector
import json

class Database:
    def connect(self):
        self.conn = mysql.connector.connect(user='root', password='candycola1199', host='localhost',
                                       database='fruits_and_vegetables_supply')

    def insert(self, newItem):
        self.myCursor = self.conn.cursor()
        self.myCursor.execute("INSERT INTO fruits_and_vegetables_supply.supply_to_storehouses (SupplyToStorehouseID, FruitAndVegetableID, Amount, PlantingID, StorehouseID, SupplyDate, TransportID) \
        VALUES(" + str(newItem)[1:-1] + ");")
        self.conn.commit()

    def update (self, newItem):
        self.myCursor = self.conn.cursor()
        self.myCursor.execute("UPDATE fruits_and_vegetables_supply.supply_to_storehouses set FruitAndVegetableID=" + str(newItem[1]) + ",Amount=" + str(newItem[2]) + \
                              ",PlantingID=" + str(newItem[3]) + ",StorehouseID=" + str(newItem[4]) + ",SupplyDate='" + str(newItem[5]) + "',TransportID=" + str(newItem[6]) + \
                              " WHERE SupplyToStorehouseID=" + str(newItem[0]) + ";")
        self.conn.commit()

    def deletion (self, newItem):
        self.myCursor = self.conn.cursor()
        self.myCursor.execute("DELETE FROM fruits_and_vegetables_supply.supply_to_storehouses WHERE SupplyToStorehouseID=" + str(newItem[0]) +";")
        self.conn.commit()

    def saveMainJson (self):
        self.myCursor = self.conn.cursor()
        self.myCursor.execute("SELECT * FROM fruits_and_vegetables_supply.supply_to_storehouses;")
        supply = self.myCursor.fetchall()
        for i in range(len(supply)):
            supply[i] = (supply[i][0], supply[i][1], supply[i][2], supply[i][3], supply[i][4], supply[i][5].strftime('%Y,%m,%d'), supply[i][6])
        return supply

    def query1 (self, date1, date2):
        self.myCursor = self.conn.cursor()
        self.myCursor.execute("SELECT * FROM fruits_and_vegetables_supply.supply_to_storehouses WHERE SupplyDate >= '" + str(date1) + "' AND SupplyDate <= '" + str(date2) + "' ORDER BY SupplyDate")
        supply = self.myCursor.fetchall()
        return  supply

    def query2 (self, petrol):
        self.myCursor = self.conn.cursor()
        self.myCursor.execute("SELECT Flue, Count(Petrol) FROM fruits_and_vegetables_supply.transport  WHERE Petrol =" + str(petrol) + " GROUP BY (Flue)")
        supply = self.myCursor.fetchall()
        return  supply

    def query3 (self, word):
        self.myCursor = self.conn.cursor()
        self.myCursor.execute("SELECT * FROM fruits_and_vegetables_supply.fruits_and_vegetables WHERE NOT MATCH(Description) AGAINST('" + word + "' IN BOOLEAN MODE);")
        fav  = self.myCursor.fetchall()
        return  fav

    def query4 (self,phrase):
        self.myCursor = self.conn.cursor()
        self.myCursor.execute("SELECT * FROM fruits_and_vegetables_supply.fruits_and_vegetables WHERE MATCH (Description) AGAINST ('\"" + phrase  + "\"' IN BOOLEAN MODE);")
        fav = self.myCursor.fetchall()
        return fav
