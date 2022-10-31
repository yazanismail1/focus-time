decode_dict = {
    "A":".-", 
    "B":"-...", 
    "C":"-.-.", 
    "D":"-..", 
    "E":".", 
    "F":"..-.", 
    "G":"--.", 
    "H":"....", 
    "I":"..", 
    "J":".---", 
    "K":"-.-", 
    "L":".-..", 
    "M":"--", 
    "N":"-.", 
    "O":"---", 
    "P":".--.", 
    "Q":"--.-", 
    "R":".-.", 
    "S":"...", 
    "T":"-", 
    "U":"..-", 
    "V":"...-", 
    "W":".--", 
    "X":"-..-", 
    "Y":"-.--", 
    "Z":"--..", 
    "1":".----", 
    "2":"..---", 
    "3":"...--", 
    "4":"....-", 
    "5":".....", 
    "6":"-....", 
    "7":"--...", 
    "8":"---..", 
    "9":"----.", 
    "0":"-----",
}

def morse_code(user_input):
    to_code = user_input.upper().split()
    coded = []
    counter = 0
    for i in to_code:
        counter += 1
        for j in i:
            if j in decode_dict:
                coded.append(decode_dict[j])
            else:
                coded.append(j)
        if counter == len(to_code):
            pass
        else:
            coded.append("     ")
    print (" ".join(coded))

