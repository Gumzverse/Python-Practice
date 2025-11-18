class SongInfo:
    pass

class Song:
    info = None
    next = None
    prev = None

now = None
last = None

def setup_songs():
    global now, last

    titles = ['My day', 'may halaga pa ba ako sayo', 'Oh, Giliw', 'Blue Dreams']
    artists = ['HELLMERRY', 'Juan Karlos', 'Adie', 'Apekz']

    for i in range(len(titles)):
        info = SongInfo()
        info.title = titles[i]
        info.artist = artists[i]

        song = Song()
        song.info = info

        if now is None:
            now = song
            last = song
            song.next = song
            song.prev = song
        else:
            end = now.prev
            end.next = song
            song.prev = end
            song.next = now
            now.prev = song
            last = song.prev

def play_next():
    global now
    if now:
        now = now.next

def play_prev():
    global now
    if now:
        now = now.prev

def show_all():
    if now is None:
        print("\nNo songs in the playlist.")
        return

    print("\nPlaylist:")
    temp = last.next
    while True:
        print(f'"{temp.info.title}" by {temp.info.artist}')
        temp = temp.next
        if temp == last.next:
            break

setup_songs()

while True:
    print("\n-----------------------------")
    if now:
        print(f'Playing: "{now.info.title}" by {now.info.artist}')
    else:
        print("No song is playing.")
    print("-----------------------------")
    print("1 - Next Song")
    print("2 - Previous Song")
    print("3 - Show Playlist")
    print("4 - Exit")

    choice = input("Pick: ")

    if choice == '1':
        play_next()
    elif choice == '2':
        play_prev()
    elif choice == '3':
        show_all()
    elif choice == '4':
        print("Bye!")
        break
    else:
        print("Pick something from 1 to 4.")