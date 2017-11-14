import pickle
import sys
from Bus import Bus
from Buses import Buses
from Route import Route
from Routes import Routes
from Plan import Plan
from Plans import Plans

buses = Buses()
routes = Routes()
plans = Plans()


def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


"""buses .add(Bus(1, "BMW", "Panov", 16))
buses.add(Bus(2," Mercedes-Benz", "Miller", 18))
buses.add(Bus(3," Mercedes-Benz", "Kolesnyk", 25))
buses.add(Bus(4,"BMW", "Zapara", 30))
buses.add(Bus(5,"Ford", "Volobyev", 15))
with open('Buses.txt', 'wb') as f: pickle.dump(buses, f)

routes.add(Route(1, "Kiev", "Dnepr", 453, 6))
routes.add(Route(2, "Kiev", "Odessa", 475, 6))
routes.add(Route(3, "Kiev", "Lviv", 540, 8))
routes.add(Route(4, "Lviv", "Odessa", 795, 12))
routes.add(Route(5, "Odessa", "Dnepr", 522, 10))
routes.add(Route(6, "Dnepr", "Lviv", 1000, 15))
with open('Routes.txt', 'wb') as f: pickle.dump(routes, f)

plans.add(Plan(1,1, "29.09.17 18:45"))
plans.add(Plan(1,1, "19.09.17 12:20"))
plans.add(Plan(5,3, "29.09.17 17:00"))
plans.add(Plan(1,2, "24.09.17 15:55"))
plans.add(Plan(4,3, "02.10.17 06:00"))
plans.add(Plan(3,1, "20.09.17 13:05"))
plans.add(Plan(2,4, "22.09.17 14:15"))
plans.add(Plan(2,5, "27.09.17 16:00"))
plans.add(Plan(1,6, "19.09.17 20:20"))
with open('Plans.txt', 'wb') as f: pickle.dump(plans, f)"""


def mainMenu(buses, routes, plans):
    chooseFlag = False
    print("\t\nWelcome to the menu!\nChoose the section:\n1.Buses\n2.Routes\n3.Plans\n"
          "4.Save data to the file\n5.Load data from the file\n0.Exit")
    while (chooseFlag == False):
        choose = input('Your choice: ')
        if (choose == "1"):
            chooseFlag = True
            funcBuses(buses)
        elif (choose == "2"):
            chooseFlag = True
            funcRoutes(routes)
        elif (choose == "3"):
            chooseFlag = True
            funcPlans(plans)
        elif (choose == "4"):
            with open('Buses.txt', 'wb') as f:
                pickle.dump(buses, f)
            with open('Routes.txt', 'wb') as f:
                pickle.dump(routes, f)
            with open('Plans.txt', 'wb') as f:
                pickle.dump(plans, f)
            print("Successfully saved!")
        elif (choose == "5"):
            try:
                with open('Buses.txt', 'rb') as file:
                    busFile = pickle.load(file)
                with open('Routes.txt', 'rb') as file:
                    routeFile = pickle.load(file)
                with open('Plans.txt', 'rb') as file:
                    planFile = pickle.load(file)
                for bus in busFile.buses:
                    buses.add(Bus(bus.busID, bus.model, bus.driver, bus.numberOfSeats))
                for route in routeFile.routes:
                    routes.add(Route(route.routeID, route.wherefrom, route.where, route.distance, route.time))
                for plan in planFile.plans:
                    plans.add(Plan(plan.busID, plan.routeID, plan.dateOfLeaving))
                print("Successfully load!")
            except:
                print("One of the files is emply")
        elif (choose == "0"):
            chooseFlag = True
            sys.exit()
        else:
            print("You input wrong symbol! You can input only 0,1,2,3,4,5. Try again.")


