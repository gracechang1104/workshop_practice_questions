# 1. DATA TYPE OF THE FOLLOWING EXPRESSIONS?

print(type(5))

print(type(5.0))

print(type(5*2))

print('5' * 2)

print(5 in [1, 4, 6])


# 2. String Manipulation
# Write string expressions involving s1 and s2 and operators + and * that evaluate to:
# '-+'
# '-+-'
# '+--+--'
# '+--+--+--+--+--+--+--+--+'

s1 = '-'
s2 = '+'


# 3. List Manipulation

'''Step 1. Write an expression creating a new list called roman, containing
the strings 'Julius', 'Augustus', 'Brutus', and 'Cassius'.'''

roman = ['Julius', 'Augustus', 'Brutus', 'Cassius']

'''Step 2. Write an expression creating a list called english,
# containing the strings 'Dickens', 'Austen', 'Henry', and 'Elizabeth'.'''

english = ['Dickens', 'Austen', 'Henry', 'Elizabeth']

'''Step 3. Print out 'Brutus' from the roman list'''


'''Step 4. Now write an expression creating a list called rulers, containing the first two elements of roman
and the last two elements of english. Use list manipulation expressions; do not just copy the data manually.'''

rulers = roman[0:2] + english[2:]

print(rulers)

# 5. List namespace and method invocations
'''Let list lst be:
number_list = [2,3,4,5]

What happens when you call the following?
list.sort(number_list)
number_list.append(3)
number_list.count(3)
number_list.insert(2, 1)'''

number_list = [4, 3, 2, 5]

list.sort(number_list)
print(number_list)



''' 
If you've ever visited Europe (or Canada), you'll know that they tend to 
measure temperature in degree Celsius rather than Fahrenheit.
Conversion is pretty simple:
if f is the temperature in degree Fahrenheit,
then the temperature in degree Celsius is:
c = (f-32)*5/9.
Write a function convert() that
takes as an input degree Fahrenheit and
returns degree Celsius. '''

# 4. For Loops, If Statements, and List
'''Write a function called tallEnough() that
takes a single parameter, the user’s height in inches.
If the height is 48 or more, the function should return “You can go on this ride.”
Otherwise it should return the string “Sorry, you’re not tall enough.”'''



'''Write a function that takes a list of names and returns a list of names
that has at least 5 characters.'''

''' INPUT: ['Fiona', 'Alex', 'Bob', 'Bill', 'Jessica']
    OUTPUT: ['Fiona', 'Jessica']'''



