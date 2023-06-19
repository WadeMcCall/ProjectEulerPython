class PokerHand:
    def __init__(self, cards):
        assert len(cards) == 5
        self.cards = cards
        self._getHandType()

    cards = []
    handType = 0

    def __gt__(self, other):
        if self.handType > other.handType:
            return True
        if self.handType < other.handType:
            return False
        
        assert self.handType == other.handType

        
        values = [card.intNum for card in self.cards]
        oValues = [card.intNum for card in other.cards]

        values.sort(reverse=True)
        oValues.sort(reverse=True)

        if self.handType == 0:
            for i in range(len(values)):
                if values[i] != oValues[i]:
                    return values[i] > oValues[i]
            return False

        valuePair = 0
        oValuePair = 0
        
        # both players have a pair
        if self.handType == 1:
            value_counts = {value: values.count(value) for value in values}
            oValue_counts = {value: oValues.count(value) for value in oValues}

            # Iterate over the items in the dictionary
            for key, value in value_counts.items():
                # If the value is 2, return the key
                if value == 2:
                    valuePair = key  
                    break

            # Iterate over the items in the dictionary
            for key, value in oValue_counts.items():
                # If the value is 2, return the key
                if value == 2:
                    oValuePair = key  
                    break
            
            if valuePair != oValuePair:
                return valuePair > oValuePair
            
            
            for i in range(len(values)):
                if values[i] != oValues[i]:
                    return values[i] > oValues[i]
            return False
        
        # rest of the hands don't matter since this print is never reached
        print("we've got some 'splaining to do!~ " + str(self.handType))

        return True

    def __str__(self):
        Hand = ""
        match self.handType:
            case 9:
                Hand = "Royal Flush"
            case 8:
                Hand = "Straight Flush"
            case 7:
                Hand = "Four of a kind"
            case 6:
                Hand = "Full House"
            case 5:
                Hand = "Flush"
            case 4:
                Hand = "Straight"
            case 3:
                Hand = "Three of a kind"
            case 2:
                Hand = "Two pair"
            case 1:
                Hand = "Pair"
            case 0:
                Hand = "High card"

        return Hand + " with cards: " + str(self.cards)
    
    def isRoyalFlush(self):
        if not self.isFlush():
            return False
        nums = [10, 11, 12, 13, 14]
        for card in self.cards:
            if card.intNum not in nums:
                return False
            nums.remove(card.intNum)
        return True
    
    def isStraightFlush(self):
        if not self.isFlush():
            return False
        if not self.isStraight():
            return False
        return True
    
    def isFourOfAKind(self):
        values = [card.intNum for card in self.cards]
        for i in range(2, 15):
            numi = values.count(i)
            if numi == 4:
                return True
        return False
    
    def isFullHouse(self):
        values = [card.intNum for card in self.cards]

        # Count the occurrences of each value
        value_counts = {value: values.count(value) for value in values}
        
        # Check if there are exactly two values that occur twice
        pairs = [value for value, count in value_counts.items() if count == 2]
        triples = [value for value, count in value_counts.items() if count == 3]

        return len(pairs) == 1 and len(triples) == 1
    
    def isFlush(self):
        suit = self.cards[0].suit
        for card in self.cards:
            if card.suit != suit:
                return False
        return True
    
    def isStraight(self):
        values = [card.intNum for card in self.cards]

        # handle a straight with A, 2, 3, 4, 5
        if 2 in values and 14 in values:
            values.remove(14)
            values.append(1)

        values.sort()
    
        # Check if the sorted values are consecutive
        for i in range(len(values) - 1):
            if values[i + 1] - values[i] != 1:
                return False

        return True
    
    def isThreeOfAKind(self):
        values = [card.intNum for card in self.cards]
        for i in range(2, 15):
            numi = values.count(i)
            if numi == 3:
                return True
        return False
    
    def isTwoPair(self):
        values = [card.intNum for card in self.cards]

        # Count the occurrences of each value
        value_counts = {value: values.count(value) for value in values}
        
        # Check if there are exactly two values that occur twice
        pairs = [value for value, count in value_counts.items() if count == 2]

        return len(pairs) == 2
    
    def IsPair(self):
        values = [card.intNum for card in self.cards]
        for i in range(2, 15):
            numi = values.count(i)
            if numi == 2:
                return True
        return False


    def _getHandType(self):
        if(self.isRoyalFlush()):
            self.handType = 9
            return
        if(self.isStraightFlush()):
            self.handType = 8
            return
        if(self.isFourOfAKind()):
            self.handType = 7
            return
        if(self.isFullHouse()):
            self.handType = 6
            return
        if(self.isFlush()):
            self.handType = 5
            return
        if(self.isStraight()):
            self.handType = 4
            return
        if(self.isThreeOfAKind()):
            self.handType = 3
            return
        if(self.isTwoPair()):
            self.handType = 2
            return
        if(self.IsPair()):
            self.handType = 1
            return
        self.handType = 0 # High card


class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
        self.intNum = self.strToNumber(self.number) # for comparison

    def strToNumber(self, num):
        if num == "T":
            return 10
        if num == "J":
            return 11
        if num == "Q":
            return 12
        if num == "K":
            return 13
        if num == "A":
            return 14
        return int(num)

    def __eq__(self, other):
        assert type(other) is Card
        return self.intNum == other.intNum
    
    def __gt__(self, other):
        assert type(other) is Card
        return self.intNum > other.intNum
    
    def __lt__(self, other):
        assert type(other) is Card
        return self.intNum < other.intNum
    
    def __ne__(self, other):
        assert type(other) is Card
        return self.intNum != other.intNum

    def __str__(self):
        return(str(self.number) + str(self.suit))
    
    def __repr__(self):
        return self.__str__()

def getHands(cardsStr):
    cards = []
    cArr = cardsStr.split()
    assert len(cArr) == 10
    for card in cArr:
        cards.append(Card(card[1], card[0]))

    p1 = PokerHand(cards[0:5])
    p2 = PokerHand(cards[5:])

    return p1, p2

def main():
    f = open("data/poker.txt", "r")
    sum = 0
    for x in f:
        p1, p2 = getHands(x)
        if p1 > p2:
            sum += 1

    print(sum)
    return

if __name__ == "__main__":
    main()