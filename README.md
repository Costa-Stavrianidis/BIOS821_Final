# FinalProject_821

The general idea behind this project will be to have a user input information to create their restaurant profile, and based on this profile,
the library will output an ordered list of restaurants in the city nearest to the user based on an optimization function. The restaurants will
be ordered based on this optimization function, with the top restaurant being the restaurant the function believes the user will like the most 
based on their preferences. The user will be able to input several preferences for their profile, including but not limited to: cuisine type 
(Italian, Indian, etc.), price range, accessibility options (delivery, pickup, etc.), and having vegan or vegetarian options. The profile will
be a custom Class, with preferences being stored as attributes of that class.

The cities will all be in North Carolina. When inputting their restaurant profile, the user will enter their geographical coordinates, which 
will be a tuple with latitude and longitude. Based on this, the optimization function will find the closest city to the user, and then order
the restaurants within that city. The optimization function will assign a certain weight to each preference that a user inputs into their profile.
The profile will have the option to prioritize certain factors over others. For example, if a user wants a highly rated restaurant,
they can list that as a main priority, and the function will adjust the weight of the restaurant's review score when calculating its final score.
Restaurants will be listed in descending order of final score.

This library will have a dynamic review system as well. The restaurants will have a variable called "Comments", which will be a list of strings.
Each string will be a comment from someone who has dined at the restaurant, which could be something like "kid friendly" or "dog friendly". The 
user will be able to specify if anything like this is important to them, and the optimization function will search this variable in every 
restaurant and try to match the keywords, and then factor that into the final score for the restaurant. Users will be able to add a comment about
a restaurant after they have dined there, and there will be a function to add their comment to the list of comments for that particular restaurant.
The restaurants will also have "Reviews" and "Average Review" variables. The "Reviews" variable will have a list of integers, with the integers
being from 0-100, reflecting all of the scores from people that have dined at that restaurant. The "Average Review" variable will be an average of 
all of those scores. Users will be able to add their score out of 100 to the "Reviews" variable for a particular restaurant after dining there.

We will simulate the data for the different restaurants. Using SQLite, we will have a table for every city, which has every restaurant in that 
city. The SpatiaLite extension for SQLite will be used for the geographic coordinates of the restaurants. 

The final library will have: 
- a function that creates a class, called a restaurant profile, for each user, where they can input their preferences for a restaurant and location
- a function that takes a user's restaurant profile and lists the restaurants in the city nearest to them, in order, that it believes the user
will have the best dining experience at
- a function that allows users to add comments or reviews after dining at a particular restaurant
- multiple tests for each function
- a database made using SQLite, that has tables of restaurants data for each city
