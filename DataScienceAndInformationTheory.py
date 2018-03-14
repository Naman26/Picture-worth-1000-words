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


#Entropy= Sum(p(xi)*(logBASE 2(1/ p(xi)))
def entropy(X, total):
    summation = 0.0
    #For every key in dictionary
    for x in X:
        #p(x)= occurance of x / sample size
        #Storing (logBASE 2(1/ p(xi))
        logArg= math.log((1/(X[x]/total)), 2)
        #Adding all entropy values of sample
        summation+= (X[x]/total)*logArg
    #Return the sample entropy
    return summation


from PIL import Image

def pixelIntensity():
    #Open the image and convert it to greyscale
    img = Image.open('image.png').convert('LA')
    #Save the image as greyscale.png
    img.save('greyscale.png')
    #Open the greyscale image to read
    img = Image.open('greyscale.png','r')
    #Storing size of image
    x,y = img.size
    #Storing image as a list of pixel intensities
    image= list(img.getdata())
    intensity={}
    #Converting list image into dictionary of intensities
    for i in image:
        if i[0] in intensity:
            intensity[i[0]]+= 1
        else:
            intensity[i[0]] = 1
    # Return dictionary of intensities and total pixels
    return intensity, x*y

def main():
    dictionaryBook, total=letterCount()
    #Calculate entropy of book
    print("Book Entropy: ",entropy(dictionaryBook,total)*total)
    dictionaryImage, total=pixelIntensity()
    #Calculate entropy of image
    print("Image Entropy: ", entropy(dictionaryImage,total)*total)

main()