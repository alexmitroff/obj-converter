import numpy as np
from formats.obj.settings import *


class Vertex:
    """Vertex class

    Attrs:
        `coords` (list/tuple)

    Properties:
        `x` (float)
        `y` (float)
        `z` (float)
        `w` (float)
        `as_vector` (numpy Array)

    Usage:
        ```
        from formats.obj.primitives.vertex import Vertex

        coords = (1.0, 0.5, 0.7, 1.0)
        vertex = Vertex(coords)

        print(vertex.x)
        print(vertex.as_vector)
        ```
    """

    __slots__ = ('x', 'y', 'z', 'w')

    def __init__(self, coords=None):
        if not coords:
            coords = (0.0, 0.0, 0.0, 1.0)

        self.x = coords[0]
        self.y = coords[1]
        self.z = coords[2]
        if len(coords) == 4:
            self.w = coords[3]
        else:
            self.w = 1.0

    @property
    def as_vector(self):
        return np.array((self.x, self.y, self.z, self.w))


class VertexDataIndexes:
    """Full vertex data

    Contains vertex coords, texture coords, vertex normal by index

    """
    __slots__ = (
        f'{VERTEX}_index',
        f'{TEXTURE_COORDINATE}_index',
        f'{NORMAL}_index'
    )

    def __init__(self, data):
        for i, slot in enumerate(self.__slots__):
            setattr(self, slot, data[i])

    @property
    def as_vector(self):
        data = [getattr(self, slot) for slot in self.__slots__]
        return np.array(data)
