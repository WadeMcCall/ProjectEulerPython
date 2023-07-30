# find the number of heads required to win at least $1 billion
def getNumHeads(tosses, target, fValue):
    winMultiplier = 1 + 2 * fValue 
    loseMultiplier = 1 - fValue
    # perform a linear search to find the minimum number of heads required to reach the target

    result = 1

    while True:
        heads = result
        tails = tosses - heads

        if tails < 0:  # Ensure tails is never negative
            return None

        total = (winMultiplier ** heads) * (loseMultiplier ** tails)
        if(total > target):
            return heads
        result += 1
        
        

# Test fValues from .8 to .3
best_fValue = None
lowest_heads = None

for fValue in [i/100 for i in range(8, 30)]:  # This will give you a list [.08, .09, .10, ..., .29, .30]
    heads = getNumHeads(1000, 1000000, fValue)
    if heads is not None and (lowest_heads is None or heads < lowest_heads):
        lowest_heads = heads
        best_fValue = fValue

print(f"Best fValue: {best_fValue}, Lowest number of heads: {lowest_heads}")
