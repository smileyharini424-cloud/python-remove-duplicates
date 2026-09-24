numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

seen = set()
unique_numbers = []

for number in numbers:
    if number not in seen:
        seen.add(number)
        unique_numbers.append(number)

print("List without duplicates:", unique_numbers)
