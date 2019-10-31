import sqlite3
from Movies import Movie


def insertMovie(Movie):
        c.execute("""Insert into Movies values(:Title,:imdbRating,:Rated,:Released,:Runtime,:Genre,:Actors,
        :Director,:Country,:Plot)""",{'Title':Movie.Title,'imdbRating':Movie.imdbRating,'Rated':Movie.Rated,'Released':Movie.Released,'Runtime':Movie.Runtime,'Genre':Movie.Genre,'Actors':Movie.Actors,'Director':Movie.Director,'Country':Movie.Country,'Plot':Movie.Plot})
     


def get_movie_by_name(Movie):

    c.execute("""Select from Movies where Title=:Title""",{'Title':Movie.Title})
    return c.fetchall()


def get_movie_name(Movie):
    c.execute("""Select Title from Movies where Title=:Title""",{'Title':Movie.Title})
    return c.fetchone()
    
