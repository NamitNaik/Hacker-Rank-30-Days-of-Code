def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError(
            "Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx


class TestDataEmptyArray(object):

    @staticmethod
    def get_array():
        empty_array = []
        return empty_array


class TestDataUniqueValues(object):

    @staticmethod
    def get_array():
        unique_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        return unique_array

    @staticmethod
    def get_expected_result():
        seq = TestDataUniqueValues.get_array()
        min_idx = 0
        for i in range(1, len(seq)):
            if seq[i] < seq[min_idx]:
                min_idx = i
        return min_idx


class TestDataExactlyTwoDifferentMinimums(object):

    @staticmethod
    def get_array():
        min_2_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        return min_2_array

    @staticmethod
    def get_expected_result():
        seq = TestDataExactlyTwoDifferentMinimums.get_array()
        min_idx = 0
        for i in range(1, len(seq)):
            if seq[i] < seq[min_idx]:
                min_idx = i
        return min_idx


def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False


def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2

    assert len(list(set(seq))) == len(seq)

    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result


def TestiWithExactyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result


TestWithEmptyArray()
TestWithUniqueValues()
TestiWithExactyTwoDifferentMinimums()
print("OK")
