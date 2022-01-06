class BinaryTreeSimple:
    def __init__(self, value, left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, value):
        if self.value == None:
            self.value = BinaryTreeSimple(value)

        elif value < self.value:
            if self.left !=None:
                self.left.insert(value)
            else:
                self.left = BinaryTreeSimple(value)

        elif value >= self.value:
            if self.right !=None:
                self.right.insert(value)
            else:
                self.right = BinaryTreeSimple(value)

    def search(self, value):
        if self.value == value:
            return True

        elif self.left != None:
            self.left.search(value)
        elif self.right != None:
            self.right.search(value)
        else: return  False

    def print_tree(self):
        if self.left != None:
            self.left.print_tree()
        else:
            print(self.value)
        if self.right!=None:
            self.right.print_tree()




import random
numbers = []
root=BinaryTreeSimple(11)
for i in range(100):
    numbers.append(random.randint(-1000, 1000))
    root.insert(numbers[-1])

for number in numbers:
    if root.search(number) == False:
        print("error - could not find {} ".format(number))

root.print_tree()