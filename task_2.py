from typing import Callable
import re

def generator_numbers(text: str):
    pattern = r' \d*\.\d+ | \d+ '
    match = re.findall(pattern, text)
    
    if match:
        for n in match:
            yield float(n)


def sum_profit(text: str, func: Callable):
    total_sum = 0
    numbers = func(text)
    
    for n in numbers:
        total_sum += n
    
    return total_sum

# text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
text = "20.12 or 12.28 . 333.1  and 2.9  or 0.2 and 2 or4.4 end 5.5."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")