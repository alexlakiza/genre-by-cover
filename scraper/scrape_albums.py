import pickle
import time
import urllib.request

import deezer as de

client = de.Client(headers={'Accept-Language': 'en'})

albums = {}

with open("artists_folder/all_artists.pkl", "rb") as f:
    artists_dict = pickle.load(f)

genres = ['Jazz', 'R&B', 'Pop', 'Rap/Hip Hop', 'Alternative', 'Rock', 'Metal', 'Electro']

i = 0

cur_genre = ""

for deezer_genre in genres:  # For each genre

    cur_genre = deezer_genre

    for artist in artists_dict[deezer_genre]:  # For each artist of genre

        print(artist)

        current_artist_albums_list = artist.get_albums()  # Collecting all artist's albums

        time.sleep(0.1)

        for album in list(current_artist_albums_list):  # Looping through all albums of artist

            album_dict = album.as_dict()  # Working with dict is better than built-in deezer-python type

            gen_list = [genre.name for genre in album.genres]

            album_dict['genres'] = gen_list  # Adding genres of album to dict

            time.sleep(0.45)

            proper_album_types = ['album', 'ep']  # Leaving only albums and EP, dumping singles
            # if album does not have any genre, we skip it
            if album_dict['record_type'].lower() in proper_album_types and len(album_dict['genres']) != 0:

                try:
                    cur_filename = f"../data/album_covers/{deezer_genre}/{i}.jpg"
                    urllib.request.urlretrieve(album_dict['cover_medium'], cur_filename)  # Saving album's cover

                    time.sleep(0.1)

                    # Collecting all necessary metadata about album
                    albums[i] = {'album_title': album_dict['title'],
                                 'album_artist:': artist.name,
                                 'album_cover_link': album_dict['cover_medium'],
                                 'album_cover_local_name': cur_filename,
                                 'album_genres': album_dict['genres'],
                                 'deezer_artist_genre': deezer_genre,
                                 'record_type': album_dict['record_type']}

                    i += 1
                    time.sleep(0.25)

                except:  # this is not pep-8 friendly, but does the job
                    pass

            else:
                pass

with open(f"../data/albums_from_deezer_{cur_genre}.pkl", "wb") as f:
    # save pickle of metadata of albums
    pickle.dump(albums, f, protocol=pickle.HIGHEST_PROTOCOL)
