import math


class Prime():
    def checkInvalid(self, n):
        try:
            int(n)
            return False
        except ValueError:
            print('Input value should be an Integer')
            return True

    def getInput(self, n=None):
        n = n or input("Enter a number to get a list of all prime numbers up to that number: ")
        try:
            if checkInvalid(n):
                getInput()
            else:
                return int(n)
        except ValueError:
            print('Input should be a number greater than 1')
            getInput()

    def primeNumbers(self, n):
        primes = []
        # use trial division
        i = 2
        while (i <= round(math.sqrt(n))):
            if not n % i == 0:
                primes.append(i)
                i += 1
        return primes
