# CS340-Project-2

by Afshin E. Ahvazi
Dr. Sherri Maciosek
SNHU CS340-J7659 23WE3

# Introduction
This project combines the Dash web framework and MongoDB to overview useful information to users using data tables and charts, including a geo-location chart. The Dash framework turns creating interactive websites and web applications into a relatively easy task. Just as in HTML, it allows us to create and style web page elements. We can also add behavior to these elements, as if using JavaScript or PHP. MongoDB is a versatile No-SQL database system that is also quick to learn and configure. In addition, it stores data in the so-called documents. These special JSON objects allow us to store many types of data. Furthermore, because these tools have drivers and libraries available for many programming languages, they make for optimal tools for developing web applications.

# App Overview
Let us now focus on this web application. Created for Grazioso Salvare, it allows their users to draw data from a MongoDB database. Users can select their desired data from a drop-down menu. Each item in this list pertains to a group of rescue dogs specific to certain missions, such as water, wilderness or mountain, and disaster and individual tracking rescues. Users may also choose to view all data. The following shows the state of the application when no data categories are selected from the dropdown menu:
However, if the user selects the ‘Water Rescue’ category, the relevant data is presented in a table. For ease of access, users can interact with this table to sort through and filter data. For large numbers of rows, data is divided into multiple pages through which the users can browse.
 
Similarly, here we can see what happens if the user selects the ‘Mountain or Wilderness’ category. Underneath the table, we can also see a geo-location chart that highlights the locations of the animals from the table. Hovering over each map marker reveals more information about the animals, such as their names and breeds.
And finally, here is an app view if users wish to view data from the ‘Disaster Rescue’ category.
 

# Development
The development of this application started by creating the CRUD module from Project 1. This module facilitates performing the CRUD operations on the database with only a single method call. We then began work on the dash elements of the application by creating the data table, followed by the geo-location chart. 
There were many challenges faced during every step of this project. From configuring the table, to the chart, to even displaying the logo of the application. Unfortunately, some challenges were too great to overcome and require more time to complete. This refers to the ‘Dog Breeds’ section of the application, which is meant to display a pie-chart that represents the percentage of various dog breeds from the data table.

# Resources
In addition to the numerous threads on stackoverflow.com and YouTube tutorials, the following resources proved most effective in completing this project.
Dash Documentation
https://dash.plotly.com/
MongoDB Documentation
https://www.mongodb.com/docs/ 
MongoDB Tutorials 
https://learn.mongodb.com/ 