def funcBuses(buses):
    print("\t\nWelcome to the section Buses!\nChoose the option:\n1.Display all buses\n"
          "2.Display buses according to the specified filed\n3.Add the bus\n4.Edit a bus by ID\n"
          "5.Delete the bus according to the specified filed\n6.Go back\n0.Exit")
    while (True):
        choose = input('Your choice: ')
        if (choose == "1"):
            print("\n***Display all buses***")
            print(buses)
            if (input("Enter 1 to continue. Enter any other value to exit: ") == '1'):
                funcBuses(buses)
            else:
                sys.exit()

        elif (choose == "2"):
            funcstrBusParameter(buses)

        elif (choose == "3"):
            busID = buses.lastID()
            model = input("Model = ")
            driver = input("Driver = ")
            while (True):
                numberOfSeats = input("Number of seats = ")
                if (isint(numberOfSeats)):
                    numberOfSeats = int(numberOfSeats)
                    break
                else:
                    print("Number of seats can be only a number.")
                    if (input("Enter 1 to try again. Enter any other value to go back: ") == '1'):
                        continue
                    else:
                        funcBuses(buses)
            buses.add(Bus(busID + 1, model, driver, numberOfSeats))
            print("You add the bus.")
            if (input("Enter 1 to continue. Enter any other value to exit: ") == '1'):
                funcBuses(buses)
            else:
                sys.exit()

        elif (choose == "4"):
            funcEditBus(buses)

        elif (choose == "5"):
            funcDeleteBus(buses, plans)

        elif (choose == "6"):
            mainMenu(buses, routes, plans)

        elif (choose == "0"):
            sys.exit()

        else:
            print("You input wrong symbol! You can input only 0,1,2,3,4,5,6. Try again.")


def funcRoutes(routes):
    chooseFlag = False
    print("\t\nWelcome to the section Routes!\nChoose the option:\n1.Display all routes\n"
          "2.Display routes according to the specified filed\n3.Add the route\n4.Edit a route by ID\n"
          "5.Delete the route according to the specified filed\n6.Go back\n0.Exit")
    while (chooseFlag == False):
        choose = input('Your choice: ')
        if (choose == "1"):
            chooseFlag = True
            print("\n***Display all routes***")
            print(routes)
            if (input("Enter 1 to continue. Enter any other value to exit: ") == '1'):
                funcRoutes(routes)
            else:
                sys.exit()

        elif (choose == "2"):
            chooseFlag = True
            funcstrRouteParameter(routes)

        elif (choose == "3"):
            chooseFlag = True
            routeID = routes.lastID()
            wherefrom = input("Wherefrom = ")
            where = input("Where = ")
            while (True):
                distance = input("Distance = ")
                if (isint(distance)):
                    distance = int(distance)
                    break
                else:
                    print("Distance can be only a number.")
                    if (input("Enter 1 to try again. Enter any other value to go back: ") == '1'):
                        continue
                    else:
                        funcRoutes(routes)
            while (True):
                time = input("Time = ")
                if (isint(time)):
                    distance = int(time)
                    break
                else:
                    print("Time can be only a number.")
                    if (input("Enter 1 to try again. Enter any other value to go back: ") == '1'):
                        continue
                    else:
                        funcRoutes(routes)
            routes.add(Route(routeID + 1, wherefrom, where, distance, time))
            print("You add the route.")
            if (input("Enter 1 to continue. Enter any other value to exit: ") == '1'):
                funcRoutes(routes)
            else:
                sys.exit()

        elif (choose == "4"):
            chooseFlag = True
            funcEditeRoute(routes)

        elif (choose == "5"):
            chooseFlag = True
            funcDeleteRoute(routes, plans)

        elif (choose == "6"):
            mainMenu(buses, routes, plans)

        elif (choose == "0"):
            sys.exit()

        else:
            print("You input wrong symbol! You can input only 0,1,2,3,4,5,6. Try again.")


def funcPlans(plans):
    print("\t\nWelcome to the section Plans!\nChoose the option:\n1.Display all plans\n"
          "2.Delete the plan according to the specified filed\n3.Go back\n0.Exit")
    while (True):
        choose = input('Your choice: ')
        if (choose == "1"):
            print("\n***Display all plans***")
            print(plans)
            if (input("Enter 1 to continue. Enter any other value to exit: ") == '1'):
                funcPlans(plans)
            else:
                sys.exit()
        elif (choose == "2"):
            funcDeletePlan(plans)
        elif (choose == "3"):
            mainMenu(buses, routes, plans)
        elif (choose == "0"):
            sys.exit()
        else:
            print("You input wrong symbol! You can input only 0,1,2,3. Try again.")


