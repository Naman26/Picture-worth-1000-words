import math

def letterCount():
    #Reading the book
    with open('book.txt', 'r') as inp:
        data = inp.read()
    str = ""
    for i in data:
        str += i
    #Storing data as list
    str = list(str)
    dictionaryChar = {}
    for i in str:
        #If key exists, increase value
        if i in dictionaryChar:
            dictionaryChar[i] += 1
        #Else create a new key set value to one
        else:
            dictionaryChar[i] = 1
    #Total number of characters in the text
    totalChars = sum(dictionaryChar.values())
    #Return dictionary of characters and total characters
    return dictionaryChar, totalChars

def entropy(X, total):
    summation = 0.0
    #For every key in dictionary
    for x in X:
        
        logArg= math.log((1/(X[x]/total)), 2)
        summation+= (X[x]/total)*logArg
    return summation

#
# n= {"0": 0.25, "1": 0.75}
# print(entropy(n,1))

from PIL import Image

def pixelIntensity():
    img = Image.open('image.png').convert('LA')
    img.save('greyscale.png')
    img = Image.open('greyscale.png','r')
    x,y = img.size
    image= list(img.getdata())
    intensity={}
    for i in image:
        if i[0] in intensity:
            intensity[i[0]]+= 1
        else:
            intensity[i[0]] = 1
    return intensity, x*y

def main():
    dictionaryBook, total=letterCount()
    print("Book Entropy: ",entropy(dictionaryBook,total)*total)
    dictionaryImage, total=pixelIntensity()
    print("Image Entropy: ", entropy(dictionaryImage,total)*total)


main()