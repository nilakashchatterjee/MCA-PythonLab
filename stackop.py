# Q5. Define one class as names 𝒔𝒕𝒂𝒄𝒌 , which contains and data member 𝑣𝑎𝑙𝑢𝑒, and the
# methods as
# follows:
# Constructor : initialize data member 𝑣𝑎𝑙𝑢𝑒 with empty list
# Push: append one element in the stack
# Pop: return top most element from the list
# isEmpty: return true if the stack is empty, false otherwise
# top: return top element of the stack
# size: return length of the list
# __str__: return string representation of the stack.
# Implement the stack of integers using the above-mentioned class.
class stack:
    def __init__(self):
        self.stack = []
    # Adding values to the end of the stack
    def Push(self,data):
        if  data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False
    # Removing the the top value from the stack
    def Pop(self):
        if len(self.stack)<=0:
            print("No data can be deletd as the list is empty")
        else:
            print("The element to be deleted is:",self.stack.pop())
    # Checking the top value of the stack
    def top(self):
        print("The top element of the stack is:")
        return print(self.stack[-1])
    # Checking whether the stack is empty or not
    def isempty(self):
        if len(self.stack)<=0:
            print("The list is empty!!!")
            return True 
        else:
            print("List is not empty there is data in the stack!!!")
            return False
    # Checking the size of the stack
    def size(self):
        print("The length of the stack:")
        return print(len(self.stack))
    # Printing the stack
    def __str__(self):
        return print("The stack is:",str(self.stack))

stk = stack() # instance of the class

stk.Push(15)
stk.Push(42)
stk.Push(11)
stk.Push(23)
stk.Push(8)

stk.Pop()
stk.isempty()
stk.size()
stk.top()
stk.__str__()