=========
tnsmaster
=========

Toolset for mastering tnsnames.ora

.. contents::

Travis Status
=============

.. image:: https://travis-ci.org/difu/tnsmaster.svg
    :target: https://travis-ci.org/difu/tnsmaster
.. image:: https://coveralls.io/repos/github/difu/tnsmaster/badge.svg?branch=master
    :target: https://coveralls.io/github/difu/tnsmaster?branch=master

.. important::
  At the moment ``tnsmaster`` is in the development phase. Not all features are
  working. But be encouraged to participate!

``tnsmaster``'s goal is to be the Swiss army knife for creating and maintaining
``tnsname.ora`` files.

Features
========

* Syntax verification
    - check for correct syntax before rollout
* Semantic verification assistance
    - create and extract easy-to-test components that let you connect easily to
      each service node (Dataguard, RAC) directly

* Apply different styles to existing ``tnsnames.ora``
    - consistent upper/lower cases of keywords or values
    - neat indentation
    - transform entries to one line per alias or alias list for easy scripting
      and copy/pasting to application server configurations


Usage
=====

Quickstart
----------

- To format a tnsnames.ora file with default settings::

    python3 formatter.py path/to/tnsnames.ora

  A neat indented tnsnnames.ora will be printed to stdout.

- To extract all aliases from a tnsnames.ora::

    python3 aliases.py path/to/tnsnames.ora

  All aliases will be printed to stdout.


Semantic verification assist
----------------------------

Consider this address list of a tnsnames.ora file::

    ...
            (load_balance=yes)
            (address_list=
                (address=(protocol=tcp)(host=host1.domain.foo)(port=1522))
                (address=(protocol=tcp)(host=host2.domain.foo)(port=1524))
                (address=(protocol=tcp)(host=host3.someotherdomain.foo)(port=1522))
                (address=(protocol=tcp)(host=host1.someotherdomain.foo)(port=9210))
                (address=(protocol=tcp)(host=host2.farawaydomain.foo)(port=1522))
            )
    ...

It is hard to test if all connections are correct and the destination can be
reached, because the client will choose an address randomly. ``tnsmaster`` will
create a single tnsnames file for each address. You can now connect to this
specific destination and test if it is reachable.
