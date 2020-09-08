def func(new_func):
	print("func started")
	new_func()
	print("func ended")

def hello_func():
	print("hello world")


func(hello_func)



def new_func():
	print("new func")
	def new_func_2():
		print("new func 2")
	return new_func_2


string_new = new_func()
string_new()


def decorator_function (func):
	def wrapper_function():
		print("wrapper started")
		func()
		print("wrapper stopped")
	return wrapper_function

def func_new():
	print("hello")

decorator_function(func_new)

@decorator_function
def func_new():
    print("hello world")

func_new()