# BIOSTAT 821 Final Project

The general idea behind this project is to have a user input information to create their restaurant profile, and based on this profile,
the library will have a function that outputs an ordered list of restaurants in Durham based on an optimization function. The restaurants will
be ordered based on this optimization function, with the first restaurant being the restaurant the function believes the user will like the most 
based on their preferences. The user will be able to input several preferences for their profile, including but not limited to: cuisine type 
(Italian, Indian, etc.), price range, accessibility options (delivery, pickup, etc.), and having vegan options. The profile will
be a custom Class, with preferences being stored as attributes of that class.

The restaurants are all in Durham, North Carolina. The restaurant information is held in a SQLite database. When inputting their restaurant profile, the user will also enter their geographical coordinates, which 
will be a tuple with latitude and longitude. Based on this, the optimization function will account for the user's proximity to the restaurants and incorporate this into each restaurant's final ranking. The optimization function will assign a certain score to every restaurant based on how well they match the user's preferences and how close they are by location, and then the restaurants will be listed in descending order of final score.

The SQLite database will have two tables, one called Durham and one called Comments. The Durham table will have all of the information for the restaurants that the optimization function will use to sort the restaurants for the user. The Comments table will have a variable for the restaurants, and a variable for comments. Restaurants can have multiple comments in this table. These tables will be read in from text files that are included in the library.

The library will also have a function to allow the user to search for comments for a particular restaurant. This function will also allow them to search for keywords that could be found in a comment, and the function will output any restaurant with its comments that contain that keyword. A user could also search for a restaurant and a particular keyword at the same time, and the function will allow them to view all of the comments for that particular restaurant that contain that keyword. There will also be a function that allows a user to add a comment to the Comments table in the SQLite database for a restaurant after they have dined there.

To summarize, the final library will have: 
- two text files, one with Durham restaurant information and one with comments for those restaurants
- a database made using SQLite, that makes a table of restaurant data and a table of comments for those restaurants in Durham using the text files
- a custom class, called Customer (which serves as the restaurant profile), where the user can input their preferences for a restaurant and their location
- a function that takes a user's restaurant profile and lists the restaurants in Durham in the order that it believes the user will have the best dining experience at
- a function that allows a user to search all the commments for a particular restaurant, or search for keywords in comments and then output the restaurants that have those keywords in their comments
- a function that allows a user to add new comments to the Comments table in the SQLite database for a restaurant
- multiple tests for each function in a testing file

The user should refer to the user_instructions.py file for instructions on running the functions in the library.
