"""Median calculator."""
"""!ENTER YOUR SOLUTION HERE!"""

median = 0

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        numbers.sort()
        print(numbers)
        if len(numbers) % 2 != 0:
            median = numbers[len(numbers)//2]
        else:
            middleIndx = numbers[len(numbers)//2]
            median = (middleIndx + middleIndx-1) / 2
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(median)
