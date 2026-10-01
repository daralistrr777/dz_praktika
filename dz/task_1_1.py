import sys

print('versia pythona:', sys.version.split()[0])
print('interpretator:', sys.executable)

print('kolichestvo putey poiska:', len(sys.path))
for p in sys.path[:4]:
  print('  ', p)

import math, random

print("math.pi =", math.pi)
print('random.random()= ', random.random())

mods = sorted(sys.modules)
print('vsego zagruzheno moduley:', len(mods))
print('primer:', mods[:5])

public = [n for n in dir(math) if not n.startswith(('__'))]
print('publichnie imena v math:', len(public))
print('pervie 8:', public[:8])

print("мой __name__=", __name__)
print('file', __file__)