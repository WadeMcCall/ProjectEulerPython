BILLION = 10 ** 9

def findTriple(m, n):
    a = m ** 2 - n ** 2
    b = 2 * m * n
    c = m ** 2 + n ** 2
    return (a, b, c)

# More use for Euclid's formula, these are pythagorean triples with one leg exactly one off half the hypotenuse 
def main():
    n = 1
    sum = 0
    m = 2
    while True:
        a, b, c = findTriple(m, n)

        if 3 * c > BILLION:
            break

        # +1 solution found
        if (c + 1) / 2 == a or (c + 1) / 2 == b:
            sum += 3 * c + 1

            # -1 solution implicitly exists at this m for this n
            m += 2 * n
            
            a, b, c = findTriple(m, n)
            if 3 * c > BILLION:
                break

            sum += 3 * c - 1
            n = m
        m += 1
    print (sum)
    return

if __name__ == '__main__':
    main()