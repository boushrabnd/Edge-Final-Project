print("Welcome to Story House! \nIf you wanna have some fun, push in a character's name and gender and make the character's decisions as you read a unique story you design!\n    ")
for i in range (10):
    print("*", end="")
print()

#CHARACTER name and gender

char_1 = input("Who is your character?\n")

while char_1 == " " or char_1 == "" or char_1 == "no":
    char_1 = input("Please type a character name!\n")

char_1_gender = input("Is your character a lady, a gentleman or else?\nType *she* for lady, *he* for gentleman, *it* for other!\n")

while char_1_gender != "she" and char_1_gender != "he" and char_1_gender != "it":
            char_1_gender = input("Nah, you gotta type a pronoun for your character!\n\n")

if char_1_gender == "it":
    char_1_gender = input("Wow! So what exactly is your character?\nType your character's species with an indefinite article *a* or *an* :)\n")

print()

for i in range (1,4):
    for j in range (i):
        print ("*", end="")
    print()
l = [char_1,char_1_gender]
print("\nThis is your character:\n", char_1)

if char_1_gender == "she":
    print("She's a lady")
elif char_1_gender == "he":
    print("He's a gentleman")
else:
    print ("It is", char_1_gender)
    
print()

for i in range (3,0,-1):
    for j in range (i):
        print ("*", end="")
    print()
    
class Scene:
    
    
