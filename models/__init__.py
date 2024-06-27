#!/usr/bin/python3
"""This module instantiates an instance of the Storage that will be used.

The storage type is determined by the value of the environment variable 'HBNB_TYPE_STORAGE'.
If the value is 'db', an instance of DBStorage is created.
Otherwise, an instance of FileStorage is created.

The storage is then reloaded to load any existing data.
"""

from os import getenv

storage_type = getenv('HBNB_TYPE_STORAGE')

if storage_type == 'db':
	from models.engine.db_storage import DBStorage
	storage = DBStorage()
else:
	from models.engine.file_storage import FileStorage
	storage = FileStorage()

storage.reload()