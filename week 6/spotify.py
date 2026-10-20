playlist = {
    "Blinding Lights": {
        "artist": "The Weeknd",
        "duration": 200,
        "plays": 5
    },
    "Numb": {
        "artist": "Linkin Park",
        "duration": 187,
        "plays": 8
    },
    "Shape Of You": {
        "artist": "Ed Sheeran",
        "duration": 234,
        "plays": 3
    }
}

def add_song():
    title = input("title: ").title()
    artist = input("artist: ").title()
    minutes = int(input("duration (minutes): "))
    seconds = int(input("duration (seconds): "))
    duration = minutes * 60 + seconds

    playlist[title] = {"artist": artist, "duration": duration, "plays": 0}

    return playlist

def record_listen():
    title = input("title: ").title()
    if title not in playlist:
        print("No song found")
    else:
        playlist[title]["plays"] += 1
    
    return playlist

def generate_wrapped():
    if not playlist:
        input("No songs in playlist...")
        return

    total_songs = 0
    total_plays = 0
    total_duration = 0
    most_song = ""
    most_artist = ""
    most_plays = -1

    for title in playlist:
        song = playlist[title]
        total_songs += 1
        total_plays += song["plays"]
        total_duration += song["duration"] * song["plays"]

        if song["plays"] > most_plays:
            most_plays = song["plays"]
            most_song = title
            most_artist = song["artist"]

    if total_plays == 0:
        input("No songs have been played yet...")
        return

    input(
        f"""
        ========== YOUR SPOTIFY WRAPPED ==========

        Total Songs: {total_songs}
        Total Plays: {total_plays}
        Total Listening Time: {total_duration / 60:.2f} minutes

        Your Most Played Song:
        {most_song} - {most_artist} ({most_plays} plays)

        ==========================================
        ...
        """
    )