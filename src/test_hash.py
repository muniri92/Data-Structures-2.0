# -*-coding:utf-8 -*-
"""Test Hash Table Algorithim Implementation."""
import pytest


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
