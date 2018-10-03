'''
<input, output, assignment, declaration, arithmetic and logic, comment, block, selection, iteration, function (prototype, definition, call).
'''
import datetime
def kaliyamardan(size):               #function declaration
    #function definition
    #block
    '''
    To increase krishna's size till he becomes bigger than even kaliya's hoods!     #comment
    '''
    size = size + 1                   #arithmetic and logic
    return size                       #output
def raas(common, krishna_steps):      #function declaration
    #function definition
    #block
    '''
    Dance for both the common people and for krishna        #comment
    '''
    step1 = "Dance"                     #assignment
    step2 = "Clap"                      #assignment
    step = "Dances on Kaliya's head"    #assignment
    common.appends(step1)               #logic
    common.append(step2)                #logic
    krishna_steps.append(step)          #logic
    return common, krishna_steps        #output

krishna = input("Enter your name")      #input
krishna_size = 10                       #assignment
common_people = 10                      #assignment
common = []                             #assignment, declaration
krishna_steps = []                      #assignment, declaration
janmashtami = input('Enter your birthdate')  #input
kaliya = 'Naga'                         #assignment
happiness = 0                           #assignment
kaliya_hoods = 110                      #assignment
while kaliya_hoods > krishna_size:      #logic, arithmetic
    #block
    #iteration
    krishna_size = kaliyamardan(krishna_size) #function call
common, krishna_steps = raas(common, krishna_steps) #function call
print(krishna, krishna_steps)           #output
while common_people > happiness:        #logic, arithmetic
    # Repeat all dance steps till all people become happy
    #block
    #iteration
    for p in common:
        #block
        #iteration
        print("People " + p)            #output
    for k in krishna_steps:
        #block
        #iteration
        print(krishna + " " + k)        #output
    happiness = happiness + 1           #arithmetic

print("Lets celebrate Janmashtami on", datetime.datetime.strptime(janmashtami, "%d/%m/%Y")) #output #function call
