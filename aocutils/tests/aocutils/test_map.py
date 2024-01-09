from aocutils import IntInterval, Subset, Mapper


def test_map():
    domain = Subset([IntInterval(1, 5), IntInterval(8, 10)])
    image = Subset([IntInterval(100, 104), IntInterval(108, 110)])
    mapping_dict = {1: 100, 8: 108}
    mapper = Mapper(domain, image, mapping_dict)

    # Test mapping with full intersections between input and domain intervals
    input_subset1 = Subset([IntInterval(1, 5), IntInterval(8, 10)])
    result1 = mapper.map(input_subset1)
    assert len(result1.content) == 2
    assert result1[0] == IntInterval(100, 104)
    assert result1[1] == IntInterval(108, 110)

    # Test mapping with no intersections between input and domain intervals
    input_subset2 = Subset([IntInterval(15, 20), IntInterval(20, 30)])
    result2 = mapper.map(input_subset2)
    assert len(result2.content) == 2
    assert result2[0] == IntInterval(15, 20)
    assert result2[1] == IntInterval(20, 30)

    # Test mapping with partial intersections
    input_subset3 = Subset([IntInterval(3, 7), IntInterval(5, 8)])
    result3 = mapper.map(input_subset3)
    assert len(result3.content) == 2
    assert result3[0] == IntInterval(5, 8)
    assert result3[1] == IntInterval(102, 104)

    # Test mapping with differences
    input_subset4 = Subset([IntInterval(1, 10)])
    result4 = mapper.map(input_subset4)
    assert len(result4.content) == 3
    assert result4[0] == IntInterval(5, 8)
    assert result4[1] == IntInterval(100, 104)
    assert result4[2] == IntInterval(108, 110)
