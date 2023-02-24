# Creating a web application with Python

## Introduction
This is a *very* simple and basic introduction to building a web application using a language that is not necessarily associated with web technology, Python. Python has been for a number of years, and remains, the most popular programming language in the world (on, for example, the [TIOBE Index](https://www.tiobe.com/tiobe-index/) as of February of 2023, among others). Along with R and Matlab, Python is also one of the favourite languages of code-writing researchers from non-computer related disciplines, as well as one of the easiest languages to learn to code with.

One of Python's advantages (or disadvantages, depending on your particular point of view or objectives), is in being a very general-purpose language rather than a highly specialised one (like R or Matlab for statistics, or JavaScript for the web). You can do pretty much anything in computing with Python -- and although this is also true for any [Turing-complete programming languages](https://en.wikipedia.org/wiki/Turing_completeness), in Python that aspiration is actually feasable. And that includes writing for the web.

Although this is a basic tutorial, it assumes a basic understanding of Python, and (at least) a reading understanding of HTML. In this tutorial we will explore a simple approach to creating a webapp using Python, using a particular framework (Flask) for its simplicity and relative lightweight (other options are available and we will talk briefly about the most famous one soon). Perhaps, before diving right in, it would be beneficial to define what we mean by a webapp (and why is that different from a webpage), why and when you might want to use Python to create it, and what are the most popular Python frameworks to create it.

### 1. What is a webapp
If we are about to create one, perhaps we should clarify what we mean by a web application: the crucial difference between a web application and a simple web page or site (i.e., a collection of interlinked web pages using the same domain name) is that an application allows the user to interact with a piece of software through the web; i.e., in simple terms, there is some form of calculation being performed at some point to generate the content the user can access, even if its end-product is a static read-only file. Any website that changes its content based on user interaction, or allows for user registration and personalised content, or performs a calculation, however simple, can be thought of as a web application.

This distinction between webapps and web pages is more or less irrelevant in most applications; though if you only intend to have a static page with your name and contact (i.e., a stable personal page, a place for people interested in you to visit), having a full-blown app is probably overkill: it will be cheaper, and quicker, to simply write a plain html page. If, on the other hand, you want your users to be able to explore some of your research code directly on your page (think, for example, a dashboard-style data explorer), you are probably looking at some form of web application.

If you really want to get into the technical weeds, you might see terms like [Progressive Web Applications](https://en.wikipedia.org/wiki/Progressive_web_app) (i.e., apps that are designed to work regardless of the platform used by the user, be it mobile iOS, Android / desktop MacOS, Windows, Linux, etc. -- think about it like a mobile app that you access through the browser); [Single-Page Applications (SPA)](https://en.wikipedia.org/wiki/Single-page_application) that re-write the content of the page based on user interaction (like Twitter or Facebook, for example), or Multi-Page Applications (MPA), which are closer to a traditional website with new content being generated at the same time as the page itself and, therefore, demanding navigating away from it to see different content (or refreshing the page). This [Medium article](https://medium.com/@NeotericEU/single-page-application-vs-multiple-page-application-2591588efe58) gives you a good overview of the differences between, and respective advantages and disadvantages, of SPAs and MPAs.
### 2. Why / when to use Python
### 3. What are your framework options?
####   1. Django
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