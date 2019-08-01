# PLEASE READ THIS !!
# I'm brazilian so sorry for my bad english in this project, but I'm doing english classes, so don't worry, in the future I will make a project with perfect english :)

numbers_to_fill  = ["(__1__)", "(__2__)", "(__3__)", "(__4__)"]
answers = []
big_string = ""

print "What level do you like to try?"
print "1 -> Easy"
print "2 -> Medium"
print "3 -> Hard"
print "4 -> Exit"

while True:
    option = int(raw_input("Type the number of the level: "))
    if option == 1:
        big_string = """This (__1__) language is named (__2__). Each line have one (__3__), if only one line have an error, all the (__4__) will not execute"""
        answers = ["programming","python","instruction","code"]
        break
    if option == 2:
        big_string =  """To create a function you must use the word (__1__) followed by its name. If your function needs to receive values, you almost put the (__2__) inside parentheses. (__3__) are traditionally used when you have a piece of code which you want to repeat n number of times. In stage 2, we've learned 'for' loops and '(__4__)' loops"""
        answers = ["def","variables","Loops","while"]
        break
    if option == 3:
        big_string = """In stage 2, we've learned 'for' loops and 'while' loops, this loops end with a control variable or with the (__1__) command. To turn a string into a list, we must use the command 'string.(__2__)()'. To turn a list into a string we must use the command " ".(__3__)(list). To add a value to a list we can use the command list.(__4__)(value)."""
        answers = ["break","split","join","append"]
        break
    if option == 4:
        print "Exiting..."
        exit(0)
    else:
        print "Invalid option, try again"

chances = int(raw_input("Type the number of chances do you want: "))
chances_left = chances

print "Fill the numbers with the correct word!"
print big_string

# If the target word is found in a string, return only the word, if not, return None.
def word_in_pos(word, numbers_to_fill):
    for pos in numbers_to_fill:
        if pos in word:
            return pos
    return None

# Validate if the user input word is correct, if it is correct, return the 'user_input', if not, give the user the chances that he asked for,
# and if the chances end, exit the program.
def validating(user_input, replacement, answers, i, chances_left):
    while True:
        user_input = raw_input("What word correctly fill the space " + replacement + "? ")
        if str(user_input) == str (answers[i]):
            print "Correct!"
            return str(user_input)
        else:
            chances_left = chances_left - 1
            if chances_left == 0:
                print "Sorry but you lose, you don't have more chances."
                print "Exiting..."
                exit(0)
            print "Wrong word you have " + str(chances_left) + " more chances left."

def play_game(ml_string, numbers_to_fill):
    i = 0
    replaced = []
    ml_string = ml_string.split()
    for word in ml_string: # Find the words that need to be replaced and ask for the user input, after that, fill the big_string with the words, with the correct punctuation
        replacement = word_in_pos(word, numbers_to_fill)
        if replacement != None:
            user_input = ""
            user_input = validating(user_input, replacement, answers, i, chances_left)
            i = i + 1
            word = word.replace(replacement, user_input)
            replaced.append(word)
        else:
            replaced.append(word)
        chances_left = chances
    return " ".join(replaced)
    
print play_game(big_string, numbers_to_fill)