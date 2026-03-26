from functools import wraps
def logactivity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"finished {func.__name__}")
        return result
    return wrapper

@logactivity
def brew_chai(type, milk="no"):
    print(f"brewing {type} chai")
    print(f"milk status {milk}")

brew_chai("masala", milk="yes")
#yaha pe decorator function kon sa hai?Yaha pe decorator function `logactivity` hai.
# aur brew chai function ko decorate kar raha hai. Jab brew_chai function call hota hai, to pehle logactivity ka wrapper function execute hota hai, jo function ke naam aur return value ko print karta hai.
# brew chai basically function hai jispe hm logactivity decorator apply kar rahe hain. Jab brew_chai function call hota hai, to pehle logactivity ka wrapper function execute hota hai, jo function ke naam aur return value ko print karta hai. Is tarah se humne brew_chai function ko logactivity decorator ke through modify kiya hai, jisse hume function ke execution ke baare mein information milti hai.