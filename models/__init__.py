#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os

from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

storage = DBStorage() if os.getenv(
	'HBNB_TYPE_STORAGE') == 'db' else FileStorage()
"""A unique FileStorage/DBStorage instance for all models.

This module is responsible for instantiating an object of either the FileStorage or DBStorage class,
depending on the value of the 'HBNB_TYPE_STORAGE' environment variable. If the value is set to 'db',
a DBStorage instance is created, otherwise a FileStorage instance is created.

The storage object serves as a unique instance of either FileStorage or DBStorage, and is used to
manage the storage and retrieval of objects in the application.

The storage object is initialized by calling the reload() method, which loads all the objects from
the storage system into memory.
"""
storage.reload()