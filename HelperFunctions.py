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
    def max_score_number(numbers):
        def calculate_score(number):
            numbers_list = numbers.copy()
            numbers_list.remove(number)
            factors = HelperFunctions.remaining_factors(number, numbers_list)
            factors_sum = sum(factor for factor in factors)
            return number - factors_sum

        scores = {num: calculate_score(num) for num in numbers}
        max_score_number = max(scores, key=scores.get)

        return max_score_number

    @staticmethod
    def continue_game():
        while True:
            continue_game = input("(press return to continue)")
            if continue_game == "":
                print("")
                break


