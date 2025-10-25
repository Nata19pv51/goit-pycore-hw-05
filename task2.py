from typing import Callable
import re

def generator_numbers(text: str):
    words = text.split(" ")
    pattern = r"\d*\.\d+"
    
    for word in words:
        match = re.search(pattern, word)
        
        if match:
            number = float(match.group().strip())
            yield number

def sum_profit(text: str, func: Callable):
    total_sum = 0
    numbers = func(text)
    
    for n in numbers:
        total_sum += n
    
    return total_sum

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")