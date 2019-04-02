import pytest


def int_to_bin(i_number):
    return f"{bin(i_number)}"


@pytest.fixture(params=[{"input": 8,
                         "expected_result": "0b1000"},
                        {"input": 5,
                         "expected_result": "0b0011"},
                        {"input": 1,
                         "expected_result": "0b1"}])
def test_case(request):
    return request.param


def test_my_converter(test_case):
    result = int_to_bin(test_case['input'])
    assert result == test_case['expected_result']

# if __name__ == '__main__':
#     pass
