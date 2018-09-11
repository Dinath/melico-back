import os.path

class Config:
    
    """
        Globals
    """
    DEBUG = os.path.isdir("/home/alex")

    """
        SECURITY
    """
    USERS_AUTH = {'root': 'pass'} if DEBUG else {'root': 'pass'}
    DOMAIN_AUTH = '*' if DEBUG else 'https://melico.fr'

    """
        ANDROID PATHS
    """
    GEN_ANDROID_PATH = '/home/alex/Projects/melico' if DEBUG else '/var/www/melico-app'
    GEN_ANDROID_PATH_CONFIG = GEN_ANDROID_PATH + '/src/app/class/auth.class.ts'
    GEN_ANDROID_PATH_APK = GEN_ANDROID_PATH + '/platforms/android/build/outputs/apk/'
    GEN_ANDROID_PATH_APK_FILE = 'android-release-unsigned.apk'

    """
        DATABASE
    """
    DB_USER = 'root' 
    DB_PASS = 'pass' if DEBUG else '*'
    DB_HOST = 'melico'
    DB_TABLE_REQUEST = 'request'

    """
        EMAILS
    """
    EMAIL_ADDRESS_RECEIVE = 'a.soyer@outlook.com'
    EMAIL_SMTP_USER = '*'
    EMAIL_SMTP_PASSWORD = '*'
    EMAIL_SMTP_HOST = '*'
    EMAIL_SMTP_PORT = 587
