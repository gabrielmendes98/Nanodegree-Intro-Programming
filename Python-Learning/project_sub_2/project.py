# PLEASE READ THIS !!
# I'm brazilian so sorry for my bad english in this project, but I'm doing english classes, so don't worry, in the future I will make a project with perfect english :)

numbers_to_fill  = ["(__1__)", "(__2__)", "(__3__)", "(__4__)"]
answers = []
big_string = ""
'''
Behavior: Immediately after running the program, user is prompted to select a difficulty level from easy / medium / hard
Input: User type the number of the level
Output: Assign the big_string and answers according to the difficult
'''
def menu():
    print "What level do you like to try?"
    print "1 -> Easy"
    print "2 -> Medium"
    print "3 -> Hard"
    print "4 -> Exit"
    option = 0
    while option < 1 or option > 4:
        option = int(raw_input("Type the number of the level: "))
        if option < 1 or option > 4:
            print "Invalid option. Try again!"
    big_string, answers = menu_assign(option)
    return big_string, answers

''' 
Input: The option that user typed
Output: Once a level is selected, return the big_string and answers according to the user input, if user input '4', the program will be ended
'''
def menu_assign(option):
    if option == 1:
        big_string = """This (__1__) language is named (__2__). Each line have one (__3__), if only one line have an error, all the (__4__) will not execute"""
        answers = ["programming","python","instruction","code"]
        return big_string, answers
    if option == 2:
        big_string =  """To create a function you must use the word (__1__) followed by its name. If your function needs to receive values, you almost put the (__2__) inside parentheses. (__3__) are traditionally used when you have a piece of code which you want to repeat n number of times. In stage 2, we've learned 'for' loops and '(__4__)' loops"""
        answers = ["def","variables","Loops","while"]
        return big_string, answers
    if option == 3:
        big_string = """In stage 2, we've learned 'for' loops and 'while' loops, this loops end with a control variable or with the (__1__) command. To turn a string into a list, we must use the command 'string.(__2__)()'. To turn a list into a string we must use the command " ".(__3__)(list). To add a value to a list we can use the command list.(__4__)(value)."""
        answers = ["break","split","join","append"]
        return big_string, answers
    if option == 4:
        print "Exiting..."
        exit(0)

''' 
Behavior: If the target word is found in a string, return only the word, if not, return None.
'''
def word_in_pos(word, numbers_to_fill):
    for pos in numbers_to_fill:
        if pos in word:
            return pos
    return None

''' 
Behavior: Validate if the user input word is correct
Input: User type the word
Output: If the user is correct, print the big_string replaced by the user input, if not, print "try again"
'''
def validating(user_input, replacement, answers, index, big_string):
    while True:
        user_input = raw_input("What word correctly fill the space " + str(replacement) + "? ")
        if str(user_input) == str (answers[index]):
            big_string = big_string.replace(replacement, user_input)
            print '\n' + big_string + '\n'
            return str(user_input), big_string
        else:
            print "Wrong answer! Try again!"

'''
Behavior: It's the main function of this program, it just call the other functions
Input: Receives numbers_to_fill, wich is just the blanks like '(__1__)', that needs to be replaced
'''
def play_game(numbers_to_fill):
    big_string, answers = menu()
    print '\n' + big_string + '\n'
    print big_string
    index = 0
    big_string_splited = big_string.split()
    for word in big_string_splited:
        replacement = word_in_pos(word, numbers_to_fill)
        if replacement:
            user_input = ""
            user_input, big_string = validating(user_input, replacement, answers, index, big_string)
            index = index + 1



play_game(numbers_to_fill)