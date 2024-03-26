def incremental(numbers):
    result = []
    for number in numbers:
        if number%2 == 0:
            result.append(number + 1)
        elif number%2 != 0:
            result.append(number + 1)
        else:
            result.append(number)
    return result

original_numbers = [1,2,3,4,5,6,7,8]
result_numbers = incremental(original_numbers)
print("Original numbers:", original_numbers)
print("Modified numbers:", result_numbers)