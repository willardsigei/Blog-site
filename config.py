import os

class Config:
    QUOTE_API_BASE_URL ='http://quotes.stormconsultancy.co.uk/random.json'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/blog'
    SECRET_KEY =os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'