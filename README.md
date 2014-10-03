This is my workthrough of [Pro AngularJS](http://www.apress.com/9781430264484) done using the Django 1.7 framework.

If you want to follow along, Use the commits. Each commit works for the relevant stage in the book and you can look
at the commit details to see exactly what I did.

This work was done in Ubuntu 14.04 with Python 2.7. No special requirements but I recommend you use the requirements.txt in a virtualenv.

This workthrough of the book does not use [deployd](http://deployd.com/) because it relies instead upon Django's built in ORM and models.

I use Django features to support all the server side issues and address the use of Django templates in concert with AngularJS.

## Creating the products collection
To create the products collection, I created a Product model object in the sportstore with the required properties.

## 6.5 thoughts
The filter does not filter the list of products. It transforms the list into a list of unique category names.
AngularJS filters include a 'filter' filter to filter things. They are really 'transforms' or 'mappers'.

## 6.11 thoughts
Implementing the page handling locally is very wrong. The page elements should be pulled in via AJAX for each page.
However, this could possibly be viewed as an optimisation and left to the end.

## 7.12 thoughts
Partials have become views which I guess are a partial in the general sense.
I've kept them in the partials folder for now.

## 8.7 User authentication
As Django already supports user authentication this deviates significantly from the book. It supports staff and
superusers out of the box. It also has an implicit base level user as a 'registered' user - a user who is not staff
or a superuser and we'll use that base level as our 'shopper' who can create orders.

At this stage we have not associated any special permissions with our registered user - we just use the basic
authentication to ensure that they are registered.

