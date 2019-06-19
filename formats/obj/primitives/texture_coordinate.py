import numpy as np


class TextureCoordinate:
    """Vertex class

    Attrs:
        `coords` (list/tuple)

    Properties:
        `u` (float)
        `v` (float)
        `w` (float)
        `as_vector` (numpy Array)

    Usage:
        ```
        from formats.obj.primitives.texture_coordinate import TextureCoordinate

        coords = (1.0, 0.5, 0.0)
        texture_coordinate = TextureCoordinate(coords)

        print(texture_coordinate.x)
        print(texture_coordinate.as_vector)
        ```
    """

    __slots__ = ('u', 'v', 'w')

    def __init__(self, coords=None):
        if not coords:
            coords = (0.0, 0.0, 0.0)

        self.u = coords[0]
        self.v = coords[1]
        if len(coords) == 3:
            self.w = coords[2]
        else:
            self.w = 0.0

    @property
    def as_vector(self):
        return np.array((self.u, self.v, self.w))