def funcstrParameterHelp(objects, strParametr, index, busOrRoute):
    while (True):
        parameter = input('Input %s: ' % strParametr)
        if (index == "1" or index == "4" or index == "5"):
            parameter = int(parameter)
        if (objects.exist(parameter, index)):
            print("\n***Display buses with %s = %s***" % (strParametr, parameter))
            print(objects.strParameter(parameter, index))
            if (input("Enter 1 to continue. Enter any other value to exit: ") == '1'):
                if busOrRoute == "bus":
                    funcstrBusParameter(objects)
                if busOrRoute == "route":
                    funcstrRouteParameter(objects)
            else:
                sys.exit()
        else:
            print("This %s does not exist." % strParametr)
            if (input("Enter 1 to try again. Enter any other value to go back: ") == '1'):
                continue
            else:
                if busOrRoute == "bus":
                    funcstrBusParameter(objects)
                if busOrRoute == "route":
                    funcstrRouteParameter(objects)


def funcstrBusParameter(buses):
    print("\t\nChoose the parameter:\n1.BusID\n2.Model\n3.Driver\n4.Number Of Seats\n5.Go back\n0.Exit")
    while (True):
        index = input('Your choice: ')
        if (index == "1"):
            while (True):
                try:
                    funcstrParameterHelp(buses, "busID", index, "bus")
                    break
                except ValueError:
                    print("BusID can be only a number.")
                    if (input("Enter 1 to try again. Enter any other value to go back: ") == '1'):
                        continue
                    else:
                        funcstrBusParameter(buses)

        elif (index == "2"):
            funcstrParameterHelp(buses, "model", index, "bus")

        elif (index == "3"):
            funcstrParameterHelp(buses, "driver", index, "bus")

        elif (index == "4"):
            while (True):
                try:
                    funcstrParameterHelp(buses, "number of seats", index, "bus")
                    break
                except ValueError:
                    print("Number of seats can be only a number.")
                    if (input("Enter 1 to try again. Enter any other value to go back: ") == '1'):
                        continue
                    else:
                        funcstrBusParameter(buses)

        elif (index == "5"):
            funcBuses(buses)

        elif (index == "0"):
            sys.exit()

        else:
            print("You input wrong symbol! You can input only 0,1,2,3,4,5. Try again.")


def funcstrRouteParameter(routes):
    print("\t\nChoose the parameter:\n1.RouteID\n2.Wherefrom\n3.Where\n4.Distance\n5.Time\n6.Go back\n0.Exit")
    while (True):
        index = input('Your choice: ')
        if (index == "1"):
            while (True):
                try:
                    funcstrParameterHelp(routes, "routeID", index, "route")
                    break
                except ValueError:
                    print("RouteID can be only a number.")
                    if (input("Enter 1 to try again. Enter any other value to go back: ") == '1'):
                        continue
                    else:
                        funcstrRouteParameter(routes)

        elif (index == "2"):
            funcstrParameterHelp(routes, "wherefrom", index, "route")

        elif (index == "3"):
            funcstrParameterHelp(routes, "where", index, "route")

        elif (index == "4"):
            while (True):
                try:
                    funcstrParameterHelp(routes, "distance", index, "route")
                    break
                except ValueError:
                    print("RouteID can be only a number.")
                    if (input("Enter 1 to try again. Enter any other value to go back: ") == '1'):
                        continue
                    else:
                        funcstrRouteParameter(routes)

        elif (index == "5"):
            while (True):
                try:
                    funcstrParameterHelp(routes, "time", index, "route")
                    break
                except ValueError:
                    print("Time can be only a number.")
                    if (input("Enter 1 to try again. Enter any other value to go back: ") == '1'):
                        continue
                    else:
                        funcstrRouteParameter(routes)

        elif (index == "6"):
            funcRoutes(routes)

        elif (index == "0"):
            sys.exit()

        else:
            print("You input wrong symbol! You can input only 0,1,2,3,4,5,6. Try again.")


