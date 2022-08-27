#!/usr/bin/env python
# encoding: utf-8
from urllib import response

from flask import Flask, jsonify, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__ , template_folder='templates')
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'sookh'
 
mysql = MySQL(app)
 
@app.route('/')
def main():
    return render_template('index.html')
 
@app.route('/users')
def users():
    cursor = mysql.connection.cursor()
    sql= '''SELECT id, name, email from users  LIMIT 5'''
    cursor.execute(sql)
    users = cursor.fetchall()
    
    sql= '''SELECT id, name,slug from brands  LIMIT 5'''
    cursor.execute(sql)
    brands = cursor.fetchall()
   

    sql= '''SELECT id, name,slug from categories where parent_id=0  LIMIT 5'''
    cursor.execute(sql)
    categories = cursor.fetchall()
   


    return render_template('index.html', users=users,brands=brands, categories=categories)


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
        cursor.execute(''' INSERT INTO users VALUES(%s,%s)''',(name,age))
        mysql.connection.commit()
        cursor.close()
 
app.run(host='localhost', port=5000, debug=True)
