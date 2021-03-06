# Made by Jordan Leich on 6/16/2020


# restart of program function
def restart():
    import time
    import end

    user_restart_choice = str(input("Do you wish to restart (yes or no): "))
    print()
    time.sleep(1)

    if user_restart_choice.lower() == 'y' or user_restart_choice.lower() == 'yes':
        print("Restarting program...\n")
        time.sleep(2)
        import main
        main.start()

    elif user_restart_choice.lower() == 'n' or user_restart_choice.lower() == 'no':
        end.end()

    else:
        print("Invalid input... Restarting input...\n")
        time.sleep(2)
        restart()
