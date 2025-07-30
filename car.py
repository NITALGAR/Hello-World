command = ""
command_list = """
> Start --> to start engine.
> Stop --> to stop engine.
> Quit --> to quit
"""
engine_start = False


while command.lower() != "quit": 
    command = input("> ")
    if command.capitalize() == "Help":
        print(command_list)  
    elif command.capitalize() == "Start" and not engine_start:
        print("Engine started..")
        engine_start = True
    elif command.capitalize() == "Start" and  engine_start:
        print("The engine is already started..")
    elif command.capitalize() == "Stop" and engine_start:
        print("Engine stopped ..")
        engine_start = False
    elif command.capitalize() == "Stop" and not engine_start:
        print("Engine is already stopped ..")
    else:
        print("Command invalid! Please enter 'Help' to see commands")
    continue




















