from lib.FigurateNumbers import pentagonalNumber
import time

def main():
    partitions = [1, 1] # base case p(0) = 1, also p(1) = 1, trivially.
    goal = 100

    # generate partitions
    # https://en.wikipedia.org/wiki/Partition_function_(number_theory)#Recurrence_relations
    for n in range(2, goal + 1):
        partitions.append(0)
        for k in range(1, n+1):
            pent = pentagonalNumber(k)
            if pent > n:
                break
            partitions[n] += ((-1) ** (k + 1)) * partitions[n - pent]
            if pent + k <= n:
                partitions[n] += ((-1) ** (k + 1)) * partitions[n - pent - k]

    print(partitions[goal] - 1)

if __name__ == '__main__':
    main()