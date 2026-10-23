import pytest
from slugify import slugify
from slugify.slugify import _modern_truncate


# ---------- Module 1: slugify() ECP ----------

@pytest.mark.smoke
@pytest.mark.parametrize("text,expected", [
    ("Hello World", "hello-world"),            # valid normal
    ("  Hello   World  ", "hello-world"),      # extra spaces
    ("fish &amp; chips", "fish-chips"),        # html entity
    ("", ""),                                  # empty string
    ("!!!", ""),                               # only special chars
    ("C'est déjà l'été.", "c-est-deja-l-ete"),   # unicode accents
])
@pytest.mark.parametrize("algo", ["legacy", "modern"])
def test_slugify_basic_ecp(text, expected, algo):
    assert slugify(text, algorithm=algo) == expected


@pytest.mark.regression
def test_slugify_custom_separator():
    assert slugify("Hello World", separator="_") == "hello_world"


@pytest.mark.regression
def test_slugify_lowercase_false():
    assert slugify("Hello World", lowercase=False) == "Hello-World"


@pytest.mark.regression
def test_slugify_stopwords():
    assert slugify("the quick fox", stopwords=["the"]) == "quick-fox"


@pytest.mark.regression
def test_slugify_replacements():
    result = slugify("10 | 20 %", replacements=[["|", "or"], ["%", "percent"]])
    assert result == "10-or-20-percent"


@pytest.mark.regression
def test_slugify_bytes_modern():
    assert slugify(b"Hello World", algorithm="modern") == "hello-world"


# ---------- Module 1: invalid inputs ----------

@pytest.mark.regression
def test_invalid_algorithm():
    with pytest.raises(ValueError):
        slugify("abc", algorithm="bad")


@pytest.mark.regression
def test_modern_rejects_int_text():
    with pytest.raises(TypeError):
        slugify(123, algorithm="modern")


@pytest.mark.regression
def test_modern_rejects_bool_max_length():
    with pytest.raises(TypeError):
        slugify("abc", max_length=True, algorithm="modern")


@pytest.mark.regression
def test_modern_invalid_replacement_stage():
    with pytest.raises(ValueError):
        slugify("abc", replacement_stage="wrong", algorithm="modern")


# ---------- Module 2: _modern_truncate() BVA ----------
# text = "hello-world" (length 11)

@pytest.mark.boundary
@pytest.mark.parametrize("max_length,expected", [
    (0, "hello-world"),     # 0 = no limit
    (11, "hello-world"),    # exactly length
    (10, "hello-worl"),     # length - 1
    (6, "hello"),           # no trailing dash
    (5, "hello"),           # exactly first word
    (4, "hell"),            # inside first word
    (1, "h"),               # minimum
])
def test_modern_truncate_hard_cut(max_length, expected):
    assert _modern_truncate("hello-world", max_length, False, "-", False) == expected


@pytest.mark.boundary
@pytest.mark.parametrize("max_length,expected", [
    (11, "hello-world"),
    (10, "hello"),
    (5, "hello"),
])
def test_modern_truncate_word_boundary(max_length, expected):
    assert _modern_truncate("hello-world", max_length, True, "-", False) == expected