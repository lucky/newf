# Newf, A New (web) Framework for Python

Yes, another one. Why? Because I can, that's why. I started Newf when I got
frustrated with the bloat of Django when it went from 0.96 to 1.0. Django is
great, but not my bag anymore.

Newf strictly utilizes WSGI and makes creating a web application
super-ridiculously simple. You set some urls, create some functions and you're
basically done.

## What doesn't it do?

Lots of things!

Newf doesn't have a templating language. Use [Jinja](http://jinja.pocoo.org/) or
[Cheetah](http://www.cheetahtemplate.org/) or 
[Mako](http://www.makotemplates.org/) or roll you own or whatever.

Newf doesn't do Sessions. We recommend using [Beaker](http://beaker.groovie.org/)
for that.

Newf doesn't have an ORM. We recommend 
[Autumn](https://github.com/JaredKuolt/autumn/tree) (shocked?) or 
[Storm](https://storm.canonical.com/) or [SQLObject](http://www.sqlobject.org/).

## How do I use it?

Check out `example_app.py`.
