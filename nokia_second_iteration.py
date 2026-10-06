main_menu = """
     1. Phone book
     2. Messages
     3. Chat
     4. Call register
     5. Tones
     6. Settings
     7. Call divert
     8. Music
     9. Games
     10. Calculator
     11. Reminders
     12. Clocks
     13. Profile
     14. Services
     15. SIM services
     0. Exit
"""
while True:
        print(main_menu)
        main_menu_no = int(input("Enter number: "))
        match main_menu_no:
            case 1:
                print("Phone book")
            case 2:
                print("Messages")
            case 3:
                print("Chat")
            case 4:
                print("Call register")
            case 5:
                print("Tones")
            case 6:
                print("Settings")
            case 7:
                print("Call divert")
            case 8:
                print("Music")
            case 9:
                print("Games")
            case 10:
                print("Calculator")
            case 11:
                print("Reminders")
            case 12:
                print("Clocks")
            case 13:
                print("Profile")
            case 14:
                print("Services")
            case 15:
                print("SIM services")
            case 0:
                print("Goodbye!")
                break
            case _:
                print("Invalid input")

