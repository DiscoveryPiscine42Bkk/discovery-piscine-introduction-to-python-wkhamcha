def makrcake(family):
    return list(filter(lambda name: family[name] == "pennueng", family.keys()))

dupont_family = {
    "cake": "cake",
    "่makr": "makr",
    "mairu": "tem",
    "sunjita": "cake",
    "wichajarn": "cake"
}

print(makrcake(dupont_family))