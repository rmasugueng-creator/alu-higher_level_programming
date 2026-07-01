#!/usr/bin/python3
str = "Python is an interpreted, object-oriented programming language that combines remarkable power with very clear syntax"
str = str[str.find("obj"):str.find(" lan")] + str[str.find(" with"):str.find(" very")] + " " + str[:6]
print(str)

