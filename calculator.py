class Calculator(object):
    """docstring for ClassName"""

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

    def isfloat(self,x):
        try:
            float(x)
            return True 
        except ValueError:
            return False

    def toPolishNotation(self,infixNotation_):
        stack = self.Stack()
        polish_string = ""
        infixNotation = infixNotation_.split()

               
        for x in infixNotation:
                    
            if self.isfloat(x):
                polish_string += ' ' + x
                #print(polish_string + " --")

            if x in "+-*/^":

                if not stack.isEmpty():
                    #print("here")
                    while (not stack.isEmpty()) and (stack.peek() in "+-*/^")  and self.operators[x]['prec'] <= self.operators[stack.peek()]['prec']:
                        polish_string += ' ' +  stack.pop()
                    stack.push(x)            
                    #print(polish_string)
                    #print(stack.peek() + "--stack peek")
                else:
                 stack.push(x)
                 #print(polish_string + "--operator string")
                 #print(stack.peek() + "--stack peek")
                # print(stack.peek())

            if x == '(':
                stack.push(x)


            if x == ')':
                if not stack.isEmpty():

                    while stack.peek() != '(':
                        polish_string += ' ' + stack.pop()
                    stack.pop()

                    #if (not stack.isEmpty()) and (stack.peek() in "+-*/^") :
                       # polish_string += ' ' + stack.pop()


        if not stack.isEmpty():
            while not stack.isEmpty():
                polish_string += ' ' +  stack.pop()

        return polish_string



    def calculate(self,sRPN_):

        sRPN = sRPN_.split()
        stack = self.Stack()
        for x in sRPN:
            if self.isfloat(x):
                #print("operand")
                stack.push(x)
                #print(stack.peek())
            else:
                #print("operator")
                b = float(stack.pop())
                a = float(stack.pop())
                stack.push(self.operators[x]['calc'](a, b))
                #print(stack.peek())
        return stack.pop()

    def evaluate(self,string):
        rpn = self.toPolishNotation(string)
        print(rpn)
        return round(float(self.calculate(rpn)),3)



def to_postfix (infix):
    new_infix = ' '.join(list(infix))
    polish = Calculator().toPolishNotation(new_infix)
    return polish

print to_postfix("5+(6-2)*9+3^(7-1)")