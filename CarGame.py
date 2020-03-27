Name = input('What is your name : ')
print(f'Hello {Name} welcome to Mehuls car game')



command = ""
while command.lower() != "quit":
    command = input('> ').lower()
    if command == 'start':
        print('Car has started.Read to go')
    elif command == 'stop':
        print('Car has stopped.Now get out')
    elif command == 'help':
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quit 
        """)
    elif command =='quit':
        break

    else:
        print('I do not understand.Please use the given instructions.For instructions type help')

