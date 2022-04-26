"""
This testing file will assess the performance of the functions
in our library.

"""

import pytest

from restaurant_functions import (
    parse_durham_data,
    parse_comments_data,
    Customer,
    restaurant_ranker,
    search_comments,
    new_comments,
    con,
)

parse_durham_data("Durham")
parse_comments_data("Comments")


def test_parse_durham_data():
    """Test parse_durham_data."""
    cur = con.cursor()
    assert (
        list(cur.execute("SELECT * FROM Durham WHERE Name = 'Vin Rouge'"))[0][1]
    ) == 36.0106356
    assert (
        list(cur.execute("SELECT * FROM Durham WHERE Name = 'Vin Rouge'"))[0][9]
    ) == "French"


def test_parse_comments_data():
    """Test parse_comments_data."""
    cur = con.cursor()
    assert (
        list(cur.execute("SELECT * FROM Comments WHERE Name = 'Vin Rouge'"))[0][1]
    ) == "Good environment"


def test_restaurant_ranker():
    """
    Test to check best restaurant for fake users is first in the returned list.
    Fake users have preferences that match the restaurant exactly to confirm
    the function is giving the most optimal restaurant as first in the list.

    """
    fake_customer1 = Customer(
        "Fake Person 1",
        35.9975740,
        -78.9417355,
        "$$$",
        "17:00",
        "24:00",
        ["Japanese"],
        "Sit down",
        "Yes",
        "Yes",
        "Yes",
        "No",
        "Yes",
        "Yes",
        4.4,
    )
    fake_customer2 = Customer(
        "Fake Person 2",
        35.9658939,
        -78.9532714,
        "$",
        "10:00",
        "24:00",
        ["American"],
        "Sit down",
        "No",
        "Yes",
        "Yes",
        "No",
        "No",
        "Yes",
        4.2,
    )
    assert restaurant_ranker(fake_customer1)[0] == "M Sushi"
    assert restaurant_ranker(fake_customer2)[0] == "Cook Out"


def test_search_comments():
    """Test search_comments."""
    assert (search_comments(restaurant_name="M Kokko", keyword="service")) == [
        ("Slow service",)
    ]
    assert (search_comments(restaurant_name="M Kokko")) == [
        ("Slow service",),
        ("Hard to find",),
        ("Long wait time",),
    ]
    assert (search_comments(keyword="service")) == [
        ("Flake's Breakfast Sandwiches", "Good service"),
        ("Naan Stop", "Bad service"),
        ("Shanghai", "Amazing service"),
        ("Wang's Hotpot", "Terrible service"),
        ("M Kokko", "Slow service"),
        ("Cook Out", "Quick service"),
    ]


def test_new_comments():
    """Test new_comments,"""
    cur = con.cursor()
    new_comments("Vin Rouge", "Not good at all")
    assert (
        ("Not good at all",)
        in list(cur.execute("SELECT Comments FROM Comments WHERE Name = 'Vin Rouge'"))
    ) == True
