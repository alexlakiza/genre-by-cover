import deezer as de
import time
import pickle

client = de.Client(headers={'Accept-Language': 'en'})

all_genres = {
    'Jazz': 0,
    'R&B': 1,
    'Pop': 2,
    'Rap/Hip Hop': 3,
    'Alternative': 4,
    'Rock': 5,
    'Metal': 6,
    'Electro': 7
}

deezer_genres_ids = {'Jazz': 129,
                     'R&B': 165,
                     'Pop': 132,
                     'Rap/Hip Hop': 116,
                     'Alternative': 85,
                     'Rock': 152,
                     'Metal': 464,
                     'Electro': 106}

# deezer_genres = client.list_genres()
# print(deezer_genres)

# deezer_genres_ids_dict = {}
#
# for genre in all_genres:
#     for deezer_genre in deezer_genres:
#         if genre == deezer_genre.name:
#             deezer_genres_ids_dict[genre] = deezer_genre.id

genre_artists_dict = {}

for genre in deezer_genres_ids:
    genre_id = deezer_genres_ids.get(genre)

    genre_artists_dict[genre] = client.get_genre(genre_id).get_artists()

    time.sleep(0.3)

with open("artists_folder/ru_artists.pkl", "wb") as f:
    pickle.dump(genre_artists_dict, f, protocol=pickle.HIGHEST_PROTOCOL)

with open("artists_folder/ru_artists.pkl", "rb") as f:
    us_artists_dict = pickle.load(f)

print(us_artists_dict['Rap/Hip Hop'][0].get_albums())
