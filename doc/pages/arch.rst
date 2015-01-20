Software Architecture
=====================

Overview
--------

The code will consist of the following components:

* Data types: The underlying data model.
* File operations: Moving information into and out of the program.
* CRUD operations: Create, read, update, and delete entries from address books.
* Views: Sort and/or filter the data.
* GUI: Graphically invoke operations, visualize views.

Dependencies for each component are shown below.

File operations -> Data types
CRUD operations -> Data types
Views -> Data types
Interface -> Data types
Interface -> File operations
Interface -> CRUD operations
Interface -> Views


Data types
----------

Abstractly, an address book is a recursive data structure consisting of maps, lists, and primitive data types.
Each address book MUST have the following eight fields: 

* First name
* Last name
* Street Address
* State
* Zip code
* Phone number
* email

Other fields may be present. Any field, including the mandatory eight, may be marked as a missing value.
All missing values will be represented by null in JSON, None in Python, and some equivalent in any other format.

This architecture should be extensible because the underlying data types are flexible.

Input handling will be done at the operations level.


File operations
---------------

The program will be capable of reading and writing data to the JSON format as well as any customer defined formats.

Data will be stored in the user's home directory in a folder named ".address".
There will be a single file mapping address-book names to file names and storing other metadata associated with the address book, e.g. user-defined fields for the address book.
Each other file in this folder will correspond to a single address book.


CRUD operations
---------------

CRUD operations will be supported by methods associated with the Book class.
These operations are characterized by the fact that each one will change the state of the address book.


Views
-----

Views will also be supported as methods on address books.
The purpose of these methods is to allow a programmer to select and organize data in a meaningful way.
View methods MUST NOT alter the state of the address book.
A view method must return an ordered list of entries from the address book.


Interface
---------

The no other component of the project depends on the interface.
It is critical that this property always holds in order to allow the creation of alternate interfaaces and to avoid unneeded coupling.

The interface will consume the APIs provided by all other components of the project.
The interface should provide the user with the ability to perform any CRUD operation.
The interface should provide the user with the ability to visualize the data in multiple ways.
The views component is intended to provide an easy way for the interface programmer to access the data without needing to write much logic to rearrange the data.
