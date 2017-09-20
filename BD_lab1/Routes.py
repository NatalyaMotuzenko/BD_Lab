class Routes(object):
    # инициализация
    def __init__(self):
        self.routes = []

    # добавление записи
    def add(self, route):
        self.routes.append(route)

    # вывод всех записей на экран
    def __str__(self):
        fullInfo = ""
        for ind, route in enumerate(self.routes):
            fullInfo = fullInfo + str(ind) + ". " + str(route) + "_____________________\n"
        return fullInfo

    # дополнительная функция для вывода записи с учетом параметра
    def changeInfo(fullInfo, ind, route):
        fullInfo = fullInfo + str(ind) + ". " + str(route) + "_____________________\n"
        ind += 1
        return (fullInfo, ind)

    # вывод записи с учетом параметра на экран
    def strParameter(self, parameter, index):
        fullInfo = ""
        ind = 0
        for route in self.routes:
            # routeID
            if route.routeID == parameter and index == "1":
                fullInfo, ind = Routes.changeInfo(fullInfo, ind, route)
                break
            # wherefrom
            if route.wherefrom == parameter and index == "2":
                fullInfo, ind = Routes.changeInfo(fullInfo, ind, route)
                continue
            # where
            if route.where == parameter and index == "3":
                fullInfo, ind = Routes.changeInfo(fullInfo, ind, route)
                continue
            # distance
            if route.distance == parameter and index == "4":
                fullInfo, ind = Routes.changeInfo(fullInfo, ind, route)
                continue
            # time
            if route.time == parameter and index == "5":
                fullInfo, ind, = Routes.changeInfo(fullInfo, ind, route)
                continue
        return fullInfo

    def exist(self, parameter, ind):
        if ind == "1":  # проверка существования routeID
            for route in self.routes:
                if route.routeID == parameter:
                    return True
            return False
        if ind == "2":  # проверка существования wherefrom
            for route in self.routes:
                if route.wherefrom == parameter:
                    return True
            return False
        if ind == "3":  # проверка существования where
            for route in self.routes:
                if route.where == parameter:
                    return True
            return False
        if ind == "4":  # проверка существования distance
            for route in self.routes:
                if route.distance == parameter:
                    return True
            return False
        if ind == "5":  # проверка существования time
            for route in self.routes:
                if route.time == parameter:
                    return True
            return False

            # удаление записей по параметру

    def delete(self, parameter, index, plans):
        ind = 0
        while ind < len(self.routes):
            # routeID
            if self.routes[ind].routeID == parameter and index == "1":
                plans.delete(self.routes[ind].routeID, "2")  # удаление связанного плана
                self.routes.pop(ind)
                break
            # wherefrom
            if self.routes[ind].wherefrom == parameter and index == "2":
                plans.delete(self.routes[ind].routeID, "2")  # удаление связанного плана
                self.routes.pop(ind)
                continue
            # where
            if self.routes[ind].where == parameter and index == "3":
                plans.delete(self.routes[ind].routeID, "2")  # удаление связанного плана
                self.routes.pop(ind)
                continue
            ind += 1  # подсчет количества пропущеных записей

            # модификация записи, заданной ID

    def modification(self, routeID, parameter, index):
        for route in self.routes:
            if route.routeID == routeID:
                if index == 1:
                    route.wherefrom = parameter
                    break
                if index == 2:
                    route.where = parameter
                    break
                if index == 3:
                    route.distance = parameter
                    break
                if index == 4:
                    route.time = parameter
                    break

    def lastID(self):
        try:
            return self.routes[len(self.routes) - 1].routeID
        except:
            return 1
