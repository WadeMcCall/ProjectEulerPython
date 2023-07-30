from itertools import permutations, combinations

def getAllArithmeticExpressions():
    expressions = ["+", "+", "+", "-", "-", "-", "*", "*", "*", "/", "/", "/"]
    gennedExpressions = combinations(expressions, 3)
    gennedExpressions = list(set(gennedExpressions))
    newExpressions = []
    for e in gennedExpressions:
        newExpressions += permutations(e, 3)
    newExpressions = list(set(newExpressions))
    return newExpressions
    
def createExpression(nums, symbols):
    result = [None] * 7
    result[::2] = nums
    result[1::2] = symbols
    return result

# eval is slow lol
def evaluate(num1, num2, symbol):
    if symbol == "+":
        return num1 + num2
    elif symbol == "-":
        return num1 - num2
    elif symbol == "*":
        return num1 * num2
    elif symbol == "/":
        try:
            return num1 / num2
        except:
            return 0
    else:
        return 0

# (a op b) op (c op d) breaks my assumptions because it cannot be rearranged as a left-to-right expression
def edgeCase(exp):
    result = 0
    try:
        leftSide = evaluate(exp[0], exp[2], exp[1])
        rightSide = evaluate(exp[4], exp[6], exp[5])
        result = evaluate(leftSide, rightSide, exp[3])
    except ZeroDivisionError:
        return 0
    return result

def evaluateExpression(exp):
    result = exp[0]
    for i in range(1, len(exp), 2):
        result = evaluate(result, exp[i+1], exp[i])
    return result

def evaluateSet(nums):
    results = []
    for e in getAllArithmeticExpressions():
        for perm in permutations(nums):
            exp = createExpression(perm, e)
            result = evaluateExpression(exp)
            edge = edgeCase(exp)
            if result >= 1 and result % 1 == 0 and result not in results:
                results.append(result)
            if edge >= 1 and edge % 1 == 0 and edge not in results:
                results.append(edge)
    results.sort()
    i = 1
    while True:
        if len(results) < i:
            return i - 1
        if results[i-1] != i:
            return i - 1
        i += 1

def main():
    max = 0
    bestSet = []
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sets = combinations(nums, 4)
    for set in sets:  
        result = evaluateSet(set)
        if result > max:
            max = result
            bestSet = set
    print(max)
    print(bestSet)
    return

if __name__ == '__main__':
    main()