Software Architecture
=====================

Overview
--------

The code will consist of the following components:

* *Data types*: The underlying data model.
* *File operations*: Moving information into and out of the program.
* *CRUD operations*: Create, read, update, and delete entries from address books.
* *View methods*: Sort and/or filter the data.
* *Interface*: Graphically invoke operations, visualize views.

Dependencies for each component are shown below.

.. graphviz::

  digraph arch {
    "File operations" -> "Data types";
    "CRUD operations" -> "Data types";
    "Views" -> "Data types";
    "Interface" -> "Data types";
    "Interface" -> "File operations";
    "Interface" -> "CRUD operations";
    "Interface" -> "Views";
  }


Data types
----------

The application will consist of two primary data types: `Books` and `Entries`.

An `Entry` is a mapping between field names and values. The class also
provide methods as described in later sections. There are eight fields that
require a key value pair in each initial `Entry`:

* First name
* Last name
* Street Address
* State
* Zip code
* Phone number
* Email

Other fields may be present. Any field, including the mandatory eight, may be
marked as a missing value.  All missing values will be represented by null in
JSON, None in Python, and some equivalent in any other format.

Non-mandatory fields may be supplied using the kwargs mechanism built into
Python. Arbitrary keyword arguments should be interpreted as key value pairs to
be stored in the `Entry`. This makes the `Entry` class easier to extend for new
features such as user-defined fields.

Invalid input should be handled by raising an exception.

A `Book` is a collection of `Entry` objects with supporting methods described
in later sections. When a method defined in `Book` uses the `Entry` class, it
must handle any exceptions raised. It is valid to handle an exception by raising
another exception in this context. This allows the programmers using the `Book` 
class to only need to check exceptions raised by the `Book` class.


File operations
---------------

The application will be capable of reading and writing data to the JSON format as
well as any other user-defined formats.

Data will be stored in the user's home directory in a folder named ".address".
There will be a single file mapping address-book names to file names and
storing other metadata associated with the address book, e.g. user-defined
fields for the address book. All other files in this folder will have one to
one correspondence with a single address book.


CRUD operations
---------------

An address book must support CRUD operations, i.e., create, read, update, and
delete. This section will be implemented as a set of methods in the `Book` class.
Each CRUD operation is characterized by the ability to change the state of the 
address book.


View methods
-----

View methods will also be supported as methods on the `Book` class. These 
methods allow a programmer to select and organize data in a meaningful way.
View methods must not alter the state of the address book. A view method must
return an ordered list of entries from the address book.

As an example of a view method, consider `.sort_by(field_name)` a method that
takes the name of a field as a parameter. By providing a `field_name` such as
`"zip_code"`, the programmer can access a list of entries sorted by their
zipcode.

View methods should raise exceptions when passed invalid parameters. These 
exceptions should be handled by the programmer any time there is a call to
a view method.


Interface
---------

No component of the application must depends on the interface. This property must
be maintained in order to allow the creation of alternate interfaces.

The interface will interact with the APIs provided by all components of the
application. The interface should provide the user with the ability to perform any
CRUD operation. The interface should also provide the user with the ability to
visualize the data in multiple ways. The view methods component is intended to provide
an easy way for a programmer to access the data without needing to rewrite much of logic
for rearrange the data.
