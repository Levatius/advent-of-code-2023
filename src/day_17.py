import math
from queue import PriorityQueue

from numpy import array, ndenumerate

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def get_neighbours(current_index, unvisited, min_range):
    current_pos, current_step, current_direction = current_index

    for new_direction in DIRECTIONS:
        if current_direction:
            # Constraint: Not allowed to reverse
            if new_direction == tuple(-array(current_direction)):
                continue
            # Constraint: If minimum range is specified, not allowed to turn until it is met
            if min_range and current_direction != new_direction and current_step < min_range:
                continue

        new_pos = tuple(array(current_pos) + array(new_direction))
        new_step = current_step + 1 if new_direction == current_direction else 1
        if (new_index := (new_pos, new_step, new_direction)) in unvisited:
            yield new_index


def dijkstra(heatmap, start, min_range, max_range):
    distances = {}
    unvisited = set()
    queue = PriorityQueue()

    # Add start node
    distances[start] = 0
    unvisited.add(start)
    queue.put((0, start))
    # Add all other nodes
    for pos, heat_loss in ndenumerate(heatmap):
        for step in range(1, max_range + 1):
            for direction in DIRECTIONS:
                index = (pos, step, direction)
                distances[index] = math.inf
                unvisited.add(index)
                queue.put((math.inf, index))

    while unvisited:
        current_distance, current_index = queue.get()
        if current_index in unvisited:
            unvisited.remove(current_index)

        for neighbour_index in get_neighbours(current_index, unvisited, min_range):
            distance = current_distance + heatmap[neighbour_index[0]]
            if distance < distances[neighbour_index]:
                distances[neighbour_index] = distance
                queue.put((distance, neighbour_index))
    return distances


def part_x(heatmap, min_range=None, max_range=3):
    start = ((0, 0), 0, None)
    target = (heatmap.shape[0] - 1, heatmap.shape[1] - 1)
    distances = dijkstra(heatmap, start, min_range, max_range)

    target_distances = []
    for index, distance in distances.items():
        pos, step, _ = index
        if pos != target or (min_range and step < min_range):
            continue
        target_distances.append(distance)
    return min(target_distances)
