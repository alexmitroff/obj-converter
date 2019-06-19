import numpy as np

class Vertex:
    """Vertex class

    Attrs:
        `coords` (list/tuple)

    Properties:
        `x` (float)
        `y` (float)
        `z` (float)
        `w` (float)
        `as_vector` (tuple)

    Usage:
        ```
        from formats.obj.vertex import Vertex

        coords = (1.0, 0.5, 0.7, 1.0)
        vertex = Vertex(coords)
        
        print(vertex.x)
        print(vertex.as_vertex)
        ```
    """
 
    __slots__ = ['x', 'y', 'z', 'w']

    def __init__(self, coords=None):
        if not coords:
            coords = (0.0, 0.0, 0.0, 1.0)

        self.x = coords[0]
        self.y = coords[1]
        self.z = coords[2]
        self.w = coords[3]

    @property
    def as_vector(self):
        return np.array(self.x, self.y, self.z, self.w)
