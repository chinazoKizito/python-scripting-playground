import re

# Finds where there is one or more numbers in the sentence
x = "my Favourite 3 numbers are 10, 42, 78"
a = re.findall("[0-9]+", x)
print(a)

x = "X-Sieve, Kizito Chinazo, HALLELUYA"

# Finds where a string begins with a space, characters are not white space,matches any character and more characters
# until exhaustion
b = re.findall("\s\S.*", x)

# Finds where white-space, non-white space, all characters around it but the string ends with 'A'
b = re.findall("\s\S+A", x)

# Finds where a string begins with X matches any number of characters after X repeatedly and ends were there is a
# comma(,)
j = re.findall("^X.+,", x)
print(j)

# () denotes where the search will start and end as well: This code finds ["Kilimanjaro and Abokina"]
x = "From Kilimanjaro % abokina, weterem Bread and malt"
y = re.findall("^From (\S.+\s%\s\S+,)", x)
print(y)

x = "From kizitochinazo@gmail.com sat Jan 5 8:18:2  2022"

# look through the string, find where @ is located
# Start extracting with the parenthesis
# Match Non-blank characters
y = re.findall('@([^ ]*)', x)
m = re.findall("^From .*@([^ ])", x)  # Fine-tuning the code above
print(y)


# prefexing with \ before a character to make it behave like a regex function
x = "We just receieved $500.00 for clothes"
y = re.findall('\$[0-9.]+', x)
print(y)


