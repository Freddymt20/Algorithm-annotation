
# Input
Word = 'String'


# Methods


#Method 1: Py Indexing
def Palindrome(Word):
    P =  Word[::-1]
    return 'Succes' if Word == P else 'Fail'

    
#Method 2: Function Generator
def Palindro(Word):
    s = [i for i in Word] #Op: [[i for i in Word][-n] for n in range(1,len(Word)+1)]
    z = [s[-i] for i in range(1,len(s)+1)] #Op: ''.join(eval(str([[i for i in Word][-n] for n in range(1,len(Word)+1)]).replace(',','+')))
    P = ''.join(eval(str(z).replace(',','+')))
    return 'Succes' if Word == P else 'Fail'

