import pydoc
import random

class Queue:
    """ A queue that uses first in first out """
    def __init__(self):
        #Empty list to store queued numbers 
      self.data = []

    def enqueue(self, value):
        #Add number to the back of the queue 
      self.data.append(value)
    
    def dequeue(self, value):
        #Remove and return the first number in the queue 
      self.data.pop(0)

   def is_empty(self):
       #Check to see if the queue contains 0 numbers (nothing)
     return len(self.data) == 0

   def current_queue(self):
       #Return the contents of the current queue 
     return self.data
       
class stack:
    """Stack class that follows last in first out""" 
   def __init__(self):
       #Empty list to store stacked numbers 
       self.data = []
       
   def push(self,value):
       # Add a number to the top of the stack 
       self.data.append(value)

   def pop(self):
       #Remove and return the top number from the stack
       return self.data.pop()

   def peek(self):
       #Look at the top number without removing it
       return self.data[-1]

   def is_full(self):
       #Check if stack contains 3 numbers (FULL)
       return len(self.data) == 3

   def current_stack(self):
       #Return the contents of the current stack
       return self.data

def check_matches (queue, stacks):
    """Checking for matching pairs and matching triple stack tops"""
    #Continue check if true until no matches are found
    while True:
           #We have to make sure that all three stacks contain one number 
           #Then compare the top numbers in the stack
           #Follow the game rule for 3 matching tops 
        if (all(len(stack.data) > 0 for stack in stacks
                and stacks[0].peek() == stacks[1].peek()
                and stacks[1].peek() == stacks[2].peek()):
                    
            #Remove the matching top number from stack a
            number = stacks[0].pop()
            #Remove the matching top number from stack b
            stacks[1].pop()
            #Remove the marching top number from stack c 
            stacks[2].pop()
                    
            #Add a copy of the number to the back of the queue
            queue.enqueue(number)
            #Print the 3 matches that were removed 
            print("Three matching numbers removed", number)

        else:
            #If no matching pairs have been found (Found/False)
            match_found = False 
            
            # Individually check each stack
            for stack in stacks:
                
                #We are making sure the stack has at least 2 numbers 
                #before seeing the top 2 positions 
                #The last 2 numbers are compared to find a pair
                if (len(stack.data) >= 2 
                        and stack.data[-1] == stack.data[-2]):
                            
                    #Remove the first matching number 
                    number = stack.pop()
                            
                    #Remove the second matching number 
                    stack.pop()
                            
                    # Add a copy of the number to the queue 
                    queue.enqueue(number)
                            
                    # Print the matching pair
                    print("Two matching numbers removed")
                    # When found the matching pair is remembered in the queue
                    match_found = True 
                            
                    #Stop checking for matches 
                    break
            #If no matching pair was found then checking stops and the loop repeats to check for another match
            if not match_found:
                    break
def display_game(queue, stacks):
    """Display the current queue and all three stacks"""
    
    #Print the current queue contents 
    print("\nCurrent queue:", queue.current_queue())
    
    #Print the current contents of stack a
    print("a:", stacks[0].current_stack())
    
    #Print the current contents of stack b
    print("b:", stacks[1].current_stack())
    
    #Print the current contents of stack c
    print("c:", stacks[2].current_stack())


def main():
    """Start of the creation of the stacks and queue game"""
    #New empty queue 
    game_queue = Queue()
    
    #15 random numbers generatated 
    for i in range(15):
        #Random number between 1 and 5 generated 
        number = random.randint(1, 5)
        
        #Adding the random number to the queue 
        game_queue.enqueue(number)
        
        #Creating 3 empty stacks 
        stacks = [Stack(), Stack(), Stack()]
        
        #Store the names of the three stacks 
        names = ["a", "b", "c"]

        print("Welcome to the Stackr Game")
        
        #Print the original queue contents 
        print("\nStarting Queue:", game_queue.current_queue())

        #Continue playing if queue is not empty
        While not game_queue.is_empty():

            if all(stack.is_full() for stack in stacks):
               # Message the player gets when they lost
               print(\nYou Loose All Stacks Are Full.")
                
               # End the game 
               return
                    
    
    
