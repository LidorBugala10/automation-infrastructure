text = "hello world"
print(len(text))
text = "hello world"
print(text.upper())
text = "hello world"
print(text.lower())


word = "bananas"
print(word.count('a'))
word = "bananas"
print(word.index('n'))


massage = "i love python"
print(massage.replace('python', 'programming'))
massage = "i love python"
print(text.replace('o','0'))
massage = " i love programming"
print(massage.upper())

greeting = "hello"
name = "Alice"
print(greeting.replace('hello','hi'))
result = greeting +" "+ name
print(result)
print(greeting.upper() + " " + name.upper())


word = "python"
result = word [0].upper() + word[1:]
print(result)

word = "hello world"
second_word_start = word.find(' ')+1
print(word[second_word_start:])

price = "30$"
dollar_to_ils = 3.3
amount_usd = 30
amount_ils = amount_usd * dollar_to_ils
print("price",price)
print("dollar to ils rate",dollar_to_ils)
price = ('30 usd in ils',amount_ils)

age = "2000"
birth_year = 2022 - int(age)
print(birth_year)

my_list = ['shopping']
my_list.append('sales')
my_list.append('banana')
my_list.append('cherry')
print(my_list)

my_list = ['shopping']
my_list.insert(0 ,'banana')
print(my_list)
my_list.remove('banana')
print(my_list)
print(my_list)

my_list = ['shopping']
my_list.remove('sales')
print(my_list)

my_list = ['shopping']
print(len(my_list))
print(my_list)




