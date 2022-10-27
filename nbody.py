# Taken from:
# The Computer Language Benchmarks Game
# https://salsa.debian.org/benchmarksgame-team/benchmarksgame/
#
# originally by Kevin Carson
# modified by Tupteq, Fredrik Johansson, and Daniel Nanz
# modified by Maciej Fijalkowski
# 2to3
# modified by Andriy Misyura
# slightly modified by bmmeijers

import sys
from math import sqrt, pi as PI
import time


def combinations(l):
    result = []
    for x in range(len(l) - 1):
        ls = l[x + 1:]
        for y in ls:
            result.append((l[x][0], l[x][1], l[x][2], y[0], y[1], y[2]))
    return result


SOLAR_MASS = 4 * PI * PI
DAYS_PER_YEAR = 365.24

BODIES = {
    "sun": ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0], SOLAR_MASS),
    "jupiter": (
        [4.84143144246472090e00, -1.16032004402742839e00, -1.03622044471123109e-01],
        [
            1.66007664274403694e-03 * DAYS_PER_YEAR,
            7.69901118419740425e-03 * DAYS_PER_YEAR,
            -6.90460016972063023e-05 * DAYS_PER_YEAR,
        ],
        9.54791938424326609e-04 * SOLAR_MASS,
    ),
    "saturn": (
        [8.34336671824457987e00, 4.12479856412430479e00, -4.03523417114321381e-01],
        [
            -2.76742510726862411e-03 * DAYS_PER_YEAR,
            4.99852801234917238e-03 * DAYS_PER_YEAR,
            2.30417297573763929e-05 * DAYS_PER_YEAR,
        ],
        2.85885980666130812e-04 * SOLAR_MASS,
    ),
    "uranus": (
        [1.28943695621391310e01, -1.51111514016986312e01, -2.23307578892655734e-01],
        [
            2.96460137564761618e-03 * DAYS_PER_YEAR,
            2.37847173959480950e-03 * DAYS_PER_YEAR,
            -2.96589568540237556e-05 * DAYS_PER_YEAR,
        ],
        4.36624404335156298e-05 * SOLAR_MASS,
    ),
    "neptune": (
        [1.53796971148509165e01, -2.59193146099879641e01, 1.79258772950371181e-01],
        [
            2.68067772490389322e-03 * DAYS_PER_YEAR,
            1.62824170038242295e-03 * DAYS_PER_YEAR,
            -9.51592254519715870e-05 * DAYS_PER_YEAR,
        ],
        5.15138902046611451e-05 * SOLAR_MASS,
    ),
}

SYSTEM = tuple(BODIES.values())
PAIRS = tuple(combinations(SYSTEM))


def advance(dt, bodies=SYSTEM, pairs=PAIRS):
    for ([x1, y1, z1], v1, m1, [x2, y2, z2], v2, m2) in pairs:
        dx = x1 - x2
        dy = y1 - y2
        dz = z1 - z2
        dist = sqrt(dx * dx + dy * dy + dz * dz)
        mag = dt / (dist * dist * dist)
        b1m = m1 * mag
        b2m = m2 * mag
        v1[0] -= dx * b2m
        v1[1] -= dy * b2m
        v1[2] -= dz * b2m
        v2[2] += dz * b1m
        v2[1] += dy * b1m
        v2[0] += dx * b1m
    for (r, [vx, vy, vz], m) in bodies:
        r[0] += dt * vx
        r[1] += dt * vy
        r[2] += dt * vz


def report_energy(bodies=SYSTEM, pairs=PAIRS, e=0.0):
    for ((x1, y1, z1), v1, m1, (x2, y2, z2), v2, m2) in pairs:
        dx = x1 - x2
        dy = y1 - y2
        dz = z1 - z2
        e -= (m1 * m2) / ((dx * dx + dy * dy + dz * dz) ** 0.5)
    for (r, [vx, vy, vz], m) in bodies:
        e += m * (vx * vx + vy * vy + vz * vz) / 2.0
    print("Energy: %.9f" % e)


def offset_momentum(ref, bodies=SYSTEM, px=0.0, py=0.0, pz=0.0):
    for (r, [vx, vy, vz], m) in bodies:
        px -= vx * m
        py -= vy * m
        pz -= vz * m
    (r, v, m) = ref
    v[0] = px / m
    v[1] = py / m
    v[2] = pz / m


def main(n, file_nm="python_positions.csv", ref="sun", out=False):
    offset_momentum(BODIES[ref])
    report_energy()
    if out:     # use a boolean to control write file or not
        with open(file_nm, "w") as fh:      # write with descriptive column names
            fh.write('{},{},{},{},{}\n'.format('steps', 'name of the body', 'position_x', 'position_y', 'position_z'))
            name_list = list(BODIES.keys())
            for i in range(n):
                advance(0.01)
                for j in range(5):
                    fh.write('{};{};{:.9f};{:.9f};{:.9f}\n'.format(i, name_list[j], SYSTEM[j][0][0], SYSTEM[j][0][1],SYSTEM[j][0][2]))
    else:
        for i in range(n):
            advance(0.01)
    report_energy()


if __name__ == "__main__":
    iteration_number=['5000','500000','5000000','50000000']
    sys.argv.extend(iteration_number)    # extend list
    # automatically run 4 times with different number
    if len(sys.argv) >= 2:
        for j in range(len(sys.argv)-1):
            start = time.perf_counter()     # time start
            main(int(sys.argv[j+1]))
            end = time.perf_counter()       # time end
            print('The number of this iteration is', int(sys.argv[j+1]))
            print('This program spends', "%.2f" % ((end-start)*1000), 'ms')
        sys.exit(0)
    else:
        print(f"This is {sys.argv[0]}")
        print("Call this program with two arguments")
        print("(an integer as the number of iterations for the n-body simulation and an string as output filename).")
        sys.exit(1)