# [Maths Plus Revsion](https://maths-plus-revision.herokuapp.com/)

![Image description](/UX/welcomepage.jpg)

This is a revision app for  
students taking the maths 11 plus
13 plus and 16 plus exams.

I designed a revision app for students who are studying for demanding 11 plus, 13 plus and 16 plus exams in maths.  The exams are hard work and currently there is no existing central resource for students to use.  Thus the idea was to put useful past and practice papers with markschemes and advice, together in this app.  The app is to be used by students and parents.

Students can view and order one paper and its associated markscheme for free and then they can order extra papers and markschemes using stripe.
The app was deployed to heroku and can be accessed by clicking on the title above.   Alternatively here is a link to the [heroku app](<https://maths-plus-revision.herokuapp.com/>)

## UX

### User stories

1. Each user has a unique username chosen by them and password and a user profile showing past and present orders.
2. Users can choose to reset their password when needed.
3. A user who has forgotten their password can be issued with a temporary password, go onto the site,then reset their password using a given link.
4. A user can see 11 plus, 13 plus and 16 plus papers to select from without logging in.
5. A user can only purchase 11 plus, 13 plus or 16 plus papers if they are logged in.
6. If a user attempts to buy these papers without login in, the app will direct them to login.
7. Once logged in, the user can checkout items in the cart.
8. A user will see a message on the screen stating that they are logged in.
9. If a user does not have an account they will be directed to create one.
10. Once a user has created an account, they will see a message on the screen informing them that their account has been successfully created.
11. A user can select items to be purchased and each item selected will be added to their cart.
12. A user will be able to view all the items in their cart.
13. A user can choose to checkout items using the checkout button.  At checkout a user will be asked for their details.
14. Checked out items will be paid for using credit or debit cards.
15. The user will get an acknowledgement of payment.
16. A user can access a blog on the app from the main menu.
17. The blog will contain tips on learning maths and ideas on how to measure progress made.
18. A contact address appears on the about us page for users to use if required.
19. A logged in or logged out user can see a blog which gives extra information on study skills and learning maths.
20. A user can see how many times each post has been viewed together with the name of the author and the date the blog post was created.

## Design features

* The navbar must appear on every page so that the user can easily navigate between pages.

* The navbar has the title of of the website, "Maths Plus Revision" on the left hand side.  If a user clicks on this they are taken to the Papers page.

* The home page shows the following items in the navbar:  "MathsPlusRevision", "About Us", "Register", "Log in", "Blog", "Cart"

![Image description](/UX/welcomepage.jpg)

* A logged out user can see all these items and can select papers to purchase, but they will need to either log in or register an account in order to purchase papers.

* On logging in or creating an account a user is first take to the about us page which gives some information about the site.  A user will know that they are logged in as a message will appear on the top left of the screen.

![Image description](/UX/loggedinpage.jpg)

* Once a paper has been selected and has been put in the cart, the user is taken to the checkout page. The cart icon will change to show the number of items in the cart and the user can then click on checkout to buy these papers.
![Image description](/UX/cartpage.jpg)

* A logged out user will see a logged out message on the screen to indicate that they are logged out.
![Image description](/UX/loggedoutpage.jpg)

* The blog page can be seen by all users regardless of whether or not they are logged in.
![Image descritption](/UX/blogpage.jpg)

## Technologies Used

* [HTML](https://www.w3schools.com/html/)

Hypertext markup language is used to create the structure of web pages. It consists of tags which tell the browser how to set out text and images on the page. Hypertext is the method by which you move around on the web, markups are the tags which set out the structure of the webpage, thus HTML is a language for web creation with its own structure and syntax. The data in the tags is read by the web browser enabling you to create any web page you like. In this project my templates are all written in HTML. There is a template for adding, deleting, editing and adding recipes as well as one for viewing information about each island. The base template sets out the way in which the website should look and information from this is used in each of the other templates.

* [CSS](https://www.w3schools.com/Css/) stands for Cascading Style sheets which is a type of style language which sets out how the webpage should be styled. It allows the user to style the webpage in a particular way, making the UX richer and more meaningful for the user.

* [Django](https://www.djangoproject.com/)
is a web development framework that assists in building and maintaining quality web applications. Django helps eliminate repetitive tasks making the development process an easy and time saving experience.

* django templating language

The django templating language is a templating language which is used for rendering data in html templates and is used for communication between the front end and back end of an app.

* [jquery](https://jquery.com/) is used to simplify DOM manipulation. Jquery is a javascript library that is used to provide interactivity on websites. The $ sign signals to the browser that jquery is being used.

* [python](https://www.python.org/psf-landing/) is a high level programming language used for apps in many frameworks such as flask, pyramid and django. Python supports many programming paradigms and is object orientated and has a comprehensive set of libraries. Python is managed by a non profit organsation the Python software foundation.  The version of Python I used in my app is 3.7

* [Postgres](https://www.postgresql.org/)

I used Postgres for the models in my database, although sqlite3 was available in django. Mongodb is a document database that provides the user with the facility to create, read, update and delete documents in a database. Mongodb documents are stored in collections in json or bson format and this makes it easy to work with in Python and other programming languages.

* Heroku

Heroku is a cloud platform that allows a developer to build, deliver, scale and monitor apps. Heroku makes the experience of deploying an app relatively straightforward.

* [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools/)

I used chrome developer tools to work on my code. Chrome dev tools are a set of tools designed to give the developer tools to amend code in a testing environment in order to enhance the UX and functionality experience. I was also able to test the responsiveness of my app using these tools.

## Databases used

[SQLite3](https://www.sqlite.org/index.html) is a database provided by django and is the default database for django projects.
[Postgres](https://www.postgresql.org/) is an open source relational database.

Django does not determine a type of database to be used.  I decided to use two types of databases.

## Data Models used

In Django, data models are the databases which store data about the objects in the database.  The MathsRevisionPlus app used 2 models in addition to the django provided user model which stored details of users.  The models were:

### Product model

Name | Key in db | Validation| Fieldtype
-----|----------| ----------|-------
Name| name |maxlength=254|Charfield
Description|description|no maxlength|Textfield
Price|price|maxdigits=6, decimalplaces=2|Decimalfield
Image|image|nomaxlength|Upload to images

### Order model

Name | Key in db | Validation| Fieldtype
-----|----------| ----------|-------
Fullname| full_name |maxlength=150|Charfield
AddressLine1|address_line_1|maxlength=150|Charfield
AddressLine2|address_line_2|maxlength=150, blank=True|Charfield
Town/City|town_or_city|maxlength=150|Charfield
County|county|max_length=150,blank=True|Charfield
Postcode|postcode|max_length=10|Charfield
Date ordered|date_ordered|default=date.time.today|DateField

* An order is created first before order line item is created as orderline item connects to order using a foreign key.

### OrderLineItem model

Name | Key in db | Validation| Fieldtype
-----|----------| ----------|-------
Order| order |maxlength=150|Charfield
Product|product|maxlength=150|Charfield
Quantity|quantity|maxlength=150, blank=True|Charfield

*An instance of orderlineitem is only created on receipt of an order by a user for each item the user selects and places in the cart so it uses a foreign key.

### Posts model

Name | Key in db | Validation| Fieldtype
-----|----------| ----------|-------
Title| title |maxlength=200|Charfield
Content|content|no maxlength|Textfield
Created date|createddate|dateformat = 6 chars|DateTimefield
Published date|publisheddate|dateformat=6 chars|DateTimeField
Views|views|no max length|IntegerField
Tag|tag|maxlength=30|Textfield

## Testing

Testing was carried out by human beings.

* Manual Testing

 Log in page:

Ensure that only registered users can login. If an unregistered user tries to log in they are directed to the register page.

A message is shown that tells the user that they are logged in or that they have created an account.

* Papers
 Check that one paper in each set of 11 plus, 13 plus and 16 plus is free to order.  Other sets of papers cost £10 each.

* User profile
 Check that the user profile for each registered order is up to date and accurate.

* Cart
Check that the items purchased by users are transferred to the cart ready for checkout.

* Checkout

Check that only the items in the users cart are available for checkout and that the checkout process works.  The user is shown a message to say that checkout has been successful for each order.

## Interesting bugs or problems I discovered during testing

The most annoying bug I came across was when I was trying to push my code to heroku. I followed the instructions above but got an error 500 after each attempt. Despite looking at my code in detail I couldnt find anything wrong with it. My mentor suggested that my environment variables may be incorrect or missing, and once I looked into this I discovered that this was the case.  Once I corrected my mistakes with my environment variables, I was able to push to Heroku with no problems.

After I pushed my app to heroku I needed to change some details and needed to remember to set debug back to true in the cloud9 editor. However on more than one occasion I forgot to change debug back to false resulting in error messages.

I also discovered that the cloud9 editor can be temperamental and had to log off and log back on several times on some occasions so that I could run my code.

Development process of my project

I created a new folder for my project.  
I created a virtual environment and installed django in this.

I then created a new django project, called mathsplusrevision in vscode as well as a .gitignore folder ready to hold files that I didnt want to push to github.
My settings.py file contained the list of apps that I created as I created my project.  The apps I created were

* media
This app would hold pictures of images for the products that would appear on the website.
* products
This app contained information about the products I was selling including models for the database design.
* search
This app contained code for searching the app for a particular item and then displaying it on the screen.
* accounts
This app allowed a user to create an account.
* cart
This app enabled a user to place items on the cart ready for purchase.
* checkout
This app enabled a user to checkout and pay for their purchases.
* blog
This app contained a blog with tips on how to successfully learn maths needed to pass the relevant exams, and finally
* review
This app allowed users to rate and review their purchases.

I created a static folder for my images and my styles.css files and a templates folder for my templates.
Next thing was to set up my base template folder with four files inside:  base.html,  and registration.html.

Effects for the nav bar were put into my styles.css file which was in the static folder.
In my django virtual environment, I imported all the modules I would need and put this in git ignore.  I then set up a stripe account and used the secret and publishable key from my env.py file.  I ensured that the keys could only be accessed from this and not on public display on github.  
At this point I pushed my app to heroku in readiness for the final push to heroku later on. This meant I had to create my procifle and requirements file in order for the app to run.

Lastly I checked that the entire app worked before doing a final push to heroku, making sure that my environment variables were correctly input into the heroku dashboard for the app and that debug was set to false so that the app was secure.
My mentor had a look at my project and advised some changes, so I needed to set debug to true in my cloud9 editor whilst I made these changes, then I needed to remember to set debug back to false before pushing to heroku again.
Finally I created a favicon for my app, using a freefavicom creator

## Deployment

The following section describes the process I undertook to deploy this project to Heroku.

1. I ensured that all required technologies were installed locally, as per the requirements.txtfile.
2. I ensured that I had created a procfile indicating that my app was based on python.
3. I used the bash terminal to log in to Heroku, using 'heroku login' command. Input Heroku login details.
4. I then created a new Heroku app, using heroku apps:create appname command.
5. I pushed my project to github and enabled automatic link to heroku.  This took some time to set up as I had to make sure that my environmental variables were correct.
6. I then logged into Heroku and selected newly created app.
7. Then from the 'More' menu on the top right, I selected 'Restart all dynos'.
8. I checked that my app was now deployed via Heroku

## Breakdown of steps involved in creating my django app

 Initially I found django really difficult.  Although I had gone through the CI videos several times, it all seemed so disjointed, jumping around all over the place and so many files in different folders, some folders with the same name, so I spent many hours trying to work out how the code all fitted together.  I looked at you tube videos and 2 udemy courses which I viewed several times before getting django sorted out in my head.  The steps below indicate the steps I took to produce my app.

 1. First I created a virtual environment and made a .gitignore file.  I then installed django.
 2. I put all my virtual environment files and database files into .gitignore so that they would not be pushed to github.
 3. I then created a new github repo and initialised a local repo for my project.
 4. I then created a project using djano-admin start project command, giving my project the name mathsplusrevision.
 5. I set up my project in heroku - linking my github account to heroku so that each time I pushed to github I also pushed to heroku.  This took some time as initially my environmental variables were incorrect in heroku and it took a while to figure out what was wrong.
 6. I then created my env file to hold all my passwords for my database and my secret and publishable keys for stripe.  This file was put in .gitignore.
 7. I then ensured that my settings were correct in my settings.py file in my project.  This meant that I had to ensure that heroku was included in my allowed hosts and that my apps were added as I created them into my installed apps list.
 8. I then started creating my apps.  The first one I created was my accounts app which was cloned from the CI site.  Sounds easy but there were changes I had to make to this app to make it work, and as I had chosen to use django 2.2 instead of django 1.11 these changes took some time to sort out.  
 9. I had to remember to create a requirements.txt file as I downloaded different packages for my app as I went along. Pillow was used to handle images and whitenoise for my media files.
 10. I created an overall templates folder which contained my base.html file which controlled the way in which the app which initially be rendered to the screen.  This file contained the code for my navbar and the general layout of the initial screen.  Within my accounts app I created another templates folder which contained four html files- login, index, profile and register.  Each file took its main format from the base.html file and displayed appropriate messages to the user for loging in, registering and displaying a loged in users profile.
 11. Whilst working through the accounts app, I regularly saved my work to github.  I also tried to get travis to work several times without success.  I put a link to travis in this readme file and also created a .yml file but despite my best efforts I was unable to get travis to work and the build kept failing, despite the app working as required.  I know that there is an issue with travis working with python 3.x and django 2.x so this is something I will need to keep working on after the submission of this project.
 12. I created the model for my accounts app before creating the views and urls. In my accounts app, I added my url patterns to the url.py file and in my views.py file I added in the python code to render the appropriate view for a user depending on whether they were logging in, displaying their profile once logged in or registering for an account.
 13. I then moved onto creating my products app, which would store details of all the papers for sale on the mathsplusrevision app.  First I created the models for the products app, then the views and the urls, adding patterns for the urls to the app, and finally ensuring that the products app was present in the installed app section of the settings.py file.
 14. I created a templates folder inside my products app which contained the products.html file which contained the logic for rendering the products app to the website.
 15. During the creating of my products app I pushed to github and heroku after each bit of functionality had been added.
 16. I then created my search app so that products could be searched for by a user.  I made sure that this was included in my installed app list in my settings.py file and that the url patterns were in the urls.py file in the search app.  Views.py in the search app contained the logic for rendering results of the search to the screen.
 17. The creation of my static folder was done prior to creating the products or search app so that I could style the way that the results of the search and products app displayed using the custom.css file which was held in the css directory.  Additionally in the static folder I created the font-awesome folder to contain the fonts I would use in the project and the js folder which contained the stripe file, for use when users wanted to buy a product.
 18. I then created my carts app; firstly models, then views.py containing the views for this, then the urls.py containing the urls for the cart app.  Throughout the project I ensured that I used ``python manage.py make migrations`` to ensure that migrations of my models for each app were successful and then I used ``python manage.py migrate`` to ensure that the migrations were applied. I added the cart app to the list of installed apps in settings.py
 19. Finally I created my checkout app, which would enable a user to successfully pay for goods purchased.  I needed to create a stripe account, then install stripe ensuring that my public and private key were carefully stored in env.py and in turn, env.py was put in my .gitignore file.  Again the checkout app was added to the list of installed apps.
 20. At the start of this process I ensured that created a media directory to store all the images of the papers on the website and ensured that the correct code was added to the settings.py file in order for the uploaded images to be stored in this directory.
 21. I created a super user using ``django-admin create superuser`` so that I could add in my products to the products model using the admin dashboard.
 22. I pushed my app to heroku  at regular interavls, I had linked my git hub repo to heroku so it was automatically pushed to heroku each time I made a change to the repo. As the app was working I hoped that the travis build would be fine but I was wrong.  Travis repeatedly failed, so I needed to resort to manual testing.

## Credits

* Media The photo used on the about us page was by Dawid Małecki on Unsplash.

## Acknowledgements

I received inspiration for this project from my mentor Simen Daehlin, fellow students especially family, friends and my teaching colleagues and school students were also very helpful in giving me feedback. I used the django documentation to help me sort things out on a regular basis, although I have to admit that at times it was difficult to understand what to do to sort out a problem and I spent around 80% of my time on this project looking things up on the internet or using the slack room or CI tutors to help me work out how to do something.
