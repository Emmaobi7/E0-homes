# GOODIE FETCH
* goodie-fetch is a convenient and user friendly **product** purchase and delivery app that brings the your favourite products ranging from clothes, home appliances, furnitures and lots more to your doorstep. Need to refurnish your home or change your wardrope **goodie** got you covered.

# TABLE OF CONTENTS
<ol>
  <li>Getting started </li>
  <ul>
    <li>Prerequisites</li>
    <li>Installation</li>
  </ul>
  <li>usage</li>
  <li>Contribution</li>
  <li>Acknowlegements</li>
</ol>
~       
# Getting started
* This project was built on ubuntu 20, so once you've got your ubuntu 20 clone this repo and get started

## Prerequisites
* This libraries are required to run this project python 3.6xx and flask and sqlalchemy and react js with other libraries which would be authomatically installed in the **installation section**

## Installation
* simply execute the below command to get all the build libraries in your setup
<code> pip3 install -r requirements.txt</code>

* then to start the app simply:
<code>python3 main.py</code>

* you can use environment variables(remember to edit the 'app/__init__.py' for your prefrred database info)  for the database or just simply:
<code>./set_mysql.sql</code>

#Usage
* This project uses a react js frontend and a python backend api with these endpoints:
## API
  ### POST requests
* 'app/auth/sign_up': for registering users to the database
  ### #Usage:
* fieldnames must contain exactly 'first_name', 'email, 'password1, 'password2' in any order.

  
* 'app/auth/login': for logging in users
  ### #Usage:
* fieldnames must contain exactly 'email' and 'password'
  ### GET requests only
* 'app/v1/products': for getting a listing of all our producuts
* 'app/v1/products/{product_id}: for a particular product
* 'app/v1/products/search/{query}: to sort the database by titile and description
** and of course all these end points return a json response and should be use ( for post requests) with the application/json dtatype in the request headers

# Contribution
* for contributions feel free to fork the repo and you can reach us via our email at 'emma46574@gmail.com'

# Acknowlegements
* Emma obinna (backend)
* sharaff (frontend)
* diane ezinne (frontend)
