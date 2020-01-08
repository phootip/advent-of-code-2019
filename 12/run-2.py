import math
f = open('example1.txt')
f = open('example2.txt')
f = open('input.txt')


class Moon():
    def __init__(self, pos, moons):
        self.x, self.y, self.z = self.init_x, self.init_y, self.init_z = pos
        self.v_x = self.v_y = self.v_z = 0
        self.moons = moons

    def move(self):
        self.x += self.v_x
        self.y += self.v_y
        self.z += self.v_z

    def cal_v(self):
        for moon in self.moons:
            if moon != self:
                self.v_x += 0 if moon.x == self.x else (
                    moon.x - self.x) // abs(moon.x - self.x)
                self.v_y += 0 if moon.y == self.y else (
                    moon.y - self.y) // abs(moon.y - self.y)
                self.v_z += 0 if moon.z == self.z else (
                    moon.z - self.z) // abs(moon.z - self.z)

    def energy(self):
        pot = sum(list(map(abs, [self.x, self.y, self.z])))
        kin = sum(list(map(abs, [self.v_x, self.v_y, self.v_z])))
        return pot*kin

    def __str__(self):
        return f'pos<{self.x},{self.y},{self.z}>, vel<{self.v_x},{self.v_y},{self.v_z}>'

    def check_x(self):
        return self.init_x == self.x and self.v_x == 0

    def check_y(self):
        return self.init_y == self.y and self.v_y == 0

    def check_z(self):
        return self.init_z == self.z and self.v_z == 0


def total_e():
    ans = 0
    for moon in moons:
        ans += moon.energy()
    return ans


moons = []
for line in f:
    pos = line.strip()[1:-1]
    pos = pos.split(',')
    pos = [int(i.split('=')[1]) for i in pos]
    moons.append(Moon(pos, moons))

[print(moon) for moon in moons]
print()
mem = set()
c = ans_x = ans_y = ans_z = 0
while True:
    c += 1
    for moon in moons:
        moon.cal_v()
    for moon in moons:
        moon.move()
    if not ans_x:
        ans_x = c if all((moon.check_x() for moon in moons)) else 0
    if not ans_y:
        ans_y = c if all((moon.check_y() for moon in moons)) else 0
    if not ans_z:
        ans_z = c if all((moon.check_z() for moon in moons)) else 0
    print(c)
    if ans_x and ans_y and ans_z:
        break


[print(moon) for moon in moons]

print(f'ans_x: {ans_x}, ans_y: {ans_y}, ans_z: {ans_z}')


def get_lcm(x, y):
    return x*y//math.gcd(x, y)


lcm = get_lcm(ans_x, get_lcm(ans_y, ans_z))
print(lcm)
