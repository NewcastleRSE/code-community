# Creating a web application with Python

## Introduction
This is a *very* simple and basic introduction to building a web application using a language that is not necessarily associated with web technology, Python. Python has been for a number of years, and remains, the most popular programming language in the world (on, for example, the [TIOBE Index](https://www.tiobe.com/tiobe-index/) as of February of 2023, among others). Along with R and Matlab, Python is also one of the favourite languages of code-writing researchers from non-computer related disciplines, as well as one of the easiest languages to learn to code with.

One of Python's advantages (or disadvantages, depending on your particular point of view or objectives), is in being a very general-purpose language rather than a highly specialised one (like R or Matlab for statistics, or JavaScript for the web). You can do pretty much anything in computing with Python -- and although this is also true for any [Turing-complete programming languages](https://en.wikipedia.org/wiki/Turing_completeness), in Python that aspiration is actually feasable. And that includes writing for the web.

Although this is a basic tutorial, it assumes a basic understanding of Python, and (at least) a reading understanding of HTML. In this tutorial we will explore a simple approach to creating a webapp using Python, using a particular framework (Flask) for its simplicity and relative lightweight (other options are available and we will talk briefly about the most famous one soon). Perhaps, before diving right in, it would be beneficial to define what we mean by a webapp (and why is that different from a webpage), why and when you might want to use Python to create it, and what are the most popular Python frameworks to create it.

### 1. What is a webapp
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