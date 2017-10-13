from ida_kernwin import Choose


class MyChoose(Choose):

    def __init__(self, title, nb = 5):
        Choose.__init__(
            self,
            title,
            [ ["Bit", Choose.CHCOL_HEX | 10] ],
            flags = Choose.CH_MULTI)
        self.items = [ str(1 << x) for x in xrange(nb) ]

    def OnGetSize(self):
        return len(self.items)

    def OnGetLine(self, n):
        return [self.items[n]]

    def OnSelectLine(self, n):
        self.deflt = n  # save current selection
        return (Choose.NOTHING_CHANGED, )

    def show(self, num):
        self.deflt = [x
                      for x in xrange(len(self.items))
                      if (num & (1 << x)) != 0]
        if self.Show(True) < 0:
            return 0
        return sum([(1 << x) for x in self.deflt])


# -----------------------------------------------------------------------
def test_choose(num):
    c = MyChoose("Choose - sample 2", nb = 5)
    return c.show(num)

# -----------------------------------------------------------------------
if __name__ == '__main__':
    print test_choose(11)
