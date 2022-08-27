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

    app = Flask(__name__)

    @app.route("/")
    def index():
        return "<h1>Hello!</h1>"

    if __name__ == "__main__":
        from waitress import serve
        serve(app, host="127.0.0.1", port=8080)

```

## Python Modules

Like other mainstream programming languages, Python also has the concept of modules to enable developers to organize source code according to subjects/functionalities.

## Flask connect with Mysql

Flask connects to MySQL via the flask mysqldb connector. To install the package, use the following command:
`pip install flask_mysqldb`

## Setting Up Flask MySQL Database

Step 1: Connecting a Flask Application to a MySQL Database

```python
    from flask import Flask,render_template, request
    from flask_mysqldb import MySQL

    app = Flask(__name__)

    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'flask'

    mysql = MySQL(app)

```

Step 2: Configuring the MySQL Connection Cursor

```python
    mysql = MySQL(app)

    #Creating a connection cursor
    cursor = mysql.connection.cursor()

    #Executing SQL Statements
    cursor.execute(''' CREATE TABLE table_name(field1, field2...) ''')
    cursor.execute(''' INSERT INTO table_name VALUES(v1,v2...) ''')
    cursor.execute(''' DELETE FROM table_name WHERE condition ''')

    #Saving the Actions performed on the DB
    mysql.connection.commit()

    #Closing the cursor
    cursor.close()
```

Step 3: Programming a Flask application

```python

    from flask import Flask,render_template, request
    from flask_mysqldb import MySQL

    app = Flask(__name__)

    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'flask'

    mysql = MySQL(app)

    @app.route('/form')
    def form():
        return render_template('form.html')

    @app.route('/login', methods = ['POST', 'GET'])
    def login():
        if request.method == 'GET':
            return "Login via the login Form"

        if request.method == 'POST':
            name = request.form['name']
            age = request.form['age']
            cursor = mysql.connection.cursor()
            cursor.execute(''' INSERT INTO info_table VALUES(%s,%s)''',(name,age))
            mysql.connection.commit()
            cursor.close()
            return f"Done!!"

    app.run(host='localhost', port=5000)

```

The form.html will be as follows:

```html
<form action="/login" method="POST">
  <p>name <input type="text" name="name" /></p>
  <p>age <input type="integer" name="age" /></p>
  <p><input type="submit" value="Submit" /></p>
</form>
```

Step 4: Putting the Code into Action

- Now start the server and navigate to “/form”
- Enter the information and press the Submit button.
- Let’s take a look at it in the phpMyAdmin web interface now.

Finally! This concludes the Setting Up Flask MySQL Database Connection
