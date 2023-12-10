import itertools
from enum import Enum

import networkx as nx
from numpy import array


class Connection(Enum):
    NORTH = (0, -1)
    EAST = (1, 0)
    SOUTH = (0, 1)
    WEST = (-1, 0)


PIPE_CONNECTIONS = {
    "|": {Connection.NORTH, Connection.SOUTH},
    "-": {Connection.EAST, Connection.WEST},
    "L": {Connection.NORTH, Connection.EAST},
    "J": {Connection.NORTH, Connection.WEST},
    "7": {Connection.SOUTH, Connection.WEST},
    "F": {Connection.SOUTH, Connection.EAST},
    "S": {Connection.NORTH, Connection.EAST, Connection.SOUTH, Connection.WEST},
}


def add_nodes(graph, lines):
    for j, pipes in enumerate(lines):
        for i, pipe in enumerate(pipes):
            if pipe == ".":
                continue
            graph.add_node((i, j), pipe=pipe, is_start=(pipe == "S"))


def add_edges(graph):
    for node, node_data in graph.nodes(data=True):
        pipe = node_data["pipe"]
        valid_connections = set()
        for connection in PIPE_CONNECTIONS[pipe]:
            # Follow the connection to see if there is another pipe there
            other_node = tuple(array(node) + array(connection.value))
            if not graph.has_node(other_node):
                continue
            other_pipe = graph.nodes[other_node]["pipe"]
            # Check compatibility between the two connections
            inverse_connection = Connection(tuple(-array(connection.value)))
            if inverse_connection in PIPE_CONNECTIONS[other_pipe]:
                graph.add_edge(node, other_node)
                valid_connections.add(connection)
        # Update S to its actual pipe type
        if pipe == "S":
            for pipe_type, connections in PIPE_CONNECTIONS.items():
                if connections == valid_connections:
                    graph.nodes[node]["pipe"] = pipe_type


def get_graph(lines):
    graph = nx.Graph()
    add_nodes(graph, lines)
    add_edges(graph)
    return graph


def get_loop(graph):
    starting_node = next(node for node, node_data in graph.nodes(data=True) if node_data["is_start"])
    for connected_component in nx.connected_components(graph):
        if starting_node in connected_component:
            return connected_component


def part_1(graph):
    loop = get_loop(graph)
    return len(loop) // 2


def part_2(graph):
    loop = get_loop(graph)
    total_in_loop = 0
    min_j = min(loop, key=lambda node: node[1])[1]
    max_j = max(loop, key=lambda node: node[1])[1]
    for j in range(min_j, max_j + 1):
        line = sorted(node for node in loop if node[1] == j and graph.nodes[node]["pipe"] != "-")
        inside = False
        for node_a, node_b in itertools.pairwise(line):
            pipe_a = graph.nodes[node_a]["pipe"]
            pipe_b = graph.nodes[node_b]["pipe"]
            # Case 1: U-Turn ┗┉┉┉┛ or ┏┉┉┉┓, just skip through
            if (pipe_a == "L" and pipe_b == "J") or (pipe_a == "F" and pipe_b == "7"):
                continue
            # Case 2: Zig-Zag ┗┉┉┉┓ or ┏┉┉┉┛, flip inside flag and skip through
            elif (pipe_a == "L" and pipe_b == "7") or (pipe_a == "F" and pipe_b == "J"):
                inside = not inside
                continue
            # Case 3: Wall ┃, just flip inside flag
            elif pipe_a == "|":
                inside = not inside
            if inside:
                total_in_loop += node_b[0] - node_a[0] - 1
    return total_in_loop
