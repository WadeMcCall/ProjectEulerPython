from itertools import cycle

def average_word_length(words):
    # Sum the lengths of all the words
    total_length = sum(len(word) for word in words)
    
    # Divide by the number of words
    average_length = total_length / len(words)
    
    return average_length

def decrypt(msg, key):
    newVals = (a ^ b for a, b in zip(msg, cycle(key)))

    return (list(newVals))

def arrToMsg(arr):
    return ''.join(map(chr, arr))

# very sophisticated english detection algorithm :)
def isEnglish(msg):
    words = msg.split()
    if(average_word_length(words) < 10):
        if not ("the" in words or "are" in words):
            return False
        print(words)
        return True
    return False

def main():
    f = open("data/0059_cipher.txt")
    fileStr = f.read()
    valuesArr = [eval(i) for i in fileStr.split(",")]
    tempVals = []
    for i in range(97, 123):
        for j in range(97, 123):
            for k in range(97, 123):
                key = [i, j, k]
                tempVals = decrypt(valuesArr, key)
                msg = (arrToMsg(tempVals))
                if(isEnglish(msg)):
                    print(sum(tempVals))
                

if __name__ == "__main__":
    main()