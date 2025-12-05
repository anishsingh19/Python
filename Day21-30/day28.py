#Day28 - f-strings in Python

# String Formatting in Python
letter = "Hey my name is {} and I am from {}"
country = "India"
name = "James"
print(letter.format(name, country))

letter2 = "Hey my name is {1} and I am from {0}"
print(letter2.format(country,name))


# f-strings in Python
print(f"Hey my name is {name} and I am from {country}")
print(f"Hey my name is {{name}} and I am from {{country}}")


txt = "For only {price:.2f} dollars!"    #2f
print(txt.format(price=49.09999))

price = 69.088888                        #2f
txt = f"For only {price:.2f} dollars!"
print(txt)

print(f"{2 * 30}")             #f produces string
print(type(f"{2 * 30}"))

