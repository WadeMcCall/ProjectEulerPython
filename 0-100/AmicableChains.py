from lib.convenience import properFactors

LIMIT = 10 ** 6
chains = [0 for _ in range(LIMIT+ 1)] 

# kind of a yikes function lol
def getChainLength(num):
    global chains
    numToFind = num
    if chains[num] != 0:
        return chains[num]
    chain = [num]
    while True:
        next = sum(properFactors(chain[-1]))
        if next > LIMIT or next == 1: # diverged
            for num in chain:
                chains[num] = -1
            if next < LIMIT:
                chains[next] = -1
            return -1
        if chains[next] == -1: # already marked as divergent
            for num in chain:
                chains[num] = -1
            return -1
        
        if chains[next] != 0:
            for num in chain:
                chains[num] = -1
            return -1
        if next == numToFind:
            for num in chain:
                chains[num] = len(chain)
            return len(chain)
        
        # sometimes chains have tails. We mark the tail as divergent because it is not amicable, but mark the rest of the chain as amicable
        if next in chain:
            for i in range(len(chain)):
                if chain[i] != next:
                    chains[i] = -1
                elif chain[i] == next:
                    chain = chain[i:]
                    break
            for num in chain:
                chains[num] = len(chain)
            return -1
        chain.append(next)

def main():
    max = 0
    index = 0
    for i in range(2, LIMIT):
        len = getChainLength(i)
        if len > max:
            max = len
            index = i
            print(index, max)
    print(chains[index])
    return

if __name__ == '__main__':
    main()