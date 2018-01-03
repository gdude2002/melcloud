MELCloud Library
================

A module providing access to Mitsubishi's `MELCloud <https://www.melcloud.com/>`_ API.
This API is not officially documented, but has been reverse-engineered by some diligent
users. This API is relied upon for several projects, so it should be pretty stable, but
remember to take the necessary precautions in your application.

Installing
----------

You can install this module in the usual way. ::

    pip install melcloud

This will install the module with all its dependencies.

Usage
-----

TODO: Write documentation

This module contains two sets of classes, and a set of basic objects to represent various concepts.

* For code using asyncio, you can use ``melcloud.async``, which uses aiohttp under the hood
* For synchronous code, you can use ``melcloud.sync``, which uses Requests under the hood

----

This library would not have been possible without the work of `ilcato <https://github.com/ilcato/homebridge-melcloud/>`_
and `Simon "mgeek" Rubuano <http://mgeek.fr/blog/un-peu-de-reverse-engineering-sur-melcloud>`_. Many thanks to both
of these people for their diligence!
