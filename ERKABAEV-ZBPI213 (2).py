def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1) 
    pass

def filter_even(li):
    return list(filter(lambda x : x % 2 == 0, li))
    pass

def square(li):
    return list(map(lambda x: x**2, li))
    pass

def bin_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

def is_palindrome(string):
    start = 0
    end = len(string) - 1
    while start < end:
        while not string[start].isalpha():
            start = start + 1
        while not string[end].isalpha():
            end = end - 1
        if string[start].lower() != string[end].lower():
            print('NO')
            return
        start = start + 1
        end = end - 1
    print('YES')
    pass

def calculate(path2file):
    operations = {
        '+' : lambda x,y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '//': lambda x, y: x // y,
        '%': lambda x, y: x % y,
        '**': lambda x, y: x ** y,
    }
    results = []
    with open(path2file, encoding='utf-8') as text:
        for line in text:
            words = line.split()
            results.append(str(operations[words[0]](int(words[1]), int(words[2]))))
        return ','.join(results)
    pass

def substring_slice(file1, file2):
    words = []
    result = ''
    i = 0
    with open(file1, encoding='utf-8') as text:
        for line in text:
            words.append(line.split())
    with open(file2, encoding='utf-8') as numbers:
        for line in numbers:
            nums = line.split()
            result += (str(words[i]))[int(nums[0])+2:int(nums[1])+3] + ' '
            i += 1
    return result.strip()
    pass

import json
def decode_ch(string_of_elements):
    result = ''
    L = []
    with open('periodic_table.json', 'r', encoding='utf-8') as f:
        text = json.load(f) 
    for i in range(1,len(string_of_elements)):
        j = i - 1
        if string_of_elements[j].islower():
            continue

        if string_of_elements[j].isupper() and string_of_elements[i].isupper():
            L.append(string_of_elements[j])
        else:
            if i == len(string_of_elements)-1 and string_of_elements[i].isupper():
                L.append(string_of_elements[i])
                break    
            L.append(string_of_elements[j]+string_of_elements[i])

    for c in L:
        for txt in text:
            if c == txt:
                result += text[txt]
    return result
    pass

class Student:
    def __init__(self, name, surname, grades = []):
        self.name = name
        self.surname = surname
        self.fullname = name + ' ' + surname
        self.grades = grades

    def mean_grade(self):
        return sum(self.grades) / len(self.grades) if len(self.grades) > 0 else 0

    def is_otlichnik(self):
        return 'YES' if self.mean_grade() >= 4.5 else 'NO'

    def greeting(self):
        return 'Hello, I am Student'

    def __add__(self, other: 'Student'):
        return self.name + ' is friends with ' + other.name

    def __str__(self):
        return self.fullname
    pass

class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg
        
    def __str__(self):
        return self.msg
