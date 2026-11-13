def check_prime(x):
  for i in range(2,x):
    if x % i == 0:
      return 0
  else:
    return 1

print('Checking for 10',check_prime(10))
print('Checking for 13',check_prime(13))

def first_N_primes(N):
    x = 2
    count_primes = 0
    primes = []
    while count_primes < N :
        for i in range(2,x):
            if x % i == 0:
                break
        else:
            count_primes +=1
            primes.append(x)
        x +=1
    return primes

print('First Ten Prime numbers are :',first_N_primes(10))

def check_palindrome(x):
    if str(x) == str(x)[::-1]:
        return f"{x} is Palindrome"
    else:
        return f"{x} is Not Palindrome"


class Employees:
    def __init__(self, name, employee_id, position, salary, department):
        self.name = name
        self.employee_id = employee_id
        self.position = position
        self.salary = salary
        self.department = department

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Position: {self.position}")
        print(f"Salary: ${self.salary}")
        print(f"Department: {self.department}")

    def calculate_annual_salary(self):
        return print(f"Annual Salary of {self.name} is : {self.salary * 12}")

e1 = Employees('Elvis','E001','Project Lead',500000,'IT')
e2 = Employees('Carla','E002','Project Manager',750000,'Marketing')


grocery_list=['Desserts','Shopping Bags','Soft Cheese','Bottled Water','Oranges','Tomatoes','Milk ',
'Canned Meat','Apples','Cheese Popcorn','Dry Mix','Brown Rice','Rolls Buns','Oregano',
'Butter','Oil','Potato Chips','Brown Bread','Meat','Noodles','Pastry','Yogurt','Cookies',
'Ham','Tea','Pip Fruit','Pretzels','Sliced Cheese','Fruit Juice','Lettuce','Napkins',
'White Bread','Cottage Cheese','Poultry','Oats','Rice','Paper Plates','Eggs',
'Chocolate Marshmallow','Bananas','Butter Milk','Chewing Gum','Chocolate','Curd',
'Coffee','Juice','Sausage','Ice Cream','Water','Whole Milk']


word_index_dict = {
 'a': 1, 'acting': 2, 'again': 3, 'and': 4, 'art': 5, 'breathtaking': 6,
 'brilliant': 7, 'but': 8, 'captivating': 9, 'character': 10, 'cinematography': 11,
 'could': 12, 'development': 13, 'dialogue': 14, 'direction': 15, 'disappointing': 16,
 'execution': 17, 'experience': 18, 'fantastic': 19, 'film': 20, 'for': 21,
 'good': 22, 'great': 23, 'had': 24, 'haunting': 25, 'highly': 26, 'impression': 27,
 'impressive': 28, 'incredible': 29, 'its': 30, 'left': 31, 'masterful': 32,
 'me': 33, 'mediocre': 34, 'memorable': 35, 'moments': 36, 'money': 37,
 'movie': 38, 'not': 39, 'of': 40, 'overall': 41, 'performances': 42,
 'piece': 43, 'plot': 44, 'quality': 45, 'recommended': 46, 'remarkable': 47,
 'somewhat': 48, 'speechless': 49, 'superb': 50, 'the': 51, 'thus': 52,
 'to': 53, 'visuals': 54, 'was': 55, 'waste': 56, 'watch': 57, 'weak': 58,
 'were': 59, 'with': 60}
