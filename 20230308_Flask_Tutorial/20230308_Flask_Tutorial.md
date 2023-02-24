# Creating a web application with Python

## Introduction
This is a *very* simple and basic introduction to building a web application using a language that is not necessarily associated with web technology, Python. Python has been for a number of years, and remains, the most popular programming language in the world (on, for example, the [TIOBE Index](https://www.tiobe.com/tiobe-index/) as of February of 2023, among others). Along with R and Matlab, Python is also one of the favourite languages of code-writing researchers from non-computer related disciplines, as well as one of the easiest languages to learn to code with.

One of Python's advantages (or disadvantages, depending on your particular point of view or objectives), is in being a very general-purpose language rather than a highly specialised one (like R or Matlab for statistics, or JavaScript for the web). You can do pretty much anything in computing with Python -- and although this is also true for any [Turing-complete programming language](https://en.wikipedia.org/wiki/Turing_completeness), in Python that aspiration is actually feasable. And that includes writing for the web.

Although this is a basic tutorial, it assumes a basic understanding of Python, and (at least) a reading understanding of HTML. In this tutorial we will explore a simple approach to creating a webapp using Python, using a particular framework (Flask) for its simplicity and relative lightweight (other options are available and we will talk briefly about the most famous one soon). Perhaps, before diving right in, it would be beneficial to define what we mean by a webapp (and why is that different from a webpage), why and when you might want to use Python to create it, and what are the most popular Python frameworks to create it.

### 1. What is a webapp
If we are about to create one, perhaps we should clarify what we mean by a web application: the crucial difference between a web application and a simple web page or site (i.e., a collection of interlinked web pages using the same domain name) is that an application allows the user to interact with a piece of software through the web; i.e., in simple terms, there is some form of calculation being performed at some point to generate the content the user can access, even if its end-product is a static read-only file. Any website that changes its content based on user interaction, or allows for user registration and personalised content, or performs a calculation, however simple, can be thought of as a web application.

This distinction between webapps and web pages is more or less irrelevant in most applications; though if you only intend to have a static page with your name and contact (i.e., a stable personal page, a place for people interested in you to visit), having a full-blown app is probably overkill: it will be cheaper, and quicker, to simply write a plain html page. If, on the other hand, you want your users to be able to explore some of your research code directly on your page (think, for example, a dashboard-style data explorer), you are probably looking at some form of web application.

If you really want to get into the technical weeds, you might see terms like [Progressive Web Applications](https://en.wikipedia.org/wiki/Progressive_web_app) (i.e., apps that are designed to work regardless of the platform used by the user, be it mobile iOS, Android / desktop MacOS, Windows, Linux, etc. -- think about it like a mobile app that you access through the browser); [Single-Page Applications (SPA)](https://en.wikipedia.org/wiki/Single-page_application) that re-write the content of the page based on user interaction (like Twitter or Facebook, for example), or Multi-Page Applications (MPA), which are closer to a traditional website with new content being generated at the same time as the page itself and, therefore, demanding navigating away from it to see different content (or refreshing the page). This [Medium article](https://medium.com/@NeotericEU/single-page-application-vs-multiple-page-application-2591588efe58) gives you a good overview of the differences between, and respective advantages and disadvantages, of SPAs and MPAs.
### 2. Why / when to use Python
So, assuming you know you *need* a webapp rather than a simple static webpage, and that you want (or need) to code it yourself (rather than using a bloated Content Management System), why would you choose to do it in Python? The answer is probably simpler than you expect: more likely than not, you choose to write your app in Python because you either a) are already confortable with Python, or b) are willing to learn a little more about coding, and are more confortable learning Python than other languages; or c) you already have a piece of (research) code in Python that you want visitors to your page to be able to interact with. There is nothing wrong with any of these reasons however, all other things being equal, you should keep in mind that Python is not necessarily better than any other approach to creating a webapp -- and in some cases, it might be a bad option. Not to go into too much detail here but, one thing to keep in mind *before* creating your app is whether you need server-side processing in your app -- with a Python webapp, the calculations are made in a computer elsewhere and only the result is shown to the user. In practical terms, this means that some of the cheaper web hosting solutions will not work for you, and you might need to spend a little more to keep your app online.

