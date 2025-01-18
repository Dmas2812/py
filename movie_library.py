import json
from collections import Counter


class MovieLibrary:
    def __init__(self, json_file):
        '''Creazione della classe e del metodo costruttore,
        inizializzazione dei due attributi di istanza
        json_file'''
        self.json_file = json_file
        try:
            with open(self.json_file,"r", encoding =  "utf=8") as file:
                self.movies = json.load(file)
        
        except FileNotFoundError:
            raise FileNotFoundError (f"File not found: {json_file}")

    def __update_json_file(self):
        '''Aggiorna il file ogni volta che subisce una modifica'''
        with open(self.json_file,'w', encoding='utf-8') as file:
            json.dump(self.movies, file)
    
    def get_movies(self):
        '''Restituisce una lista di tutti i film'''
        return self.movies
    
    def add_movie(self, title: str, director: str, year: int, genres: list):
        '''Aggiunge un nuovo film alla lista e aggiorna il file'''
        new_movie={
            "title": title,
            "director": director,
            "year" : year,
            "genre" : genres
        }
        self.movies.append(new_movie)
        self.__update_json_file()
        return (f"{new_movie['title']} è stato aggiunto con successo")

    def remove_movie(self, title):
        '''Rimuove un film dalla lista e aggiorna il file'''

        for movie in self.movies:
            if movie['title'].lower()==title.lower():
                self.movies.remove(movie)
                self.__update_json_file()
                return movie
            
        raise MovieNotFoundError 
        
# Modifica i metodi remove_movie e update_movie affinché,
# se non viene trovato alcun film avente come titolo title,
# venga sollevata l’eccezione personalizzata MovieNotFoundError,
# avente il messaggio “Movie was not found”.
# Tale eccezione va definita all’interno della classe MovieLibrary.

    def update_movie(self, title, director=None, year=None, genres=None):
        ''' Modificare un film già presete nella lista, passando dei parametri opzionali'''
        for movie in self.movies:

            if movie['title'].lower() == title.lower():
                if director is not None:
                    movie['director'] = director
                                    
                if year is not None:
                    movie['year'] = year
                                    
                if genres is not None:
                    movie['genres'] = genres
                   
                self.__update_json_file()
                return movie
            
            
        raise MovieNotFoundError
            
    def get_movie_titles(self):
        '''Restituisce una lista completa dei titoli dei film'''
        return [movie['title'] for movie in self.movies]
        

    def count_movies(self):
        '''Restituisce il numero totale di film nella collezione'''
        return len(self.movies)
        
    def get_movie_by_title(self, title):
        '''Restituisce il film tramite il titolo ricercato'''
        return [movie for movie in self.movies if movie['title'].lower() == title.lower()]
            

    def get_movie_by_title_substring(self, substring):
        '''Restituisce una lista di film che contengono 
           la sottostringa nel titolo.'''
        return [movie for movie in self.movies if substring in movie['title']]
            
    def get_movies_by_years(self, year):
        '''Restituisce una lista di film con anno year'''
        result = [movie for movie in self.movies if movie['year'] == year]
        if not result:
            raise MovieNotFoundError
        return result            

    def count_movies_by_director(self, director):
        '''Restituisce il numero di film girati da uno specifico regista'''
        return len([movie for movie in self.movies if movie['director'].lower() == director.lower()])
            
    def get_movies_by_genre(self, genres: str):
        '''Restituisce film appartenenti ad un genere specifico'''
        return [movie for movie in self.movies if movie['genres'] == genres]
        
    
    def get_oldest_movie_title(self):
        ''' Restituisce il film meno recente'''
        oldest_movie = self.movies[0]
        for movie in self.movies:
            if movie['year'] < oldest_movie['year']:
                oldest_movie = movie
        return oldest_movie['title']

    def get_average_release_year(self):
        '''Restituisce la media degli anni di pubblicazione dei film come float'''
        total_year = sum(movie['year'] for movie in self.movies)
        average_year = total_year/len(self.movies)
        return average_year
        
    def get_longest_title(self):
        '''Restituisce il titolo più lungo della collezione'''
        longest_title=""
        for movie in self.movies:
            if len(movie['title']) > len(longest_title):
                longest_title = movie['title']
        return longest_title

    def get_titles_between_years(self, start_year, end_year):
        '''Restituisce una lista di titoli di film pubblicati
           tra start_year e end year '''
        return [movie['title']for movie in self.movies if start_year <= movie['year'] <= end_year]

            
    def get_most_common_year(self):
        '''Restituisce l' anno che si ripete più volte 
           tra i film della collezione'''
        list_year=[]
        for movie in self.movies:
            list_year.append(movie['year'])
        count_common_year = Counter(list_year)
        common_year = count_common_year.most_common(1)[0]
        return common_year
        
class MovieNotFoundError(Exception):
        def __init__(self):
            super().__init__("Movie was not found")

json_path= "C:/Users/Dmasi/OneDrive/Desktop/Corso Py/Prova scritta/movies (1).json"
film = MovieLibrary(json_path)        
#print(film.get_movies())
#print(film.add_movie('Il miglio verde', 'Frank Daranbot', 1999, ['Giallo','Fantasy']))
#print(film.remove_movie('Il miglio verde'))
#print(film.remove_movie("Le Iene"))
#print(film.update_movie('The Godfather','Coppola', 2021,['Commedia']))
#print(film.get_movie_titles())
#print(film.count_movies())
#print(film.get_movie_by_title('The Godfather'))
#print(film.get_movie_by_title_substring(' The Return of the King'))
#print(film.get_movies_by_years(1994))
#print(film.get_movies_by_years(1800))
#print(film.count_movies_by_director('Steven Spielberg')) 
#print(film.get_movies_by_genre(['Drama']))
#print(film.get_oldest_movie_title())
#print(film.get_average_release_year())
#print(film.get_titles_between_years(1992,1994))
#print(film.get_longest_title())
#print(film.get_most_common_year())

