class Number:
    def __init__(self, num):
        self.num = num
    def __str__(self):
        return str(self.num)
    def interp(self):
        return self.num
class add:
    def __init__(self, l, r):
        self.l = l
        self.r = r
    def __str__(self):
        return '('+str(self.l)+' + '+str(self.r)+')'
    def interp(self):
        return self.l.interp() + self.r.interp()
class mul:
    def __init__(self, l, r):
        self.l = l
        self.r = r
    def __str__(self):
        return '('+str(self.l)+' * '+str(self.r)+')'
    def interp(self):
        return self.l.interp() * self.r.interp()     
class atom:
    def __init__(self, val):
        self.value = val
    def __str__(self):
        return str(self.value)

class cons:
    def __init__(self, atom, n):
        self.value = atom
        self.next = n
    def desugar(self):
        temp = None
        if isinstance(self.value, atom):
            temp_value = str(self.value)
            if temp_value == '*':
                temp = mul(Number(1), Number(1))
                temp.l = self.next.desugar()[0]
                temp.r = self.next.desugar()[1]
                return temp
            elif temp_value == '+':
                temp = add(Number(0), Number(0))
                temp.l = self.next.desugar()[0]
                temp.r = self.next.desugar()[1]
                return temp
            else:
                if isinstance(self.next.value, atom):
                    tt = str(self.next.value)
                return (temp_value, tt)
        elif isinstance(self.value, cons):
            return self.value.desugar()
    def __str__(self):
        return str(self.value) + ' ' + str(self.next)

x = cons(atom('*'), cons(atom('5'), cons(cons(atom('+'), cons(atom('3'), cons(atom('5'), atom('')))), atom(''))))
print(x)
# mul(Number(3), Number(5))
y = cons(atom('+'), cons(atom(3), cons(atom(5), atom(''))))
print(y.desugar())
z = cons(atom('+'), cons(cons(atom('+'), cons(atom(1), cons(atom(1), atom('')))), cons(atom(5), atom(''))))
print(z.desugar())
