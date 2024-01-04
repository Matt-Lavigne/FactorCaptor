class HelperFunctions:

    def get_factors(number):
        factors = []
        for i in range(1, number + 1):
            if number % i == 0:
                factors.append(i)
        return factors

    def remaining_factors(number, numbers):
        factors = number.get_factors()
        for element in factors:
            if element not in numbers:
                factors.remove(element)
        return factors
