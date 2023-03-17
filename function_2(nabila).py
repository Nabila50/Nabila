
#1.
def name(firstname, lastname):
    print(firstname,'',lastname)
name('Nabila', 'Nawshin')

#2. eikhne lamisa and nawshin nam 1st and 2nd parameter e pre define kora cilo.
# ei jnno name() faka thakleo pre define er jnno print e lamisa nawshin asbe
def name(firstname='lamisa', lastname='nawshin'):
    print(firstname, lastname)
name()

#3. eikhne Ausma r roti pre define kora thakleo argument e UL deyar jnno vorname e ul asce..
#that means argument e jaitay thakbe oitay print hobe. tokn pre define jai thak na keno argument tay print hbe
def name3(vorname ='Ausma', nachname= 'Roti'):
    print(vorname, nachname)
name3('ul', )

#4 eikhne jehetu parameter 3 ta so addition e argument e 3 ta value dite hbe. otherwise code error asbe
def addition(num1, num2, num3):
    total= num1+num2+num3
    print(total)
addition(25, 14, 1)

#5.
def addition(num1, num2):
    print(num1 + num2)
addition(num1=2, num2= 10)

# 6. Arbitrary Argument: eita k * sign diye prokash kora hoi. In programming language * this sign is called as asterise.
def summation(*numbers):
    print(numbers)
summation(25, 15, 85, 49, 76, 18, 2.48)

# 7.Keyword Argument: it is defined with 2* sign like **
def multi(**data):
    print(f"Her name is {data['name']} and she is {data['age']} years old and she is a {data['profession']}") # eikhne double code ("") use krte hbe.
multi(name='nabila', age='31', profession='student')

# 8.
def addition(num1, num2):
    return num1 + num2
print(addition(12, 10))
# 9.

def addition(num1, num2):
    return num1+num2
result = addition(20,10)/2
print(result)


