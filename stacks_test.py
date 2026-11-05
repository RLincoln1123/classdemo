class Stack
""" -This class impliments a stack using a list
    -Values/Characters are stored in order and accessed using 
     last in first out (LIF0) procedure.
"""
    def __init__(self):
""" Initialize the stack with a list """
#Initialize empty list to store values
        self.data = []
    def push(self, value):
""" Add a new value to the top of the stack
    Args:
         value: The item that will be added to the stack 
"""
#Add the given values to the end of the list 
        self.data.append(value)
""" Remove and return the value at the top of the stack
    Returns:
         The most recent item added to the stack
"""
#Remove and return the last known value in the list 
    def pop(self):
        return self.data.pop()

def main():
""" Ryan Lincoln 
    csc-212
    
    This program analyzes the post fix notation using a stack

    -Numbers are added into the stack until an opperator is found
    -Opperator is applied to the two most recent values 
    -The calculated result is returned to the stack until 
     the whole postfix expression has been analyzed. 
"""
#Created a stack object to add values 
code_stack = Stack()

#Storing the postfix expression 
postfix_code = "3 5 1 - * 2 +"

#Split the postfix expression into seperate numbers and operators 
for character in postfix_code.split(): #Start of for loop

    #Check if current character is a number
    if character.isdigit():
        code_stack.push(int(character) #Coverted to int and pushed to the stack

    #Check if current chatacter is a math operator
    if character == '+' or character == '-' or character == '*' or character == '/':

        #Remove the top two numbers from the stack
        first_opperand = code_stack.pop() #Gather first opperand 
        second_opperand = code_stack.pop()#Gather second opperand 
        
        #Add when operator is a plus sign 
        if character == '+'
            calculation = first_opperand + second_opperand 
        #Subtract when the opperator is a minus sign 
        if character == '-'
            calculation = first opperand - second_opperand 
        #Multiply when the opperator is a multiplication sign 
        if character == '*'
            calculation = first_opperand * second_opperand
        #Divide when the opperator is a division sign 
        if character == '/'
            calculation = first_opperand / second_opperand


        #Push the calculated data to the stack
        code_stack.push(calculation)
        
# Remove the calculation from the stack and print it 
print("Final Answer:", code_stack.pop())

if __name__ == "__main__":
    main()
        



    
