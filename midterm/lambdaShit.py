
#functions to access list
l_head = lambda l: l[0]
l_tail = lambda l: l[1:]

#operators
l_add = lambda x, y: x+y
l_mul = lambda x, y: x*y

l_list_desc = lambda n: [] if n == 0 else [n]+l_list_desc(n-1)
l_list_asc = lambda n: [] if n == 0 else l_list_asc(n-1)+[n]

l_repeat = lambda x, n: [] if n ==0 else [x]+l_repeat(x, n-1)

x = l_list_desc(10)
x = l_list_asc(10)
x = l_repeat('aa', 3)
print(x)