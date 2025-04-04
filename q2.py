#took this dictionary from the net which has conversion between morse code and english
MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I',
    '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q',
    '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7',
    '---..': '8', '----.': '9'
}

def decoder(morse_code): #decoder function to convert
    words = morse_code.split('   ') #each word in worse code is seperated by 3 spaces
    plain_english = [] #empty list to story final result
    #for loop for each word in this list words
    for word in words:
        letters = word.split()
        decoded_word = ""
        #each word is again seperated into letters and stored in letters as a list
        for letter in letters:
            if letter in MORSE_CODE_DICT:
                decoded_word += MORSE_CODE_DICT[letter]
        #appending the word to the plain_english list
        plain_english.append(decoded_word)
    return plain_english

morse_message = input("enter your morse code:")
list=decoder(morse_message)
for i in list:
    print(i)
