class IntInterval:
    """Represents an interval of integers with a start and end values.

    Attributes:
        start (int): The starting value of the interval.
        end (int): The ending value of the interval (inclusive).
        width (int): The width of the interval (difference between `end` and `start`).
        num_elems (int): The number of elements in the interval.

    Methods:
        __init__(self, start, end, closed="left"):
            Initializes an IntInterval object.

        contains(self, number: int) -> bool:
            Checks if the given number is contained within the interval.

        intersection(self, other) -> IntInterval or None:
            Finds the intersection of two intervals.

        union(self, other) -> IntInterval or Subset:
            Finds the union of two intervals.

        difference(self, other) -> IntInterval or None:
            Finds the difference between two intervals.

        __repr__(self) -> str:
            Returns a string representation of the interval.

        __eq__(self, other) -> bool:
            Compares if two IntInterval objects are equal.

    Example usage:
    ```python
    interval1 = IntInterval(1, 5, closed="left")
    interval2 = IntInterval(3, 8, closed=True)
    interval3 = IntInterval(8, 10, closed=True)

    print(interval1.intersection(interval2))  # [3, 4]
    print(interval1.union(interval2))         # [1, 8]
    print(interval1.union(interval3))    # [[1, 4], [8, 10]]
    print(interval1.difference(interval2))    # [1, 2]
    ```

    Note: The class assumes integer intervals and uses the closed/open semantics.
    """

    def __init__(self, start, end, closed="left"):
        """Initializes an interval of integer with a start and end value.

        Note that the attributes ``start`` and ``end`` are different from the arguments.

        Args:
            start (int): The starting value of the interval.
            end (int): The ending value of the interval (exclusive).
            closed (str | bool): which end to be closed
                left: creates a left-closed interval, i.e. only ``start`` is included in the interval.  # noqa: E501
                right: creates a right-closed interval, i.e. only ``end`` is included in the interval.
                True: creates a closed interval, i.e. both ``start`` and ``end`` are included in the interval.
                False: creates an open interval, i.e. Neither of ``start`` not ``end`` are included in the interval.
        """
        assert closed in ["left", "right", True, False]
        if closed == "left":
            self.start = start
            self.end = end - 1
        elif closed == "right":
            self.start = start + 1
            self.end = end
        elif closed:
            self.start = start
            self.end = end
        else:
            self.start = start + 1
            self.end = end - 1
        self.width = self.end - self.start
        self.num_elems = self.width + 1

    def contains(self, number: int):
        """Checks if the given number is contained within the interval.

        Args:
            number (int): The number to check.

        Returns:
            (bool): True if the number is within the interval, False otherwise.
        """
        return self.start <= number <= self.end

    def intersection(self, other):
        """Finds the intersection of two intervals.

        Args:
            other (Interval): Another Interval object.

        Returns:
            (Interval) or None: The intersection interval if it exists, None otherwise.
        """
        if (
            self.contains(other.start)
            or self.contains(other.end)
            or other.contains(self.start)
            or other.contains(self.end)
        ):
            return IntInterval(
                max(self.start, other.start), min(self.end, other.end), closed=True
            )

    def union(self, other):
        """Finds the union of two intervals.

        Note: tangent intervals (e.g. [1, 5) and [5, 8)) are considered disjoint and
        return a ``Subset`` of two intervals.

        Args:
            other (Interval): Another Interval object.

        Returns:
            (Interval) or (Subset): The union interval if self intersects other.
            Otherwise a Subset of two intervals.
        """
        if self.intersection(other):
            return IntInterval(
                min(self.start, other.start), max(self.end, other.end), closed=True
            )
        else:
            return Subset([self, other])

    def difference(self, other):
        """Finds the difference between two intervals.

        Args:
            other (Interval): Another Interval object.

        Returns:
            (Interval) or None: The difference interval if it exists, None otherwise.
        """
        # no intersection
        if not self.intersection(other):
            return self
        # other contains self
        if other.contains(self.start) and other.contains(self.end):
            return None
        # difference on the left
        if self.start < other.start:
            return IntInterval(self.start, other.start, closed="left")
        # difference on the right
        else:  # self.start >= other.start and self.end>other.start
            return IntInterval(other.end, self.end, closed="right")

    def __repr__(self) -> str:
        return f"[{self.start}, {self.end}]"

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end


class Subset:
    # collection of intervals
    def __init__(self, interval_list):
        """Initializes a Subset object with a list of intervals.

        Args:
            interval_list (list): A list of Interval objects.
        """
        self.content = self._clean_intervals(interval_list)

    def _clean_intervals(self, intervals_list):
        """Cleans a list of intervals to make them mutually disconnected and ordered.

        Args:
            intervals_list (list): A list of Interval objects.

        Returns:
            (list): Cleaned list of mutually disconnected and ordered Interval objects.
        """
        if not intervals_list:
            return []
        sorted_intervals_list = sorted(intervals_list, key=lambda x: x.start)
        clean_intervals_list = [sorted_intervals_list.pop(0)]
        while sorted_intervals_list:
            interval = clean_intervals_list[-1]
            j = 0  # tracks other intervals
            for other_interval in sorted_intervals_list:
                if interval.intersection(other_interval):
                    # union is interval because there is intersection
                    interval = interval.union(other_interval)
                    clean_intervals_list[-1] = interval
                else:
                    # new disconnected from old interval
                    clean_intervals_list.append(sorted_intervals_list[j])
                    break
                j += 1
            # empty if j+1>=len()
            sorted_intervals_list = sorted_intervals_list[j + 1:]
        return clean_intervals_list

    def __iter__(self):
        return iter(self.content)

    def __getitem__(self, index):
        return self.content[index]

    def __repr__(self) -> str:
        return str(self.content)
