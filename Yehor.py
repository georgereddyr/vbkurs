#1
'''
def fahrenheit(c):
    celsius = (c * 9/5) + 32
    return celsius

print(fahrenheit(20))

def celsius(f: float) -> float:
    fahrenheit = (f - 32) * (5/9)
    return fahrenheit

print(celsius(68))


#----------------------------------------------------------------------
#2

string = ""
letter = ""
def zeichen_zaehlen(string, letter):
    print(string.count('g'))
        
print(zeichen_zaehlen('Hugo Huggendubbel fuhr im Bus nach Limoges.', 'g'))

#-------------------------------------------------------------------------
#3

def ascii_summe(string):
    return sum(ord(char) for char in string)
print (ascii_summe('Hugo Huggendubbel'))


#--------------------------------------------------------------------------
#4

def erste_buchstaben(string, uppercase = False):
    words = string.split()
    r = ""
    
    for w in words:
        if len(w) > 0:
            r = r + w[0]
    
    if uppercase:
        r = r.upper()
    
    return r

print (erste_buchstaben('Wer reitet so spät durch Nacht und Wind?'))


#--------------------------------------------------------------------------
#5

def heron_square_root(a):
    x = a
    
    while (x**2 - a) > 0.000001:
        x = (x + a / x) / 2
        
    return round(x, 6)

print (heron_square_root(2))
'''


def zwei_schleifen(a, b, c, x, y, z):
    result = []
    for i in range(a, b + 1, c):
        j = x
        while j <= y:
            result.append(i * j)           
            j += z
            
    return result


print(zwei_schleifen(0, 3, 1, -2, 2, 2))
