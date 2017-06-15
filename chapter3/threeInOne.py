import IPython

array_size = 8

class multi_stack(object):
    
    def __init__(self,stacks,array):
        self.stacks = stacks
        self.array = array
    
    def display_all(self):
        for i in self.array:
            print(i)

    def display_stack(self,numstack):
        for i in range(self.stacks[numstack].top -(self.stacks[numstack].size - 1),self.stacks[numstack].top + 1):
            print(self.array[i%array_size])

    def push(self,numstack_number,value):
        try:
            stack_bottoms = []
            for element in self.stacks:
                stack_bottoms.append(element.top -(element.size-1))
            if((self.stacks[numstack_number].top + 1 ) in stack_bottoms):
                #the index is already occupied by the bottom of another stack => move that stack
                self.move(self.stacks[stack_bottoms.index(self.stacks[numstack_number].top + 1)])
            #we can now safely add an element to that location
            self.array[(self.stacks[numstack_number].top + 1)%array_size] = value
            #and change the top to point to that location
            self.stacks[numstack_number].top = (self.stacks[numstack_number].top + 1)
            self.stacks[numstack_number].size += 1
        except:
            raise
    
    #moves a numstack in the array
    def move(self,stack):
        stack_bottoms = []
        for element in self.stacks:
            #make a list of bottoms of stack
            stack_bottoms.append((element.top -(element.size)))
        for index in range(stack.top,(stack.top-stack.size -1),-1):
             #check that not occupied
            if index+1 in stack_bottoms:
                #if occupied we move the stack to which it belongs
                self.move(self.stacks[stack_bottoms.index(self.array[(index+1)%array_size])])
            else:
                #if not occupied we assign new value
                self.array[(index+1) % array_size]=self.array[index]
            if index == stack.top :
                #we assign a new value to the top of the stack
                stack.top = (stack.top + 1)
     
class simple_stack(object):

    def __init__(self,top,size):
        self.top = top
        self.size = size

def init_multi_stack(numstacks,array):
    stack = []
    for i in range(0,numstacks):
        stack.append(simple_stack(i,1))
    m_stack = multi_stack(stack,array)
    return m_stack

def init_array(array,array_sizo):
    for i in range(array_sizo):
        array.append(0)

def main():
    numstacks = 3
    array = []
    init_array(array,array_size)
    multi_stack = init_multi_stack(numstacks,array)
    multi_stack.display_all()
    print('---------')
    multi_stack.push(0,782)
    multi_stack.push(1,23)
    multi_stack.display_all()
    multi_stack.push(2,64)
    multi_stack.push(1,22)
    print('---------')
    multi_stack.display_all()
    multi_stack.push(1,21)
    print('---------')
    multi_stack.display_all()
    print('--------')
    multi_stack.display_stack(0)
    print('--------')
    multi_stack.display_stack(1)
    print('--------')
    multi_stack.display_stack(2)
    print('--------')
    
if __name__ == "__main__":
    main()
