#basic exercise directory by Andre de Biasi

#GUI
import PySimpleGUI as sg

def exercise_window( which_test ): #takes in which test
    dict = { #("NAME", "INTRO", "INPUT INTRO", num of inputs)
        "1": ("STUTTER","This exercise teaches you to be more humble", "Tell me a word:", 1),
        "2": ("RADtoDEG","This exercise converts numbers in radians to degrees", "Give me a number:", 1),
        "3": ("CURZONnumbers","This exercise returns true is 1 + 2 to the power of a number is equal to 1 + 2 multiplied by a number", "Give me a number", 1),
        "4": ("RELtoLUKE","Featured characters you know and love including: Darth Vader, Leia, Han, and R2D2!", "Help the character remind Luke who they are!", 1),
        "5": ("nthTETEHEDRAL","This exercise calculates the nth tetrahedral number!", "Give me a number:", 1),
        "6": ("CONVERTtoBINARY","This exercise converts any number less than 1025 into binary!", "Give me a number:", 1),
        "7": ("HEXCODE","This exercise returns the inverse of a characters hexcode (if it exists)", "Give me a character:", 1),
        "8": ("CONNECTEDnodes","Choose two nodes to see if they are adjacent in the undirected graph", "Give me two nodes:", 2),
        "9": ("SNAKEeats","See how many times the snake can eat an apple (doubles its size, starts at 1)", "Give me a number:", 1),
        "10": ("CALCbonues","See what your bonus will be based on the amount of days you work per quarter!\nYou earn inventives progressively\n$0 per day for 0 to 32 days\n$325 per day for 33 to 40 days\n$550 per day for 41 to 48 days\n$600 per day for 49 days onwards","How many days did you work this quarter?", 1),
        "11": ("DRUNKpython","Python forgot what strings and integers are!", "Give me a string or an integer:", 1),
        "12": ("CONSTRUCTdeconstruct","I can construct and deconstruct any words you give me", "Give me a word:", 1)
    }
    test = str(dict[f"{which_test}"][0]) #the test name
    descript = str(dict[f"{which_test}"][1]) #test description
    layout = [[sg.Text("Exercise Test",size=(45,1),justification="center")],
                    [sg.Text(f"Test Name: {test}"), sg.Text(size=(30,1), key="-NAME-")], #name of the test
                    [sg.Text(f"Test Description: {descript}"), sg.Text(size=(30,1), key="-DESC-")], #description of the test
                    [sg.Text("Input: "), sg.Input(key="-VALUE-")], #where to add values
                    [sg.Text("Output: "), sg.Input(key="-PRINT-")],
                    [sg.Button("TEST"),
                    #sg.Button("COPY"),
                    sg.Button("EXIT")]]
    window = sg.Window("Tester", layout) #create window with layout

    while True: #GUI event loop
        event, values = window.read()
        #tests which test values to find the test to display
        print(event,values)
        if event == "EXIT" or event == sg.WIN_CLOSED: #close window
            break
        if event == "TEST":
            if values["-VALUE-"] == None:
                window["-PRINT-"].update("You must enter an input value")
            elif which_test == 8: #Test 8 needs two inputs, make this based on third dict element
                if which_test == 8: is_adjacent(1,2)
            else: #one input needed
                input = values["-VALUE-"] #input
                if which_test == 1: output = stutter(input)
                if which_test == 2: output = radians_to_degrees(int(input))
                if which_test == 3: output = isCurzon(int(input))
                if which_test == 4: output = relation_to_luke(input)
                if which_test == 5: output = tetra(int(input))
                if which_test == 6: output = binary(int(input))
                if which_test == 7: output = counterpart_Charcode(input)
                if which_test == 9: output = snakefill(int(input))
                if which_test == 10: output = bonus(int(input))
                if which_test == 11: output = int_to_str(int(input))
                #if which_test == 12: output = c_and_r(input) #must create an output box that changes depending on size of output

                window["-PRINT-"].update(f"{output}")
    window.close()

def main():
    layout = [[sg.Text("Welcome to my Exercises Directory",size=(45,1),justification="center")],
                    [sg.Text("Which exercise would you like to test?")],
                    [sg.Text("1: Stuttering Function"),sg.Text("2: Radians to Degress"),sg.Text("3: Curzon Numbers")],
                    [sg.Text("4: Relation to Luke"),sg.Text("5: nth Tetehedral"),sg.Text("6: Convert to Binary")],
                    [sg.Text("7: Invert ASCII Charcode of Case Character"),sg.Text("8: Finding Adjacent Nodes")],
                    [sg.Text("9: Snake Fill"), sg.Text("10: Calculated Bonus"),sg.Text("11: Construct and Deconstruct")],
                    [sg.Text("Enter the exercise key"), sg.Input(key="-EKEY-")],
                    [sg.Button("TEST OUT EXERCISE"),
                    #sg.Button("COPY"),
                    sg.Button("EXIT")]]
    window = sg.Window("Exercise Directory",layout) #create window with layout

    while True: #GUI event loop
        event, values = window.read()
        print(event,values)
        if event == "EXIT" or event == sg.WIN_CLOSED: #close window
            break
        if event == "TEST OUT EXERCISE":
            if 0 > int(values["-EKEY-"]) > 12:
                break
            else:
                ex_num = int(values["-EKEY-"]) #gets the key of the exercise wanted
                window["-EKEY-"].update("") #clear the key spot
                exercise_window( ex_num ) #call the exercise window

    window.close()

