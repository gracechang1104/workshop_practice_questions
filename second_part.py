''' Implement a function date that takes 4 inputs:
a non-abbreviated weekday (as a string)
a non-abbreviated month (as a string)
a day in the month (a an integer)
a year (as an integer)
Function date() should return the complete date (as a string)
using 3-character abbreviations for the weekday and month and
using the format shown below:

INPUT: date('Tuesday', 'October', 20, 2014)
OUTPUT: 'Tue, Oct 20, 2014'

INPUT: date('Thursday', 'May', 1, 2014)
OUTPUT: 'Thu, May 1, 2014' '''



'''Write a function called countWord(). It takes 2 parameters:
The name of a text file (e.g. frankenstein.txt) and
a word to be searched within that file.

INPUT: countWord('frankenstein.txt', 'people')
OUTPUT: 11
'''

def countWord(filename, word):
    file = open(filename, "r")
    content = file.read()
    wordList = content.split()


