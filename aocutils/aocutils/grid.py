from copy import deepcopy
from typing import List


class Grid:
    """Represents a 2D grid with customizable content and padding.

    Attributes:
        content (List[List]]): grid represented as a list of lists.
        sep (str): Separator used to join elements when converting the grid to a string.

    Methods:
        __init__(self, content: List[List]] = None, sep: str = ""):
            Initializes a Grid object with optional content and separator.

        append_row(self, row: List):
            Appends a row to the grid.

        pad(self, fill_value: Union[int, str] = "."):
            Pads the grid with specified fill value to rows and columns.

        __str__(self) -> str:
            Returns a string representation of the grid.

        __getitem__(self, coords: Tuple[int, int]) -> Any:
            Returns the element at the specified coordinates.

        __setitem__(self, coords: Tuple[int, int], elem: Any):
            Sets the element at the specified coordinates.

        shape(self) -> Tuple[int, int]:
            Returns the shape of the grid as a tuple (n_rows, n_columns).

        get_subset(self, i_min: int, i_max: int, j_min: int, j_max: int) -> Grid:
            Returns a subset of the grid defined by the given specified range.

    Example usage:
    ```python
    grid = Grid([[1, 2], [3, 4]], sep=", ")
    print(grid)  # "1, 2\n3, 4"
    grid.append_row([5, 6])
    print(grid)  # "1, 2\n3, 4\n5, 6"
    grid.pad()
    print(grid)  # "., 0, 0, .\n., 1, 1, .\n1, 2, 3, 4\n5, 6, 7, 8\n., 3, 2, .\n., 4, 3, ."  # noqa: E501
    ```
    """

    def __init__(self, content: List[List] = None, sep: str = ""):
        """Initializes a Grid object.

        Args:
            content (List[List], optional): Initial grid content. Defaults to None.
            sep (str, optional): Separator for joining elements in the string
            representation. Defaults to "".
        """
        self.content = deepcopy(content) if content else []
        for row in self.content:
            assert len(row) == self.shape[1]
        self.sep = sep

    def append_row(self, row: list):
        """Appends a row to the grid.

        Args:
            row (List): Row to be appended to the grid.
        """
        if self.content:
            assert len(row) == self.shape[1]
        self.content.append(deepcopy(row))

    def pad(self, fill_value="."):
        """Pads the grid with the specified fill value to rows and columns.

        Args:
            fill_value (Union[int, str], optional): Fill value for padding.
            Defaults to ".".
        """
        # pad two columns, then two rows
        for i, row in enumerate(self.content):
            self.content[i] = [fill_value] + row + [fill_value]
        first_row = [fill_value for j in range(len(self.content[0]))]
        last_row = [fill_value for j in range(len(self.content[0]))]
        self.content = [first_row] + self.content + [last_row]

    def __str__(self):
        rows_string = "\n".join(
            self.sep.join(str(elem) for elem in line_list) for line_list in self.content
        )
        return rows_string

    def __getitem__(self, coords):
        i, j = coords
        return self.content[i][j]

    def __setitem__(self, coords, elem):
        i, j = coords
        self.content[i][j] = elem

    @property
    def shape(self):
        return len(self.content), len(self.content[0])

    def get_subset(self, i_min, i_max, j_min, j_max):
        """Returns a subset of the grid defined by the specified range.

        Args:
            i_min (int): Minimum row index.
            i_max (int): Maximum row index.
            j_min (int): Minimum column index.
            j_max (int): Maximum column index.

        Returns:
            Grid: Subset of the grid.
        """
        subset = Grid(
            [self.content[i][j_min: j_max + 1] for i in range(i_min, i_max + 1)]
        )
        return subset
