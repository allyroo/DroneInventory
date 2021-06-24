import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

# be able to make sure path works;
#Give access to the project in ANY OS that we find ourselves in
# ALlow outside files/folders to be added to the project from the base directory




class Config():
    """
        Set Config variables for the flask app.
        Using Enviornment variables where available
        Otherwise create the config variable if not done already.
    """
    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_ENV = os.getenv('FLASK_ENV')
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'You will never guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Turn off update messaes from sqlalchemy