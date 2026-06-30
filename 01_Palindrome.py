## checking whether the given string is palindrome or not 

s = input("Enter String:")

s = s.lower()           ## used to convert the strings to convert into lowercase letters to avoid misconsuptions in the cases like "Madam"
s = s.replace(" ", "")  ## to removee the spaces

if(s == s[::-1]):
  print("It is a palindrome")
else:
  print("It is not a palindrome")
