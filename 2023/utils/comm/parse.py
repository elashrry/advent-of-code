from __future__ import annotations
from typing import List, Callable, Match
import re

from utils.comm import Grid

class Parser:
    """
    A utility class for parsing text data and performing operations.

    Attributes:
    - data (str): The input text data.
    - lines (List[str]): A list containing individual lines of the input data.
    - sections (List[str]): A list containing sections separated by double newline characters.
    - grid (Grid): An instance of the Grid class for handling tabular data.

    Methods:
    - __init__(self, file_name: str | None = None, text: str | None = None): 
      Initializes the Parser object with either a file name or direct text input.
      
    - get_lines(self) -> List[str]:
      Returns a list containing individual lines of the input data.

    - get_sections(self) -> List[str]:
      Returns a list containing sections separated by double newline characters.

    - get_grid(self, sep="", dtype: Callable = str) -> Grid:
      Parses the input data into a Grid object with an optional separator and data type for each cell.

    - apply_regex(self, pattern: str, return_loc=False) -> Iterator[Match[str]]:
      Applies a regular expression pattern against each line of the input data and returns match groups.

    Args:
    - pattern (str): The regular expression pattern to apply.
    - return_loc (bool): If True, returns match groups along with their locations.
    
    Returns:
    - Iterator[Match[str]]: An iterator containing match groups for each line.
    """
    data: str
    lines: List[str]
    sections: List[str]
    grid: Grid

    def __init__(self, file_name: str | None = None, text: str | None = None):
        """
        Initializes the Parser object with either a file name or direct text input.

        Args:
        - file_name (str | None): The name of the file to read data from. Default is None.
        - text (str | None): The direct input text. Default is None.

        Raises:
        - ValueError: If both file_name and text are provided.
        """
        if file_name and text:
            raise ValueError("Only one of file_name or text must be provided.")
        elif file_name is None and text is None:
            raise ValueError("One of file_name or text must not be None.")
        if file_name:
            with open(file_name, "r") as f:
                self.data = f.read()
        else:
            self.data = text

        self.data = self.data.strip()

    def get_lines(self) -> List[str]:
        """
        Returns a list containing individual lines of the input data.

        Returns:
        - List[str]: A list of strings representing individual lines.
        """
        lines = self.data.split("\n")
        # lines = lines[:-1] if not lines[-1].strip() else lines
        return lines

    def get_sections(self) -> List[str]:
        """
        Returns a list containing sections separated by double newline characters.

        Returns:
        - List[str]: A list of strings representing sections.
        """
        return self.data.split("\n\n")

    def get_grid(self, sep="", dtype: Callable = str) -> Grid:
        """
        Parses the input data into a Grid object with an optional separator and
        data type for each cell.

        Args:
        - sep (str): The separator to use. Default is an empty string.
        - dtype (Callable): The data type conversion function for each cell.
            Default is str.

        Returns:
        - Grid: An instance of the Grid class containing the parsed data.
        """
        lines = self.get_lines()
        grid = Grid()
        for l in lines:
            if l.strip():
                line_list = l.split(sep) if sep else l.split()
                line_list = list(map(dtype, line_list))
                grid.append_row(line_list)
        return grid

    def apply_regex(self, pattern: str, return_loc=False) -> List[str] | List[Match[str]]:
        """
        Applies a regular expression pattern against each line of the input data and returns match groups.

        Args:
        - pattern (str): The regular expression pattern to apply.
        - return_loc (bool): If True, returns match groups along with their locations.

        Returns:
        - List[List[str]] | List[List[Match[str]]]: if `return_loc=True`, an iterator containing 
        match groups for each line. Otherwise, a list of matched substrings.
        """
        # I think some regex patters don't behave the same with findall and finditer !
        lines = self.get_lines()
        match_grp_list = []
        for l in lines:
            if return_loc:
                match_grp = list(re.finditer(pattern, l))
            else:
                match_grp = re.findall(pattern, l)
            match_grp_list.append(match_grp)
        return match_grp_list
