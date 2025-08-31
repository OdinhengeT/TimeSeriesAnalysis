# tests/placeholder.py

def test_math_addition():
    """A trivial test to make sure pytest is running correctly."""
    assert 2 + 3 == 5


def test_import_package():
    """Check that the package can be imported without errors."""
    import tsa_lth  # replace with your actual package folder name
    assert tsa_lth is not None
