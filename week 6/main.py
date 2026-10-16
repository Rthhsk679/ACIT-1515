from spotify import add_song, record_listen, generate_wrapped

def main():
    commands = [add_song, record_listen, generate_wrapped]

    choice = 5

    while choice != 4:
        print(
            """
            ====== SPOTIFY WRAPPED ======
            1. Add a song
            2. Record a listen
            3. Generate Spotify Wrapped
            4. Exit
            """
        )
        choice = int(input("Enter your choice: "))
        
        if choice < 1 or choice > 4:
            input("invalid input...")
            choice = 5
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            commands[choice - 1]()

main()
