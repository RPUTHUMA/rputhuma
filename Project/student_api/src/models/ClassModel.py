# src/models/ClassModel.py

from . import db
from marshmallow import fields, Schema
import datetime


class ClassModel(db.Model):
	#table name
	__tablename__ = 'classes'
	id = db.Column(db.Integer,primary_key=True,nullable=False)
	name = db.Column(db.String(128),nullable=False)
	created_on = db.Column(db.DateTime,nullable=False)
	updated_on = db.Column(db.DateTime,nullable=False)
	student = db.relationship("StudentModel",back_populates="classes")
	
	# class constructor
	def __init__(self,name,id):
		self.id= id
		self.name = name
		self.created_on = datetime.datetime.utcnow()
		self.updated_on = datetime.datetime.utcnow()
	
	def save(self):
		db.session.add(self)
		db.session.commit()
		
	def update(self,data):
		for key,item in data.items():
			setattr(self,key,item)
		self.updated_on = datetime.datetime.utcnow()
		db.session.commit()
		
	def delete(self):
		# have to see abt foreign key
		db.session.delete(self)
		db.session.commit()
		
	@staticmethod
	def get_all_class():
		return ClassModel.query.all()
	
	@staticmethod
	def get_one_class(id):
		return ClassModel.query.get(id)
		
	def __repr__(self):
		return '<id {}>'.format(self.id)

class ClassesSchema(Schema):
	id = fields.Int(dump_only=True)
	name = fields.Str(required=True)
	created_on = fields.DateTime(dump_only=True)
	updated_on = fields.DateTime(dump_only=True)
	



