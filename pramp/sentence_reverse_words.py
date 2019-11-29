'''
Sentence Reverse - Pramp

You are given an array of characters arr that consists of sequences of characters separated by
space characters. Each space-delimited sequence of characters defines a word.
Implement a function reverseWords that reverses the order of the words in the array
in the most efficient manner.
Explain your solution and analyze its time and space complexities.

Example:
input:  arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
                'm', 'a', 'k', 'e', 's', '  ',
                'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]
output: [ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ',
          'm', 'a', 'k', 'e', 's', '  ',
          'p', 'e', 'r', 'f', 'e', 'c', 't' ]
'''
def reverse_words(arr):
  word = []
  spaces = []
  output = []
  for c in arr:
    if c == ' ':
      spaces.append(c)
      if word:
        output = word + output
      word = []
    else:
      word.append(c)
      if spaces:
        output = spaces + output
      spaces = []
  output = spaces + word + output
  return output