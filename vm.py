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
#test-suite
#1
print(str(mul(add(add(Number(1), Number(2)),mul(Number(3),Number(4))), Number(10))) == "(((1 + 2) + (3 * 4)) * 10)")
#2
print(str(mul(Number(12), add(Number(10), mul(Number(5), Number(56))))) == "(12 * (10 + (5 * 56)))")
#3
print(str(mul(Number(3), Number(5))) == "(3 * 5)")
#4
fifteen = mul(Number(1), Number(15))
print(str(fifteen) == "(1 * 15)")
#5
two = add(Number(1), Number(1))
sixteen = mul(Number(4), mul(two, two))
thiry_two = mul(two, sixteen)
print(str(thiry_two) == "((1 + 1) * (4 * ((1 + 1) * (1 + 1))))")
#6
sixty_four = mul(two, mul(two, mul(two, mul(two, mul(two, two)))))
print(str(sixty_four) == "((1 + 1) * ((1 + 1) * ((1 + 1) * ((1 + 1) * ((1 + 1) * (1 + 1))))))")
#7
ten = mul(Number(5), Number(2))
hundred = mul(ten, ten)
thousand = mul(ten, hundred)
six_four_three_two = add(add(mul(Number(6),thousand),mul(Number(4),hundred)),add(mul(Number(3), ten),Number(2)))
print(str(six_four_three_two) == "(((6 * ((5 * 2) * ((5 * 2) * (5 * 2)))) + (4 * ((5 * 2) * (5 * 2)))) + ((3 * (5 * 2)) + 2))")
#8
temp = add(Number(1), Number(1))
for i in range(5):
    temp = add(temp,temp)
print(str(temp) == "((((((1 + 1) + (1 + 1)) + ((1 + 1) + (1 + 1))) + (((1 + 1) + (1 + 1)) + ((1 + 1) + (1 + 1)))) + ((((1 + 1) + (1 + 1)) + ((1 + 1) + (1 + 1))) + (((1 + 1) + (1 + 1)) + ((1 + 1) + (1 + 1))))) + (((((1 + 1) + (1 + 1)) + ((1 + 1) + (1 + 1))) + (((1 + 1) + (1 + 1)) + ((1 + 1) + (1 + 1)))) + ((((1 + 1) + (1 + 1)) + ((1 + 1) + (1 + 1))) + (((1 + 1) + (1 + 1)) + ((1 + 1) + (1 + 1))))))")
#9
print(str(add(add(Number(1), Number(1)), mul(ten, mul(hundred, thousand)))) == "((1 + 1) + ((5 * 2) * (((5 * 2) * (5 * 2)) * ((5 * 2) * ((5 * 2) * (5 * 2))))))")
#10
meaning_of_life = add(mul(Number(4),ten), Number(2))
print(str(meaning_of_life) == "((4 * (5 * 2)) + 2)")
#11
print(str(add(hundred, ten)) == "(((5 * 2) * (5 * 2)) + (5 * 2))")
#12
print(str(add(ten, Number(-1))) == "((5 * 2) + -1)")