

def printString(string):
    if(string=="Hi"):
        return ""
    return print(string)
    
printString(string)
    
# str = "python"

for char in string:
    print(char)

for i in range(len(string)):
    print("Index:", i, "Letter", string[i])
    

# new_str = "" 

# for char in str:
#     new_str += char.upper()
    
# print(new_str)

found = 0

for char in string:
    if char == 'M':
        print("It's an M series BMW")
        found = 1
        break
    print("Checking if it's an M")

if(found == 0):
    print("It's a regular BMW model")


word = "rishabda"
reversed_word = ""

for char in word:
    # print(char)
    print(reversed_word)
    reversed_word = char + reversed_word  # insert at the beginning
    

print(reversed_word)


for index, letter in enumerate(string):
    if letter == " ":
        print(f"Index {index}: Space Letter")
        # continue    
    else:
        print(f"Index {index}: {letter} Letter")

String Slicing

string = "BMW M5 Competition"

string = "hello"
print(string[2::-1])

string = "hello"
print(string[4::-1])

print("world"[2::-1])

print("banana"[1:5:2])

print("python"[5:1:-1])