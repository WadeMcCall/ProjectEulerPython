def main():
    i = 1
    numSamePowers = 0
    for val in range(1,10):
        j = 1
        while True:
            if len(str(val ** j)) == j:
                numSamePowers += 1
            else:
                break
            j += 1
    print(numSamePowers)

if __name__ == "__main__":
    main()