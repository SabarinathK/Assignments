#Write a program to read the string and replace a space in a string with given character.

string = "C: Localdrive Documents user File1.png"
import re
   
#Replace space with specific character ch  
string = string.replace(" ","\ " )
whitespace = r"\s+"
nospaces = re.sub(whitespace, "", string)

print(nospaces)