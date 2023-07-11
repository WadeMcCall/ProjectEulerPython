class RomanNumeral:
    ORDER = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    VALUES = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }

    def __init__(self, roman):
        self.roman = roman
        self.decimal = self._convert_to_decimal()
        self.minimal = None
        self.minimal = self._minimal()

    def _minimal(self):
        if self.minimal is not None:
            return self.minimal
        return self._convert_to_roman()

    def _convert_to_roman(self):
        num = self.decimal
        roman = ""
        while num > 1000:
            roman += "M"
            num -= 1000
        while num > 0:
            if num >= 100:
                subPart = "C"
                midPart = "D"
                topPart = "M"
                x = num // 100
                num = num % 100
            elif num >= 10:
                subPart = "X"
                midPart = "L"
                topPart = "C"
                x = num // 10
                num = num % 10
            else:
                subPart = "I"
                midPart = "V"
                topPart = "X"
                x = num
                num = 0
            if x == 9:
                roman += subPart + topPart
            elif x >= 5:
                roman += midPart + (subPart * (x - 5))
            elif x == 4:
                roman += subPart + midPart
            else:
                roman += subPart * x
        return roman

    def _getChunkValue(self, chunk):
        if len(chunk) == 1:
            return self.VALUES[chunk]
        subValue = sum([self.VALUES[char] for char in chunk[:1]])
        return self.VALUES[chunk[-1]] - subValue

    def _convert_to_decimal(self):
        tempRoman = self.roman
        sum = 0
        while tempRoman != "":
            chunk = self._getChunk(tempRoman)
            tempRoman = tempRoman[len(chunk):]
            sum += self._getChunkValue(chunk)
        return sum

    def _getChunk(self, remainingNumeral):
        subtractiveValues = ["I", "X", "C"]
        if remainingNumeral[0] not in subtractiveValues:
            return remainingNumeral[0]
        if len(remainingNumeral) == 1:
            return remainingNumeral
        if self.ORDER.index(remainingNumeral[1]) < self.ORDER.index(remainingNumeral[0]):
            return remainingNumeral[:2]
        return remainingNumeral[0]