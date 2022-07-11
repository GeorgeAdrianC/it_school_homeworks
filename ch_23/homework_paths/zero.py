import os
from pathlib import Path

# Find zero.txt
zero_path = Path("./zero.txt")
print(zero_path, zero_path.exists())
print(os.path.abspath(zero_path))

# Find one.txt
one_path = Path("./one/oneone/oneoneone/one.txt")
print(one_path, one_path.exists())
print(os.path.abspath(one_path))

# Find two.txt
two_path = Path("./two/twotwo/two.txt")
print(two_path, two_path.exists())
print(os.path.abspath(two_path))

# Find three.txt
three_path = Path("./three/three.txt")
print(three_path, three_path.exists())
print(os.path.abspath(three_path))

# Find one.txt recursively
one_root_path = Path("./one")
one_path = list(one_root_path.rglob("one.txt"))[0]
print(one_path, one_path.exists())
print(os.path.abspath(one_path))
