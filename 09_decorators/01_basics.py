from functools import wraps
def mydecorator(func):
    @wraps(func)
    def wrapper():
        print("before function runs")
        func()
        print("after function runs")
    return wrapper

@mydecorator
#decorator basically ek function ko leta hai aur usme kuch extra functionality add karta hai bina us function ke code ko modify kiye.
# yaha pe greet function is decorator ka argument hai, aur mydecorator function greet function ko wrap karta hai wrapper function ke andar, jisme humne extra functionality add ki hai.
def greet():
    print("hello from decorators class from chai code")

greet()
print(greet.__name__) #output: greet, because functools.wraps preserves the original function's name and metadata.