def average(grades):
    return sum(grades.values()) / len(grades)

class_B = {
    "m": 1,
    "a": 5,
    "k": 8,
    "r": 9
}

class_C = {
    "c": 40,
    "a": 35,
    "k": 30,
    "e": 25,
}

print(f"Average for class B: {average(class_B)}")
print(f"Average for class C: {average(class_C)}")