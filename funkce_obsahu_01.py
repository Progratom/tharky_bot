import json
import random

def tharkun_bot(inpt):
    #quotes
    f = open("data.json")
    data = json.load(f)

    if inpt == "help":
        
        return("""
        *****help****
        Hi, and welcome to the my bot. Here follows list of possible inputs.
        -quote
        -quote:'surname_of_author'
        -fact
        -rhyme:'language (cze, eng, lat, elf)':'word_to_rhyme'
        -cipher:
            NOTE: all of them are using small letters of english alphabet - 26 characters
            -to_morse:"word_to_translate"
            -to_morse:"word_to_translate":"symbol_for '.'":symbol_for '_':symbol_for '/'
            -from_morse:"text_to_translate" using '.' '_' and '/', without spaces
            -backwards:"text_to_translate"
            -skipping:"text_to_translate" ressult is every second character. Between are random letters.
            -first_last:"text_to_translate"
            -random_rearrange:"text_to_traslate"
            -skipp02:"text_to_traslate" every second letter and then back
            -caesar:"text_to_traslate":"number_of_move"
            -addition:"text_to_traslate":"password"
            -backwards_alphabet:"text_to_traslate"
            -own_alphabet:"text_to_traslate":'27 characters of new alphabet
            -to_numbers:"text_to_traslate"
            -from_numbers:"numbers with spaces to translate to letters"
            -pair:"text_to_traslate"
            -nokia:"text_to_traslate"
            -nokia02:text_to_traslate""")
    
    elif inpt == "quote": #returnt random quote of any author
        #load of all quotes for random quote. It can be definitely done with initializing of class, but now it is not class, so we let it this way
        all_quotes = []
        for aut in data["quotes"].keys():
            for i in data["quotes"][aut]:
                all_quotes.append(i)
        return random.choice(all_quotes)
    
    elif "quote" in inpt: #in form  "quote:" 'surname_of_author' returns random quote of that specific author
        aut = inpt.split(":")[1]
        if aut in data["quotes"].keys():
            return random.choice(data["quotes"][aut])
        else:
            return "err - wrong name of author"
    
    elif inpt == "fact": #returns random fact
        return random.choice(data["facts"])
    
    elif inpt.startswith("rhyme"): #form "rhyme:"your_language":"your_word, returns list of minimum 10 words with same ending (as many letters as possible)
        if len(inpt.split(":")) == 3:
            language = inpt.split(":")[1]
            word = inpt.split(":")[2]
            arr1 = data["rhyme"][language] #"smaller" list. Just words that fits. In the begining bigger of the two, because lists are switsched on beggining of algorithm
            arr0 = [] #list of all words from specific languages
            nop = 0 #actual number of parity, on begining lenght of word

            while len(arr1) >= 10 and nop < len(word):
                #print(nop)
                arr0 = arr1.copy()
                arr1 = []
                nop += 1

                compare = word[len(word)-nop:]
                for i in arr0:
                    if i.endswith(compare):
                        arr1.append(i)
                
            if len(arr1) > 10:
                return(arr1)
            else:
                return(arr0)


    elif inpt.startswith("cipher"):
        inpt_l = inpt.split(":") #list from input split by ":"
        if len(inpt_l) >= 3:
            result = ""
            type_of_cipher = inpt_l[1]
            word = inpt_l[2]

            if type_of_cipher == "to_morse":
                if len(inpt_l) == 3:
                    for i in word:
                        result += to_morse(".", "_", "|", i)
                else:
                    if len(inpt_l[3].split(",")) > 1 and len(inpt_l[3]) > 1:
                        for i in word:
                            result += to_morse_rnd(inpt_l[3], inpt_l[4], inpt_l[5], i)
                            #result += to_morse(random.choice(inpt_l[3].split(",")), random.choice(inpt_l[4].split(",")), random.choice(inpt_l[5].split(",")), i)
                    else:
                        for i in word:
                            result += to_morse(inpt_l[3], inpt_l[4], inpt_l[5], i)
            elif type_of_cipher == "from_morse":
                to_translate = inpt_l[2].split("/")
                for i in to_translate:
                    result += from_morse(i)

            elif type_of_cipher == "backwards":
                return word[::-1]
            elif type_of_cipher == "skipping":
                for i in word:
                    result += i
                    result += chr(random.randint(97, 122))

            elif type_of_cipher == "first_last":
                help_res = ""
                for i in range(len(word)):
                    if i % 2 == 0:
                        result += word[i]
                    else:
                        help_res += word[i]
                result = result + help_res[::-1]

            elif type_of_cipher == "random_rearrange":
                word = list(word)
                lenght = len(word)
                for i in range(lenght):
                    add = random.choice(word)
                    result += add
                    word.remove(add)

            elif type_of_cipher == "skipp02":
                help_res0 = word[0:len(word)//2+1]
                help_res1 = word[len(help_res0):]
                help_res1 = help_res1[::-1]
                for i in range(len(help_res0)):
                    result += help_res0[i]
                    if i < len(help_res1):
                        result += help_res1[i]

            elif type_of_cipher == "caesar":
                num = int(inpt_l[3]) #number of positions to move
                for i in word:
                    result += caesar(i, num)
            elif type_of_cipher == "big_caesar":
                for num in range(0, 26):
                    for i in word:
                        result += caesar(i, num)
                    result  += "\n"

            elif type_of_cipher == "addition": #caesar based on password
                password = inpt_l[3]
                while len(word) > len(password):
                    if len(word) - 2*len(password) >= 0:
                        password = password + password
                    else:
                        password = password + password[0:len(word)-len(password)]

                for i in range(len(word)):
                    result += caesar(word[i], ord(password[i])-96)

            elif type_of_cipher == "backwards_alphabet":
                for i in word:
                    result += chr((27-(ord(i)-96))+96)
            
            elif type_of_cipher == "own_alphabet":
                alphabet = list(inpt_l[3])
                for i in word:
                    result += alphabet[ord(i)-96]

            elif type_of_cipher == "to_numbers": #order in alphabet
                for i in word:
                    result += str(ord(i)-96)+" "

            elif type_of_cipher == "from_numbers":
                word = word.split(" ")
                for i in word:
                    result += chr(int(i) + 96)

            elif type_of_cipher == "pair":
                for i in word:
                    if i == "a":
                        result += "zb "
                    elif i == "z":
                        result += "ya "
                    else:
                        result += chr(ord(i)-1) + chr(ord(i)+1) + " "
            
            elif type_of_cipher == "nokia":
                for i in word:
                    num = ord(i)-96
                    num01 = num // 3
                    num02 = num % 3
                    if num02 != 0:
                        for i in range(num02):
                            result += str(num01+1)   
                    else:
                        for i in range(3):
                            result += str(num01)
                    result += " "

            elif type_of_cipher == "nokia02":
                for letter in word:
                    result += nokia(letter)
                    result += " "

            elif type_of_cipher == "snake":
                result = squares(word)
                

            return(result)
               
        

        #snake

def nokia(letter):
    sheet = [
            [],["A", "B", "C"], ["D", "E","F"],
            ["G", "H", "I"], ["J", "K", "L"], ["M", "N", "O"],
            ["P", "Q", "R", "S"], ["T", "U", "V"], ["W", "X", "Y", "Z"]
            ]
    res = ""
    for i in range(len(sheet)):
        for n in range(len(sheet[i])):
            if letter == sheet[i][n]:
                for y in range(n+1):
                    res += str(i+1)
                return res
                    

         
def caesar(letter, num):
    for i in letter:
        if ord(i)+num > 122:
            return chr(ord(i)+num - 26)
        else:
            return chr(ord(i)+num)


def to_morse(a, b, c, letter):
    alphabet = {"a":a+b+c, "b":a+b+b+b+c, "c":b+a+b+a+c, "d":b+a+a+c, "e":a+c, "f":a+a+b+a+c, "g":b+b+a+c, "h":a+a+a+a+c, "i":a+a+c, "j":a+b+b+b+c, "k":b+a+b, "l":a+b+a+a+c, "m":b+b+c, "n":b+a+c, "o":b+b+b+c, "p":a+b+b+a+c, "q":b+b+a+b+c, "r":a+b+a+c, "s":a+a+a+c, "t":b+c, "u":a+a+b+c, "v":a+a+a+b+c, "w":a+b+b+c, "x":b+a+a+b+c, "y":b+a+b+b+c, "z":b+b+a+a+c}
    if letter in alphabet.keys():
        return alphabet[letter]
    

def to_morse_rnd(d, e, f, letter):
    a = "a"
    b = "b"
    c = "c"
    alphabet = {"a":a+b+c, "b":a+b+b+b+c, "c":b+a+b+a+c, "d":b+a+a+c, "e":a+c, "f":a+a+b+a+c, "g":b+b+a+c, "h":a+a+a+a+c, "i":a+a+c, "j":a+b+b+b+c, "k":b+a+b, "l":a+b+a+a+c, "m":b+b+c, "n":b+a+c, "o":b+b+b+c, "p":a+b+b+a+c, "q":b+b+a+b+c, "r":a+b+a+c, "s":a+a+a+c, "t":b+c, "u":a+a+b+c, "v":a+a+a+b+c, "w":a+b+b+c, "x":b+a+a+b+c, "y":b+a+b+b+c, "z":b+b+a+a+c}
    res = ""
    if letter in alphabet.keys():
        for i in alphabet[letter]:
            if i == a:
                res += random.choice(d.split(","))
            elif i == b:
                res +=  random.choice(e.split(","))
            elif i == c:
                res += random.choice(f.split(","))
        return res
    
def from_morse(inp):
    alphabet = {'._': 'a', '.___': 'j', '_._.': 'c', '_..': 'd', '.': 'e', '.._.': 'f', '__.': 'g', '....': 'h', '..': 'i', '_._': 'k', '._..': 'l', '__': 'm', '_.': 'n', '___': 'o', '.__.': 'p', '__._': 'q', '._.': 'r', '...': 's', '_': 't', '.._': 'u', '..._': 'v', '.__': 'w', '_.._': 'x', '_.__': 'y', '__..': 'z'}
    return alphabet[inp]    
        

def squares(word):
    result = ""
    lenght = len(word)
    side = False
    if lenght < 100:
        for i in range(10):
            if lenght > i*i and lenght <= (i+1)*(i+1):
                side = i+1
    while len(word) != side*side:
        word += chr(random.randint(65, 91))
    
    square_l = snake(word, side)
    for y in square_l:
        for x in y:
            result += x
            result += " "
        result += "\n"
    return(result)


def snake(word, side):
    output = []
    for i in range(side):
        l = []
        for j in range(side):
            l.append("_")
        output.append(l)
    smer = "r"
    x = 0
    y = 0
    for i in word:
        output[y][x] = i
        if smer == "r":
            if x == side-1:
                smer = "d"
                y += 1
            elif output[y][x+1] != "_":
                smer = "d"
                y += 1
            else:
                x += 1
        elif smer == "d":
            if y == side-1:
                smer = "l"
                x -= 1
            elif output[y+1][x] != "_":
                smer = "l"
                x -= 1
            else:
                y += 1
        elif smer == "l":
            if y == 0:
                smer = "l"
                y -= 1
            elif output[y][x-1] != "_":
                smer = "u"
                y -= 1
            else:
                x -= 1
        elif smer == "u":
            if y == 0:
                smer = "r"
                x += 1
            elif output[y-1][x] != "_":
                smer = "r"
                x += 1
            else:
                y -= 1
    return(output)

#------------------------------------------------------------------------------------
inp = input("vstup: ")
while inp != "q":
    print(tharkun_bot(inp))
    inp = input("vstup: ")