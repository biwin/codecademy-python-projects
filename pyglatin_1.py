__author__ = 'payload'

print 'Welcome to the Pig Latin Translator!'

# len(x) computes the length of the given 'x'
# isalpha checks whether the given string is alphabet or not

original = raw_input("Enter a word")
if len(original) > 0 and original.isalpha():
    print(original)
else:
    print "empty"