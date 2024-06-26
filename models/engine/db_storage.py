#!/usr/bin/python3
""" Module for DBStorage class """
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place, place_amenity
from models.amenity import Amenity
from models.review import Review

class DBStorage:
	"""
	This class represents the database storage engine for the AirBnB clone project.
	It provides methods to interact with the database and perform CRUD operations.
	"""

	def __init__(self):
		"""
		Initializes a new instance of the DBStorage class.
		It sets up the database connection and performs necessary configurations.
		"""
		user = os.getenv('HBNB_MYSQL_USER')
		pword = os.getenv('HBNB_MYSQL_PWD')
		host = os.getenv('HBNB_MYSQL_HOST')
		db_name = os.getenv('HBNB_MYSQL_DB')
		DATABASE_URL = f"mysql+mysqldb://{user}:{pword}@{host}:3306/{db_name}"
		self.__engine = create_engine(DATABASE_URL, pool_pre_ping=True)
		env = os.getenv('HBNB_ENV')
		if env == 'test':
			Base.metadata.drop_all(self.__engine)

	def all(self, cls=None):
		"""
		Retrieves all objects from the database.

		Args:
			cls (optional): The class of objects to retrieve. If not provided, retrieves all objects.

		Returns:
			A dictionary of objects, where the keys are in the format "<class_name>.<object_id>".
		"""
		objects = {}
		all_classes = (User, State, City, Amenity, Place, Review)
		if cls is None:
			for class_type in all_classes:
				query = self.__session.query(class_type)
				for obj in query.all():
					obj_key = f"{obj.__class__.__name__}.{obj.id}"
					objects[obj_key] = obj
		else:
			query = self.__session.query(cls)
			for obj in query.all():
				obj_key = f"{obj.__class__.__name__}.{obj.id}"
				objects[obj_key] = obj
		return objects

	def delete(self, obj=None):
		"""
		Deletes an object from the database.

		Args:
			obj (optional): The object to delete. If not provided, does nothing.
		"""
		if obj is not None:
			self.__session.query(type(obj)).filter(type(obj).id == obj.id).delete(synchronize_session=False)

	def new(self, obj):
		"""
		Adds a new object to the database.

		Args:
			obj: The object to add to the database.
		"""
		if obj is not None:
			try:
				self.__session.add(obj)
				self.__session.flush()
				self.__session.refresh(obj)
			except Exception as ex:
				self.__session.rollback()
				raise ex

	def save(self):
		"""
		Saves any changes made to the objects in the database.
		"""
		self.__session.commit()

	def reload(self):
		"""
		Reloads the database session and performs necessary configurations.
		"""
		Base.metadata.create_all(self.__engine)
		SessionFactory = sessionmaker(bind=self.__engine, expire_on_commit=False)
		self.__session = scoped_session(SessionFactory)()

	def close(self):
		"""
		Closes the database session.
		"""
		self.__session.close()
