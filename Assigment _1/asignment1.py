import sys
def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))
def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m
def enc_cesar(encpath, decpath, key):
    encfile = open(encpath, 'r')
    text = encfile.read()
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char==" ":
            result+=char
        elif (char.isupper()):
            result += chr((ord(char) + int(key[0]) - 65) % 26 + 65)
        else:
            result += chr((ord(char) + int(key[0]) - 97) % 26 + 97)
    dec_file = open(decpath, 'w')
    days = dec_file.write(result)
    #return result

def dec_cesar(encpath, decpath, key):
    decfile = open(decpath, 'r')
    text = decfile.read()
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char==" ":
            result+=char
        elif (char.isupper()):
            result += chr((ord(char) - int(key[0]) - 65) % 26 + 65)
        else:
            result += chr((ord(char) - int(key[0]) - 97) % 26 + 97)
    enc_file = open(encpath, 'w')
    days = enc_file.write(result)
    #return result
def enc_affine(encpath, decpath, key):
    encfile = open(encpath, 'r')
    text = encfile.read()
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char == " ":
            result+=char
        elif (char.isupper()):
            result += chr((( int(key[0])*(ord(char) - ord('A')) + int(key[1]) ) % 26) + ord('A'))
        else:
            result += chr(((int(key[0]) * (ord(char) - ord('a')) + int(key[1])) % 26) + ord('a'))
    dec_file = open(decpath, 'w')
    days = dec_file.write(result)
    #return result
def dec_affine(encpath, decpath, key):
    decfile = open(decpath, 'r')
    text = decfile.read()
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char == " ":
            result += char
        elif (char.isupper()):
            result += chr((( modinv(int(key[0]), 26)*(ord(char) - ord('A') - int(key[1]))) % 26) + ord('A'))
        else:
            result +=   chr((( modinv(int(key[0]), 26)*(ord(char) - ord('a') - int(key[1]))) % 26) + ord('a'))
    enc_file = open(encpath, 'w')
    days = enc_file.write(result)
    #return resultdef enc_affine(encpath, decpath, key):
    encfile = open(encpath, 'r')
    text = encfile.read()
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char == " ":
            result+=char
        elif (char.isupper()):
            result += chr((( int(key[0])*(ord(char) - ord('A')) + int(key[1]) ) % 26) + ord('A'))
        else:
            result += chr(((int(key[0]) * (ord(char) - ord('a')) + int(key[1])) % 26) + ord('a'))
    dec_file = open(decpath, 'w')
    days = dec_file.write(result)
    #return result
def dec_affine(encpath, decpath, key):
    decfile = open(decpath, 'r')
    text = decfile.read()
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char == " ":
            result += char
        elif (char.isupper()):
            result += chr((( modinv(int(key[0]), 26)*(ord(char) - ord('A') - int(key[1]))) % 26) + ord('A'))
        else:
            result +=   chr((( modinv(int(key[0]), 26)*(ord(char) - ord('a') - int(key[1]))) % 26) + ord('a'))
    enc_file = open(encpath, 'w')
    days = enc_file.write(result)
    #return result
 ###############################################
def enc_vigenere(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))


def dec_Vigenere(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))
if __name__ == "__main__":
    type=sys.argv[1]
    opreation=sys.argv[2]
    encfile=sys.argv[3]
    decfile=sys.argv[4]
    key= []
    key.append(sys.argv[5])
    key.append(sys.argv[6])
    if type=="shift" :
        if opreation=="enc":
            enc_cesar(encfile, decfile, key)
        else:
            dec_cesar(encfile, decfile, key)
    elif type =="affine":
        if opreation=="enc":
            enc_affine(encfile, decfile, key)
        else :
            dec_affine(encfile,decfile,key)

    elif type =="vigenere":
        if opreation=="enc":
            encfile = open(encfile, 'r')
            text = encfile.read()
            key = generateKey(text, key[0])
            string=enc_vigenere(text,key)
            dec_file = open(decfile, 'w')
            dec_file.write(string)
        else :
            decfile = open(decfile, 'r')
            text = decfile.read()
            key = generateKey(text, key[0])
            string=dec_Vigenere(text,key)
            enc_file = open(encfile, 'w')
            enc_file.write(string)





