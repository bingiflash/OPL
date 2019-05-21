from task1 import add, mul, Number
def tree_form(tree):
    if isinstance(tree, add):
        oper = '+'
    elif isinstance(tree, mul):
        oper = '*'
    elif isinstance(tree, Number):
        res = tree.num
    if tree is not None and not isinstance(tree, Number):
        temp = tree_form(tree.l)
        if temp is not None:
            res = "(" +str(temp) + ' ' + oper + ' '
    if tree is not None and not isinstance(tree, Number):
        temp = tree_form(tree.r)
        if temp is not None: 
            res = res + str(temp) + ')'
    return res