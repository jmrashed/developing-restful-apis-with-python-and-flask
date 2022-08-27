## Developing RESTful APIs with Python and Flask

Let's learn how to develop RESTful APIs with Python and Flask. We are going to use Flask and Python to develop a RESTful API. We will start by creating an endpoint that returns static data (dictionaries). After, we are going to create a class with two specializations and a few endpoints to insert and retrieve instances of these classes. Finally, will take a look on how to run the API on a Docker container.

## Why Python?

Nowadays, choosing Python to develop applications is becoming a very popular choice. Python is one of the fastest-growing programming languages, having surpassed even Java on the number of questions asked on the platform.

## Why Flask?

When it comes to web development on Python, there are two frameworks that are widely used: Django and Flask. Django is older, more mature, and a little bit more popular. Even though Django is older and having a slightly bigger community, Flask has its strengths.

From the ground up, Flask was built with scalability and simplicity in mind. Flask applications are known for being lightweight, mainly when compared to their Django counterparts. Flask won’t make many decisions for us, such as what database to use or what template engine to choose. Lastly, Flask also has extensive documentation that address everything that developers need to start.

## Bootstrapping a Flask Application

First and foremost, we will need to install some dependencies on our development machine. Basically, what we will need to install is Python 3, Pip (Python Package Index), and Flask. Fortunately, the process of installing these dependencies is quite simple.

## Installing Python 3

After installing Python 3 on our machine, we can check that we have everything set up as expected by running the following command:

`python --version # Python 3.6.2`

## Installing Pip

`pip --version # pip 9.0.1 ... (python 3.X)`

## Installing Flask

Let's focus on installing it on our machine and testing to see if we can get a basic Flask application running. The first step is to use pip to install Flask:
`pip install Flask`
After installing the package, we will create a file called hello.py and add five lines of code to it.

```python
from flask import Flask
app = Flask(**name**)

@app.route("/")
def hello_world():
return "Hello, World!"
```

## Python Modules

Like other mainstream programming languages, Python also has the concept of modules to enable developers to organize source code according to subjects/functionalities.
