
def print_result(fn):
    def inside():
        print(fn.__name__)
        fun = fn()
        if type(fun) == list:
            for i in fun:
                print(i)
        elif type(fun) == dict:
            for i in fun:
                print(i, "=", fun[i])
        else:
            print(fun)
    return inside
