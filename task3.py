from task1 import add, mul, Number
from task2 import tree_form
#1
print(tree_form(mul(add(add(Number(1), Number(2)),mul(Number(3),Number(4))), Number(10))))
#2
print(tree_form(mul(Number(12), add(Number(10), mul(Number(5), Number(56))))))
#3
print(tree_form(mul(Number(3), Number(5))))
#4
fifteen = mul(Number(1), Number(15))
print(tree_form(fifteen))
#5
two = add(Number(1), Number(1))
sixteen = mul(Number(4), mul(two, two))
thiry_two = mul(two, sixteen)
print(tree_form(thiry_two))
#6
sixty_four = mul(two, mul(two, mul(two, mul(two, mul(two, two)))))
print(tree_form(sixty_four))
#7
ten = mul(Number(5), Number(2))
hundred = mul(ten, ten)
thousand = mul(ten, hundred)
six_four_three_two = add(add(mul(Number(6),thousand),mul(Number(4),hundred)),add(mul(Number(3), ten),Number(2)))
print(tree_form(six_four_three_two))
#8
temp = add(Number(1), Number(1))
for i in range(5):
    temp = add(temp,temp)
print(tree_form(temp))
#9
print(tree_form(add(add(Number(1), Number(1)), mul(ten, mul(hundred, thousand)))))
#10
meaning_of_life = add(mul(Number(4),ten), Number(2))
print(tree_form(meaning_of_life))
#11
print(tree_form(add(hundred, ten)))
#12
print(tree_form(add(ten, Number(-1))))