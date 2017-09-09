class Config(object):
    SECRET_KEY = 'my_secret_key'
    BASE_URL = 'http://127.0.0.1:8080'


class DevelopmentConfig(Config):
    DEBUG = True
    CASSANDRA_PORT = 9042
    CASSANDRA_HOSTS = ['127.0.0.1']
    CASSANDRA_KEYSPACE = 'bomberman'
    BASE_URL = 'http://127.0.0.1:8080'
    # CASSANDRA_SETUP_KWARGS = {'protocol_version': 3}
