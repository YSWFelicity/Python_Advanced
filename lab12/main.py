from actor import Actor
from show import Show
from channel import Channel


def shows_starring(actor, available_channels):
    '''
    shows_starring -- check if an actor appears in a series of channels
    Parameters:
        self -- the current piece object
        available_channels -- A list of channels
    Return:
        A list of shows having the actor
    '''
    lst = []
    for item in available_channels:
        lst += item.get_shows_by_actor(actor)
    return lst


def main():
    actor1 = Actor("Actor", "1")
    actor2 = Actor("Actor", "2")
    actor3 = Actor("Actor", "3")

    show1 = Show("Monday Show", [actor1, actor2])
    show2 = Show("Tuesday Show", [actor1, actor2, actor3])
    show3 = Show("Friday Show", [actor2, actor3])

    channel1 = Channel("DEF", 42, [show1])
    channel2 = Channel("XYZ", 31, [show2, show3])

    channel = [channel1, channel2]

    lst = shows_starring(actor3, channel)
    for i in lst:
        print(i.print_show())


main()
