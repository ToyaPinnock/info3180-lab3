from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY']='WASDFETRCSwcvvhgt324536bdg'
app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '8ec007c68adedb'
app.config['MAIL_PASSWORD'] = 'df7fae80c4d59a'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail=Mail(app)
from app import views