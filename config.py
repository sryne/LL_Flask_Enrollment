import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\xcax\xc8o\xa5\x953\x8c~\x9bE\x866\\I\x99'

    MONGODB_SETTINGS = { 'db' : 'UTA_Enrollment' }
