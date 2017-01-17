import math


class Prime():
    def checkInvalid(self, n):
        try:
            int(n)
            return False
        except ValueError:
            return True

    def getInput(self, n=None):
        try:
            if self.checkInvalid(n):
                return 'Input value should be an Integer'
            else:
                if int(n) > 1:
                    return int(n)
                else:
                    raise ValueError
        except ValueError:
            return 'Input should be a number greater than 1'

    def isPrime(self, n):
            i = 2
            m = math.sqrt(n)
        # use trial division
            while i <= m:
                if n % i == 0:
                    return False
                i += 1
            else:
                return True

    def primeNumbers(self, n):
        n = self.getInput(n)
        if isinstance(n, int):
            primes = []
            for number in range(2, n+1):
                if self.isPrime(number):
                    primes.append(number)
            return primes
        else:
            return n
