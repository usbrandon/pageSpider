from utilities.url_utilities import load_urls_from_file


def test_load_files():
    test_urls = load_urls_from_file("input.txt")
    assert(len(test_urls) > 1)
