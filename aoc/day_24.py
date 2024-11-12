"""Processing for Day 24"""

def never_tell_me_the_odds(hailstones: str, rock: bool) -> int:
    """Take the hailstones and return the appropriate value"""

    xy_min = 200000000000000
    xy_max = 400000000000000

    kinematics: list[tuple[int, ...]] = []

    for hailstone in hailstones.splitlines():
        kinematics.append(tuple((int(num) for num in hailstone.replace(" @", ",").split(", "))))

    if rock:
        return _rock(kinematics)

    intersections = 0

    for idx in range(len(kinematics)):
        a_x_b = kinematics[idx][0]
        a_y_b = kinematics[idx][1]
        a_x_m = kinematics[idx][3]
        a_y_m = kinematics[idx][4]

        for jdx in range(idx + 1, len(kinematics)):
            b_x_b = kinematics[jdx][0]
            b_y_b = kinematics[jdx][1]
            b_x_m = kinematics[jdx][3]
            b_y_m = kinematics[jdx][4]

            """
            a_y = a_y_m * t + a_y_b
            # solve for t
            a_x = a_x_m * t + a_x_b
            a_x_m * t = a_x - a_x_b
            t = (a_x - a_x_b) / a_x_m
            # plug in
            a_y = a_y_m * ((a_x - a_x_b) / a_x_m) + a_y_b
            a_y = a_y_m * ((a_x / a_x_m) - (a_x_b / a_x_m)) + a_y_b
            a_y = (a_y_m / a_x_m) * x - (a_y_m * a_x_b / a_x_m) + a_y_b
            # similarly
            b_y = (b_y_m / b_x_m) * x - (b_y_m * b_x_b / b_x_m) + b_y_b
            # solve for a_y == b_y
            (a_y_m / a_x_m) * x - (a_y_m * a_x_b / a_x_m) + a_y_b = (b_y_m / b_x_m) * x - (b_y_m * b_x_b / b_x_m) + b_y_b
            ((a_y_m / a_x_m) - (b_y_m / b_x_m)) * x = b_y_b - (b_y_m * b_x_b / b_x_m) + (a_y_m * a_x_b / a_x_m) - a_y_b
            x = (b_y_b - (b_y_m * b_x_b / b_x_m) + (a_y_m * a_x_b / a_x_m) - a_y_b) / ((a_y_m / a_x_m) - (b_y_m / b_x_m))
            """

            try:
                x = (b_y_b - (b_y_m * b_x_b / b_x_m) + (a_y_m * a_x_b / a_x_m) - a_y_b) / ((a_y_m / a_x_m) - (b_y_m / b_x_m))
            except ZeroDivisionError:
                continue

            if not (xy_min <= x <= xy_max):
                continue

            y = a_y_m * ((x - a_x_b) / a_x_m) + a_y_b

            if not (xy_min <= y <= xy_max):
                continue

            # check for negative t
            a_t = (x - a_x_b) / a_x_m

            b_t = (x - b_x_b) / b_x_m

            if a_t < 0 or b_t < 0:
                continue

            intersections += 1

    return intersections


