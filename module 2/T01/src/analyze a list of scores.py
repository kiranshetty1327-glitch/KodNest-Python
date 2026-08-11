n = int(input())
scores = []

for i in range(n):

    score = int(input())
    scores.append(score)
search_score = int(input())

maximum = max(scores)
minimum = min(scores)
total = sum(scores)
print("Highest Score:",maximum)
print("Lowest Score:",minimum)
print("Total Score:",total)

if search_score in scores:
    print("Search Result: Found")
    print("Search Result: Not Found")
