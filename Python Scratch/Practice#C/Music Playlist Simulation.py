class Song:
    elem = {'Title': '', 'Artist': ''}
    next = None
    prev = None

live = None
last_song = None

def add_song():
    global live, last_song
    new = Song()
    new.elem = {'Title': '', 'Artist': ''}
    new.elem['Title'] = input("Title: ")
    new.elem['Artist'] = input("Artist: ")
    if live is None:
        live = new
        last_song = new
        new.next = new
        new.prev = new
    else:
        last = live.prev
        last.next = new
        new.prev = last
        new.next = live
        live.prev = new
        last_song = new.prev

def next_song():
    global live, last_song
    if live:
        if live == last_song:
            print("(End of queue. Restarting playlist from the first song...)")
        live = live.next

def prev_song():
    global live
    if live:
        live = live.prev

def show_playlist():
    if live is None:
        print('''
          \33[91m\33[1mEmpty Playlist\33[0m''')
        return

    first = last_song.next
    temp = first
    print("          \33[97m\33[1mPlaylist:\33[0m")
    while True:
        live_marker = ""
        if temp == live:
            live_marker = " ⬅️ (Now Playing)"

        print(f'          "{temp.elem["Title"]}" by {temp.elem["Artist"]}{live_marker}')
        temp = temp.next
        if temp == first:
            break

while True:
    print("         \33[97m\33[1m =====================================\33[0m")
    if live:
        title = live.elem["Title"]
        artist = live.elem["Artist"]
        print(f'           Current Song: "{title}" by {artist}')
    else:
        print("                                     \33[92m\33[1mCurrent Song: None\33[0m")
    print("         \33[97m\33[1m =====================================\33[0m")
    print('''\33[92m\33[1m                                    🗒️ Menu
           [1] ⏭️Next Song 
           [2] ⏮️  Previous Song 
           [3] 🎶 Show Playlist
           [4] 🎵 Add Song
           [5] ❌ Exit\33[0m
         \33[97m\33[1m =====================================\33[0m''')
    choose = input("Choose: ")
    if choose == '1':
        next_song()
    elif choose == '2':
        prev_song()
    elif choose == '3':
        show_playlist()
    elif choose == '4':
        add_song()
    elif choose == '5':
        print("👋 Alright then, I’ll go quiet now. Until next time!")
        break
    else:
        print("⚠️ Invalid selection. Please enter a number between 1 and 5.")
