# -*-coding:utf-8 -*-
"""Test Hash Table Algorithim Implementation."""
import io
import pytest

WORDS = '/usr/share/dict/words'


@pytest.fixture(scope='function')
def words():
    """Create a fixture of words."""
    from hash_table import HashTable
    b = HashTable(11)
    count = 0
    with open(WORDS, 'r') as lot_o_words:
        for word in lot_o_words:
            count += 1
            clean_word = word.strip()
            b.set(clean_word, clean_word)
    return (b, count)


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


def test_set():
    """Test the set function."""
    from hash_table import HashTable
    h = HashTable(1)
    h.set("keyone", 1)
    assert h.table == [[("keyone", 1)]]


def test_hash_length():
    """Test the length of the instance."""
    from hash_table import HashTable
    h = HashTable(1024)
    assert len(h.table) == 1024
