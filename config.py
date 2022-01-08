class Config:
    SECRET_KEY = 'secret key'
    MYSQL_USERNAME = 'rasbet'
    MYSQL_PASSWORD = 'password'
    MYSQL_HOST = 'localhost'
    #MYSQL_PORT = 5000
    MYSQL_DATABASE = 'RASBetDB'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{ Config.MYSQL_USERNAME }:{ Config.MYSQL_PASSWORD }@' \
                                f'{ Config.MYSQL_HOST }/{ Config.MYSQL_DATABASE }'
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{ Config.MYSQL_USERNAME }:{ Config.MYSQL_PASSWORD }@' \
                                f'{ Config.MYSQL_HOST }/{ Config.MYSQL_DATABASE }'


config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}