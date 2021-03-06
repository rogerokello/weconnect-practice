import os

class Config:
    #get exported secret key or just assign it
    SECRET_KEY = os.environ.get('SECRET_KEY') or '#gfchyt678iui1224><>_'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER = {
            'swagger': '2.0',
            'title': 'weConnect API',
            'description': "This API brings businesses and individuals together.\
             By using it one will be able to create awareness of businesses and \
             give users the ability to write reviews about the businesses that \
             they have interacted with.",
            'basePath': '/',
            'version': '0.0.1',
            'contact': {
                'Developer': 'Roger Okello',
                'email': 'rogerokello@gmail.com'
            },
            'license': {
                'name': 'MIT'
            },
            'tags': [
                {
                    'name': 'User',
                    'description': 'The user of the system'
                },
                {
                    'name': 'Business',
                    'description': 'Businesses that you can connect with to get\
                    a service'
                },
                {
                    'name': 'Review',
                    'description': 'A user rating and remarks for a business'
                },
            ]
        }
    
    #initialise the application with config settings
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://postgres:admin@localhost/apibusinessdb'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'postgresql://postgres:admin@localhost/business_test_db'

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}