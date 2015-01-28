"""
This module provides the Metadata class.
"""

import os
import json

from address.book import Book, BookEncoder

HOME = os.path.expanduser("~")
METADATA_DIRECTORY = os.path.join(HOME, ".address")
METADATA_FILE = ".metadata"
METADATA_PATH = os.path.join(METADATA_DIRECTORY, METADATA_FILE)
SUFFIX = ".json"

def _metadata_exists():
    """
    Return True if the metadata folder and files already exist.

    :returns: whether or not metadata already exists on the system
    :rtype: Boolean
    """
    return os.path.exists(METADATA_PATH)

def _create_initial_metadata():
    """
    Create an empty file to store metadata.

    :returns: None
    :rtype: None

    :raises: Permissions error?
    """
    if os.path.exists(METADATA_PATH):
        return
    if not os.path.exists(METADATA_DIRECTORY):
        os.mkdir(METADATA_DIRECTORY)
    with open(METADATA_PATH, "a") as metadata_file:
        metadata_file.write("{}")

def _get_path_from_name(name):
    """
    Takes the name of a book and creates an absolute path to store the book
    at. This can be used for books that are not yet saved to determine where
    to save them to.

    :arg name: the name of a book
    :type name: String

    :returns: The path to store the book at
    :rtype: String
    """
    return os.path.join(METADATA_DIRECTORY, name) + SUFFIX

def _get_metadata():
    """
    Load the metadata stored on the system and return it.

    :returns: the metadata for the address book
    :rtype: Dictionary
    """
    if not _metadata_exists():
        _create_initial_metadata()
    with open(METADATA_PATH) as metadata_file:
        return json.load(metadata_file)

def _write_metadata(metadata):
    """
    Save some data to the metadata file.

    :arg metadata: The metadata to save
    :type metadata: Dictionary

    :returns: None
    :rtypes: None
    """
    if not _metadata_exists():
        _create_initial_metadata()
    with open(METADATA_PATH, "w") as metadata_file:
        json.dump(metadata, metadata_file)

def get_book_names():
    """
    Get a list of all books stored on the system.

    :returns: Names for all books stored in METADATA_DIRECTORY
    :rtype: list of strings
    """
    return sorted(_get_metadata().keys())

def load(name):
    """
    Get a Book object corresponding to a name of an book.

    :arg name: Name of the book to open
    :type name: String

    :returns: The book with the appropriate name
    :rtype: Book
    """
    #TODO handle names that are not in the metadata
    return Book(_get_path_from_name(name))

def save(name, book):
    """
    Save a book and update the metadata appropriately. The book is saved as a
    JSON file on the system in the METADATA_DIRECTORY

    :arg name: The name to save the book with
    :type name: String
    :arg book: The book to save to a file
    :type book: Book

    :returns: None
    :rtype: None
    """
    path = _get_path_from_name(name)
    with open(path, "w") as book_file:
        json.dump(book, book_file, cls=BookEncoder)
    metadata = _get_metadata()
    metadata[name] = path
    _write_metadata(metadata)

def delete(name):
    """
    Delete a book from the system. Removes the file corresponding to the book
    with the provided name.

    :arg name: Name of the book to delete
    :type name: String

    :returns: None
    :rtype: None
    """
    os.remove(_get_path_from_name(name))
