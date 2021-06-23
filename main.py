import string, random

letters=string.ascii_letters
digits=string.digits
special_char=string.punctuation

possibilities=[]
possibilities.extend(list(letters))
possibilities.extend(list(digits))
possibilities.extend(list(special_char))
random.shuffle(possibilities)
password_length=int(input("Enter Your Password length"))
print("".join(possibilities[0:password_length]))
