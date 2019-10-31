import sqlite3

class Movie:
    def __init__(self,Title,imdbRating,Rated,Released,Runtime,Genre,Actors,Director,Country,Plot):
        self.Title = Title
        self.imdbRating = imdbRating
        self.Rated = Rated
        self.Released = Released
        self.Runtime = Runtime
        self.Genre = Genre
        self.Actors = Actors
        self.Director = Director
        self.Country = Country
        self.Plot = Plot
    
    def get_str(self):
        finalstr = 'Title: '+str(self.Title) + '\n'+ 'ImdbRating: '+ str(self.imdbRating) + '\n'+ 'Rated: '+ str(self.Rated) + '\n'+'Release Date: ' +str(self.Released) + '\n'+'Runtime: '+ str(self.Runtime) + '\n'+'Genre: '+ str(self.Genre) + '\n'+'Actors: '+ str(self.Actors) + '\n'+'Director: '+ str(self.Director) + '\n'+'Country: '+ str(self.Country) + '\n'+'Plot: '+ str(self.Plot)
        return finalstr

    def run_query(self,dbname,query,param):
        with sqlite3.connect(self.dbname) as conn:
            c = conn.cursor()
            query_result = c.execute(self.query,self.param)
            c.commit()
        return query_result

    def insertMovie(self):
        query = 'Insert into Movies values(:Title,:imdbRating,:Rated,:Released,:Runtime,:Genre,:Actors,:Director,:Country,:Plot)'
        param = {'Title':self.Title,'imdbRating':self.imdbRating,'Rated':self.Rated,'Released':self.Released,'Runtime':self.Runtime,'Genre':self.Genre,'Actors':self.Actors,'Director':self.Director,'Country':self.Country,'Plot':self.Plot}
        try:
            list = self.run_query(query,param)
        except:
            print('error')
