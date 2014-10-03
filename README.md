This is my workthrough of [Pro AngularJS](http://www.apress.com/9781430264484) done using the Django 1.7 framework.

If you want to follow along, Use the commits. Each commit works for the relevant stage in the book.

This work was done in Ubuntu 14.04. No special requirements but I recommend you use the requirements.txt in a virtualenv.

This workthrough of the book does not use [deployd](http://deployd.com/) because it relies instead upon Django's built in ORM and models.

## Creating the products collection
To create the products collection, I created a Product model object in the sportstore with the required properties.

## 6.5 thoughts
The filter does not filter the list of products. It transforms the list into a list of unique category names. I don't like this - filters should be filters.
