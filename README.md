# Overview

In this Django web app project my main goal was to learn the basics of Django development. I had never done anything in Django prior to this project, and all of the learning in this project was done through Django documentation and free online tutorials. 
The web app I wrote is a polling app that displays polls for people to vote on, in addition to functionality for people to create their own polling questions and options. 
All of the polling data is stored in the built in Django SQLite database using the django.db models function. A model is generally a set of information that is going to be saved into a database, and the model class automatically build the database from the input data. 
The reason I wrote this web app is because I couldn't find a reliable free polling site online, so I figured I could make one, and also because the project scope seemed like something that could be done in the two week time frame that I worked within.

[Software Demo Video](http://youtube.link.goes.here)

# Web Pages

I have a few different web pages in my app. The home page is the default page that displays all of the available polls to be voted on, the voting page allows users to vote, the results page displays the results of all votes, and the create page allows users to create a new poll. 
The HTML on the site was from a template because the tutorials main focus was to learn Django and not HTML, that is for another time.  
Inside of each page the poll data is dynamically pulled from the SQLite database to populate the different HTML tags. This is done by passing in the poll database information as context inside fo the views.py file for each webpage. 

# Development Environment

- Django-admin 3.2.8
- Python 3.9.7
- widget_tweaks (library)
- VSCode

# Useful Websites

* [Django Documentation](https://docs.djangoproject.com/en/3.2/)
* [Django for Beginners in 1 Hour](https://www.youtube.com/watch?v=rHux0gMZ3Eg&t=3202s)
* [YouTube](http://youtube.com)

# Future Work

* Deleting Polls from the Database
* Displaying all of the available poll results on one page (in progress)
* Options to have multiple people vote before results are displayed
* Visualizations from the data (pandas, altair?)