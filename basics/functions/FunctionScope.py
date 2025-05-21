#Local variables are only accessible within the function they are defined in.
def my_function():
    local_variable = 10
    print(local_variable)

global_variable = 20

def my_global_function(a):
    num = global_variable + 10+a
    print(num)
my_global_function(100)