def funcEditBus(buses):
    busID = input('Input busID: ')
    if (isint(busID)):
        busID = int(busID)
        if (buses.exist(busID, "1")):
            print("Changeable parameter:\n1.Model\n2.Driver\n3.Number of seats\n4.Go back\n0.Exit")
            while (True):
                index = input('Your choice:')
                if (index == "1"):
                    model = input('Input Model: ')
                    buses.modification(busID, model, 1)
                    break
                elif (index == "2"):
                    driver = input('Input Driver: ')
                    buses.modification(busID, driver, 2)
                    break
                elif (index == "3"):
                    while (True):
                        try:
                            numberOfSeats = int(input('Input number of seats: '))
                            buses.modification(busID, numberOfSeats, 3)
                            break
                        except ValueError:
                            print("Number of seats can be only a number. Try again.")
                    break
                elif (index == "4"):
                    funcBuses(buses)
                elif (index == "0"):
                    sys.exit()
                else:
                    print("You input wrong symbol! You can input only 0,1,2,3,4. Try again.")

        else:
            print("This busID does not exist.")
            if (input("Enter 1 to try again. Enter any other value to go back: ") == '1'):
                funcEditBus(buses)
            else:
                funcBuses(buses)
    else:
        print("BusID can be only a number.")
        if (input("Enter 1 to try again. Enter any other value to go back: ") == '1'):
            funcEditBus(buses)
        else:
            funcBuses(buses)
    print("You edit the bus with ID=%d." % busID)
    if (input("Enter 1 to continue. Enter any other value to exit: ") == '1'):
        funcBuses(buses)
    else:
        sys.exit()


def funcEditeRoute(routes):
    routeID = input('Input routeID: ')
    if (isint(routeID)):
        routeID = int(routeID)
        if (routes.exist(routeID, "1")):
            print("Changeable parameter:\n1.Wherefrom\n2.Where\n3.Distance\n4.Time\n5.Go back\n0.Exit")
            while (True):
                index = input('Your choice:')
                if (index == "1"):
                    wherefrom = input('Input Wherefrom: ')
                    routes.modification(routeID, wherefrom, 1)
                    break
                elif (index == "2"):
                    where = input('Input Where: ')
                    routes.modification(routeID, where, 2)
                    break
                elif (index == "3"):
                    while (True):
                        try:
                            distance = int(input('Input Distance: '))
                            routes.modification(routeID, distance, 3)
                            break
                        except ValueError:
                            print("Distance can be only a number. Try again.")
                    break
                elif (index == "4"):
                    while (True):
                        try:
                            time = int(input('Input Time: '))
                            routes.modification(routeID, time, 4)
                            break
                        except ValueError:
                            print("Time can be only a number. Try again.")
                    break
                elif (index == "5"):
                    funcRoutes(routeID)
                elif (index == "0"):
                    sys.exit()
                else:
                    print("You input wrong symbol! You can input only 0,1,2,3,4,5. Try again.")

        else:
            print("This routeID does not exist.")
            if (input("Enter 1 to try again. Enter any other value to go back: ") == '1'):
                funcEditeRoute(routes)
            else:
                funcRoutes(routes)
    else:
        print("routeID can be only a number.")
        if (input("Enter 1 to try again. Enter any other value to go back: ") == '1'):
            funcEditeRoute(routes)
        else:
            funcRoutes(routes)
    print("You edit the route with ID=%d." % routeID)
    if (input("Enter 1 to continue. Enter any other value to exit: ") == '1'):
        funcRoutes(routes)
    else:
        sys.exit()


def funcDeleteHelp(objects, plans, strParametr, index, busOrRoute):
    while (True):
        parameter = input('Input %s: ' % strParametr)
        if (index == "1" or index == "4"):
            parameter = int(parameter)
        if (objects.exist(parameter, index)):
            print("\n***These records were successfully deleted***")
            print(objects.strParameter(parameter, index))
            objects.delete(parameter, index, plans)
            if (input("Enter 1 to continue. Enter any other value to exit: ") == '1'):
                if busOrRoute == "bus":
                    funcDeleteBus(objects, plans)
                if busOrRoute == "route":
                    funcDeleteRoute(objects, plans)
            else:
                sys.exit()
        else:
            print("This %s does not exist." % strParametr)
            if (input("Enter 1 to try again. Enter any other value to go back: ") == '1'):
                continue
            else:
                if busOrRoute == "bus":
                    funcDeleteBus(objects, plans)
                if busOrRoute == "route":
                    funcDeleteRoute(objects, plans)


