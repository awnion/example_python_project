@lambda cls: cls()
class mega_print:
    def __call__(self, *args, **kwds):
        if args or kwds:
            print(*args, **kwds)
        return self


mega_print()()()()()("hm... 🤔")

G = 1


class If:
    """🏴‍☠️"""

    if G > 0:  # 🤔

        def a(self):
            print(1)

    else:

        def b(self):
            print(2)


G = -1

If().a()
If().b()
