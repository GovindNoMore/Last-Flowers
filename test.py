import requests

def get_artist_info(artist_name):
    url = f"https://musicbrainz.org/ws/2/artist/?query=artist:{artist_name}&fmt=json"
    response = requests.get(url)
    data = response.json()
    if data['artists']:
        artist = data['artists'][0]
        name = artist.get('name', 'Unknown')
        genres = [tag['name'] for tag in artist.get('tags', [])] if 'tags' in artist else []
        print(f"\nArtist: {name}")
        print(f"Genres: {', '.join(genres) if genres else 'Not available'}")
        return artist
    else:
        print("Artist not found.")
        return None

def recommend_similar_artists(artist):
    if 'tags' in artist:
        genre = artist['tags'][0]['name']
        url = f"https://musicbrainz.org/ws/2/artist/?query=tag:{genre}&fmt=json"
        response = requests.get(url)
        data = response.json()
        print(f"\nArtists similar to {artist['name']} (genre: {genre}):")
        for a in data['artists'][:5]:
            print(f"- {a['name']}")
    else:
        print("No genre information available for recommendations.")

def main():
    fav_artist = input("Who is your favorite artist? ")
    artist = get_artist_info(fav_artist)
    if artist:
        recommend_similar_artists(artist)

if __name__ == "__main__":
    main()