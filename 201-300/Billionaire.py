import random

fValues = [i/1000 for i in range(80, 300)]  # Test f-values from 0 to 1

def getNewCoinTosses():
    return [random.randint(0,1) for _ in range(1000)]  # Generate 1000 tosses

def runSimulation(fValue, coinTosses):
    sum = 1
    for toss in coinTosses:
        bet = fValue * sum
        if(toss == 1): # Win
            sum += 2 * bet
        else:
            sum -= bet
    return sum

def main():
    numSimulations = 100 # Number of simulations to run for each f-value
    for f in fValues:
        billionaireCount = 0
        for _ in range(numSimulations):
            coinTosses = getNewCoinTosses()
            result = runSimulation(f, coinTosses)
            if result >= 1000000000:  # Check if result is greater than or equal to 1 billion
                billionaireCount += 1
        print("f = " + str(f) + " : " + str((billionaireCount / numSimulations) * 100) + "% chance of becoming a billionaire")

if __name__ == "__main__":
    main()