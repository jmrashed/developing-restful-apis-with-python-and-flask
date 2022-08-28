#!/usr/bin/env python
# encoding: utf-8
from urllib import response

from flask import Flask, jsonify, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__ , template_folder='templates')
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'sookh'
 
mysql = MySQL(app)
 
@app.route('/')
def main():
    return render_template('index.html')
 
@app.route('/products')
def products():
    cursor = mysql.connection.cursor()
    sql= '''SELECT id, name, slug, serial, published, thumbnail_img from products'''
    
    
    cursor.execute(sql)
    products = cursor.fetchall()
  
    return render_template('products.html', items=products)
 
 
@app.route('/brands')
def brands():
    cursor = mysql.connection.cursor()
    sql= '''SELECT id, name, slug from brands  LIMIT 50'''
    cursor.execute(sql)
    brands = cursor.fetchall() 
    return render_template('brands.html', items=brands)
 
@app.route('/users')
def users():
    cursor = mysql.connection.cursor()
    sql= '''SELECT id, name, email from users  LIMIT 500'''
    cursor.execute(sql)
    users = cursor.fetchall() 
    return render_template('users.html', items=users)
 
@app.route('/categories')
def categories():
    cursor = mysql.connection.cursor()
    sql= '''SELECT id, name, slug, banner, flat_icon from categories  LIMIT 500'''
    cursor.execute(sql)
    categories = cursor.fetchall() 
    return render_template('categories.html', items=categories)


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
 
app.run(host='localhost', port=8080, debug=True)
