class Hours:
    def __init__(self, seans1_start_time, seans1_end_time, seans2_start_time, seans2_end_time):
        self.seans1_start_time = seans1_start_time
        self.seans1_end_time = seans1_end_time
        self.seans2_start_time = seans2_start_time
        self.seans2_end_time = seans2_end_time
        
    def __str__(self):
        return "Seans 1: {} - {} : Seans 2: {} - {}".format(self.seans1_start_time, self.seans1_end_time, self.seans2_start_time, self.seans2_end_time)
    
    
class Movie:
    def __init__(self, name, director, year, genre, imdb, hours):
        self.name = name
        self.director = director
        self.year = year
        self.genre = genre
        self.imdb = imdb
        self.hours = hours
    
    def year_info(self):
        try:
            year = int(self.year)
            if year <= 2015:
                return "Old Film"
            else:
                return "New Film"
        except ValueError:
            return "Invalid year"

    def rating_info(self):
        try:
            rating = float(self.imdb)
            if rating < 6:
                return "Reytin seviyesi: E"
            elif 6 <= rating < 7:
                return "Reytin seviyesi: D"
            elif 7 <= rating < 8:
                return "Reytin seviyesi: C"
            elif 8 <= rating < 9:
                return "Reytin seviyesi: B"
            elif 9 <= rating <= 10:
                return "Reytin seviyesi: A"
        except ValueError:
            return "Invalid rating"
       

class Forsaj_10(Movie):
    def __init__(self, name, director, year, genre, imdb, duration, hours, price, ):
        super().__init__(name, director, year, genre, imdb, hours)
        self.price = price
        self.duration = duration

    def info(self):
        return(""" 
        Name: {}
        Director:{}
        Year:{}
        Genre:{}
        IMDB: {}
        Duration: {}
        Hours: {}
        Price: {}
        """.format(self.name, self.director, self.year, self.genre, self.imdb, self.duration, self.hours, self.price))
    
  


       

class Spider_man(Movie):
    def __init__(self, name, director, year, genre, imdb, duration, hours, price, ):
        super().__init__(name, director, year, genre, imdb, hours)
        self.price=price
        self.duration=duration

    def info(self):
        return(""" 
        Name: {}
        Director: {}
        Year: {}
        Genre: {}
        IMDB: {}
        Duration: {}
        Hours: {}
        Price: {}
        """.format(self.name, self.director, self.year, self.genre, self.imdb, self.duration, self.hours, self.price ))


      

class Avatar(Movie):
    def __init__(self, name, director, year, genre, imdb, duration, hours, price, ):
        super().__init__(name, director, year, genre, imdb, hours)
        self.price=price
        self.duration=duration

    def info(self):
        return(""" 
        Name: {}
        Director: {}
        Year: {}
        Genre:{}
        IMDB: {}
        Duration: {}
        Hours: {}
        Price: {}
        """.format(self.name, self.director, self.year, self.genre, self.imdb, self.duration, self.hours, self.price ))
    


class Breaking_bad(Movie):
    def __init__(self, name, director, year, genre, imdb, duration, hours, price, ):
        super().__init__(name, director, year, genre, imdb, hours)
        self.price=price
        self.duration=duration

    def info(self):
        return(""" 
        Name: {}
        Director: {}
        Year: {}
        Genre: {}
        IMDB: {}
        Duration: {}
        Hours: {}
        Price: {}
        """.format(self.name, self.director, self.year, self.genre, self.imdb, self.duration, self.hours, self.price ))
    


class Iron_man(Movie):
    def __init__(self, name, director, year, genre, imdb, duration, hours, price, ):
        super().__init__(name, director, year, genre, imdb, hours)
        self.price=price
        self.duration=duration

    def info(self):
        return(""" 
        Name: {}
        Director:{}
        Year:{}
        Genre:{}
        IMDB: {}
        Duration: {}
        Hours: {}
        Price:{}
        """.format(self.name, self.director, self.year, self.genre, self.imdb, self.duration, self.hours, self.price))
    


class Maze_Runner_3(Movie):
    def __init__(self, name, director, year, genre, imdb, duration, hours, price, ):
        super().__init__(name, director, year, genre, imdb, hours)
        self.price=price
        self.duration=duration

    def info(self):
        return(""" 
        Name: {}
        Director:{}
        Year:{}
        Genre:{}
        IMDB: {}
        Duration: {}
        Hours: {}
        Price:{}
        """.format(self.name, self.director, self.year, self.genre, self.imdb, self.duration,self.hours, self.price ))
    


class Need_for_speed(Movie):
    def __init__(self, name, director, year, genre, imdb, duration, hours, price, ):
        super().__init__(name, director, year, genre, imdb, hours)
        self.price=price
        self.duration=duration

    def info(self):
        return(""" 
        Name: {}
        Director:{}
        Year:{}
        Genre:{}
        IMDB: {}
        Duration: {}
        Hours: {}
        Price:{}
        """.format(self.name, self.director, self.year, self.genre, self.imdb, self.duration, self.hours, self.price, ))



class Avengers_Endgame(Movie):
    def __init__(self, name, director, year, genre, imdb, duration, hours, price, ):
        super().__init__(name, director, year, genre, imdb, hours)
        self.price=price
        self.duration=duration

    def info(self):
        return(""" 
        Name: {}
        Director:{}
        Year:{}
        Genre:{}
        IMDB: {}
        Duration: {}
        Hours: {}
        Price:{}
        """.format(self.name, self.director, self.year, self.genre, self.imdb, self.duration, self.hours, self.price))



class The_last_of_us(Movie):
    def __init__(self, name, director, year, genre, imdb, duration, hours, price, ):
        super().__init__(name, director, year, genre, imdb, hours)
        self.price=price
        self.duration=duration

    def info(self):
        return(""" 
        Name: {}
        Director:{}
        Year:{}
        Genre:{}
        IMDB: {}
        Duration: {}
        Hours: {}
        Price:{}
        """.format(self.name, self.director, self.year, self.genre, self.imdb, self.duration, self.hours, self.price ))
    


class Star_Wars(Movie):
    def __init__(self, name, director, year, genre, imdb, duration, hours, price, ):
        super().__init__(name, director, year, genre, imdb, hours)
        self.price=price
        self.duration=duration

    def info(self):
        return(""" 
        Name: {}
        Director:{}
        Year:{}
        Genre:{}
        IMDB: {}
        Duration: {}
        Hours: {}
        Price:{}
        """.format(self.name, self.director, self.year, self.genre, self.imdb, self.duration, self.hours, self.price))
    






   
