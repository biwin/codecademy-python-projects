__author__ = 'payload'

pyg = 'ay'

original = raw_input('Enter a word:')


if len(original) > 0 and original.isalpha():
    print original
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]
    print new_word
else:
    print 'empty'


# notes
# x.lower() change the x to lowercase
# x.upper() change the x to uppercase
# string = "hello dude", string[1:8] tells to slice the-
# string from the 1st index to the 8th index, not including 8.
# "word"[0] is 'w', [1] is 'o'