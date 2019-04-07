#/src/views/StudentView
#import sys
#sys.path.append("../models")
#import student_api.src.models as m
from flask import request, json, Response, Blueprint, jsonify
from src.models import StudentModel,ClassModel
from src.models.StudentModel import StudentSchema
from src.models.ClassModel import ClassesSchema
#from m.StudentModel import StudentModel

student_api = Blueprint('student', __name__)
student_schema=StudentSchema()
class_schema=ClassesSchema()

@student_api.route('/', methods=['POST'])
def create():
	''' 
		create student function
	'''
	req_data = request.get_json() # convert body to dictionary
	#class_data,error =class_schema.load(req_data)
	classes=ClassModel(name=req_data['class_name'],id=req_data['class_id'])
	#checkif class already exist in db or not
	classes_in_db=ClassModel.get_one_class(req_data['class_id'])
	data, error = student_schema.load(req_data)
	if error:
		return custom_response(error,400)
        # check if student already exist in db
	#student_in_db = StudentModel.get_student_by_name_class(req_data['name'],req_data['class_id'])
	if(classes_in_db):
		pass
	else:
		classes.save() 
	#if(student_in_db):
		#message={'error' :'student with same name exist in the same class' }
		#return custom_response(message,400)
	student=StudentModel(data)
	student.save()
	message={'o/p':'Student data successfully saved'}
	return custom_response(message,201)
	
	#student=StudentModel(name=req_data['name'],class_id=req_data['class_id'])
	#print(student)
	#student.save()
	#return jsonify({'message':'New student successfully created.'}),200


@student_api.route('/', methods=['GET'])
def get_all_students():
	'''
		get student function
	'''
	#data = []
	students = StudentModel.get_all_student()
	ser_students=student_schema.dump(students,many=True).data
	return custom_response(ser_students,200)
	#import pdb; pdb.set_trace()
	#for student in students:
		#_student = student_schema.dump(student).data
		#data.append(_student)
	#return jsonify(data)

@student_api.route('/<uuid:id>', methods=['PUT'])
def update(id):
	'''
		update the student 
	'''
	req_data = request.get_json()
	data,error= student_schema.load(req_data,partial=True)
	if error:
		return custom_response(error,400)
	student=StudentModel.get_one_student(str(id))
	student.update(data)
	ser_student=student_schema.dump(student).data
	message={'o/p':'Student data successfully updated'}
	return custom_response(message,200)

@student_api.route('/<uuid:id>', methods=['DELETE'])
def delete(id):
	'''
		delete a user
	'''
	student = StudentModel.get_one_student(str(id))
	student.delete()
	message={'o/p':'Student data successfully deleted'}
	return custom_response(message,204)

@student_api.route('/<uuid:id>', methods=['GET'])
def get_student(id):
	'''
		get student
	'''
	student = StudentModel.get_one_student(str(id))
	ser_student= student_schema.dump(student).data
	return custom_response(ser_student,200)


def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )	
