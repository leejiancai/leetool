class Printer:
    def __init__(self, msg):
        self.msg = msg

    def my_print(self):
        print(self.msg)


def my_print():
    p = Printer("lijiancai")
    p.my_print()