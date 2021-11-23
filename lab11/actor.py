class Actor:
    def __init__(self, lastname, show_collection):
        '''
        Constructor -- creates an object of actor
        Parameters:
            self -- the current piece object
            firstname -- first name of actor, String
            lastname -- last name of actor, String
            show_collection -- show collection, list
        '''

        self.lastname = lastname
        self.collection = show_collection
