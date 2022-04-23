"""
Create restaunrant functions to be imported by user.
"""

from datetime import datetime


class Customer:
    """
    This class will store user preferences for restaurants
    and be used in later functions to distinguish restaurant
    profiles that match user preferences.
    """

    def __init__(
        self,
        Name: str,
        Coordinates: tuple[float, float],
        PriceLevel: list[str],
        HoursOfOperation: tuple[str, str],
        CuisineType: str,
        RestaurantType: str,
        VeganFriendly: str,
        Delivery: str,
        CurbSide: str,
        LargeParty: str,
        PetFriendly: str,
        Catering: str,
        Reviews: str,
    ):
        """Initialize user information."""
        self.Name = Name
        self.Coordinates = Coordinates
        self.PriceLevel = PriceLevel
        self.HoursOfOperation = HoursOfOperation
        self.CuisineType = CuisineType
        self.RestaurantType = RestaurantType
        self.VeganFriendly = VeganFriendly
        self.Delivery = Delivery
        self.CurbSide = CurbSide
        self.LargeParty = LargeParty
        self.PetFriendly = PetFriendly
        self.Catering = Catering
        self.Reviews = Reviews
