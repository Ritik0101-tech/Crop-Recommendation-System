from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# =========================================
# DATABASE OBJECT
# =========================================

db = SQLAlchemy()



# =========================================
# USER TABLE
# =========================================

class User(db.Model):

    __tablename__ = "users"


    id = db.Column(

        db.Integer,

        primary_key=True
    )


    name = db.Column(

        db.String(100),

        nullable=False
    )


    mobile = db.Column(

        db.String(20),

        unique=True,

        nullable=False
    )


    password = db.Column(

        db.String(255),

        nullable=False
    )


    created_at = db.Column(

        db.DateTime,

        default=datetime.utcnow
    )



# =========================================
# HISTORY TABLE
# =========================================

class History(db.Model):

    __tablename__ = "history"


    id = db.Column(

        db.Integer,

        primary_key=True
    )


    user_id = db.Column(

        db.Integer,

        db.ForeignKey('users.id')
    )


    crop = db.Column(

        db.String(100)
    )


    confidence = db.Column(

        db.Float
    )


    n = db.Column(

        db.Float
    )


    p = db.Column(

        db.Float
    )


    k = db.Column(

        db.Float
    )


    ph = db.Column(

        db.Float
    )


    state = db.Column(

        db.String(100)
    )


    district = db.Column(

        db.String(100)
    )


    soil = db.Column(

        db.String(100)
    )


    temperature = db.Column(

        db.Float
    )


    humidity = db.Column(

        db.Float
    )


    rainfall = db.Column(

        db.Float
    )


    weather_condition = db.Column(

        db.String(100)
    )


    created_at = db.Column(

        db.DateTime,

        default=datetime.utcnow
    )



# =========================================
# INIT DATABASE
# =========================================

def init_db(app):

    app.config[
        'SQLALCHEMY_DATABASE_URI'
    ] = 'sqlite:///database.db'


    app.config[
        'SQLALCHEMY_TRACK_MODIFICATIONS'
    ] = False


    db.init_app(app)


    with app.app_context():

        db.create_all()


        print(
            "Database initialized successfully!"
        )