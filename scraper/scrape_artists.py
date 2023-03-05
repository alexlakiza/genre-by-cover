import deezer as de
import time
import pickle

client = de.Client(headers={'Accept-Language': 'en'})

# we will collect covers from artists of these 8 deezer genres
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

# HINT: Code for collecting ids of each deezer genre
# deezer_genres = client.list_genres()
# print(deezer_genres)

# deezer_genres_ids = {}
#
# for genre in all_genres:
#     for deezer_genre in deezer_genres:
#         if genre == deezer_genre.name:
#             deezer_genres_ids[genre] = deezer_genre.id

# ID's I've collected when writing code
deezer_genres_ids = {'Jazz': 129,
                     'R&B': 165,
                     'Pop': 132,
                     'Rap/Hip Hop': 116,
                     'Alternative': 85,
                     'Rock': 152,
                     'Metal': 464,
                     'Electro': 106}


genre_artists_dict = {}  # dict to store artists of each genre

for genre in deezer_genres_ids:
    genre_id = deezer_genres_ids.get(genre)

    genre_artists_dict[genre] = client.get_genre(genre_id).get_artists()

    time.sleep(0.3)  # sleep is necessary to not exceed limit of API calls

with open("artists_folder/all_artists.pkl", "wb") as f:
    # save pickle of dict for the future
    pickle.dump(genre_artists_dict, f, protocol=pickle.HIGHEST_PROTOCOL)
