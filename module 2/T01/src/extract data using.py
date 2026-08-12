word = input()

first = int(input())
second = int(input())
third = int(input())

numbers = [first, second, third]
record = (first, second, third)

print("Middle:",word[1:-1])
print("First Two:",numbers[:2])
print("Reversed Tuple:",tuple(numbers[::-1]))
