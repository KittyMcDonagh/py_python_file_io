# Import 2 standard libraries - Regular Expressions and Collections

# Import Regular Expressions (https://docs.python.org/3/library/re.html?highlight=regular%20expressions#re-objects)
import re

# Import Collections (https://docs.python.org/3/library/collections.html?highlight=collections#module-collections)
import collections

# Open the book and read into a string called text in lower case
text = open('book.txt').read().lower()

# Find all expressions with the following - 'w' means anythng that's not a whitespace, '+' means one or more
# That means every occurrence of one or more characters that's not a whitespace, is viewed as a word
words = re.findall('\w+', text)

# Of the word picked up above, use the counter method to find the 10 most common words
# The result will be a tuple with the word and the number of occurrences
print(collections.Counter(words).most_common(10))




