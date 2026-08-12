sentence = input()

clened =sentence.strip()
print("Clened:",clened)
sentence=clened.lower().replace(".","")
print("Normalized:",sentence)
print("Words:",sentence.split(" "))

print("Slug:","-".join(sentence.split()))
print("Uppercase:",sentence.upper())

print("Python Position:",sentence.find("python"))
