def test(*args):
    def add(*args):
        return args
    return add(*args)

print test(1,2,3)