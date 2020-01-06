import time
import threading
from computer import Computer


def foo():
    for i in range(3):
        print(f'foo {i}')
        pass
        time.sleep(2)


def bar():
    for i in range(5):
        print(f'bar {i}')
        time.sleep(1)


A = threading.Thread(target=foo)
B = threading.Thread(target=bar)

threads = [A, B]
for thread in threads:
    thread.start()

a = Computer([99], [12])
b = Computer([99], [5])
print(b.inputs)
b.inputs = a.outputs
print(b.inputs)
a.output(30)
print(b.inputs)
a.output(40)
print(b.inputs)