The most unavoidable reason to create a Python webapp is the one outlined in c): you have a piece of code that you need to interact with that is already in Python. In this case, writing a native Python webapp is probably the easiest, simplest, and probably cheapest solution. For any other use cases, Python is *always* an option, which will be better or worse suited depending on your specific use case.

However, if you are here, you probably *want* to write in Python. So, how exactly do you go about doing it? Because Python is a Turing-complete language, you *could* write the entire system from the ground up without using any additional tools and libraries. But just because you *can*, doesn't mean you *should*: the vast majority of basic operations that you would need to create -- from generating HTML files, serving them to a browser, giving error messages, etc -- have all been written already. If you've used Python in the past, you'll also know that one of its biggest advantages is in the giant community of users around it that wrote `libraries` for just about anything you could think of. When you put a series of libraries together with a common language of interaction between them, you have a `framework`. So, to write a webapp quickly and efficiently, you first need to choose your framework.

### 3. What are your framework options?
There are web frameworks for nearly every conceavable programming language out there. Some of the big hitters include [Ruby on Rails](https://rubyonrails.org/) (for Ruby), [Laravel](https://laravel.com/) for PHP, or [Rocket](https://rocket.rs/) (for Rust). If you are into Javascript, you are in luck (or hell): JS is absolutely (and appropriately, since we are talking about a web-focused language) littered with web frameworks, including but not limited to: [AngularJS](https://angularjs.org/), [VueJS](https://vuejs.org/), [React](https://reactjs.org/), and [Svelte](https://svelte.dev/). Python is similarly well served with frameworks though the two most popular ones are [Django](https://www.djangoproject.com/) and [Flask](https://flask.palletsprojects.com/).

####   1. Django
Django is a powerful Python web-framework that is particularly well-suited for creating webapps that have extensive interaction with, and dependence on, databases. In fact, one of Django's headline features is the inclusion of a simple but effective CRUD (Create, Read, Update, Delete) interface that can be used in development as a sanity check. Out of the box, it comes with most everything any web developer could wish for but, on top of that, it was built to be extensible. As a consequence there are hundreds of libraries that allow you to add additional functionality to your website. It is based on a [Model-View-Template(MVT)](https://www.javatpoint.com/django-mvt#:~:text=The%20MVT%20(Model%20View%20Template,layer%20which%20handles%20the%20data.) architectural pattern, as opposed to many JS frameworks that implement a [Model-View-ViewModel(MVVM) pattern](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93viewmodel). Some users complain about the level of difficulty in getting up and running with Django, so let that be a warning to you; for many webapps, a fully featured framework like Django is overkill, which means that the packages end up becoming more bloated and harder to manage than necessary. If only there was a similar solution that was lightweight, just as extensible, and easier to learn, you are all thinking. Enter Flask.
####   2. Flask

## Flask

1. What is Flask?
2. Why and when to use it?

## Hands-on

### Your first Flask page

#### Before you begin

1. Create Virtual Environment
2. Install Flask

#### Creating your first project

1. Folder structure
2. `main.py`
3. Importing Flask
4. Hello world

#### More pages, more views, more variables

##### Creating more pages

##### Passing variables to pages

#### Templates

##### What are 'Templates'

##### Flask's templating language: Jinja

##### Create a simple template

##### Rendering a template

##### Bases and extensions

##### Styling

#### Passing variables to templates

### 'Is it prime?' page
(i.e., user enters a number, page replies with whether or not it is a prime)

### The 'Musk's latest adventures' page
(i.e, a one-answer type of website, 'Is the Queen still alive?' type of thing. In this case, our project will display the latest headline about Elon Musk; use a simple free API like Google News API or the Guardian API)

### The 'Florida Man' page
(alternative option: users enter their date of birth and we give them the top news result for 'Florida Man')