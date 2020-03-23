command = ""
car_started = False
while command != "quit":
    command = input(">").lower()
    if command == "start":
        if car_started:
            print("The car is already on !")
        else:
             car_started = True
             print("The car has started")
    elif command == "move":
        print("The car is moving")
    elif command == "stop":
        if not car_started:
            print("The car is already stopped !")
        else:
             car_started = False
             print("The car has been stopped")
    elif command == "quit":
        print("The car has been turned off")
    elif command == "help":
        print("""
        Start :- Ignites the car
        Move :- Gets the Car to move
        Stop :- Stops the car
        quit :- Exits the car""")
    else:
        print("Sorry i dont understand... type help to get assistance")
