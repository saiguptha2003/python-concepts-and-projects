#Write a program to reverse a string word by word. Use Python class to achieve the result.
class python_string():
     __str=None
     def __init__(self, s):
          self.__str=s
     def reverse_words(self):
          return ' '.join(reversed(self.__str.split()))
s=input()
pp=python_string(s)
print(pp.reverse_words())