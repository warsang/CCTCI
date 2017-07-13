

#Time complexity:
#Stack operations except search are O(1)
#Queue: To remove an element from the queue:
#We itterate once through stack1 and once through stack 2 => O(2N) = O(N)
#Memory complexity:
#O(2N) as there are two stacks with an array of size N each. We can imagine the array 2 being freed when empty which would slightly improve the memory complexity but it will still be O(N)

class myQueue(object):

    def __init__(self,stack1,stack2):
        self.stack1 = stack1
        self.stack2 = stack2
    
    def add(self,value):
        self.stack1.push(value)

    def remove(self):
        while self.stack1.isEmpty() == False:
            temp = self.stack1.pop()
            self.stack2.push(temp)
        return_val = self.stack2.pop()
        while self.stack2.isEmpty() == False:
            temp = self.stack2.pop()
            self.stack1.push(temp)
        return return_val
    
    def peek(self):
        return self.stack1.peek()

    def __str__(self):
        return str(self.stack1)

class stack(object):

    def __init__(self,values):
        self.values = values

    def push(self,newValue):
        self.values.append(newValue)

    def pop(self):
        poped = self.values[-1]
        self.values = self.values[:-1]
        return poped
   
    def peek(self):
        return self.values[-1]

    def isEmpty(self):
        if len(self.values) == 0:
            return True
        else:
            return False
    
    def __str__(self):
        return str(self.values)

def main():
    first_stack = stack([1,4,2,6,3,5,9,19,2,3])
    second_stack = stack([])
    queue = myQueue(first_stack,second_stack)
    print(queue)
    queue.remove()
    print(queue)
    queue.add(8)
    print(queue)
    queue.remove()
    print(queue)
    queue.add(6)
    print(queue)
    print(queue.peek())

if __name__ == "__main__":
    main()
