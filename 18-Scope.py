#### LEGB
### L -> Local
### E -> Enclosing
### G -> Global
### B -> Built-in


my_string = "Emre"

def my_func():
	my_string = "Emre"

def my_func2():
	my_string = "Alkaya"
	print(my_string)

my_func2()

print(my_func)


y = 10

def func_new():
	global y
	y = 6
	return y

y = 10
print(func_new())

