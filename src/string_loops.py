string = "BMW M5 Competition"

def printString(string):
    if(string=="Hi"):
        return ""
    return print(string)
    
printString(string)
    
str = "python"

for char in str:
    print(char)

for i in range(len(str)):
    print("Index:", i, "Letter", str[i])
    

new_str = "" 

for char in str:
    new_str += char.upper()
    
print(new_str)