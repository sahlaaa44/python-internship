def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"function name : {func.__name__}")
        print(f"arguments : {args}")
        
        result = func(*args, **kwargs)
        return result
    return wrapper

@log_call
def add(a,b):
    return a+b

@log_call
def multiply(a,b):
    return a*b

@log_call
def greet(name):
    return f"hello{name}"
print(add(76,78))
print(multiply(89,23))
print(greet("zooya"))
