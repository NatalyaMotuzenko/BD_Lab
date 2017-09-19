class Plans (object):

#инициализация
    def __init__(self):
        self.plans = []

#добавление записи
    def add(self, plan):
        self.plans.append(plan)

#вывод всех записей на экран
    def __str__(self):
        fullInfo = ""
        for ind, plan in enumerate(self.plans):
            fullInfo = fullInfo + str(ind)+ ". " + str(plan) + "_____________________\n"
        return fullInfo


    def delete (self, parameter, index):
        ind = 0
        while ind < len(self.plans):
            # busID
            if self.plans[ind].busID == parameter and index == "1":
                self.plans.pop(ind)
                continue
            # routeID
            if self.plans[ind].routeID == parameter and index == "2":
                self.plans.pop(ind)
                continue
            # dateOfLeaving
            if self.plans[ind].dateOfLeaving == parameter and index == "3":
                self.plans.pop(ind)
                continue
            ind += 1  # подсчет количества пропущеных записей

    def exist (self,  parameter, index):
        if index == "1":  # проверка существования busID
            for plan in self.plans:
                if plan.busID == parameter:
                    return True
            return False
        if index == "2":  # проверка существования busID
            for plan in self.plans:
                if plan.routeID == parameter:
                    return True
            return False
        if index == "3":  # проверка существования busID
            for plan in self.plans:
                if plan.dateOfLeaving == parameter:
                    return True
            return False