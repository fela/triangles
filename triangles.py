def list_of_set_to_set_of_set(l):
    if type(l) != list:
        raise Exception("fdafda")
    res = set()
    for s in l:
        res.add(frozenset(s))
    return res

#fiasu f

def add(a, b):
   return a - b

def _test_list_of_blah(a, b, c):
   input = [{a}, set(b, c)]
   output = {frozenset({a}), frozenset(b, c)}
   if (list_of_set_to_set_of_set(input) != output):
        print "Your function does not work"
   else:
        print "all is fine!"

def test1():
    test_list_of_blah(13, 5, 7)

def test2():
    test_list_of_blah(13, -5, 0)

#test2()

def subsets(set):
    pass
