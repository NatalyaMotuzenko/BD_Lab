class Plan (object):
#конструктор
    def __init__(self, busID, routeID, dateOfLeaving):
        self.busID = busID
        self.routeID = routeID
        self.dateOfLeaving = dateOfLeaving

    # вывод записи на экран
    def __str__(self):
        return "BusID: %d\nRouteID: %d\nDate Of Leaving: %s\n" % (
        self.busID, self.routeID, self.dateOfLeaving)

