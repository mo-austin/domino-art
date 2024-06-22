
import networkx as netx

class Tiling:
    def __init__(self):
        return

    # This is the method takes as input a list lines of input
    # as strings.  You should parse that input, find a tiling,
    # and return a list of strings representing the tiling
    #
    # @return the list of strings representing the tiling


    def compute(self, image):
        # Dimensions of the image
        n = len(image)    # Number of rows
        m = len(image[0]) # Number of columns
        G = netx.DiGraph()  # Directed graph for the flow network
        source = 'S'      # Source node identifier
        sink = 'T'        # Sink node identifier
        total_black = 0   # Counter for the number of black pixels

        # Helper function to check if a pixel is within bounds and is black
        def is_black(x, y):
            return 0 <= x < n and 0 <= y < m and image[x][y] == '#'
        
        # Build the flow network graph
        for i in range(n):
            for j in range(m):
                if image[i][j] == '#':
                    total_black += 1  # Increment black pixel count
                    node = (i, j)     # Create a node for each black pixel
                    # Connect node to sink or source based on its (i+j) parity
                    if (i + j) % 2 == 0:
                        # Even parity nodes connect to sink
                        G.add_edge(node, sink, capacity=1)
                    else:
                        # Odd parity nodes connect to source
                        G.add_edge(source, node, capacity=1)
                        # Connect the node to adjacent black pixels
                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nx, ny = i + dx, j + dy
                            if is_black(nx, ny):
                                # Connect adjacent black pixels with a capacity of 1
                                G.add_edge(node, (nx, ny), capacity=1)
        
        # Calculate maximum flow from source to sink
        flow_value, flow_dict = netx.maximum_flow(G, source, sink)
        
        # If the maximum flow is not half of the total number of black pixels, tiling is impossible
        if flow_value * 2 != total_black:
            return ["impossible"]
        
        # Extract the tiling from the flow dict if a valid tiling is possible
        result = []
        for i in range(n):
            for j in range(m):
                if (i + j) % 2 == 1 and image[i][j] == '#':  # Assuming odd-parity nodes were connected to source
                    # Check for flow in each possible domino placement direction
                    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                    for (di, dj) in directions:
                        ni, nj = i + di, j + dj
                        if (ni, nj) in flow_dict[(i, j)] and flow_dict[(i, j)][(ni, nj)] == 1:
                            # Ensure to format output correctly, avoiding duplicate entries
                            if (i < ni) or (j < nj):  # Ensure to only count each domino once
                                result.append(f"{j} {i} {nj} {ni}")
                            elif (i == ni) and (j > nj):  # Horizontal left to right
                                result.append(f"{nj} {ni} {j} {i}")
                            elif (i > ni) and (j == nj):  # Vertical top to bottom
                                result.append(f"{nj} {ni} {j} {i}")
        
        return result
    