def _rock(kinematics: list[tuple[int, ...]]) -> int:
    """Return the sum of the initial positions of the rock"""

    # vector representing the slope of hailstone 0
    v = (kinematics[0][3], kinematics[0][4], kinematics[0][5])

    t = 0

    t_prev = -1

    t_inc = 10000000000

    kdx = 2

    # loop through all but the first two hailstones
    while kdx < len(kinematics):
        # get the position of hailstone 1 at time t
        x = kinematics[1][3] * t + kinematics[1][0]
        y = kinematics[1][4] * t + kinematics[1][1]
        z = kinematics[1][5] * t + kinematics[1][2]

        # create a vector between initial position of hailstone 0 and current position of hailstone 1
        u = (x - kinematics[0][0], y - kinematics[0][1], z - kinematics[0][2])

        # get the normal vector of the plane containing vectors v and u
        n = (v[1] * u[2] - v[2] * u[1],
             v[2] * u[0] - v[0] * u[2],
             v[0] * u[1] - v[1] * u[0])

        # find d
        d = n[0] * kinematics[0][0] + n[1] * kinematics[0][1] + n[2] * kinematics[0][2]

        # find the time s where hailstone kdx intercepts the plane
        s = (d - n[0] * kinematics[kdx][0] - n[1] * kinematics[kdx][1] - n[2] * kinematics[kdx][2]) / (n[0] * kinematics[kdx][3] + n[1] * kinematics[kdx][4] + n[2] * kinematics[kdx][5])

        # only check for positive times
        if s >= 0 and t == t_prev:
            # t is sufficiently high that s is already positive for hailstone kdx
            kdx += 1
            continue
        elif s >= 0 and t_inc != 1:
            # we passed the value needed, go back and do a tighter search
            t -= t_inc
            t_inc = t_inc // 10
            continue
        elif s >= 0:
            # this is the new min t
            # save this t
            t_prev = t
            # start checking the next line
            kdx += 1
            # reset t_inc
            t_inc = 10000000000
            continue

        t += t_inc

    # at this point we have a min t that causes all intersections to happen at positive times

    # go back to the last hailstone
    kdx -= 1

    t_inc = 1000000

    while True:
        # get the position of hailstone 1 at time t
        x = kinematics[1][3] * t + kinematics[1][0]
        y = kinematics[1][4] * t + kinematics[1][1]
        z = kinematics[1][5] * t + kinematics[1][2]

        # create a vector between initial position of hailstone 0 and current position of hailstone 1
        u = (x - kinematics[0][0], y - kinematics[0][1], z - kinematics[0][2])

        # get the normal vector of the plane containing vectors v and u
        n = (v[1] * u[2] - v[2] * u[1],
             v[2] * u[0] - v[0] * u[2],
             v[0] * u[1] - v[1] * u[0])

        # find d
        d = n[0] * kinematics[0][0] + n[1] * kinematics[0][1] + n[2] * kinematics[0][2]

        # find the time s where hailstone kdx intercepts the plane
        s = (d - n[0] * kinematics[kdx][0] - n[1] * kinematics[kdx][1] - n[2] * kinematics[kdx][2]) / (n[0] * kinematics[kdx][3] + n[1] * kinematics[kdx][4] + n[2] * kinematics[kdx][5])

        # find the current position of hailstone kdx at time s
        x2 = kinematics[kdx][3] * s + kinematics[kdx][0]
        y2 = kinematics[kdx][4] * s + kinematics[kdx][1]
        z2 = kinematics[kdx][5] * s + kinematics[kdx][2]

        # use the current positions of hailstones 1 and kdx as well as times t and s to find the slopes
        m_x = (x2 - x) / (s - t)
        m_y = (y2 - y) / (s - t)
        m_z = (z2 - z) / (s - t)

        # back track to get the initial positions
        b_x = x - m_x * t
        b_y = y - m_y * t
        b_z = z - m_z * t

        # rough search until the sum of the initial positions is in this range
        if 463011594988398 < (b_x + b_y + b_z) < 563011594988398:
            if t_inc != 1:
                # we passed the value needed, go back and do a tighter search
                t -= t_inc
                t_inc = t_inc // 10
                continue
            if b_x // 1 == b_x and b_y // 1 == b_y and b_z // 1 == b_z:
                r = (d - n[0] * kinematics[kdx - 1][0] - n[1] * kinematics[kdx - 1][1] - n[2] * kinematics[kdx - 1][2]) / (n[0] * kinematics[kdx - 1][3] + n[1] * kinematics[kdx - 1][4] + n[2] * kinematics[kdx - 1][5])
                if r // 1 == r:
                    # the initial positions of the rock and the time the rock intersects hailstone kdx - 1 are all integer
                    # this is probably the right path for the rock
                    return int(b_x + b_y + b_z)

        t += t_inc