def funcDeletPlanHelp(plans, strParameter, index):
    while (True):
        parameter = input('Input %s: ' % strParameter)
        if (index == "1" or index == "2"):
            parameter = int(parameter)
        if (plans.exist(parameter, index)):
            print("\n***Your records were successfully deleted***")
            plans.delete(parameter, index)
            if (input("Enter 1 to continue. Enter any other value to exit: ") == '1'):
                funcDeletePlan(plans)
            else:
                sys.exit()
        else:
            print("This %s does not exist." % strParameter)
            if (input("Enter 1 to try again. Enter any other value to go back: ") == '1'):
                continue
            else:
                funcDeletePlan(plans)


def funcDeletePlan(plans):
    print("\t\nChoose the parameter:\n1.BusID\n2.RouteID\n3.dateOfLeaving\n4.Go back\n0.Exit")
    while (True):
        index = input('Your choice: ')
        if (index == "1"):
            while (True):
                try:
                    funcDeletPlanHelp(plans, "busID", index)
                    break
                except ValueError:
                    print("BusID can be only a number.")
                    if (input("Enter 1 to try again. Enter any other value to go back: ") == '1'):
                        continue
                    else:
                        funcDeletePlan(plans)
        elif (index == "2"):
            while (True):
                try:
                    funcDeletPlanHelp(plans, "routeID", index)
                    break
                except ValueError:
                    print("RouteID can be only a number.")
                    if (input("Enter 1 to try again. Enter any other value to go back: ") == '1'):
                        continue
                    else:
                        funcDeletePlan(plans)
        elif (index == "3"):
            funcDeletPlanHelp(plans, "dateOfLeaving", index)
        elif (index == "4"):
            funcPlans(plans)
        elif (index == "0"):
            sys.exit()
        else:
            print("You input wrong symbol! You can input only 0,1,2,3,4. Try again.")


def funcDeleteBus(buses, plans):
    print("\t\nChoose the parameter:\n1.BusID\n2.Model\n3.Driver\n4.Number Of Seats\n5.Go back\n0.Exit")
    while (True):
        index = input('Your choice: ')
        if (index == "1"):
            while (True):
                try:
                    funcDeleteHelp(buses, plans, "busID", index, "bus")
                    break
                except ValueError:
                    print("BusID can be only a number.")
                    if (input("Enter 1 to try again. Enter any other value to go back: ") == '1'):
                        continue
                    else:
                        funcDeleteBus(buses, plans)

        elif (index == "2"):
            funcDeleteHelp(buses, plans, "model", index, "bus")

        elif (index == "3"):
            funcDeleteHelp(buses, plans, "driver", index, "bus")

        elif (index == "4"):
            while (True):
                try:
                    funcDeleteHelp(buses, plans, "numberOfSeats", index, "bus")
                    break
                except ValueError:
                    print("NumberOfSeats can be only a number.")
                    if (input("Enter 1 to try again. Enter any other value to go back: ") == '1'):
                        continue
                    else:
                        funcDeleteBus(buses, plans)

        elif (index == "5"):
            funcBuses(buses)

        elif (index == "0"):
            sys.exit()

        else:
            print("You input wrong symbol! You can input only 0,1,2,3,4,5. Try again.")


def funcDeleteRoute(routes, plans):
    print("\t\nChoose the parameter:\n1.routeID\n2.Wherefrom\n3.Where\n4.Go back\n0.Exit")
    while (True):
        index = input('Your choice: ')
        if (index == "1"):
            while (True):
                try:
                    funcDeleteHelp(routes, plans, "routeID", index, "route")
                    break
                except ValueError:
                    print("RouteID can be only a number.")
                    if (input("Enter 1 to try again. Enter any other value to go back: ") == '1'):
                        continue
                    else:
                        funcDeleteRoute(routes, plans)

        elif (index == "2"):
            funcDeleteHelp(routes, plans, "wherefrom", index, "route")

        elif (index == "3"):
            funcDeleteHelp(routes, plans, "where", index, "route")

        elif (index == "4"):
            funcRoutes(routes)

        elif (index == "0"):
            sys.exit()

        else:
            print("You input wrong symbol! You can input only 0,1,2,3,4. Try again.")


mainMenu(buses, routes, plans)
