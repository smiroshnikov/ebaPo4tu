calls = 0
def tracer(func):
    def wrapper(*args, **kwargs):
        global calls
        calls += 1
        print(f"call {calls} to {func.__name__}")
        return func(*args, **kwargs)
    # return wrapper()
    return wrapper


@tracer
def spam(a, b, c):  # same as : spam = tracer(spam)
    print(f"{a + b + c} inside spam")


@tracer
def eggs(x, y):
    print(f"{x ** y} inside eggs")


spam(a=1, b=2, c=3)
