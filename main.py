import random
import string
from pyfiglet import Figlet


f=Figlet(font="slant")
print(f.renderText("Code by kisna infotech"))
print("-------------------------------------")
print(f.renderText("password generator"))


length=int(input("\nEnter your password length:"))

lower=string.ascii_lowercase
upper=string.ascii_uppercase
digit=string.digits
symbols=string.punctuation

store=lower+upper+digit+symbols

final=random.sample(store,length)

password="".join(final)

print("your password is:",password)

