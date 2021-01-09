#--------- Flask settings
SERVER_HOST = 'http://micro-func-frontend.azurewebsites.net'
SERVER_PORT = 5000
FLASK_DEBUG = False # Do not use debug mode in prod

# Flask-Restplus settings
SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_404_HELP = True
API_VERSION = 'v1'

#-------- Azure constants

# ------- For Local Testing -------
#API_URL = "http://localhost:7071/api"

# ------- For production -------
# where APP_NAME is your Azure Function App name
API_URL = "https://micro-func.azurewebsites.net/api"
