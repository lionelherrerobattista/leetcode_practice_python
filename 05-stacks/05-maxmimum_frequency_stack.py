class FreqStack:

    def __init__(self):
        self.count = {}
        self.max_count = 0
        self.stacks = {}
        

    def push(self, val: int) -> None:
        if val in self.count:
            val_count = self.count[val] + 1
        else:
            val_count = 1
        # update the count of the value in hashmap
        self.count[val] = val_count
        # check max count
        if val_count > self.max_count:
            self.max_count = val_count
            # add new list for that value
            self.stacks[val_count] = []
        # append the value to the list
        self.stacks[val_count].append(val)
        

    def pop(self) -> int:
        # look for the stack with the most frequent element
        res = self.stacks[self.max_count].pop()
        # update value count
        self.count[res] -= 1
        # update the stacks
        if not self.stacks[self.max_count]:
            self.max_count -= 1
        return res

# test
freqstack = FreqStack()
freqstack.push(5)# The stack is [5]
freqstack.push(7)# The stack is [5,7]
freqstack.push(5)# The stack is [5,7,5]
freqstack.push(7)# The stack is [5,7,5,7]
freqstack.push(4)# The stack is [5,7,5,7,4]
freqstack.push(5)# The stack is [5,7,5,7,4,5]
print(freqstack.count)
print(freqstack.pop()) # return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
print(freqstack.count)
print(freqstack.pop()) # return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
print(freqstack.pop()) # return 5, as 5 is the most frequent. The stack becomes [5,7,4].
print(freqstack.pop()) # return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].
