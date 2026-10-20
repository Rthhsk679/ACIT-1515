from spotify import add_song, record_listen, generate_wrapped, insert_example

def main():
    commands = [add_song, record_listen, generate_wrapped, insert_example]
    choice = 0

    while choice != 5:
        print(
            """
            ====== SPOTIFY WRAPPED ======
            1. Add a song
            2. Record a listen
            3. Generate Spotify Wrapped
            4. Insert Example Playlist
            5. Exit
            """
        )
        choice = int(input("Enter your choice: "))
        
        if choice < 1 or choice > 5:
            input("invalid input...")
            choice = 0
        elif choice == 5:
            print("Goodbye!")
            break
        elif choice == 4:
            commands[choice - 1]()
        else:
            print(commands[choice - 1]())

main()