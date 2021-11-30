from actor import Actor


class Show:
    def __init__(self, title, cast_collection):
        '''
        Constructor -- creates an object of actor
        Parameters:
            self -- the current piece object
            title -- title of show, String
            cast_collection -- a list of casts who join the show
        '''
        self.title = title
        self.collection = cast_collection

    def cast_contains(self, actor):
        '''
        cast_contains -- Check if an actor joins the show
        Parameters:
            self -- the current piece object
            actor-- actor name, String
        Return:
            Boolean. If an actor joins the show, return True. Otherwise,False.
        '''
        if actor in self.collection:
            return True
        else:
            return False

    def print_show(self):
        '''
        print_show -- Print out show's name
        Parameters:
            self -- the current piece object
        Return:
            Print out tile of the show
        '''
        print(self.title)
