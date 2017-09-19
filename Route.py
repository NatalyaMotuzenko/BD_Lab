class Route (object):
#конструктор
    def __init__(self, routeID, wherefrom, where, distance, time):
        self.routeID = routeID
        self.wherefrom = wherefrom
        self.where = where
        self.distance = distance
        self.time = time

#вывод записи на экран
    def __str__(self):
        return "RouteID: %d\nWherefrom: %s\nWhere: %s\nDistance: %d km\nTime: %s hours\n"%\
               (self.routeID, self.wherefrom, self.where, self.distance, self.time)
