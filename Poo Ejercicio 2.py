class Movie:
    def __init__(self, title, year, language, rating ):
        self.title = title
        self.year = year
        self.language = language
        self.rating = rating
    
favorite_movie=  Movie("Titanic", 1999, "Spanish", 5)
print (favorite_movie.title)
print (favorite_movie.year)
print (favorite_movie.language)
print (favorite_movie.rating)
