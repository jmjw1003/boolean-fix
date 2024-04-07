from src.remapping import true, false, none, null


class TestRemapping:
    def test_true(self):
        assert isinstance(true, bool)
        assert true
    
    def test_false(self):
        assert isinstance(false, bool)
        assert not false

    def test_none(self):
        assert none is None
    
    def test_null(self):
        assert null is None