#print("")
#print("Welcome")
#print("")
#print("Please only answer Yes and No (CASE SENSITIVE) unless told otherwise!")

####### Exit Program Function ##################################################
def leave ():
    pass
    stay = input("Would you like to continue? ")

    if stay == "No":
        print("")
        exit("Goodbye")
    else:
        pass

####### Stuttering Function ####################################################
def stutter( str ):
    "This prints the stuttered word"

    return str[0:2]+"..."+str[0:2]+"..."+str+"?"

######## Radians to Degrees ####################################################
def radians_to_degrees ( rad ):
    return rad*57.3 #make this use pi instead

####### Curzon Numbers #########################################################
def isCurzon ( num ):
    if (1+2**num)%(1+2*num)==0: #using modulo to see if factorable
        return True
    else:
        return False
####### Luke, I am your... #####################################################
def relation_to_luke ( str ):
    start = "Luke I am your "
    if str == "Darth Vader":
        return start+"father."
    if str == "Leia":
        return start+"sister."
    if str == "Han":
        return start+"brother in law."
    if str == "R2D2":
        return start+"droid."

####### nth Tetrahedral Number #################################################
def tetra ( num ):
    curr = (num*(num+1))/2
    prev = ((num-1)*num)/2
    return (curr+prev)

####### Convert to Binary ######################################################
def binary ( num ):
    binary_list = [*range(0,12,1)] #creates 10 item list to fill with binary number

    output = ""

    for i in range(0,11):
        abs_of_i = abs(i-10)
        if ((num <= 2**abs_of_i) and (num >= 2**(abs_of_i-1))):
        #goes through values 1,2,4,8,16,32,64,128,256,512,1024
        #if num is less than 2 exponent i then that spot = 1
#            if count < abs_of_i:
#                count = abs_of_i

            binary_list[i+1] = 1
            #if num is lesser or equal to high power and greater than low power
            #make that spot in the list a 1
            if abs_of_i != 0:
                num = num%(2**(abs_of_i-1))
                output = output + str(binary_list[i])
            else:
                break

            #now make the number smaller through modulo of the smaller power
            #repeat
        else:
            binary_list[i+1] = 0
            output = output + str(binary_list[i])

    return output

####### Find ASCII Charcode of Inverse Case Character ##########################

#ord() returns hex number of a letter
#chr() returns letter of a hex number
#swapcase()
def counterpart_Charcode ( char ):
    new_char = str.swapcase(char)
    return ord(new_char)

####### Finding Adjacent Nodes #################################################

#encode graph using adjacency matrix
#directed and undirected graphs
#n nodes in a graph means n*n matrix
#entry at row "i" and column "j" is 0 if notes "i" and "j" are not adjacent, 1 if they are
#determine if nodes are adjacent in an undirected graph

#NumPy gives ability to shape lists into matrices; np. references class; .array names an array
#.arange creates a normal list with range given; .reshape(x,y) reshapes an array to be x rows and y columns
import numpy as np #gives array shapeing
A = np.array([[0,1,0,1,1],[1,0,1,0,0],[0,1,0,1,0],[1,0,1,0,1],[1,0,0,1,0]]) #create a function to make a graph
def is_adjacent( node_1, node_2 ):
    if A[node_1, node_2] == 1:
        return f"Node {node_1} and {node_2} are adjacent"
    else:
        return f"Node {node_1} and {node_2} are not adjacent"


####### Snake ##################################################################
def snakefill( n ): #size is n in n x n grid
    size = 1
    count = 0
    continue_input = True
    while continue_input:
        size = size*2
        if size > n*n:
            continue_input = False
        else:
            count += 1

    return f"The snake can eat {count} times before filling the board\n"

####### Calculated bonus #######################################################

def bonus( days ):
    billible_days1 = 0
    billible_days2 = 0
    billible_days3 = 0
    price_1 = 325
    price_2 = 550
    price_3 = 600

    for i in range(1,days+1): #to start with day 1, end with day days
        if i <= 32:
            pass
        if 33 <= i <= 40:
            billible_days1 += 1
        if 41 <= i <= 48:
            billible_days2 += 1
        if i >= 49:
            billible_days3 += 1
    payment = billible_days1*price_1 + billible_days2*price_2 + billible_days3*price_3
    return f"You made ${payment} in bonuses this quarter!"

####### Drunken Python #########################################################
#needs work
#Job is
#create two functions to substitute str() and int()
#function that converts ints to strings, and function that converts strings to ints
#bonus points to de-drunk python
import unittest

def int_to_str( num ): #pretend this is the str function
    return ("'"+str(num)+"'")

def str_to_int( num ): #pretend this is the int function
    return int(num)

#int_to_str(4)
#str_to_int("4")

####### Construct and deconstruct ##############################################
#ADD TO DIRECTORY

def c_and_r( string ):
    count = 0
    length = len(string)
    while length >= count:
        print(string[0:count])
        count += 1
    count = 1
    while length >= count:
        print(string[0:length-count])
        count += 1


main() #only needed function
