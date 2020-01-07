import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "example.txt"
abs_file_path = os.path.join(script_dir, rel_path)
a = 3
b = 4
c = [a, b]
c[0] = 5
print(c)
print(a)

f = open(abs_file_path)
print(f.readline())
