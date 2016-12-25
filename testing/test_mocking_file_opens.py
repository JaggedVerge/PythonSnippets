"""
Mocking code that uses open requires dealing with some sublties which
are covered in this file.

In order to unit test this type of situation properly we don't want to create any file on disk.
To do this requires mocking the `open` builtin.

For simple cases we can use unittest.mock.patch along with unittest.mock.mock_open and we get all we need.

However if we have to iterate over the mocked `open` we have to do more work.
For example say we have the following code that reads a file line by line
and creates a list with it. We wish to test something like this:

>>> data = []
>>> with open(filename, 'r') as f:
>>>     for line in f: # supporting iteration requires extra work for mocking
>>>         data.append(line)
>>> return data


There's some extra work that has to be done if iteration over the mocked
file object is to be supported because this doesn't come as a default.
Specifically we much define `__iter__` for the `mock_open function.
"""

from mocking_file_opens import example_function

def test_mocking_a_file_open():
    """Test that the example function works as advertised"""
    from unittest.mock import mock_open, patch

    # The mock_data we are using for our test
    mock_data = """A
B
C
"""
    mocked_open = mock_open(read_data=mock_data)

    # mock_open does not support iteration by lines by default so
    # we must define the following:
    mocked_open.return_value.__iter__.return_value = mock_data.splitlines()

    # We need to patch the open found in the namespace of the module
    # where the function is defined
    with patch('mocking_file_opens.open', mocked_open, create=True) as mocked_file_open:
        res = example_function('Test_filename.txt')

    mocked_file_open.assert_called_once_with('Test_filename.txt', 'r')
    assert len(res) == 3
    assert res == ["A", "B", "C"]

