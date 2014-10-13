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

## 8.10 Location of admin
I've treated the front end admin being developed in the book as a 'component' and located it under sportstore. This is
because I want to minimize confusion with Django's built in admin and to have it somewhere that one naturally looks for
it.

## 8.11 Introducing Django rest framework
The authentication and server side api is becoming more complex. The book relies upon the archaic deployd and still has
to jump through a few hoops. To make things more realistic and fun, I'm taking a step back here and integrating the
django rest framework. This makes the server api easier to manage and test and gives me all the authentication
and security features needed in a manner that is also suitable for production environments.

Being able to use /sportstore/api in both html and json is very handy!

### Handling the creation of orders and order items
The Deployed service in the Pro Angular book is very flexible with respect to creating the items. As we're now using the
rest_framework, the 'natural' way to create the order would be to:
- Create an empty order
- Create and Add order items

This is supported by the rest_framework api except for the addition of the order item to the order (which is
easily added). However, the book method for creating the order bundles creation of the order and its order items into one reasonably intuitive package which
sends the server the order data plus the item data in one message.

I've chosen make the order serializer work much the same way. This makes the order items invisible outside of the order.

## 8.16 Nested views
Using views to organize the dom seems to go (against Angular a bit)[http://jan.varwig.org/archive/how-to-do-nested-views-in-angularjs-hint-dont] and I can't help feeling that this should either use
the (Angular UI)[https://github.com/angular-ui/ui-router] stuff or custom directives but I've decided to go with the book for the time being.

Using the $index in the ng-repeat feels like magic. Horrid.

In any event I'm not sure what the issue is here because we're using admin.html so they aren't nested anyway!

## 8.18 I don't think I need the WithCredentials option
As I've set Django up using token authentication, this is probably a waste.