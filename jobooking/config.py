import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  
SQLALCHEMY_DATABASE_URI = 'mysql://jobooking:jobooking@jobooking.c5uswuz5ngcu.us-west-2.rds.amazonaws.com:3306/jobooking'
SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
SECURITY_TRACKABLE = True
SECURITY_PASSWORD_SALT = 'jobooking_super_password'
