def divide(number):
	return number/2


print(divide(19))

my_list = [1,2,3,4,5,6]

for element in my_list:
	print(divide(element))

## MAP 

print(list(map(divide,my_list)))


def control_string(string):
	return "Emre" in string

print(control_string("Emre"))


my_artist_list = ["Emre","System of a down","ferdi tayfur"]

print(list(map(control_string,my_artist_list)))

### filter

print(list(filter(control_string,my_artist_list)))


### lambda

multiply = lambda number:number*3

print(multiply(6))

my_list_3 = [3,4,5,6]

print(list(map(lambda num:num*4,my_list_3)))