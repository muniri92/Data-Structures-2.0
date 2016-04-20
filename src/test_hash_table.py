# -*-coding:utf-8 -*-
"""Test Hash Table Algorithim Implementation."""
import pytest

WORDS = '/usr/share/dict/words'


@pytest.fixture(scope='function')
def words():
    """Create a fixture of words."""
    from hash_table import HashTable
    b = HashTable(11)
    count = 0
    words_list = []
    with open(WORDS, 'r') as lot_o_words:
        for word in lot_o_words:
            count += 1
            clean_word = word.strip()
            b.set(clean_word, clean_word + "value")
            words_list.append(clean_word)
    return (b, count, words_list)


def test_set():
    """Test the set function."""
    from hash_table import HashTable
    h = HashTable(1)
    h.set("keyone", 1)
    assert h.table == [[("keyone", 1)]]


def test_set_mass(words):
    """Test that set will work over multiples."""
    instance = words[0].table
    key_size = 0
    for list_ in instance:
        try:
            key_size += len(list_)
        except AttributeError:
            pass
    assert key_size == words[1]


def test_table_creation_string():
    """Test that creating table with a string as parmaeter raises error."""
    from hash_table import HashTable
    with pytest.raises(TypeError):
        HashTable("two")


def test_table_creation_boolean():
    """Test that creating table with a Boolean as parmaeter raises error."""
    from hash_table import HashTable
    with pytest.raises(TypeError):
        HashTable(True)


def test_table_creation_list():
    """Test that creating table with a list as parmaeter raises error."""
    from hash_table import HashTable
    with pytest.raises(TypeError):
        HashTable([23])


def test_table_length():
    """Test the creating table with int parameter works correctly."""
    from hash_table import HashTable
    h = HashTable(1024)
    assert len(h.table) == 1024


def test_hash():
    """Assert that the type of a hashed key is a number."""
    from hash_table import HashTable
    b = HashTable(24)
    output = b._hash("Hello")
    assert type(output) == int


def test_set_value_int():
    """Test the set value must be a string."""
    from hash_table import HashTable
    b = HashTable(22)
    with pytest.raises(TypeError):
        b.set(20, 20)


def test_set_value_list():
    """Test the set value must be a string."""
    from hash_table import HashTable
    b = HashTable(22)
    with pytest.raises(TypeError):
        b.set(["hello"], 20)


def test_to_search_not_there():
    """Test that a key that is not there returns None."""
    from hash_table import HashTable
    b = HashTable(22)
    output = b._to_search("hello", 8)
    assert output is None


def test_to_search_already_there():
    """Test that a key that is already there returns a tuple."""
    from hash_table import HashTable
    b = HashTable(1)
    b.set("hello", 8)
    output = b._to_search("hello", 0)
    assert output == (0, ("hello", 8))


def test_to_search_not_there_but_other_keys():
    """Test that a key that's not there, but table has a list returns False."""
    from hash_table import HashTable
    b = HashTable(1)
    b.set("hello", 8)
    output = b._to_search("don't find me", 0)
    assert output is False


def test_get():
    """Return the item post hash."""
    from hash_table import HashTable
    b = HashTable(10)
    b.set("hello", "thirteen")
    result = b.get("hello")[1]
    assert result == "thirteen"


def test_get_mass(words):
    """Test that a value for a key is correct."""
    instance = words[0]
    for word in words[2]:
        assert instance.get(word)[1] == word + "value"


def test_no_key():
    """Assert that if a key is not in hash table it raises a key error."""
    from hash_table import HashTable
    b = HashTable(3)
    with pytest.raises(KeyError):
        b.get("purple-nurple.")
