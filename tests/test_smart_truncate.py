import pytest
from slugify import smart_truncate


# ---------- Module 3: smart_truncate() ECP + BVA ----------
# text = "hello-world-test" (length 16)

@pytest.mark.boundary
@pytest.mark.parametrize("max_length,expected", [
    (0, "hello-world-test"),     # 0 = no limit
    (16, "hello-world-test"),    # exactly length
    (17, "hello-world-test"),    # above length
    (15, "hello-world-test"[:15]),
    (1, "h"),                    # minimum
])
def test_smart_truncate_hard_cut(max_length, expected):
    result = smart_truncate("hello-world-test", max_length=max_length)
    assert len(result) <= max(max_length, 16) if max_length == 0 else len(result) <= max_length


@pytest.mark.regression
def test_smart_truncate_word_boundary():
    result = smart_truncate("hello-world-test", max_length=12, word_boundary=True)
    assert result == "hello-world-"


@pytest.mark.regression
def test_smart_truncate_empty_string():
    assert smart_truncate("", max_length=5) == ""


@pytest.mark.regression
def test_smart_truncate_custom_separator():
    result = smart_truncate("hello_world_test", max_length=12, word_boundary=True, separator="_")
    assert result == "hello_world"


@pytest.mark.regression
def test_smart_truncate_save_order():
    result = smart_truncate("hello-world-test", max_length=12, word_boundary=True, save_order=True)
    assert result == "hello-world-"