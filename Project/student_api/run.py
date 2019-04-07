# /run.py
import os

from src.app import create_app

if __name__ == '__main__':
	env_name=os.getenv('FLASK_ENV')    
	#env_name='development'
	app=create_app(env_name)
	# run app
	#app.run(port=<new_port_number_here>)
	app.run(host='0.0.0.0')

