Usage
=====

.. _installation:

Installation
------------

#TODO 
Add Usage instructions

.. code-block:: console

   (.venv) $ pip install layover_connections

Stuff to code in Python
----------------

Sample of how to use a specific Python Function
you can use the ``layover_connection()'' function via:

.. autofunction:: lumache.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

For example:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

