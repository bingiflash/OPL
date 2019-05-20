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
print(mul(add(add(Number(1), Number(2)),mul(Number(3),Number(4))), Number(10)))
print(mul(Number(12), add(Number(10), mul(Number(5), Number(56)))))
print(mul(Number(3), Number(5)))
fifteen = mul(Number(1), Number(15))
print(fifteen)