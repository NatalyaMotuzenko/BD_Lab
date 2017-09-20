class Bus(object):
    # конструктор
    def __init__(self, busID, model, driver, numberOfSeats):
        self.busID = busID
        self.model = model
        self.driver = driver
        self.numberOfSeats = numberOfSeats

    # вывод записи на экран
    def __str__(self):
        return "BusID: %d\nModel: %s\nDriver: %s\nNumber of seats: %d\n" % (
            self.busID, self.model, self.driver, self.numberOfSeats)
