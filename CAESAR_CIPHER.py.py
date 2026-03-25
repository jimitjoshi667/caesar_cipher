alphabets = [chr(i) for i in range(ord('a'), ord('z') + 1)]

direction  = input("Type encode to encrypt type decode to decrypt: ").lower()
text = input("enter you message").lower()
shift = int(input("how many characters do you want to shift?"))

#encrypting function
def encrypt(text,shift):
    primary_shift = shift
    new_word = ""
    for letter in text:
        if letter in alphabets:
            # for validating shift by numbers greater then the length of the string
            #if (alphabets.index(letter )+1+shift)>len(alphabets):
            #    while (alphabets.index(letter)+1+shift)>len(alphabets):
            #        shift = alphabets.index(letter) + letter + shift - len(alphabets)
            #        letter = alphabets[0]
            #-------------------------------------------------------------------------
            #another way to validate shift by numbers greater then the length of the string
            #  if (alphabets.index(letter )+shift)>len(alphabets):
            #    shift = (alphabets.index(letter)+shift)%len(alphabets)
            #else:
            #    shift = primary_shift
            new_word+=alphabets[(alphabets.index(letter)+shift)%len(alphabets)]
        else:
            new_word+=letter

    print("encrypted letter is:",new_word)

def decrypt(text,shift):
    primary_shift = shift
    new_word = ""
    for letter in text:
        if letter in alphabets:
            if (alphabets.index(letter )-shift)<0:
                shift = (alphabets.index(letter)-shift)%len(alphabets)
            else:
                shift = primary_shift
            new_word+=alphabets[(alphabets.index(letter)-shift)%len(alphabets)]

        else:
            new_word+=letter

    print("encrypted letter is:",new_word)

while True:
    if direction == "encode":
        encrypt(text,shift)
    elif direction == "decode":
        decrypt(text,shift)
    else:
        print("you have entered wrong direction")
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
    if result == "no":
        print("good bye")
        break
    elif result == "yes":
        direction  = input("Type encode to encrypt type decode to decrypt: ").lower()
        text = input("enter you message").lower()
        shift = int(input("how many characters do you want to shift?"))
    
