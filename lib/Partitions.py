from lib.FigurateNumbers import pentagonalNumber
partitions = [1, 1]

def p(goal):
    global partitions
    # generate partitions
    # https://en.wikipedia.org/wiki/Partition_function_(number_theory)#Recurrence_relations
    for n in range(len(partitions), goal + 1):
        partitions.append(0)
        for k in range(1, n+1):
            pent = pentagonalNumber(k)
            if pent > n:
                break
            partitions[n] += ((-1) ** (k + 1)) * partitions[n - pent]
            if pent + k <= n:
                partitions[n] += ((-1) ** (k + 1)) * partitions[n - pent - k]

    return partitions[goal]