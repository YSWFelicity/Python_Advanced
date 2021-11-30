from show import Show


class Channel:
    def __init__(self, name, number, show_collection):
        '''
        Constructor -- creates an channel object
        Parameters:
            self -- the current piece object
            name -- channel name, String
            number == channel number, integer
            show_collection -- a list of shows that the channel has
        '''
        self.name = name
        self.number = number
        self.collectioin = show_collection

    def get_shows_by_actor(self, actor):
        '''
        Cget_shows_by_actor -- check if an actor in one of its show
        Parameters:
            self -- the current piece object
            actor -- an actor name, String
        Return:
            A list of shows having actor
        '''
        lst = []
        for i in self.collectioin:
            if i.cast_contains(actor):
                lst.append(i)
        return lst
