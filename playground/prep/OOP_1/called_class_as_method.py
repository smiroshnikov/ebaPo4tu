class CallMeAsFunction:
    def __call__(self, *args, **kwargs):
        print("called")


# example below - class called as a function
foo_instance = CallMeAsFunction()
foo_instance()
