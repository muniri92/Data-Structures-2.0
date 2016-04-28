# _*_ coding: utf-8 _*_
"""Test the Trie Algorithm."""
import pytest


# use fixtures later
def test_empty_insert():
    """Test inserting an empty string."""
    from trie import Trie
    t = Trie()
    t.insert("")
    assert t.root == {}


def test_single_insert():
    """Test inserting a single character."""
    from trie import Trie
    t = Trie()
    t.insert("a")
    assert t.root == {"a": {"$": "$"}}


def test_single_capitol_insert():
    """Test inserting a single character."""
    from trie import Trie
    t = Trie()
    t.insert("A")
    assert t.root == {"a": {"$": "$"}}


def test_token_insert():
    """Test inserting a whole token."""
    from trie import Trie
    t = Trie()
    t.insert("munir")
    assert t.root == {"m": {"u": {"n": {"i": {"r": {"$": "$"}}}}}}


def test_multipe_token_insert():
    """Test inserting a whole token."""
    from trie import Trie
    t = Trie()
    t.insert("munir")
    t.insert("moo")
    assert t.root == {"m": {"o": {"o": {"$": "$"}}, "u": {"n": {"i": {"r": {"$": "$"}}}}}}


def test_contatins():
    """Test contains responds with true for a word that has been inserted."""
    from trie import Trie
    t = Trie()
    t.insert("cat")
    result = t.contains("cat")
    assert result is True


def test_contatins_false():
    """Test contains responds with false for a word that is not inserted."""
    from trie import Trie
    t = Trie()
    t.insert("cat")
    result = t.contains("dog")
    assert result is False


def test_traversals_on_empty():
    """Test traversal for aan empty."""
    from trie import Trie
    t = Trie()
    result = []
    for item in t.traversal(t.root):
        result.append(item)
    assert result == []


def test_traversal():
    """Test traversal works on multiple items."""
    from trie import Trie
    t = Trie()
    t.insert("cat")
    t.insert("cats")
    t.insert("dog")
    result = set()
    for i in t.traversal():
        result.add(i)
    assert result == set(["cat", "cats", "dog"])
