
def print_result(fn):
    def inside(*args):
        print(fn.__name__)
        if len(args) == 0:
            fun = fn()
        else:
            fun = fn(args[0])
        if type(fun) == list:
            for i in fun:
                print(i)
        elif type(fun) == dict:
            for i in fun:
                print(i, "=", fun[i])
        else:
            print(fun)
    return inside
