import pdb

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)



operators = {
    # addition
    '+' : {
        'prec' : 1,
        'calc' : lambda a,b: a + b },
    # subtraction
    '-' : {
        'prec' : 1,
        'calc' : lambda a,b: a - b },
    # multiplication
    '*' : {
        'prec' : 2,
        'calc' : lambda a,b: a * b },
    # division
    '/' : {
        'prec' : 2,
        'calc' : lambda a,b: a / b },
    # exponentiation
    '^' : {
        'prec' : 3,
        'assoc' : 'right',
        'calc' : lambda a,b: a ** b },
    # negation
    '~' : {
        'prec' : 6,
        'assoc' : 'right',
        'arity' : 1,
        'calc' : lambda a: -a },
    # modulus
    '%' : {
        'prec' : 4,
        'calc' : lambda a,b: a % b },
    # factorial
    '!' : {
        'prec' : 4,
        'assoc' : 'right',
        'arity' : 1,
        'calc' : lambda a: factorial(a) },
    # average
    '@' : {
        'prec' : 5,
        'calc' : lambda a,b: (a + b) / 2 },
    # max
    '$' : {
        'prec' : 5,
        'calc' : lambda a,b: max(a,b) },
    # min
    '&' : {
        'prec' : 5,
        'calc' : lambda a,b: min(a,b) } }


def toPolishNotation(infixNotation_):
    stack = Stack()
    polish_string = ""
    infixNotation = infixNotation_.split()
    
    for x in infixNotation:

        if x.isdigit():
            polish_string += ' ' + x

        if x in "+-*/":

            if not stack.isEmpty:

                while operators[x]['prec'] <= operators[stack.peek()]['prec'] or stack.isEmpty():
                    polish_string += ' ' +  stack.pop()
                stack.push(x)             

            else: stack.push(x)

        if x == '(':
            stack.push(x)

        if x == ')':
            if not stack.isEmpty():

                while stack.peek() != '(':
                    polish_string += ' ' + stack.pop()
                stack.pop()

                if (not stack.isEmpty()) and (stack.peek() in "+-*/") :
                    polish_string += ' ' + stack.pop()

        print(polish_string)


    if not stack.isEmpty():
        while not stack.isEmpty():
            polish_string += ' ' +  stack.pop()

    return polish_string


print(toPolishNotation("( 3 + 5 ) * 5 * ( 4 + 7 ) * ( 9 + 7 ) / 11"))
