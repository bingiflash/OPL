class atom:
    def __init__(self, val):
        self.value = val
    def __str__(self):
        return self.value

class cons:
    def __init__(self, atom, n):
        self.value = atom
        self.next = n
    def __str__(self):
        return str(self.value) + ' ' + str(self.next)

x = cons(atom('*'), cons(atom('5'), cons(cons(atom('+'), cons(atom('3'), cons(atom('5'), atom('')))), atom(''))))
print(x)