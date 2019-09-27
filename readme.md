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
* [HTML](https://www.w3schools.com/html/)

Hypertext markup language is used to create the structure of web pages. It consists of tags which tell the browser how to set out text and images on the page. Hypertext is the method by which you move around on the web, markups are the tags which set out the structure of the webpage, thus HTML is a language for web creation with its own structure and syntax. The data in the tags is read by the web browser enabling you to create any web page you like. In this project my templates are all written in HTML. There is a template for adding, deleting, editing and adding recipes as well as one for viewing information about each island. The base template sets out the way in which the website should look and information from this is used in each of the other templates.

* [CSS](https://www.w3schools.com/Css/) stands for Cascading Style sheets which is a type of style language which sets out how the webpage should be styled. It allows the user to style the webpage in a particular way, making the UX richer and more meaningful for the user.

* [Django](https://www.djangoproject.com/)
is a web development framework that assists in building and maintaining quality web applications. Django helps eliminate repetitive tasks making the development process an easy and time saving experience.


* Jinja2

Jinja 2 is a templating language which is used for rendering data in html templates and is used for communication between the front end and back end of an app.

* [jquery](https://jquery.com/) is used to simplify DOM manipulation. Jquery is a javascript library that is used to provide interactivity on websites. The $ sign signals to the browser that jquery is being used.

* [python](https://www.python.org/psf-landing/) is a high level programming language used for apps in many frameworks such as flask, pyramid and django. Python supports many programming paradigms and is object orientated and has a comprehensive set of libraries. Python is managed by a non profit organsation the Python software foundation.  The version of Python I used in my app is 3.7

* [Postgres](https://www.postgresql.org/)

I used Postgres for the models in my database, although sqlite3 was available in django. Mongodb is a document database that provides the user with the facility to create, read, update and delete documents in a database. Mongodb documents are stored in collections in json or bson format and this makes it easy to work with in Python and other programming languages.

* Heroku

Heroku is a cloud platform that allows a developer to build, deliver, scale and monitor apps. Heroku makes the experience of deploying an app relatively straightforward.

* [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools/)

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

I then created a new django project, called mathsplusrevision in vscode as well as a .gitignore folder ready to hold files that I didnt want to push to github.

My settings.py file contained the list of apps that I created as I created my project.  The apps I created were: 
* media - this app would hold pictures of images for the products that would appear on the website.
* products - this app contained information about the products I was selling including models for the database design.
* search - this app contained code for searching the app for a particular item and then displaying it on the screen.
* accounts - this app allowed a user to create an account.
* cart - this app enabled a user to place items on the cart ready for purchase.
* checkout - this app enabled a user to checkout and pay for their purchases.
* blog - this app contained a blog with tips on how to successfully learn maths needed to pass the relevant exams, and finally
* review - this app allowed users to rate and review their purchases.


I created a static folder for my images and my styles.css files and a templates folder for my templates.
Next thing was to set up my base template folder with four files inside:  base.html,  and registration.html.

In my base html file I started with html boiler plate then added in the following command '{% block content %} {% endblock %}' so that my nav bar would appear on each page. I created my nav bar using an ordered list. 
Effects for the nav bar were put into my styles.css file which was in the static folder.
In my django virtual environment, I imported all the modules I would need and put this in git ignore.  I then set up a stripe account and used the secret and publishable key from my env.py file.  I ensured that the keys could only be accessed from this and not on public display on github.  
At this point I pushed my app to heroku in readiness for the final push to heroku later on. This meant I had to create my procifle and requirements file in order for the app to run.


Lastly I checked that the entire app worked before doing a final push to heroku, making sure that my environment variables were correctly input into the heroku dashboard for the app and that debug was set to false so that the app was secure.
My mentor had a look at my project and advised some changes, so I needed to set debug to true in my cloud9 editor whilst I made these changes, then I needed to remember to set debug back to false before pushing to heroku again.
Finally I created a favicon for my app, using a freefavicom creator
* Deployment
The following section describes the process I undertook to deploy this project to Heroku.

1. I ensured that all required technologies were installed locally, as per the requirements.txtfile.
2. I ensured that I had created a procfile indicating that my app was based on python.
3. I used the bash terminal to log in to Heroku, using 'heroku login' command. Input Heroku login details.
4. I then created a new Heroku app, using heroku apps:create appname command.
5. I pushed my project to github and enabled automatic link to heroku.  This took some time to set up as I had to make sure that my environmental variables were correct.
6. I then logged into Heroku and selected newly created app.
7. Then from the 'More' menu on the top right, I selected 'Restart all dynos'.
8. I checked that my app was now deployed via Heroku
# Credits
* Content The text for the islands was copied from wikpaedia.

* Media The photos used in this site were obtained from pixabay and pixels. All the photos used in my database were obtained from google images. These do not require creditation as they are used for educational purposes only.

Acknowledgements I received inspiration for this project from my mentor Simen Daehlin, fellow students especially family, friends and my teaching colleagues and school students were also very helpful in giving me feedback. I used pymongo and flask documentation to help me get my code correct. 