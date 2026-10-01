import mymodule
import mymodule as mm

print('1) mymodule circle_area(5) = ', mymodule.circle_area(5))
print('4) mm.PI =', mm.PI)

print('dir(mymodule) ->', [n for n in dir(mymodule) if not n.startswith('  ')])
print('mymodule.__name__=', mymodule.__name__)
print('mymodule.__file__=', mymodule.__file__)
print('mm._helper() =', mm._helper())


