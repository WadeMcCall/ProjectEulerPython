from lib.Polynomial import Polynomial

f = Polynomial([1, -1]) # x - 1
g = Polynomial([1, 1]) # x + 1

print(f)
print(f - g) # should be -2
print(f * g) # should be x^2 - 1
print(f + g)

h = Polynomial([2, -3, 4, 5])
i = Polynomial([1, 2])

res = h/i
print(res)
print(res * i)