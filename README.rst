Embedly-Cards
===============

Embedly-cards is a Pelican_ plugin providing restucturedText directives to allow
easy embedding of external content using `Embed.ly Cards <http://embed.ly/cards>`_.

`ReST <http://iza.ac/posts/2014/03/embedly-cards/>`_ and `markdown <http://iza.ac/posts/2014/04/embedly-cards-v02-markdown-support/>`_ live examples can also be viewed from a Pelican-built website.

.. _Pelican: http://getpelican.com


Features
============
Embed content within a page or blog post easily, simply by specifying the URL of
the target page. Content is automatically recognised, extracted, and formatted as
a 'card'; this may contain a short article preview, embedded video, picture etc.

To preview a card, they can be generated online using `Embed.ly <http://embed.ly/cards>`_.
Almost any site is compatible, including YouTube, Flickr, Google+, Maps, Wordpress etc.

Installation
============
Embedly-cards can be installed using `pip`

.. code-block:: bash
    
    $ pip install embedly-cards

or manually from the source code

.. code-block:: bash

    $ python setup.py install

Once installed, simply add it to your ``pelicanconf.py`` configuration file:

.. code-block:: python

    PLUGINS = [
        # ...
        'embedly_cards'
    ]

If you are planning on embedding content in markdown ``.md`` files,
you must also add it to the ``MD_EXTENSIONS`` options, like so:

.. code-block:: python
    from embedly_cards import EmbedlyCardExtension
    MD_EXTENSIONS = ['codehilite(css_class=highlight)',
                     'extra',
                     # ...
                     EmbedlyCardExtension()]

.. important::
    If creating the ``MD_EXTENSIONS`` variable for the first time,
    ensure that the Pelican ``'codehilite(css_class=highlight)'``
    and ``'extra'`` markdown extensions are included in the list.

Usage
============

In order to embed content within a restucturedText blog post/article, you can use
the `embedly-card` directive.

For example, to embed a YouTube video:

.. code-block:: ReST

    .. embedly-card:: https://www.youtube.com/watch?v=ZlfIVEy_YOA

.. code-block::

    [!embedlycard](https://www.youtube.com/watch?v=ZlfIVEy_YOA)

Or to embed an article/webpage:

.. code-block:: ReST
    
    .. embedly-card:: http://physics.stackexchange.com/questions/5265/cooling-a-cup-of-coffee-with-help-of-a-spoon
    
.. code-block::

    [!embedlycard](http://physics.stackexchange.com/questions/5265/cooling-a-cup-of-coffee-with-help-of-a-spoon)

Options
========

The `card-chrome` option, if provided, specifies whether or not to preserve the
border around the card. By default, the border will be removed automatically
*if Embed.ly supports it*; however to force the border to remain, you may pass
``:card-chrome: 1``:

.. code-block:: ReST

    .. embedly-card:: https://www.youtube.com/watch?v=ZlfIVEy_YOA
        :card-chrome: 1

.. code-block::

    [!embedlycard?chrome=1](https://www.youtube.com/watch?v=ZlfIVEy_YOA)
