class HelperFunctions:

    def get_factors(number):
        factors = []
        for i in range(1, number + 1):
            if number % i == 0:
                factors.append(i)
        return factors

    def remaining_factors(number, numbers):
        factors = HelperFunctions.get_factors(number)
        for element in factors:
            if element not in numbers:
                factors.remove(element)
        return factors


