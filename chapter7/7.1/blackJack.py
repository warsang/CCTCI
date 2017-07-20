#From  https://codereview.stackexchange.com/questions/56695/text-based-blackjack-game-in-python
class Card(object):

    FACES = {'Ace':1,'Jack':10,'Queen':10,'King':10}

    def __init__(self,face,suit):
        self.face = face
        self.suit = suit
    
    def __str__(self):
        return "{0.face} of {0.suit}".format(self)

    @property
    def value(self):
        return self.FACES.get(self.face,self.face)


class Game(object):

    def __init__(self,*players,start_credit=100):
        self.dealer = Dealer()
        self.deck = Deck()
        self.players = [Player(player,start_credit)for player in players]

class Hand(object):

    def __init__(self):
        #initialise empty list of cards
        self.cards_in_hand = []

    def draw_from(self,deck):
        #draw a card from the deck and add to list
        self.cards_in_hand.append(deck.draw())

    def return_to(self,deck):
        #empty list of cards and return to deck
        for card in self.cards_in_hand:
            deck.add_card(card)
        self.cards_in_hand = []
        deck.shuffle()
    
    @property
    def value(self):
        #all the value logic goes here
        score = 0
        for card in self.cards_in_hand:
            score += card.value
        return score

class Deck(object):

    def __init__(self):
        #initialise empty deck
        self.cards_in_deck = []

    def shuffle(self):
        #implement shuffling method
        pass

    def draw(self):
        #Draw card from top of the deck (card must be removed!)
        deck_size = len(self.cards_in_deck)
        if deck_size > 0 :
            return self.cards_in_deck.pop(deck_size - 1)

    def add_card(self,card):
        #Add card to deck
        self.cards_in_deck.append(card)

