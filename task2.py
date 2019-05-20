class Number:
    def __init__(self, num):
        self.num = num
    def __str__(self):
        return str(self.num)
class add:
    def __init__(self, l, r):
        self.l = l
        self.r = r
    def __str__(self):
        return '(+ '+str(self.l)+' '+str(self.r)+')'
class mul:
    def __init__(self, l, r):
        self.l = l
        self.r = r
    def __str__(self):
        return '(* '+str(self.l)+' '+str(self.r)+')'
# print(mul(add(add(Number(1), Number(2)),mul(Number(3),Number(4))), Number(10)))
# print(mul(Number(12), add(Number(10), mul(Number(5), Number(56)))))
# print(mul(Number(3), Number(5)))
# fifteen = mul(Number(1), Number(15))
# print(fifteen)

class Node(object):
    def __init__(self, value, left=None, right=None):
        if isinstance(value, mul):
            self.value = '*'
            self.left = Node(value.l)
            self.right = Node(value.r)
        elif isinstance(value, add):
            self.value = '+'
            self.left = Node(value.l)
            self.right = Node(value.r)
        else:
            self.value = value
            self.left = None
            self.right = None
        

    def __str__(self):
        return str(self.value)


def traverse(root):
    current_level = [root]
    while current_level:
        l = [str(node) for node in current_level]
        print(l)
        next_level = list()
        for n in current_level:
            if n.left:
                next_level.append(n.left)
            if n.right:
                next_level.append(n.right)
            current_level = next_level

fifteen = mul(Number(3), Number(5))
temp = mul(add(add(Number(1), Number(2)),mul(Number(3),Number(4))), Number(10))

rem_list = [' ', '(', ')']

# for i in input_string:
#     print(i)
# print(fifteen.l)
t = Node(fifteen)
p = Node(temp)

traverse(t)
traverse(p)
print(temp)