import itertools
from collections import Counter
import math


def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def eights_together(vector: [int]) -> bool:
    eights_indices = [i for i, num in enumerate(vector) if num == 8]

    # No 8s in the vector
    if not eights_indices:
        return True

    for i in range(len(eights_indices) - 1):
        if eights_indices[i + 1] - eights_indices[i] != 1:
            return False

    return True


def nines_separated(vector: str) -> bool:
    seen_numbers = set()
    last_nine_index = None

    for i, num in enumerate(vector):
        if num == 9:
            if last_nine_index is not None:
                intervening_number = vector[last_nine_index + 1]
                if intervening_number in seen_numbers or intervening_number == 9:
                    return False
                seen_numbers.add(intervening_number)
            last_nine_index = i

    return True


def numbers_separated(vector: [int]) -> bool:
    frequency = Counter(vector)

    numbers_appearing_twice = [num for num, count in frequency.items() if count == 2]

    if len(numbers_appearing_twice) != 2:
        return False

    for number in numbers_appearing_twice:
        first_occurrence = vector.index(number)
        second_occurrence = vector.index(number, first_occurrence + 1)

        if 8 not in vector[first_occurrence + 1:second_occurrence]:
            return False

    return True


def threes_surrounded(vector: [int]) -> bool:
    for i, num in enumerate(vector):
        if num == 3:
            if i == 0 or i == len(vector) - 1 or vector[i - 1] != vector[i + 1]:
                return False

    return True


def divisible_by_same_number(vector: [int]) -> bool:
    number1 = vector[4]
    number2 = vector[5]
    number3 = vector[6]

    gcd_first_two = math.gcd(number1, number2)

    return math.gcd(gcd_first_two, number3) == gcd_first_two


def second_divisible_by_last(vector):
    if len(vector) < 2:
        return False

    second_last_number = vector[-2]
    last_number = vector[-1]

    if last_number == 0:
        return False

    return second_last_number % last_number == 0


# Apply validations to vector
def is_valid_combination(vector: [int]) -> bool:
    string_vector = ''.join(map(str, vector))

    if not eights_together(vector):
        return False

    if not nines_separated(vector):
        return False

    if not eights_together(vector):
        return False

    if not second_divisible_by_last(vector):
        return False

    # checking last number to be prime
    if not is_prime(vector[-1]):
        return False

    return True


def generate_phone_numbers(vector):
    valid_combinations = []
    for perm in itertools.permutations(vector):
        if is_valid_combination(perm):
            valid_combinations.append(perm)
    return valid_combinations


if __name__ == "__main__":
    combinations = generate_phone_numbers([0, 0, 2, 2, 3, 4, 4, 8, 8, 9, 9])
    print(f'The possible combinations are: {len(combinations)}')
