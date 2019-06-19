import numpy as np


class Normal:
    """Normal class

    Attrs:
        `vector` (list/tuple)

    Properties:
        `x` (float)
        `y` (float)
        `z` (float)
        `as_vector` (numpy Array)

    Usage:
        ```
        from formats.obj.primitives.normal import Normal

        vector = (1.0, 0.5, 0.7)
        normal = Normal(coords)

        print(normal.x)
        print(normal.as_vector)
        ```
    """

    __slots__ = ('x', 'y', 'z')

    def __init__(self, vector=None):
        if not vector:
            vector = (0.0, 0.0, 1.0)

        self.x = vector[0]
        self.y = vector[1]
        self.z = vector[2]

    @property
    def as_vector(self):
        return np.array((self.x, self.y, self.z))