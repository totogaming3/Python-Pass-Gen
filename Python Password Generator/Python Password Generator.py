import random
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!/\()$?!{}[]@#^*"

Use_for = lowercase + uppercase + numbers + symbols
length = 20
password = "".join(random.sample(Use_for, length))
print("Your new password is", password)