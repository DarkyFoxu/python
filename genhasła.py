import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
liczby = "0123456789"
symbole = "[]{}()*;/,._-"
all = lower + upper + liczby + symbole
length = int(input("Podaj długość hasła:"))
haslo = "".join(random.sample(all,length))

print("Wygenerowane hasło:", haslo)