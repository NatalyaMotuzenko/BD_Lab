class Buses (object):

#инициализация
    def __init__(self):
        self.buses = []

#добавление записи
    def add(self, bus):
        self.buses.append(bus)

#вывод всех записей на экран
    def __str__(self):
        fullInfo = ""
        for ind, bus in enumerate(self.buses):
            fullInfo = fullInfo + str(ind)+ ". " + str(bus) + "_____________________\n"
        return fullInfo

#дополнительная функция для вывода записи с учетом параметра
    def changeInfo (fullInfo, ind, bus):
        fullInfo = fullInfo + str(ind) + ". " + str(bus) + "_____________________\n"
        ind += 1
        return (fullInfo, ind)

#вывод записи с учетом параметра на экран
    def strParameter (self, parameter, index):
        fullInfo = ""
        ind = 0
        for bus in self.buses:
            # busID
            if bus.busID==parameter and index== "1":
                fullInfo, ind= Buses.changeInfo(fullInfo, ind, bus)
                break
            #model
            if bus.model==parameter and index== "2":
                fullInfo, ind = Buses.changeInfo(fullInfo, ind, bus)
                continue
            #driver
            if bus.driver==parameter and index== "3":
                fullInfo, ind= Buses.changeInfo(fullInfo, ind, bus)
                continue
            #numberOfSeats
            if bus.numberOfSeats==parameter and index== "4":
                fullInfo, ind = Buses.changeInfo(fullInfo, ind, bus)
                continue
        return fullInfo

#удаление записей по параметру
    def delete (self, parameter, index, plans):
        ind = 0
        while ind < len(self.buses):
            # busID
            if self.buses[ind].busID == parameter and index == "1":
                plans.delete(self.buses[ind].busID, 1) #удаление связанного плана
                self.buses.pop(ind)
                break
            # model
            if self.buses[ind].model == parameter and index == "2":
                plans.delete(self.buses[ind].busID, 1)
                self.buses.pop(ind)
                continue
            # driver
            if self.buses[ind].driver == parameter and index == "3":
                plans.delete(self.buses[ind].busID, 1)
                self.buses.pop(ind)
                continue
            # numberOfSeats
            if self.buses[ind].numberOfSeats == parameter and index == "4":
                plans.delete(self.buses[ind].busID, 1)
                self.buses.pop(ind)
                continue
            ind += 1  # подсчет количества пропущеных записей


#проверка существования busID
    def exist (self, parameter, ind):
        if ind == "1": #проверка существования busID
            for bus in self.buses:
                if bus.busID == parameter:
                    return True
            return False
        if ind == "2": #проверка существования model
            for bus in self.buses:
                if bus.model == parameter:
                    return True
            return False
        if ind == "3":
            for bus in self.buses: #проверка существования driver
                if bus.driver == parameter:
                    return True
            return False
        if ind == "4":
            for bus in self.buses:
                if bus.numberOfSeats == parameter: #проверка существования numberOfSeats
                    return True
            return False

#модификация записи, заданной ID
    def modification (self, busID, parameter, index):
        for bus in self.buses:
            if bus.busID == busID:
                if index==1:
                    bus.model = parameter
                    break
                if index==2:
                    bus.driver = parameter
                    break
                if index==3:
                    bus.numberOfSeats = parameter
                    break

    def lastID(self):
        try:
            return self.buses[len(self.buses)-1].busID
        except:
            return 1