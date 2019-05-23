from task1 import add, mul, Number
from task2 import tree_form
def num_interp(self):
    return self.num
def add_interp(self):
    return  self.l.interp() + self.r.interp()
def mul_interp(self):
    return  self.l.interp() * self.r.interp()
add.interp = add_interp
mul.interp = mul_interp
Number.interp = num_interp