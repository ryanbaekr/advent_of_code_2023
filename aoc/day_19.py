"""Processing for Day 19"""

def aplenty(workflows: str) -> int:
    """Take the workflows and return the appropriate value"""

    workflows, ratings = workflows.split("\n\n")

    workflows = workflows.splitlines()
    ratings = ratings.splitlines()

    workflow_map = {
        "A": True,
        "R": False,
    }

    for workflow in workflows:
        name, steps = workflow.rstrip("}").split("{")
        workflow_map[name] = steps

    accepted = 0

    for rating in ratings:
        x, m, a, s = eval(rating.replace("{", "(").replace("}", ")").replace("x", "").replace("m", "").replace("a", "").replace("s", "").replace("=", ""))

        name = "in"

        while isinstance(workflow_map[name], str):
            for step in workflow_map[name].split(","):
                if ":" in step:
                    condition, next_name = step.split(":")
                    if eval(condition):
                        name = next_name
                        break
                else:
                    name = step
                    break

        if workflow_map[name]:
            accepted += x + m + a + s

    # TODO part 2, pass the bounds to in and then split the bounds, keep splitting the bounds at each step and when all conditions get to A or R we can count

    queue = [(1, 4000, 1, 4000, 1, 4000, 1, 4000, "in")]

    distinct = 0

    while queue:
        x_min, x_max, m_min, m_max, a_min, a_max, s_min, s_max, name = queue[-1]
        queue = queue[:-1]

        if not isinstance(workflow_map[name], str):
            if workflow_map[name]:
                distinct += (x_max - x_min + 1) * (m_max - m_min + 1) * (a_max - a_min + 1) * (s_max - s_min + 1)
            continue

        # ongoing values
        range_map = {
            "x_min": x_min,
            "x_max": x_max,
            "m_min": m_min,
            "m_max": m_max,
            "a_min": a_min,
            "a_max": a_max,
            "s_min": s_min,
            "s_max": s_max,
        }

        for step in workflow_map[name].split(","):
            if ":" in step:
                condition, next_name = step.split(":")
                condition = condition.replace(">", "_max>").replace("<", "_min<")
                if eval(condition):
                    temp_map = range_map.copy()
                    if ">" in condition:
                        var, num = condition.split(">")
                        num = int(num)
                        temp_map[var.replace("_max", "_min")] = num + 1
                        range_map[var] = num
                        queue.append(tuple(list(temp_map.values()) + [next_name]))
                    elif "<" in condition:
                        var, num = condition.split("<")
                        num = int(num)
                        temp_map[var.replace("_min", "_max")] = num - 1
                        range_map[var] = num
                        queue.append(tuple(list(temp_map.values()) + [next_name]))
            else:
                queue.append(tuple(list(range_map.values()) + [step]))

    return accepted, distinct
