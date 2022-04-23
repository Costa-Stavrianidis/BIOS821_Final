"""
Create restaurant functions to be imported by user.
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
        Latitude: float,
        Longitude: float,
        PriceLevel: list[str],
        OpeningTime: str,
        ClosingTime: str,
        CuisineType: str,
        RestaurantType: str,
        VeganFriendly: str,
        Delivery: str,
        Curbside: str,
        LargeParty: str,
        PetFriendly: str,
        Catering: str,
        Reviews: float,
    ):
        """Initialize user information."""
        self.Name = Name
        self.Latitude = Latitude
        self.Longitude = Longitude
        self.PriceLevel = PriceLevel
        self.OpeningTime = OpeningTime
        self.ClosingTime = ClosingTime
        self.CuisineType = CuisineType
        self.RestaurantType = RestaurantType
        self.VeganFriendly = VeganFriendly
        self.Delivery = Delivery
        self.CurbSide = Curbside
        self.LargeParty = LargeParty
        self.PetFriendly = PetFriendly
        self.Catering = Catering
        self.Reviews = Reviews
