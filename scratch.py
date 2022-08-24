# double_ten = (lambda x: x*2)(10)
# print(double_ten)

# print(list(map(lambda x: x*2, [1, 2, 3, 4, 5])))


import time


def first():
    time.sleep(2)
    print('First')
    time.sleep(2)

def second():
    print('Second')


# first()
# second()


# Real Life Example

def download_song(song_name):
    print(f"Downloading {song_name}...")
    time.sleep(2)
    print(f"Finished Downloading")
    return {'title': song_name, 'artist': 'Pitbull'}


def play_song(song_name):
    song = download_song(song_name)
    print(f"{song['title']} by {song['artist']} is playing!")

play_song('Wonderwall')

