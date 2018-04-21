from app.shell import args
class Printer:
    def __init__(self, msg):
        self.msg = msg

    def my_print(self):
        print(self.msg)

@args('-q', '--query', metavar='<QUERY>')
@args('a',  default=100, help='a help')
@args('b',  default=200, help='b help')
def my_print(args):
    p = Printer("lijiancai a={}, b={}".format(args.a, args.b))
    p.my_print()