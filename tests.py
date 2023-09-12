#l = [1, 2, 3, 4]
#print(l)
#print(l[::-1])

#a = "."
#b = "_"
#c = ""
#alphabet = {"a":a+b+c, "b":a+b+b+b+c, "c":b+a+b+a+c, "d":b+a+a+c, "e":a+c, "f":a+a+b+a+c, "g":b+b+a+c, "h":a+a+a+a+c, "i":a+a+c, "j":a+b+b+b+c, "k":b+a+b, "l":a+b+a+a+c, "m":b+b+c, "n":b+a+c, "o":b+b+b+c, "p":a+b+b+a+c, "q":b+b+a+b+c, "r":a+b+a+c, "s":a+a+a+c, "t":b+c, "u":a+a+b+c, "v":a+a+a+b+c, "w":a+b+b+c, "x":b+a+a+b+c, "y":b+a+b+b+c, "z":b+b+a+a+c}
#print(alphabet)

#alpha = {}
#for i in alphabet.keys():
#    alpha[alphabet[i]] = i

#print(alpha)

#word = "123456789"
#result = ""

#help_res0 = word[0:len(word)//2+1]

#help_res1 = word[len(help_res0):]

#print(help_res0)
#print(help_res1)
#help_res1 = help_res1[::-1]
#for i in range(len(help_res0)):
#    result += help_res0[i]
#    if i < len(help_res1):
#        result += help_res1[i]

#print(result)





a = """*****help****
Hi, and welcome to the my bot. Here follows list of possible inputs.
-quote
-quote:'surname_of_author'
-fact
-rhyme:'language (cze, eng, lat, elf)':'word_to_rhyme'
-cipher:
    NOTE: all of them are using small letters of english alphabet - 26 characters
    -to_morse:word_to_translate
    -to_morse:word_to_translate:"symbol_for '.'':symbol_for '_':symbol_for '/'
    -from_morse:'text_to_translate' using '.' '_' and '/', without spaces
    -backwards:'text_to_translate'
    -skipping:'text_to_translate' ressult is every second character. Between are random letters.
    -first_last:'text_to_translate'
    -random_rearrange:'text_to_traslate'
    -skipp02:'text_to_traslate' every second letter and then back
    -caesar:'text_to_traslate':'number_of_move'
    -addition:'text_to_traslate':'password'
    -backwards_alphabet:'text_to_traslate'
    -own_alphabet:'text_to_traslate':'27 characters of new alphabet
    -to_numbers:'text_to_traslate'
    -from_numbers:'numbers with spaces to translate to letters'
    -pair:'text_to_traslate'
    -nokia:'text_to_traslate'
    -nokia02:text_to_traslate"""
print(a)