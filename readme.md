# [Maths Plus Revsion](https://www.theadvisory.co.uk/house-selling/best-time-to-sell-house/)

This is a revision app for  
students taking the maths 11 plus
13 plus and 16 plus exams.

[![Build Status](https://travis-ci.org/debbiect246/mathsplusrevision.svg?branch=master)](https://travis-ci.org/debbiect246/mathsplusrevision)

I designed a revision app for students who are studying for demanding 11 plus, 13 plus and 16 plus exams in maths.  The exams are hard work and currently there is no existing central resource for students to use.  Thus the idea was to put useful past and practice papers with markschemes and advice, together in this app.  The app is to be used by students and parents.

Students can view and order one paper and its associated markscheme for free and then they can order extra papers and markschemes using stripe.


The app was deployed to heroku and can be accessed by clicking on the title above.   Alternatively here is a link to the heroku app. 
<https://maths-plus-revision.herokuapp.com/>

## UX
### User stories
1. Each user has a unique username chosen by them and password and a user profile showing past and present orders.  
2.  A user can see 11 plus, 13 plus and 16 plus papers to select from without logging in. 
3.  A user can only purchase 11 plus, 13 plus or 16 plus papers if they are logged in.
4. If a user attempts to buy these papers without login in, the app will direct them to login.
5. Once logged in, the user can checkout items in the cart.
6. A user will see a message on the screen stating that they are logged in.
7. If a user does not have an account they will be directed to create one.
8. Once a user has created an account, they will see a message on the screen informing them that their account has been successfully created. 
9. Checked out items will be paid for using credit or debit cards.
10. The user will get an acknowledgement of payment.
11. A user can access a blog on the app from the main menu.
12. The blog will contain tips on learning maths and ideas on how to measure progress made.
13. A user can comment on a blog and the moderator of the blog can decide on whether the comment can be put on the app for other users to see.
14. A user can review papers purchased using the review button in the menu.
15. The review button allows the user to give a star rating to a particular paper and to write a review for other users to see.
16. All reviews and ratings are subject to moderation by the owner of the app.
17. A user can contact the owner of the app using a contact form.
18. The contact form will have fields for: title, full name, address, city or region, postcode, country.
19. A user will submit the form using a contact button.

## Technologies Used
* HTML

Hypertext markup language is used to create the structure of web pages. It consists of tags which tell the browser how to set out text and images on the page. Hypertext is the method by which you move around on the web, markups are the tags which set out the structure of the webpage, thus HTML is a language for web creation with its own structure and syntax. The data in the tags is read by the web browser enabling you to create any web page you like. In this project my templates are all written in HTML. There is a template for adding, deleting, editing and adding recipes as well as one for viewing information about each island. The base template sets out the way in which the website should look and information from this is used in each of the other templates.

* CSS

stands for Cascading Style sheets which is a type of style language which sets out how the webpage should be styled. It allows the user to style the webpage in a particular way, making the UX richer and more meaningful for the user.

* Django

* Jinja2

Jinja 2 is a templating language which is used for rendering data in html templates and is used for communication between the front end and back end of an app.

* jquery

jquery is used to simplify DOM manipulation. Jquery is a javascript library that is used to provide interactivity on websites. The $ sign signals to the browser that jquery is being used.

* python

I used Python version 3.7 to run my app. Python is a high level programming language used for apps in many frameworks such as flask, pyramid and django. Python supports many programming paradigms and is object orientated and has a comprehensive set of libraries. Python is managed by a non profit organsation the Python software foundation.

* Postgres

I used Postgres for the models in my database, although sqlite3 was available in django. Mongodb is a document database that provides the user with the facility to create, read, update and delete documents in a database. Mongodb documents are stored in collections in json or bson format and this makes it easy to work with in Python and other programming languages.

* Heroku

Heroku is a cloud platform that allows a developer to build, deliver, scale and monitor apps. Heroku makes the experience of deploying an app relatively straightforward.

* Chrome Developer Tools

I used chrome developer tools to work on my code. Chrome dev tools are a set of tools designed to give the developer tools to amend code in a testing environment in order to enhance the UX and functionality experience. I was also able to test the responsiveness of my app using these tools.
## Testing
Testing was carried out by human beings.

* Manual Testing

 Log in page:

Ensure that only registered users can login. If an unregistered user tries to log in they are directed to the register page.

A message is shown that tells the user that they are logged in or that they have created an account.

Papers:
Check that one paper in each set of 11 plus, 13 plus and 16 plus is free to order.

Other sets of papers cost £10 each.

User profile
*Check that the user profile for each registered order is up to date and accurate.

Cart
*Check that the items purchased by users are transferred to the cart ready for checkout.

Checkout

Check that only the items in the users cart are available for checkout and that the checkout process works.  The user is shown a message to say that checkout has been successful for each order.

Interesting bugs or problems I discovered during testing.

The most annoying bug I came across was when I was trying to push my code to heroku. I followed the instructions above but got an error 500 after each attempt. Despite looking at my code in detail I couldnt find anything wrong with it. My mentor suggested that my environment variables may be incorrect or missing, and once I looked into this I discovered that this was the case.  Once I corrected my mistakes with my environment variables, I was able to push to Heroku with no problems.

After I pushed my app to heroku I needed to change some details and needed to remember to set debug back to true in the cloud9 editor. However on more than one occasion I forgot to change debug back to false resulting in error messages.

I also discovered that the cloud9 editor can be temperamental and had to log off and log back on several times on some occasions so that I could run my code.

Development process of my project

I created a new folder for my project.  
I created a virtual environment and installed django in this.

I then created a new django project in vscode as well as a .gitignore folder ready to hold files that I didnt want to push to github.


I created a static folder for my images and my styles.css files and a templates folder for my templates.
Next thing was to set up my base template html file and my app.py file.
In my base html file I started with html boiler plate then added in the following command '{% block content %} {% endblock %}' so that my nav bar would appear on each page. I created my nav bar using an ordered list. Effects for the nav bar were put into my styles.css file.
In my app.py file I imported all the modules I would need and then set up a secret key and set my debug to True so that I could get an error log if there was something wrong with my code I could sort it out with the help of the error log. I also set up my secret key as part of my cookie encryption.
At this point I pushed my app to heroku in readiness for the final push to heroku later on. This meant I had to create my procifle and requirements file in order for the app to run.
I created my database in mlab. This consisted of 3 collections: 1 for my recipes, 1 for the Caribbean islands and 1 for my users. The recipe collection was used to hold details of all my recipes. My caribbean island collection held the details of 21 Caribbean islands. My user collection held the names and passwords of all users of the recipe app. It was used to endure that only recipe authors could edit their own recipes and also enabled users to login to the app.
I created an admin user, creating a login and password in this format, noting this format as I would need it later to put in my config.py file mongodb://<dbuser>:<dbpassword>@XXXXXX.mlab.com:XXXXX/recipe_manager
I entered 8 recipes into my recipe collection,which consisted of 15 key values in json format. Schema for my recipe collection:

I returned to my app.py page to connect my database to my app. I entered the environment details in to my config.py file and then put this in gitignore. I also created my procfile and my requirements.txt file.
I then built my allrecipeslist page so that my recipes would display on the screen. Initially I used accordian format from materializecss but then changed the display to cards on the advice of my mentor. I checked that the allrecipeslist page worked, and that summary information was displayed on the front of the card with a picture of the recipe, and on clicking on the three dot icon on the right hand top side of the card, the flip side of the card would then be shown together with the ingredients and method for making the recipe.
I then put together my addrecipes and editrecipes pages using addrecipes page as a template for my editrecipes page.
I checked that both my addrecipes and editrecipes pages worked ensuring that a user could add a recipe and only the author of the recipe could edit a recipe.
I returned to my allrecipeslist page and put in a link to my islands collections so that users could find out more about the island a recipe came from. This involved building an island page which displayed a picture of the island, a picture of the map of the caribbean and some information about the island. Users checked that this worked.
Finally I built my findrecipe page. This enabled a user to find a recipe which was either a lunch, dinner or dessert recipe, or to find a recipe which contained meat, fish, vegetables or sugar. Users could also search for recipes which came from speificifed islands, or search for recipes which did not contain specified allergens. As part of this I created a results page which displayed the results of each search.
I then created a login and register page. The login page allowed registered users to access the app, and if a user was not registered, then the register page enabled them to register.
Lastly I checked that the entire app worked before doing a final push to heroku, making sure that my environment variables were correctly input into the heroku dashboard for the app and that debug was set to false so that the app was secure.
My mentor had a look at my project and advised some changes, so I needed to set debug to true in my cloud9 editor whilst I made these changes, then I needed to remember to set debug back to false before pushing to heroku again.
Finally I created a favicon for my app, using a freefavicom creator
Deployment
The following section describes the process I undertook to deploy this project to Heroku.

I ensured that all required technologies were installed locally, as per the requirements.txtfile.
I ensured that I had created a procfile indicating that my app was based on python.
I used the bash terminal to log in to Heroku, using 'heroku login' command. Input Heroku login details.
I then created a new Heroku app, using heroku apps:create appname command.
I pushed my project to Heroku, using push -u heroku master command.
Then I created scale, using heroku ps:scale web=1 command.
I then logged into Heroku and selected newly created app.
I then selected settings. Select 'Reveal Config'. I then added IP 0.0.0.0 and PORT 5000.
Then from the 'More' menu on the top right, I selected 'Restart all dynos'.
To view my app, in settings I selected the Domain URL, NOT Git URL to view your hosted application.
I checked that my app was now deployed via Heroku
Credits
Content The text for the islands was copied from wikpaedia.

Media The photos used in this site were obtained from pixabay and pixels. All the photos used in my database were obtained from google images. These do not require creditation as they are used for educational purposes only.

Acknowledgements I received inspiration for this project from my mentor Simen Daehlin, fellow students especially family, friends and my teaching colleagues and school students were also very helpful in giving me feedback. I used pymongo and flask documentation to help me get my code correct. 