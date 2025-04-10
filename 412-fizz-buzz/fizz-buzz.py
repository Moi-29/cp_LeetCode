class Solution(object):
    def fizzBuzz(self, n):
        FizzBuzzResult = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                FizzBuzzResult.append('FizzBuzz')
            elif i % 3 == 0:
                FizzBuzzResult.append('Fizz')
            elif i % 5 == 0:
                FizzBuzzResult.append('Buzz')
            else:
                FizzBuzzResult.append(str(i))
        return FizzBuzzResult
