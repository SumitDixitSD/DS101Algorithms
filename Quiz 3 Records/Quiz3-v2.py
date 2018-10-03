from collections import namedtuple
import csv


def create_movies_db(filename):
    '''
    Function to create records of movies from a csv file and store them in a list
    input : name of the csv file
    output : the list of movies
    '''
    movies_db = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        fields = next(reader)
        Movie = namedtuple('Movie', fields)
        for row in reader:
            movies_db.append(Movie(*row))
    return movies_db


def create_genres_db(filename):
    '''
    Function to create records of genres and store them in a list
    input : name of the csv file
    output : the list of genres
    '''
    genres_db = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        fields = next(reader)
        Genre = namedtuple('Genre', fields)
        for row in reader:
            genres_db.append(Genre(*row))
    return genres_db


def query_genre(genre):
    '''
    Function which prints the movies of a given genre
    input : genre
    output : The movie name and its release year of the given genre
    '''
    for genre in genres_db:
        if ip_genre == genre.genre:
            g_id = genre.genre_id
    for movie in movies_db:
        if g_id == movie.genre_id:
            print(movie.name + " released in the year "+ movie.release_year)


movies_db = create_movies_db("movies.csv")
genres_db = create_genres_db("genres.csv")
ip_genre = input("Enter the genre you want to search for : ")
print("Movies with genre "+ip_genre + " :")
query_genre(ip_genre)

