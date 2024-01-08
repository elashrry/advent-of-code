from .interval import IntInterval, Subset


class Mapper:
    def __init__(self, domain, image, mapping_dict):
        """Initializes a Mapper object with domain, image, and a mapping dictionary.

        Note: If an element of the input don't have an image, it gets mapped to itself.

        Args:
            domain (Subset): The domain subset for the mapping.
            image (Subset): The image subset for the mapping.
            mapping_dict (dict): A dictionary mapping start of each interval in the
                domain to the start of the interval's image.

        Note:
            The domain and image should be Subset objects.

        Example:
        ```
        domain = Subset([IntInterval(1, 5), IntInterval(8, 10)])
        image = Subset([IntInterval(100, 104), IntInterval(108, 110)])
        mapping_dict = {1: 100, 8: 108}
        mapper = Mapper(domain, image, mapping_dict)
        input_subset = Subset([IntInterval(3, 7)]
        print(mapper.map(input_subset)) # [[5, 7), [102, 104)]
        ```
        """
        self.domain = domain  # subset
        self.image = image  # images of intervals in domain
        self.ـmap = mapping_dict.copy()

    def map(self, subset):
        """Maps a subset using the Mapper.

        Note: If an element of the input don't have an image, it gets mapped to itself.

        Args:
            subset (Subset): The subset to be mapped.

        Returns:
            (Subset): The resulting subset after mapping.

        Example:
        ```
        domain = Subset([IntInterval(1, 5), IntInterval(8, 10)])
        image = Subset([IntInterval(100, 104), IntInterval(108, 110)])
        mapping_dict = {1: 100, 8: 108}
        mapper = Mapper(domain, image, mapping_dict)
        input_subset = Subset([IntInterval(3, 7)]
        print(mapper.map(input_subset)) # [[5, 7), [102, 104)]
        ```
        """
        all_image_list = []
        for input_interval in subset:
            total_elems = input_interval.num_elems  # to verify everything is mapped
            all_mapped = False
            image_list = []
            for domain_interval in self.domain:
                if domain_interval.intersection(input_interval):
                    input_intersection = domain_interval.intersection(input_interval)
                    input_start_dist = input_intersection.start - domain_interval.start
                    input_image_start = (
                        self.ـmap[domain_interval.start] + input_start_dist
                    )
                    image_list.append(
                        IntInterval(
                            input_image_start,
                            input_image_start + input_intersection.width,
                            closed=True,
                        )
                    )
                    image_total_elems = sum(
                        interval.num_elems for interval in image_list
                    )
                    if image_total_elems == total_elems:
                        # if domain_interval.contains(end-1):
                        all_mapped = True
                        break
                    else:
                        input_interval = input_interval.difference(domain_interval)

            if not all_mapped:
                image_list.append(
                    IntInterval(input_interval.start, input_interval.end, closed=True)
                )
            all_image_list += image_list
        return Subset(all_image_list)
