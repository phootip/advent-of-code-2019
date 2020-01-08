# f = open('example1.txt')
# f = open('example2.txt')
f = open('input.txt')


class Moon():
    def __init__(self, pos, moons):
        self.x, self.y, self.z = pos
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


moons = []
for line in f:
    pos = line.strip()[1:-1]
    pos = pos.split(',')
    pos = [int(i.split('=')[1]) for i in pos]
    moons.append(Moon(pos, moons))

[print(moon) for moon in moons]
print()
for i in range(1000):
    for moon in moons:
        moon.cal_v()
    for moon in moons:
        moon.move()
[print(moon) for moon in moons]
ans = 0
for moon in moons:
    ans += moon.energy()
print(ans)
