from mall import Mall

class Genclik(Mall):
    def __init__(self, location, floor, cinemaplus):
        super().__init__(location, floor, cinemaplus)
        self.location = location
        self.floor = floor
        self.cinemaplus= cinemaplus
    
    def info(self):
        return ('''
        _

        Salam! Genclik_Mall Xos gelmisiniz!!!
        _
        
        Location: {}

        Floor: {}
        
        CinemaPlus: {}
        
        '''.format(self.location, self.floor, self.cinemaplus))

