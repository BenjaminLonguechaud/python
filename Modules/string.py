
""" String """
""" Behaves almost exactly like the original split() method """


def mysplit(strng):
    strng = strng.strip()
    if not strng:
        return []
    indexStart = 0
    indexEnd = strng.find(" ")
    result = []
    while indexEnd != -1:
        result.append(strng[indexStart:indexEnd])
        indexStart = indexEnd + 1
        indexEnd = strng.find(" ", indexStart)
    result.append(strng[indexStart:])
    return result

def seven_segment_display(strng):
    numbers = [ ["#", "###", "###", "# #", "###", "###", "###", "###", "###", "###"],
                ["#", "  #", "  #", "# #", "#  ", "#  ", "  #", "# #", "# #", "# #"],
                ["#", "###", "###", "###", "###", "###", "  #", "###", "###", "# #"],
                ["#", "#  ", "  #", "  #", "  #", "# #", "  #", "# #", "  #", "# #"],
                ["#", "###", "###", "  #", "###", "###", "  #", "###", "###", "###"],
    ]
    for part in numbers:
        for number in strng:
            if(number.isdigit() == False):
                print("Wrong data type")
                return
            number_int = int(number) - 1
            print(part[number_int], end=" ")
        print("")

def cipher(string, order):
    result = ""
    for letter in string:
        new_order = ord(letter) + order
        last_ord = "Z" if letter.isupper() else "z"
        first_ord = "A" if letter.isupper() else "a"
        
        if not letter.isalpha():
            result += letter
        elif(new_order > ord(last_ord)):
            result += chr(new_order % ord(last_ord) + ord(first_ord) - 1)
        else:
            result += chr(new_order)

    return result

def decipher(string):
    result = ""
    string = string.upper()
    for letter in string:
        if not letter.isalpha():
            continue
        if letter == "A":
            result +=  "Z"
        else:
            result += chr(ord(letter) - 1)
    return result

def is_palindrome(string):
    if string == "":
        return False
    string = string.replace(" ", "")
    string = string.lower()
    for i in range(len(string)//2+1):
        if string[i] != string[-1-i]:
            return False
    return True

def digit_of_life(date):
    result = 0
    string_result = date
    if len(date) == 8:
        while len(string_result) > 1:
            result = 0
            for it in string_result:
                if it.isdigit():
                    result += int(it)
            string_result = str(result)
    return result

""" Are the characters comprising the first string hidden """
""" inside the second string? """
def find_word(word, playground):
    result = True
    indexes = []
    string_to_analyse = playground
    if word != "" and len(string_to_analyse) >= len(word):
        for it in word:
            index = string_to_analyse.find(it)
            if index == -1:
                result = False
                break
            string_to_analyse = string_to_analyse[index+1:] 
    return result

""" Is the given Sudoku valid """
def verify_sudoku(sudoku):
    def is_all_numbers(string):
        result = True
        for i in range(len(string)-1):
            for it in string[i+1:]:
                if it == string[i]:
                    result = False
                    break
        return result

    result = False
    if len(sudoku) != 9:
        return result
    columns = ["","","","","","","","",""]
    regions = ["","","","","","","","",""]
    for i in range(9):
        if not is_all_numbers(sudoku[i]):
            return result
        else:
            for j in range(9):
                columns[j] += sudoku[i][j]
                a = 3*(i%3)+j%3
                regions[3*(i//3)+j//3] += sudoku[i][j]
    for i in range(9):
        if is_all_numbers(columns[i]) and is_all_numbers(regions[i]):
            result = True
    return result

sudoku = ["295743861",
          "431865927",
          "876192543",
          "387459216",
          "612387495",
          "549216738",
          "763524189",
          "928671354",
          "154938672"]
