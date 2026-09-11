# return square
def getSquare(a: int) -> int:
    return a*a
print(getSquare(4))

# return largest number
def getLargestNumber(a: int, b: int) -> int:
    if a>b:
        return a
    else:
        return b
print(getLargestNumber(2,9))

# check positive number
def isPositive(a: int) -> bool:
    return a > 0
print(isPositive(-1))

# count vowels
def countVowels(s: str) -> int:
    count = 0
    for c in s:
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            count += 1
    return count
print(countVowels('clandestine'))

# return average
def getAverage(nums: list[int]) -> float:
    total = 0
    for n in nums:
        total += n
    return total/len(nums)
print(getAverage([2,5,7,3,1]))

# return range values (highest and lowest)
def getRangeValues(nums: list[int]) -> list[int]:
    highest_val = nums[0]
    lowest_val = nums[0]
    for val in nums:
        current_val = val
        if highest_val < current_val:
            highest_val = current_val
        if lowest_val > current_val:
            lowest_val = current_val
    return [lowest_val, highest_val]
print(getRangeValues([2,5,6,8,2,4]))


# Mini Units Converter

# celsius to fahrenheit
def celsiusToFahrenheit(arg: float) -> float:
    return (arg * 9/5) + 32

# fahrenheit to celsius
def fahrenheitToCelsius(arg: float) -> float:
    return (arg - 32) * 5/9

# divide the length value by 1.609
def kilometersToMiles(arg: float) -> float:
    return arg/1.609

def unitsConverter():
    print('''This is a mini units converter. Select a number to proceed...''')
    print('1. Celsius to fahrenheit\n2. Fahrenheit to celsius\n3. Kilometer to miles')
    option = input('Select a number: ')
    arg = input('Input a value: ')
    if option == '1':
        result = celsiusToFahrenheit(float(arg))
        print(f'{arg}\'C is about {result}\'F')
        return
    elif option == '2':
        result = fahrenheitToCelsius(float(arg))
        print(f'{arg}\'F is about {result}\'C')
        return
    elif option == '3':
        result = kilometersToMiles(float(arg))
        print(f'{arg}\'km is about {result}\' miles')
        return
    else: 
        print('Whoop! couldn\'t quite work with that. Wanna try that again?!')
        return
unitsConverter()