# src/models/StudentModel.py

from . import db
from sqlalchemy_utils import UUIDType
from sqlalchemy import and_
from marshmallow import fields,Schema
from .ClassModel import ClassesSchema
import uuid
import datetime

def generate_uuid():
    return str(uuid.uuid4())

class StudentModel(db.Model):
	#table name
	__tablename__ = 'student'
	id = db.Column(db.String(256),primary_key=True,nullable=False,default=generate_uuid)
	name = db.Column(db.String(128),nullable=False)
	class_id = db.Column(db.Integer,db.ForeignKey('classes.id'),nullable=False)
	created_on = db.Column(db.DateTime,nullable=False)
	updated_on = db.Column(db.DateTime,nullable=False)
	classes = db.relationship("ClassModel",uselist=False,back_populates="student")
	
	# class constructor
	def __init__(self,data):
		self.name = data.get('name')
		self.class_id = data.get('class_id')
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
	def get_all_student():
		return StudentModel.query.all()
	
	@staticmethod
	def get_one_student(id):
		return StudentModel.query.get(id)

	@staticmethod
	def get_student_by_name(value):
		return StudentModel.query.filter_by(name=value).all()

	@staticmethod
	def get_student_by_name_class(value1,value2):
		#print(value1,value2)
		#print(StudentModel.query.filter(StudentModel.name == value1,StudentModel.class_id == value2))
		return StudentModel.query.filter(StudentModel.name == value1,StudentModel.class_id == value2).first()
		
	def __repr__(self):
		return '<id {}>'.format(self.id)

class StudentSchema(Schema):
	id = fields.Str(dump_only=True)
	name = fields.Str(required=True)
	class_id = fields.Int(required=True)
	created_on = fields.DateTime(dump_only=True)
	updated_on = fields.DateTime(dump_only=True)
	classes = fields.Nested(ClassesSchema)	



