



def calculator(num1,num2,operation):
	if operation not in "+-/*":
		return "Choose operator: '+,-,*,/'!"

	if operation == "+":
		return num1+num2
	if operation == "-":
		return num1-num2
	if operation == "*":
		return num1*num2
	if operation == "/":
		return num1/num2

while True:

	num1 = int(input("Enter first number: "))
	num2 = int(input("Enter second number: "))
	operation = input("Choose between +, -, *, / ")

	print(calculator(num1, num2, operation))