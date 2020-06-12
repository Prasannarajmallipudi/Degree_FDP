Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("APSSDC_FDP")
APSSDC_FDP
>>> print(123)
123
>>> print("
	  ")
SyntaxError: EOL while scanning string literal
>>> print("123")
	  
123
>>> print("Python")
	  
Python
>>> name = "Faculty Development Program"
	  
>>> print(name)
	  
Faculty Development Program
>>> number = 2422
	  
>>> print(number)
	  
2422
>>> type(name)
	  
<class 'str'>
>>> type(number)
	  
<class 'int'>
>>> salary = 40000.0
	  
>>> type(salary)
	  
<class 'float'>
>>> num = "123456789"
	  
>>> type(num)
	  
<class 'str'>
>>> print(name,number,salary,num)
	  
Faculty Development Program 2422 40000.0 123456789
>>> name
	  
'Faculty Development Program'
>>> name = "Prasanna Raj M"
	  
>>> name
	  
'Prasanna Raj M'
>>> 1abc="qweerty"
	  
SyntaxError: invalid syntax
>>> 123 = "abc"
	  
SyntaxError: can't assign to literal
>>> abc123 = "ApSSDC"
	  
>>> abc123
	  
'ApSSDC'
>>> $abc = 123
	  
SyntaxError: invalid syntax
>>> student_name = "Prasanna Raj"
	  
>>> print(student_name)
	  
Prasanna Raj
>>> a = "APSSDC"
	  
>>> b = 2422
	  
>>> a + b
	  
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a + b
TypeError: must be str, not int
>>> str(b)
	  
'2422'
>>> a+str(b)
	  
'APSSDC2422'
>>> c = 10
	  
>>> b+c
	  
2432
>>> name
	  
'Prasanna Raj M'
>>> del name
	  
>>> name
	  
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    name
NameError: name 'name' is not defined
>>> name = ""
	  
>>> name
	  
''
>>> del name
	  
>>> name
	  
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    name
NameError: name 'name' is not defined
>>> a = 10
	  
>>> print(a)
	  
10
>>> # Expression - Expression is a combination of values,variables,and operators
	  
>>> a = 10
	  
>>> b= 20
	  
>>> c = 100
	  
>>> d = 10
	  
>>> exp = a*b+c/d
	  
>>> print(exp)
	  
210.0
>>> # Opertors
	  
>>> help(keyword)
	  
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    help(keyword)
NameError: name 'keyword' is not defined
>>> help(keywords)
	  
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    help(keywords)
NameError: name 'keywords' is not defined
>>> help()
	  

Welcome to Python 3.6's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.6/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> keywords

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               def                 if                  raise
None                del                 import              return
True                elif                in                  try
and                 else                is                  while
as                  except              lambda              with
assert              finally             nonlocal            yield
break               for                 not                 
class               from                or                  
continue            global              pass                

help> quit()
No Python documentation found for 'quit()'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> exit()
No Python documentation found for 'exit()'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> exit
Help on Quitter in module _sitebuiltins object:

exit = class Quitter(builtins.object)
 |  Methods defined here:
 |  
 |  __call__(self, code=None)
 |      Call self as a function.
 |  
 |  __init__(self, name, eof)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __repr__(self)
 |      Return repr(self).
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

help> quit

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> a = 10
	  
>>> b = 20
	  
>>> c = a+b
	  
>>> c
	  
30
>>> 
=========== RESTART: C:/Users/lenovo/Desktop/Degree_FDP/sample.py ===========
Addition is: 50
Substration is: -30
Mul is: 400
Div is: 0.25
Floor Div: 0
pow is 10000000000000000000000000000000000000000
Modules is: 10
>>> 
=========== RESTART: C:/Users/lenovo/Desktop/Degree_FDP/sample.py ===========
Addition is: 50
Substration is: -30
Mul is: 400
Div is: 0.25
Floor Div: 0
pow is 10000000000000000000000000000000000000000
Modules is: 10
>>> 
=========== RESTART: C:/Users/lenovo/Desktop/Degree_FDP/sample.py ===========
Addition is: 50
Substration is: -30
Mul is: 400
Div is: 0.25
Floor Div: 0
pow is 10000000000000000000000000000000000000000
Modules is: 10
>>> 
	  
>>> a =10
	  
>>> b = 23
	  
>>> a/b
	  
0.43478260869565216
>>> a//b
	  
0
>>> b = 25
	  
>>> a/b
	  
0.4
>>> a//b
	  
0
>>> b/a
	  
2.5
>>> a
	  
10
>>> b
	  
25
>>> x = 5
	  
>>> x**=5
	  
>>> x
	  
3125
>>> x/=10
	  
>>> x
	  
312.5
>>> x//=10
	  
>>> x
	  
31.0
>>> x
	  
31.0
>>> x = 10
	  
>>> x%=10
	  
>>> print(x)
	  
0
>>> 2>3
	  
False
>>> 2<6
	  
True
>>> 2==3
	  
False
>>> 10==10
	  
True
>>> 10!==10
	  
SyntaxError: invalid syntax
>>> 10!=10
	  
False
>>> 10!=11
	  
True
>>> 2>3 and 2>6
	  
False
>>> a
	  
10
>>> b
	  
25
>>> a and b
	  
25
>>> b and a
	  
10
>>> a or b
	  
10
>>> not a
	  
False
>>> a = True
	  
>>> b = False
	  
>>> a and b
	  
False
>>> x
	  
0
>>> a
	  
True
>>> number = 10
	  
>>> number is 5
	  
False
>>> number is 10
	  
True
>>> number is not 10
	  
False
>>> number is not 5
	  
True
>>> a = 10
	  
>>> b = 20
	  
>>> a = 10
b = 40

print("Addition is:",a+b)
print("Substration is:",a-b)
print("Mul is:",a*b)
print("Div is:",a/b)
print("Floor Div:",a//b)
print("pow is",a**b)
print("Modules is:",a%b)

SyntaxError: multiple statements found while compiling a single statement
>>> 
=========== RESTART: C:\Users\lenovo\Desktop\Degree_FDP\sample.py ===========
Traceback (most recent call last):
  File "C:\Users\lenovo\Desktop\Degree_FDP\sample.py", line 1, in <module>
    a = int(input(""))
KeyboardInterrupt
>>> 
=========== RESTART: C:\Users\lenovo\Desktop\Degree_FDP\sample.py ===========
Enter a value10
Enter a value50
Addition is: 60
Substration is: -40
Mul is: 500
Div is: 0.2
Floor Div: 0
pow is 100000000000000000000000000000000000000000000000000
Modules is: 10
>>> input("Enter a value")
	  
Enter a valueprasannaraj
'prasannaraj'
>>> input("Enter a value")
	  
Enter a value123
'123'
>>> int(input("enter Data"))
	  
enter Data
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    int(input("enter Data"))
ValueError: invalid literal for int() with base 10: ''

>>> 
	  
>>> 
	  
>>> x = [10,20,30,50,100]
	  
>>> x in 150
	  
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    x in 150
TypeError: argument of type 'int' is not iterable
>>> 150 in x
	  
False
>>> 100 in x
	  
True
>>> 100 not in x
	  
False
>>> 
