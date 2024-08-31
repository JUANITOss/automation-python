import pprint

def charCount(phrase):
    
    charCounter = dict()
    
    for character in phrase.lower():
        
        if character != ' ':
            charCounter.setdefault(character, 0)
            charCounter[character] = charCounter[character] + 1
        
    return charCounter
            
print(pprint.pformat(charCount("iii chile")))
