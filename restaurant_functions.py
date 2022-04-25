"""Create restaurant profile and function to be imported by user."""

import sqlite3
import numpy as np

con = sqlite3.connect("restaurant.db")


def parse_durham_data(filename: str) -> None:
    """Read the file and parse the data files into a SQLite table."""
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS Durham([Name] TEXT PRIMARY KEY, [Latitude] FLOAT, [Longitude] FLOAT, [VeganFriendly] BINARY, [Delivery] BINARY, [Curbside] BINARY, [PetFriendly] BINARY, [LargeParty] BINARY, [Catering] BINARY, [CuisineType] TEXT, [RestaurantType] TEXT, [OpeningTime] TEXT, [ClosingTime] TEXT, [Rating] FLOAT, [PriceLevel] TEXT)"
    )
    with open(filename, encoding="utf-8-sig") as p:
        lines = p.readlines()
        col_name = []
        first_row = True
        for line in lines:
            line = line.strip()
            if first_row:
                col_name = line.split()
                first_row = False
            elif not first_row:
                dic = {}
                dat = line.split("\t")
                for count, ele in enumerate(dat, 0):
                    dic[col_name[count]] = dat[count]
                lst = [
                    dic["Name"],
                    dic["Latitude"],
                    dic["Longitude"],
                    dic["VeganFriendly"],
                    dic["Delivery"],
                    dic["Curbside"],
                    dic["PetFriendly"],
                    dic["LargeParty"],
                    dic["Catering"],
                    dic["CuisineType"],
                    dic["RestaurantType"],
                    dic["OpeningTime"],
                    dic["ClosingTime"],
                    dic["Rating"],
                    dic["PriceLevel"],
                ]
                cur.execute(
                    "INSERT or REPLACE INTO Durham VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    lst,
                )
    return


def parse_comments_data(filename: str) -> None:
    """Read the file and parse the data files into a SQLite table."""
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Comments([Name] TEXT, [Comments] TEXT)")
    with open(filename, encoding="utf-8-sig") as p:
        lines = p.readlines()
        col_name = []
        first_row = True
        for line in lines:
            line = line.strip()
            if first_row:
                col_name = line.split()
                first_row = False
            elif not first_row:
                dic = {}
                dat = line.split("\t")
                for count, ele in enumerate(dat, 0):
                    dic[col_name[count]] = dat[count]
                lst = [
                    dic["Name"],
                    dic["Comments"],
                ]
                cur.execute("INSERT or REPLACE INTO Comments VALUES (?, ?)", lst)
    return


class Customer:
    """
    This class will store user preferences for restaurants and
    be used in the restaurant_ranker function to rank restaurants
    in Durham that best fit the user's preferences.

    """

    def __init__(
        self,
        Name: str,
        Latitude: float,
        Longitude: float,
        PriceLevel: str,
        OpeningTime: str,
        ClosingTime: str,
        CuisineType: list[str],
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


def restaurant_ranker(user: Customer) -> list[str]:
    cur = con.cursor()
    cur.execute("SELECT * FROM Durham")
    restaurant_table = cur.fetchall()
    restaurant_list = []
    for restaurant in restaurant_table:
        restaurant_sublist = [restaurant[0]]
        score = 0
        if user.VeganFriendly == "No":
            if any(
                hour
                in list(
                    range(
                        int(restaurant[11][:2] + restaurant[11][3:]),
                        int(restaurant[12][:2] + restaurant[12][3:]),
                    )
                )
                for hour in list(
                    range(
                        int(user.OpeningTime[:2] + user.OpeningTime[3:]),
                        int(user.ClosingTime[:2] + user.ClosingTime[3:]),
                    )
                )
            ):
                if restaurant[9] in user.CuisineType:
                    score += 20
                if user.LargeParty == "Yes" and restaurant[7] == 1:
                    score += 20
                if user.RestaurantType == restaurant[10]:
                    score += 10
                if user.Delivery == "Yes" and restaurant[4] == 1:
                    score += 10
                if user.Catering == "Yes" and restaurant[8] == 1:
                    score += 10
                if user.PetFriendly == "Yes" and restaurant[6] == 1:
                    score += 5
                if restaurant[13] in np.arange(
                    user.Reviews - 0.5, user.Reviews + 0.5, 0.1
                ):
                    score += 5
                elif restaurant[13] in np.arange(
                    user.Reviews - 1.0, user.Reviews + 1.0, 0.1
                ):
                    score += 3
                if len(user.PriceLevel) == len(restaurant[14]):
                    score += 5
                elif (
                    len(restaurant[12]) == len(user.PriceLevel) - 1
                    or len(user.PriceLevel) + 1
                ):
                    score += 3
                restaurant_sublist.append(score)
            else:
                restaurant_sublist.append(score)
        elif user.VeganFriendly == "Yes" and restaurant[3] == 1:
            if any(
                hour
                in list(
                    range(
                        int(restaurant[11][:2] + restaurant[11][3:]),
                        int(restaurant[12][:2] + restaurant[12][3:]),
                    )
                )
                for hour in list(
                    range(
                        int(user.OpeningTime[:2] + user.OpeningTime[3:]),
                        int(user.ClosingTime[:2] + user.ClosingTime[3:]),
                    )
                )
            ):
                if restaurant[9] in user.CuisineType:
                    score += 20
                if user.LargeParty == "Yes" and restaurant[7] == 1:
                    score += 20
                if user.RestaurantType == restaurant[10]:
                    score += 10
                if user.Delivery == "Yes" and restaurant[4] == 1:
                    score += 10
                if user.Catering == "Yes" and restaurant[8] == 1:
                    score += 10
                if user.PetFriendly == "Yes" and restaurant[6] == 1:
                    score += 5
                if restaurant[13] in np.arange(
                    user.Reviews - 0.5, user.Reviews + 0.5, 0.1
                ):
                    score += 5
                elif restaurant[13] in np.arange(
                    user.Reviews - 1.0, user.Reviews + 1.0, 0.1
                ):
                    score += 3
                if len(user.PriceLevel) == len(restaurant[14]):
                    score += 5
                elif (
                    len(restaurant[12]) == len(user.PriceLevel) - 1
                    or len(user.PriceLevel) + 1
                ):
                    score += 3
                restaurant_sublist.append(score)
            else:
                restaurant_sublist.append(score)
        elif user.VeganFriendly == "Yes" and restaurant[3] == 0:
            restaurant_sublist.append(score)
        distance = np.linalg.norm(
            np.array((restaurant[1], restaurant[2]))
            - np.array((user.Latitude, user.Longitude))
        )
        restaurant_sublist.append(distance)
        restaurant_list.append(restaurant_sublist)
    restaurant_list.sort(key=lambda x: x[2])
    for restaurants in restaurant_list:
        restaurants[1] += 15 - restaurant_list.index(restaurants)
    restaurant_list.sort(key=lambda x: x[1], reverse=True)
    restaurant_ordered_list = []
    for ordered_restaurants in restaurant_list:
        restaurant_ordered_list.append(ordered_restaurants[0])
    return restaurant_ordered_list
