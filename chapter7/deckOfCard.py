class Card(object):

    def __init__(self,value):
        self.value = value #MUST BE A23456789VQK

    @value.setter
    def value(self,value):
        if value in [1,2,3,4,5,6,7,8,9,10,11,12,13]:
            self._value=value

class BlackCard(Card):

    def __init__(self,value,color):
        super(BlackCard,self).__init__(value)
        self.color = "Black"

class RedCard(Card):

     def __init__(self,value,color):
        super(RedCard,self).__init__(value)
        self.color = "Red"

class Hearts(RedCard):

    def __init__(self,value):
        super(Heart,self).__init__(value)
        self.symbol = "Hearts"

class Diamonds(RedCard):

    def __init__(self,value):
        super(Diamonds,self).__init__(value)
        self.symbol = "Diamonds"

class Clubs(BlackCard):

    def __init__(self,value):
        super(Clubs,self).__init__(value)
        self.symbol = "Clubs"

class Spades(BlackCard):

    def __init__(self,value):
        super(Spades,self).__init__(value)
        self.symbol = "Spades"

class Deck(object):

    def __init__(self):
        self.deck_array=







