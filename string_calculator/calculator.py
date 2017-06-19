import re

CUSTOM_DELIMITER_IDENTIFIER = '//'


def add(numbers):
    if numbers:
        if numbers.startswith(CUSTOM_DELIMITER_IDENTIFIER):
            sp_numbers = numbers[4:].split(numbers[2])
        else:
            sp_numbers = re.split('[,\n]', numbers)

        ints = map(int, sp_numbers)
        if any(n < 0 for n in ints):
            raise Exception('Negative numbers not allowed')
        total = sum(ints)
        return total
    else:
        return 0
