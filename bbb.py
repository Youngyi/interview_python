def xx(*args):
    i = 2
    for ch in args:
        print(ch)

xx(1,2,3)

def yy(**kargs):
    for key, value in kargs.items():

        print(key,value)
        # print(value)

yy(t = 1, y = 2)