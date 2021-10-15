from string import * #Loading the string module

def process_shift(text = '', shift = 0): #Defining the process_shift function for reusability
    try:
        shift = int(shift) #Making sure that an integer was input for the shift value
        text = str(text) #Making sure that a string was input for the text to encode
    except:
        return
    result = ''
    letters = ascii_lowercase + ' '
    for x in range(len(text)):
        tempshift = letters.find(text[x].lower()) + shift
        while tempshift < 0 or tempshift >= len(letters):
            if tempshift < 0: tempshift += len(letters)
            else: tempshift -= len(letters)
        result += letters[tempshift]
    return result

def section_separator():
    return '~~~~~~~~~~~~~~~~~~~'

while(1):
    print(section_separator())
    text = input('Message to shift: ')
    shift = input('Factor to shift by (integer): ')
    result = process_shift(text, shift)
    if result != None:
        print('Result: ' + result)
        continue
    print('Invalid input, please try again')
