'''
This file contains the functions used to perform the translations of inputs entered into the write_encode app.

    - The binary_translator & morse_translator functions each take in a string ("input_str"), translate
    the string into either binary or morse form, respectively, and then return the binary or morse translation of
    the original string.

'''

def binary_translator(input_str:str):
    # Using string formatting to convert a normal alphabet character into binary form
    return ' '.join('{0:08b}'.format(ord(ch), 'b') for ch in input_str)

def morse_translator(input_str:str):
    # Dictionary of modern alphabet/morse alphabet key/value pairs.
    morse_dict = {
    "A":"●- ",
    "B":"-●●● ",
    "C":"-●-● ",
    "D":"-●● ",
    "E":"● ",
    "F":"●●-● ",
    "G":"--● ",
    "H":"●●●● ",
    "I":"●● ",
    "J":"●--- ",
    "K":"-●- ",
    "L":"●-●● ",
    "M":"-- ",
    "N":"-● ",
    "O":"--- ",
    "P":"●--● ",
    "Q":"--●- ",
    "R":"●-● ",
    "S":"●●● ",
    "T":"- ",
    "U":"●●- ",
    "V":"●●●- ",
    "W":"●-- ",
    "X":"-●●- ",
    "Y":"-●-- ",
    "Z":"--●● ",
    "0":"----- ",
    "1":"●---- ",
    "2":"●●--- ",
    "3":"●●●-- ",
    "4":"●●●●- ",
    "5":"●●●●● ",
    "6":"-●●●● ",
    "7":"--●●● ",
    "8":"---●● ",
    "9":"----● ",
    " ":" ",
    }
    
    output = ""
    
    for ch in input_str:
        for key, value in morse_dict.items():
            if ch.upper() == key:
                # If a character from the input_str (in uppercase form) matches a key in morse_dict,
                # the morse value of that key is appended to output.
                output += value

    return output