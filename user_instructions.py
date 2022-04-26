""""
This file provides users with instructions on the operation
and implementation of the functions within this library. Each
function will be described in detail below.

"""

from restaurant_functions import (
    parse_durham_data,
    parse_comments_data,
    Customer,
    restaurant_ranker,
    search_comments,
    new_comments,
)

"""
There are two parsing functions dedicated to creating user friendly SQLite tables. This
section will describe to users the best way to implement these functions. To implement 
the parse_durham_data() function, users should simply paste within quotations the pathway 
of the text file for "Durham" restaurant data which should be saved in the same directory 
as the restaurant_functions.py and this user_instructions.py file. This function will save 
the contents of the text file into a SQLite table where the columns refer to the different 
elements of restaurant information, outlined further in the next section where users may create 
their restaurant profile.

Users may follow the same process for the parse_comments_data() function, implementing the 
"Comments" data, which should also be saved to the same directory. This function will read the 
text file and save a SQLite table where the first column contains restaurant names and the second 
column includes comments about the restaurant from individuals who have given written reviews 
on the restaurant quality.

"""

parse_durham_data("Durham")
parse_comments_data("Comments")

# Create your restaurant profile
"""
In order to be able to successfully use our restaurant ranking function,
users must follow the directions below exactly as they are stated. This includes
following case sensitive actions and numeric inputs. Users may follow the outlined
example below for reference.

Step 1 - Give your Profile a name
Begin by using your first and last name to create an object of class Customer.
This means you will start with:
firstname_lastname = Customer()

Step 2 - Create your Profile
In the following order, users should input their restaurant profile information.

Name: Input your first and last name in the first step of creating your restaurant profile.
This should be in between quotations, as shown in the example. "First Last"

Latitude: Obtain the exact latitude of your location. Users will input this value including
any and all decimal places present in their latitude. This value will be paired with the longitude
input and used to find the restaurant closest to you that meets your profile criteria.

Longitude: Obtain the exact longitude of your location. Users will input this value including
any and all decimal places present in their longitude. This value will be paired with the latitude
input and used to find the restaurant closest to you that meets your profile criteria.

Price Level: Indicated on a scale denoted by $, $$, $$$, $$$$ where the greater number of $
implies that the desired price level of the restaurant is higher. This should be between
quotations as such, "$$".

Opening Time: Using a 24:00 hour clock, users will input the opening hours of which they are
interested in visiting the restaurant so that the function can select restaurants which
operate within the desired duration. For example, 6:45pm would be entered as "18:45".
If a restaurant does not operate during the requested hours, it will not be suggested to
users. It is important that users include a 0 before any single digits hours,
for example: 8:30am would be entered as "08:30". This input should be between quotations, as such:
"08:30".

Closing Time: Using a 24:00 hour clock, users will input the opening hours of which they are
interested in visiting the restaurant so that the function can select restaurants which
operate within the desired duration. This value will be paired with OpeningTime to calculate the
duration of hours the user is interested in. This input should be between quotations, as such:
"18:45".

Cuisine Type: Use a list to indicate the cuisine type you prefer for your dining experience.
An example could be: ["American", "Chinese"].

RestaurantType: Indicate the type of restaurant dining experience that is preferred. 
This preference should match exactly to one of the following options and should be 
between quotations:
    "Sit down", "Cafe", "Fast Food"

VeganFriendly: Users may indicate if they require a restaurant with vegan options.
If requested, input "Yes", and all restaurant which do not include this option will
not be suggested. If not requested, input "No".

Delivery: Users looking for delivery options should input "Yes"/, otherwise "No".

Curbside - Users looking for curbside options should input "Yes"/, otherwise "No".

LargeParty - Users looking for large party options should input "Yes"/, otherwise "No".

PetFriendly - Users looking for pet friendly options should input "Yes"/, otherwise "No".

Catering - Users looking for catering options should input "Yes"/, otherwise "No".

Reviews - The review option allows users to input the restaurant standard that they
are looking for. On a scale of 1-5, users can designate if they are looking for a
restaurant of quality 3/5.0 or 4.5/5.0 for example. The user need only input their
desired quality level and must use up to one decimal of exactness (ex. 2.3, 4.6).

"""

firstname_lastname = Customer(
    "Input Name",
    36.0089992,
    -78.9417355,
    "$$",
    "08:30",
    "12:00",
    ["Chinese", "Indian"],
    "Sit down",
    "Yes",
    "Yes",
    "Yes",
    "No",
    "No",
    "Yes",
    4.5,
)

# Use your restaurant profile to rank restaurants in Durham
"""
Here is where the restaurant_ranker function will take your profile you created
above, called firstname_lastname, and use your preferences for a restaurant
to rank all the available restaurants in Durham that are in our database. This
will output an ordered list with the first restaurant in the list being the one
the function believes you will have the most optimal dining experience at, and 
the last restaurant in the list being the one it believes you will have the least 
optimal dining experience at.

To receive your list of ordered restaurants, simply fill out your restaurant 
profile as a Customer class above, replace the name of your Customer class as the 
input of the restaurant_ranker function below, save, and run this Python script.

The search_comments() function allows users to input up to two commands that will sort
through the Comments table and select based on the user input. If the user inputs only the
name of their restaurant of interest, then the function will return a list of all instances where
that restaurant received a comment or review. If the user inputs only the keyword, the second
argument of the function, then this will return a list of all instances where this keyword is 
mentioned in the comments. When users input both a restaurant name and keyword, this function will 
return a list that contains comments for that specific restaurant. In the case where users input a 
name that does not exist within the Comments table, an empty list will be returned.

All inputs should be between quotations. For example, search_comments("M Sushi", "omakase")

The new_comments() function simply provides users the opportunity to input first the name of
a restaurant in quotations, and secondly, a review about the restaurant. For example,
new_comments("Hannah's Bagel", "Best bagels ever")

To run these functions, simply give your input for the functions, save, and run this Python script.

"""

print(restaurant_ranker(firstname_lastname))

print(search_comments(restaurant_name="Naan Stop", keyword="service"))

new_comments("Naan Stop", "Great Indian food")
