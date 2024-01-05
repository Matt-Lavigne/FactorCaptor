class HelperFunctions:

    def get_factors(number):
        factors = []
        for i in range(1, number + 1):
            if number % i == 0:
                factors.append(i)
        return factors

    def remaining_factors(number, numbers):
        factors = HelperFunctions.get_factors(number)
        for element in factors.copy():
            if element not in numbers:
                factors.remove(element)
        return factors

    @staticmethod
    def continue_game():
        while True:
            continue_game = input("(press return to continue)")
            if continue_game == "":
                print("")
                break


