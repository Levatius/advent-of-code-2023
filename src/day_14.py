from numpy import array, rot90


def calc_load(dish):
    return sum(sum(len(items) - i for i, item in enumerate(items) if item == "O") for items in dish)


def tilt(dish):
    tilted_dish = []
    for items in dish:
        pos = 0
        tilted_items = [item if item != "O" else "." for item in items]
        for i, item in enumerate(items):
            match item:
                case ".":
                    continue
                case "#":
                    pos = i + 1
                case "O":
                    tilted_items[pos] = item
                    pos += 1
        tilted_dish.append(tilted_items)
    return array(tilted_dish)


def part_1(dish):
    dish_rotated_north = rot90(dish, k=1)
    dish_tilted_north = tilt(dish_rotated_north)
    return calc_load(dish_tilted_north)


def part_2(dish, total_cycles=1_000_000_000):
    # Start at Eastern rotation
    dish = rot90(dish, k=2)

    seen_patterns = {}
    cycle_start = 0
    cycle_length = 1

    for cycle in range(1, total_cycles + 1):
        for _ in range(4):
            dish = rot90(dish, k=-1)
            dish = tilt(dish)

        pattern = "".join("".join(items) for items in dish)
        if pattern in seen_patterns:
            cycle_start, _ = seen_patterns[pattern]
            cycle_length = cycle - cycle_start
            break
        dish_load_north = calc_load(rot90(dish, k=-1))
        seen_patterns[pattern] = cycle, dish_load_north

    fast_forward_multiplier = (total_cycles - cycle_start) // cycle_length
    target_cycle = total_cycles - cycle_length * fast_forward_multiplier
    dish_load_north = next(load for cycle, load in seen_patterns.values() if cycle == target_cycle)
    return dish_load_north
