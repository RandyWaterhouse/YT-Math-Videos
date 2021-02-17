tableau = [[chr(i) for i in range(65, 91)]]
for k in range(25):
    last = tableau[-1]
    tableau.append(last[1:] + last[:1])

def vigenere_encrypt(keyword, message):
    l = len(keyword)
    encrypted = ""
    for k in range(len(message)):
        key = keyword[k % l]
        row = ord(key) - 65  # ASCII: 65=A, 66=B, ...
        column = ord(message[k]) - 65
        encrypted += tableau[row][column]
    return encrypted

def vigenere_decrypt(keyword, encrypted):
    l = len(keyword)
    message = ""
    for k in range(len(encrypted)):
        key = keyword[k % l]
        row = ord(key) - 65  # ASCII: 65=A, 66=B, ...
        column = tableau[row].index(encrypted[k])
        message += tableau[0][column]
    return message

print(vigenere_encrypt("GEHEIM", "PYTHONISTTOLL"))
print(vigenere_decrypt("GEHEIM", "VCALWZOWAXWXR"))

kw = "YOUTUBE"
text = "AASLDKFKHASDLKFASDLSADFKJHASDFJH"
assert vigenere_decrypt(kw, vigenere_encrypt(kw, text)) == text
