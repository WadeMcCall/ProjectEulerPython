import random

class Monopoly:
    def __init__(self):
        self.currentSquare = 0
        self.doublesCounter = 0
        self.Visited = [0 for _ in range(40)]
        self.ChanceSquares = [7, 22, 36]
        self.CommunityChestSquares = [2, 17, 33]
        self.RRSquares = [5, 15, 25, 35]
        self.UUSquares = [12, 28]
        self.CCCards = [0, 10, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
        self.CHCards = [0, 10, 11, 24, 39, 5, 'R', 'R', 'U', -3, None, None, None, None, None, None]
        random.shuffle(self.CCCards)
        random.shuffle(self.CHCards)
        self.G2J = 30
        self.JAIL = 10

    def takeTurn(self):
        roll = self.rollDice(4)
        if self.doublesCounter == 3:
            self.currentSquare = self.JAIL
            self.doublesCounter = 0
            self.Visited[self.currentSquare] += 1
            return
        self.currentSquare = (self.currentSquare + roll) % 40
        if self.currentSquare == self.G2J:
            self.currentSquare = self.JAIL
        elif self.currentSquare in self.ChanceSquares:
            self.drawChance()
        elif self.currentSquare in self.CommunityChestSquares:
            self.drawCommunityChest()
        self.Visited[self.currentSquare] += 1
        return

    def rollDice(self, numSides = 6):
        die1 = random.randint(1,numSides)
        die2 = random.randint(1,numSides)
        if die1 == die2:
            self.doublesCounter += 1
        else:
            self.doublesCounter = 0
        return die1 + die2
    
    def drawCommunityChest(self):
        card = self.CCCards.pop(0)
        if card is not None:
            self.currentSquare = card
        self.CCCards.append(card)

    def drawChance(self):
        card = self.CHCards.pop(0)
        if card is not None:
            if card == 'R':
                while self.currentSquare not in self.RRSquares:
                    self.currentSquare = (self.currentSquare + 1) % 40
            elif card == 'U':
                while self.currentSquare not in self.UUSquares:
                    self.currentSquare = (self.currentSquare + 1) % 40
            elif card == -3:
                self.currentSquare -= 3
                if self.currentSquare < 0:
                    self.currentSquare += 40
                if self.currentSquare in self.CommunityChestSquares:
                    self.drawCommunityChest()
            else:
                self.currentSquare = card
        self.CHCards.append(card)

def main():
    game = Monopoly()
    for _ in range(1000000):
        game.takeTurn()
    max = [{"visited": 0, "square": 0}, {"visited": 0, "square": 0}, {"visited": 0, "square": 0}]
    for i in game.Visited:
        if i > max[0]["visited"]:
            max[0]["visited"] = i
            max[0]["square"] = game.Visited.index(i)
            max.sort(key=lambda x: x["visited"])
    print(max)

if __name__ == '__main__':
    main()