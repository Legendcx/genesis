print("Hello my world")

def ali(a, b):
    return a +b

print(ali(5,3))

a = 5
b = 4

print(a + b)

print("burhan" * 4)
a = "Burhan"
b = "Ebru"
c = "May & Kyk"

print(f"{a} ve {b}'nun çocukları olan {c} okula gidiyorlar.")
## Burada ben f string metoduna kullandım. herkese başarılar.

class calisan:
    
calisan1 = calisan()
calisan1.name = "Ali"
calisan1.surname = ""Veli"
calisan1.age = 20

## Using loops = döngüler Okumak

sea = open("fishes.txt", "r")
for line in sea:
    print(line
sea.close()

print("Hayat olduğu gibi güzel.")
          
b = "Burhan Nasıl?"
print(b.capitalize())
print(b.upper())

def modular_function(n):
    return lambda x: x**n

print(modular_function(3))

word = input("give me a word")

counter = 0
for i in word:
    counter += 1
    if counter < len(word):
        i += "_"
    print(i, end="")


