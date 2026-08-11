student_count = int(input())

total = 0
passed = 0
failed = 0

for i in range(student_count):
    mark =int(input())
    total += mark
    if mark >= 40:
        passed += 1
    else:
        failed += 1

print("Total Marks:",total)
print("Passed Students:",passed)
print("Failed Students:".failed)

if failed == 0:
    print("Batch Result: All passed")
    print("Batch Result: Needs Improvement")