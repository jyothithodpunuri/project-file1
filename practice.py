# numbers
print(2 + 2)
print((50 - 5 * 6) / 4)

print(8 / 5)  # division always returns a floating point number

print(17 // 3)  # floor division discards the fractional part

print(17 % 3)  # the % operator returns the remainder of the division

print(2 ** 7)  # 2 to the power of 7

# strings
print('welcome to python world')
print("doesn't")
print('First line \nsecond line')

# If you don’t want characters prefaced by \ to be interpreted
# as special characters,
# you can use raw strings by adding an r before the first quote:
print(r'c:\some\name')
print('c:\some\name')

# String literals can span multiple lines.
# One way is using triple-quotes: """...""" or '''...'''
# End of lines are automatically included in the string,
# but it’s possible to prevent this by adding a \ at the end of the line.
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# Strings can be concatenated with the + operator, and repeated with *:
print(3 * 'un' + 'ium')
print('py' 'thon')
print('this is a test '
      'to write long strings '
      'Concatened together')

# can't concatenate a variable and a string literal, but (+) will work
prefix = 'py'
# print(prefix 'thon')
print(prefix + 'thon')

# Strings can be indexed,
word = 'python'
print(word[0])
print(word[4])

# Indices may also be negative numbers, to start counting from the right:
print(word[-1])
print(word[-2])
print(word[-6])

# While indexing is used to obtain individual characters,
# slicing allows you to obtain substring:
print(word[0:2])  # # characters from position 0 (included) to 2 (excluded)

# Note how the start is always included, and the end always excluded.
# This makes sure that s[:i] + s[i:] is always equal to s:
print(word[:2] + word[2:])
print(word[:4] + word[4:])

# characters from the second-last (included) to the end
print(word[-2:])

#  python cannot be changed - they are immutable
#  therefore assigning to an indexed position in the string
#  results in an error
#wotrd [0]='j'
#word [2:]='py'

#  if you need a different string, you should created new one
print('J'+word[1:])
#  len() returns length of a string
print (len('python'))
print(word)

#  Lists
#  lists might contain items of different types
#  but useully the items all have the same type
squares = [1,4,9,16,25]
print(squares)
print(squares[0])
print(squares[-3])

#  unlike string which are immutable
#  lists are mutable type, i.e. it is possible to theeir content:
cubes=[1,8,27,65,125]
cubes[3]=64
print(cubes)

#  replace some values
cubes[20:1]=[20]
print(cubes)

#  clear the replacing all the eliments with an emty list
cubes[:]=[0]
print(cubes)

#  length of lists

print(len(['a'+'b']))


#  Strings can be indexed,

print(word[0])
print(word[4])
print(word[0])
print(word[1])
print(word[2])
print(word[3])
print(word[4])
print(word[5])
print(word[6])

print(word[-1])
print(word[-2])
print(word[-3])
print(word[-4])
print(word[-5])
print(word[-6])


#  Indices may also be negative numbers, to start counting from the right:
#  print(word[-1])
#  print(word[-2])
#  print(word[-6])