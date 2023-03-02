# Creating a web application with Python

## Introduction
This is a *very* simple and basic introduction to building a web application using a language that is not necessarily associated with web technology, Python. Python has been for a number of years, and remains, the most popular programming language in the world (on, for example, the [TIOBE Index](https://www.tiobe.com/tiobe-index/) as of February of 2023, among others). Along with R and Matlab, Python is also one of the favourite languages of code-writing researchers from non-computer related disciplines, as well as one of the easiest languages to learn to code with.

One of Python's advantages (or disadvantages, depending on your particular point of view or objectives), is in being a very general-purpose language rather than a highly specialised one (like R or Matlab for statistics, or JavaScript for the web). You can do pretty much anything in computing with Python -- and although this is also true for any [Turing-complete programming language](https://en.wikipedia.org/wiki/Turing_completeness), in Python that aspiration is actually feasable. And that includes writing for the web.

Although this is a basic tutorial, it assumes a basic understanding of Python, and (at least) a reading understanding of HTML. In this tutorial we will explore a simple approach to creating a webapp using Python, using a particular framework (Flask) for its simplicity and relative lightweight (other options are available and we will talk briefly about the most famous one soon). Perhaps, before diving right in, it would be beneficial to define what we mean by a webapp (and why is that different from a webpage), why and when you might want to use Python to create it, and what are the most popular Python frameworks to create it with.

### 1. What is a webapp
If we are about to create one, perhaps we should clarify what we mean by a web application: the crucial difference between a web application and a simple web page or site (i.e., a collection of interlinked web pages using the same domain name) is that an application allows the user to interact with a piece of software through the web; i.e., in simple terms, there is some form of calculation being performed at some point to generate the content the user can access, even if its end-product is a static read-only file. Any website that changes its content based on user interaction, or allows for user registration and personalised content, or performs a calculation, however simple, can be thought of as a web application.

This distinction between webapps and web pages is more or less irrelevant in most applications; though if you only intend to have a static page with your name and contact (i.e., a stable personal page, a place for people interested in you to visit), having a full-blown app is probably overkill: it will be cheaper, and quicker, to simply write a plain html page. If, on the other hand, you want your users to be able to explore some of your research code directly on your page (think, for example, a dashboard-style data explorer), you are probably looking at some form of web application.

If you really want to get into the technical weeds, you might see terms like [Progressive Web Applications](https://en.wikipedia.org/wiki/Progressive_web_app) (i.e., apps that are designed to work regardless of the platform used by the user, be it mobile iOS, Android / desktop MacOS, Windows, Linux, etc. -- think about it like a mobile app that you access through the browser); [Single-Page Applications (SPA)](https://en.wikipedia.org/wiki/Single-page_application) that re-write the content of the page based on user interaction (like Twitter or Facebook, for example), or Multi-Page Applications (MPA), which are closer to a traditional website with new content being generated at the same time as the page itself and, therefore, demanding navigating away from it to see different content (or refreshing the page). This [Medium article](https://medium.com/@NeotericEU/single-page-application-vs-multiple-page-application-2591588efe58) gives you a good overview of the differences between, and respective advantages and disadvantages, of SPAs and MPAs.
### 2. Why and when to use Python
So, assuming you know you *need* a webapp rather than a simple static webpage, and that you want (or need) to code it yourself (rather than using a bloated Content Management System), why would you choose to do it in Python? The answer is probably simpler than you expect: more likely than not, you choose to write your app in Python because you either 

1. are already confortable with Python, or 

1. are willing to learn a little more about coding, and are more confortable learning Python than other languages; or 

1. you already have a piece of (research) code in Python that you want visitors to your page to be able to interact with.

There is nothing wrong with any of these reasons however, all other things being equal, you should keep in mind that Python is not necessarily better than any other approach to creating a webapp -- and in some cases, it might be a bad option. Not to go into too much detail here but, one thing to keep in mind *before* creating your app is whether you need server-side processing in your app -- with a Python webapp, the calculations are made in a computer elsewhere and only the result is shown to the user. In practical terms, this means that some of the cheaper web hosting solutions will not work for you, and you might need to spend a little more to keep your app online.

The most unavoidable reason to create a Python webapp is the one outlined in point 3: you have a piece of code that you need to interact with that is already in Python. In this case, writing a native Python webapp is probably the easiest, simplest, and probably cheapest solution. For any other use cases, Python is *always* an option, which will be better or worse suited depending on your specific use case.

However, if you are here, you probably *want* to write in Python. So, how exactly do you go about doing it? Because Python is a Turing-complete language, you *could* write the entire system from the ground up without using any additional tools and libraries. But just because you *can*, doesn't mean you *should*: the vast majority of basic operations that you would need to create -- from generating HTML files, serving them to a browser, giving error messages, etc -- have all been written already. If you've used Python in the past, you'll also know that one of its biggest advantages is in the giant community of users around it that wrote `libraries` for just about anything you could think of. When you put a series of libraries together with a common language of interaction between them, you have a `framework`. So, to write a webapp quickly and efficiently, you first need to choose your framework.

### 3. What are your framework options?
There are web frameworks for nearly every conceavable programming language out there. Some of the big hitters include [Ruby on Rails](https://rubyonrails.org/) (for Ruby), [Laravel](https://laravel.com/) for PHP, or [Rocket](https://rocket.rs/) (for Rust). If you are into Javascript, you are in luck (or hell): JS is absolutely (and appropriately, since we are talking about a web-focused language) littered with web frameworks, including but not limited to: [AngularJS](https://angularjs.org/), [VueJS](https://vuejs.org/), [React](https://reactjs.org/), and [Svelte](https://svelte.dev/). Python is similarly well served with frameworks though the two most popular ones are [Django](https://www.djangoproject.com/) and [Flask](https://flask.palletsprojects.com/).

####   1. Django
Django is a powerful Python web-framework that is particularly well-suited for creating webapps that have extensive interaction with, and dependence on, databases. In fact, one of Django's headline features is the inclusion of a simple but effective CRUD (Create, Read, Update, Delete) interface that can be used in development as a sanity check. Out of the box, it comes with most everything any web developer could wish for but, on top of that, it was built to be extensible. As a consequence there are hundreds of libraries that allow you to add additional functionality to your website. It is based on a [Model-View-Template(MVT)](https://www.javatpoint.com/django-mvt#:~:text=The%20MVT%20(Model%20View%20Template,layer%20which%20handles%20the%20data.) architectural pattern, as opposed to many JS frameworks that implement a [Model-View-ViewModel(MVVM) pattern](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93viewmodel). Some users complain about the level of difficulty in getting up and running with Django, so let that be a warning to you; for many webapps, a fully featured framework like Django is overkill, which means that the packages end up becoming more bloated and harder to manage than necessary. If only there was a similar solution that was lightweight, just as extensible, and easier to learn, you are all thinking. Enter Flask.
####   2. Flask
##### 1. What is Flask?

[Flask](https://flask.palletsprojects.com/) is one of the most popular, if not the most popular, web framework for Python, often trading places with Django for the top spot. Flask is sometimes called a *micro* web framework because it is stripped of many of the features that come as standard in other frameworks. Out of the box, it doesn't include any database tools, form validation, user management, or anything else that is already served by other common libraries. It is, however, designed to be highly extensible, and all this functionality (and much more) is easily available if needed.

Like Django, Flask uses the Model-View-Template (MVT) architecture and, therefore, is best suited for multi-page applications. You can use Flask to create Single Page Applications, but that (usually) involves some additional JavaScript and/or the addition of a [WebSocket](https://en.wikipedia.org/wiki/WebSocket) library (depending on your needs, of course).

Another great advantage of Flask (when compared with Django), is its ease of use -- you can (and today you will) -- have a webapp up and running mere minutes after being introduced to Flask.

##### 2. Why and when to use it?
There are as many use cases as there are Flask projects -- that is to say, you can use Flask whenever and for every purpose you can think of (but remember to think about whether you *should*). That being said, Flask projects usually fall within one or more of these groups:

1. You need a relatively lightweight framework;
2. You need to put something together very quickly as an minimum viable product (MVP)
3. You want the flexibility to extend the project as needed without having to deal with unnecessary complexities from the start.

If this sounds like you, then Flask might just be the answer. Flask is also used often by researchers to cobble together a simple [RESTful API](https://en.wikipedia.org/wiki/Representational_state_transfer) (using, for example, the [`Flask-RESTful` extension](https://flask-restful.readthedocs.io/en/latest/)) to serve another larger project. Although there are other, more focused, frameworks that achieve the same objective in Python, Flask is often chosen for its simplicity and familiarity.
## Hands-on

### Your first Flask page
Now that we have all that introduction out of the way, it's time to get our hands dirty with Flask. In this section we will construct a dummy webapp, learn how to create simple pages, and display results to the user.

#### Before you begin

##### 1. Requirements

To start working with Flask, all you need is to have Python installed in your system, and access to an Integrated Development Environment (IDE). Although an IDE is not strictly necessary, it will make your job easier in the long run. You can use the default IDLE that comes pre-packaged with Python, but I'd recommend something a little more powerful like [VS Code](https://code.visualstudio.com/). In this tutorial, we will be using VS Code.

###### Install Python
- Head over to the [Python webpage](https://www.python.org/)
- Click the `Downloads` page
- Download the latest version for your system
- Once the download is finished, execute the downloaded file and follow the instructions on the screen.

###### Install VS Code
- Head over to the [VS Code webpage](https://code.visualstudio.com/)
- Download the correct version for your system
- Execute the downloaded file and follow the instructions on your screen

Create a new folder anywhere on your system: call it something like `my-first-flask-project`. Open VS Code, choose `Open Folder` and open the folder you just created.

##### 2. Create a Virtual Environment

If you followed the instructions, you should have an open project on VS Code called `my-first-flask-project`. If so, we are ready to start.

The first thing to do is not exclusive to Flask development, but rather good practice for every Python project. We will begin by creating a [virtual environment](https://realpython.com/python-virtual-environments-a-primer/). This will allow us to install all the libraries we will need for our project without messing up our default python installation. Start by:

1. Open a terminal on VS Code (either with `Ctrl+Shift+'` or `Terminal>New Terminal`)
2. In the terminal use `venv` to create a new virtual environment. The syntax for creation is:

```
python3 -m venv [dir-for-virtual-environment]
```
In our case, this will be:
```
python3 -m venv env
```
If you are using windows, you might run into an error -- if so, whenever you see `python3` use `python`. For example, in this case, it will be:
```
python -m venv env
```
If all went well, you should see that a new folder was created in your project directory (called `env`). All we need to do now is **activate** the virtual environment by using the following command in the terminal:
```
.\env\Scripts\Activate
```
Your terminal should have changed slightly -- you might notice that now, before the command prompt there is an `env`. That's good, it means that from here on out, every Python command we make will be executed in this environment.

During development, VS Code will automatically look for virtual environments and activate them by default, but because we haven't created a python file yet, we had to activate it manually.

Finally, if you are using `git` to track your project, you might want to add the `env` folder to your `.gitignore` file.
##### 3. Install Flask
Make sure your virtual environment is active. Then, simply type this command into the terminal:
```
pip install Flask
```
That's it! It shouldn't take more than a few seconds, and now you have Flask available. It's time to create our first page.
#### Creating your first page

##### 1. Folder structure
Folder structure is very important for Flask: your main app files will live in the root directory of your project. Other files (templates, javascript files, CSS files) will have their respective places (respectively in `\templates`, `\static` and `\static\style`)

2. `app.py`

Let's start, then, by creating our main python file. We'll call it `app.py`. We don't have to call it that necessarily, but that is the convention. This file will be in the **root** of our project.

3. Importing Flask

We begin by importing Flask into our file. At the top of the file, write:

```python
from flask import Flask
```
(note the lowercase in the first, and the Uppercase in the second 'Flask')

4. Hello world

The first thing to do is to create a Flask object, and we do that like any other variable. Simply:

```python
app = Flask(__name__)
```
So `app` is our variable, and we've initialised a Flask object by calling the constructor `Flask(__name__)`

Now all we need to do is create a function to return our desired webpage. In this case, all we want is a simple `Hello World!` page. So, we begin by creating a simple function that will return that string:

```python
def hello_world():
    return 'Hello World'
```
However, for this to work as a webpage, we need to tell Flask *when* this function needs to be invoked. In this case, it will be whenever someone visits the root of the website. To do that, we simply add a [`decorator`](https://realpython.com/primer-on-python-decorators/) above the function definition. So, our `hello_world` function will look like this:

```python
@app.route('/')
def hello_world():
    return 'Hello World'
```

The decorator (indicated by the `@`) will call the method `route` on the `app` Flask object we created above. The argument we are passing (`'/'`) is the address (the route) that will call the function.

So, at the end of this process, our `app.py` should look like this:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
```

5. Running the app
To run the app, we once again turn to the terminal and execute the command:

```bash
flask run
```

You should see a message like `* Running on http://127.0.0.1:5000`. Now, you open a web browser to that address and *ta da*, you just managed to create your first webapp using Flask. It really is that simple. To stop the webserver, simply use `Ctrl+C` on the terminal (or press the `Stop` button in VS Code.)

#### More pages, more views, more variables
##### Creating more pages
To create more pages, you simply create more functions that will return a different page (each with its own `route` decorator pointing to a specific address). So let's try that: let's create an `about` and a `contact` page. To our `app.py`, we'll add:

```python
@app.route('/about')
def about():
    return 'This is the about page'

@app.route('/contact')
def contact():
    return 'This is the contact page'
```

If now you visit your page on a browser, it will seem like nothing has changed. What you need to do is visit the newly created pages: simply go to http://127.0.0.1:5000/about or http://127.0.0.1:5000/contact and you should see your new pages.

##### Passing variables to pages
Having pages that simply return static strings might be neat, but it is also pretty useless. The whole point of having a dynamic webapp is that we can change the content based on user interaction, so we need a way of passing variables to webpages. The simplest way to do so is to pass the variable via a URL. So, let's create a page that greets the user by name. The decorator will look like this:

```python
@app.route('/welcome/<name>')
```
Notice that after the 'welcome' we have a new page between angle brackets. Our function will, correspondingly look slightly different:

```python
def welcome(name):
    return 'Welcome ' + name
```

The main difference is that our function now receives a variable (called `name`) which is the same variable we're passing thorugh the URL. So if we run the app and visit the `/welcome/` page, whatever name we put at the end of the address will appear on the screen. If you attempt to visit `/welcome`, you will get an error: this is because we don't currently have a route that will generate a welcome page without a name.

Another thing to note is that whatever the variable name we choose for the URL needs to be the same for the argument in the function (i.e., you can't have `<user>` and `welcome(name)`) -- that's how Flask knows what variable to pass to the function.

At the end of this, our `app.py` should look something like this:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/about')
def about():
    return 'This is the about page'

@app.route('/contact')
def contact():
    return 'This is the contact page'

@app.route('/welcome/<name>')
def welcome(name):
    return 'Welcome ' + name
```

#### Templates

##### What are 'Templates'

##### Flask's templating language: Jinja

##### Create a simple template

##### Rendering a template

##### Passing variables to templates

##### Bases and extensions

##### Styling

### 'Is it prime?' page
(i.e., user enters a number, page replies with whether or not it is a prime)

### The 'Musk's latest adventures' page
(i.e, a one-answer type of website, 'Is the Queen still alive?' type of thing. In this case, our project will display the latest headline about Elon Musk; use a simple free API like Google News API or the Guardian API)

### The 'Florida Man' page
(alternative option: users enter their date of birth and we give them the top news result for 'Florida Man')