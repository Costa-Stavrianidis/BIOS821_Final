"""
This testing file will assess the functionality of our restaurant
ranking function.

"""

import pytest

from restaurant_functions import (
    parse_durham_data,
    parse_comments_data,
    Customer,
    restaurant_ranker,
)

parse_durham_data("Durham")
parse_comments_data("Comments")


def test_restaurant_ranker():
    """Test to check best restaurant for fake user is first in the returned list."""
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
