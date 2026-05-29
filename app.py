from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask import redirect
from flask import session
import re

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

import numpy as np
import joblib

from database import (
    db,
    User,
    History,
    init_db
)

from utils.weather import (
    get_weather,
    get_detailed_weather
)

from utils.fertilizer import (
    fertilizer_advice
)

from utils.soil import (
    soil_advice
)

from utils.tips import (
    get_general_tips,
    get_crop_tips
)



# =========================================
# APP CONFIG
# =========================================

app = Flask(__name__)

app.secret_key = "smart_crop_secret_key"



# =========================================
# DATABASE
# =========================================

init_db(app)



# =========================================
# LOAD MODEL
# =========================================

model = joblib.load(
    "model/crop_model.pkl"
)

label_encoder = joblib.load(
    "model/label_encoder.pkl"
)



# =========================================
# HOME
# =========================================

@app.route('/')
def home():

    return render_template(
        'index.html'
    )



# =========================================
# LOGIN
# =========================================

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        mobile = request.form.get('mobile')
        if not re.fullmatch(r"\d{10}", mobile):

            return render_template(

                'login.html',

            error="Mobile number must be 10 digits"
        )

        password = request.form.get('password')


        if not mobile or not password:

            return render_template(

                'login.html',

                error="All fields are required"
            )


        user = User.query.filter_by(
            mobile=mobile
        ).first()


        if user and check_password_hash(
            user.password,
            password
        ):

            session['user_id'] = user.id

            return render_template(

                'dashboard.html',

                success="Login Successful!"
            )


        return render_template(

            'login.html',

            error="Invalid mobile or password"
        )


    return render_template(
        'login.html'
    )

@app.route('/forgot-password',
methods=['GET', 'POST'])

def forgot_password():

    if request.method == 'POST':

        mobile = request.form.get(
            'mobile'
        )

        password = request.form.get(
            'password'
        )


        user = User.query.filter_by(
            mobile=mobile
        ).first()


        if not user:

            return render_template(

                'forgot_password.html',

                error="Mobile number not found"
            )


        user.password = generate_password_hash(
            password
        )

        db.session.commit()


        return render_template(

            'login.html',

            success="Password updated successfully"
        )


    return render_template(
        'forgot_password.html'
    )



# =========================================
# REGISTER
# =========================================

@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        name = request.form.get('name')

        mobile = request.form.get('mobile')

        if not re.fullmatch(r"\d{10}", mobile):

            return render_template(

                'register.html',

            error="Mobile number must be 10 digits"
        )

        password = request.form.get('password')


        # VALIDATION

        if not name or not mobile or not password:

            return render_template(

                'register.html',

                error='All fields are required'
            )


        # CHECK EXISTING USER

        existing_user = User.query.filter_by(
            mobile=mobile
        ).first()


        if existing_user:

            return render_template(

                'register.html',

                error="Mobile number already exists"
            )


        # HASH PASSWORD

        hashed_password = generate_password_hash(
            password
        )


        # CREATE USER

        user = User(

            name=name,

            mobile=mobile,

            password=hashed_password
        )


        db.session.add(user)

        db.session.commit()


        return render_template(

            'login.html',

            success="Registration Successful!"
        )


    return render_template(
        'register.html'
    )



# =========================================
# LOGOUT
# =========================================

@app.route('/logout')
def logout():

    session.clear()

    return redirect('/')



# =========================================
# DASHBOARD
# =========================================

@app.route('/dashboard')
def dashboard():

    if 'user_id' not in session:

        return redirect('/login')


    return render_template(
        'dashboard.html'
    )



# =========================================
# HISTORY
# =========================================

@app.route('/history')
def history():

    if 'user_id' not in session:

        return redirect('/login')


    records = History.query.filter_by(

        user_id=session['user_id']

    ).order_by(

        History.created_at.desc()

    ).all()


    return render_template(

        'history.html',

        records=records
    )



# =========================================
# RESULT PAGE
# =========================================

@app.route('/result')
def result():

    return render_template(
        'result.html'
    )



# =========================================
# ADVICE PAGE
# =========================================

@app.route('/advice')
def advice():

    fertilizer = {
        "advice":
        "Apply balanced NPK fertilizer. Use organic compost and maintain proper irrigation."
    }

    soil = {
        "solution":
        "Maintain soil fertility using vermicompost and crop rotation."
    }

    tips = [

        "Use drip irrigation for water saving.",

        "Avoid overuse of pesticides.",

        "Test soil every season.",

        "Use organic manure regularly.",

        "Maintain proper crop rotation."
    ]


    return render_template(

        'advice.html',

        fertilizer=fertilizer,

        soil=soil,

        tips=tips
    )



# =========================================
# WEATHER API
# =========================================

@app.route('/weather')
def weather():

    lat = request.args.get('lat')

    lon = request.args.get('lon')


    weather_data = get_detailed_weather(
        lat,
        lon
    )


    return jsonify(weather_data)



# =========================================
# PREDICT
# =========================================

@app.route('/predict', methods=['POST'])
def predict():

    try:

        data = request.json


        # INPUTS

        n = float(data['n'])

        p = float(data['p'])

        k = float(data['k'])

        ph = float(data['ph'])

        state = data['state']

        district = data['district']

        soil = data['soil']

        lat = data['lat']

        lon = data['lon']


        # WEATHER

        temp, humidity, rainfall, condition = (
            get_weather(lat, lon)
        )


        # MODEL INPUT

        features = np.array([[

            n,
            p,
            k,
            temp,
            humidity,
            ph,
            rainfall

        ]])


        # PREDICTION

        probs = model.predict_proba(
            features
        )[0]


        classes = model.classes_


        top3_idx = np.argsort(
            probs
        )[-3:][::-1]


        crops = [

            label_encoder.inverse_transform(
                [classes[i]]
            )[0]

            for i in top3_idx
        ]


        confidence = [

            round(
                probs[i] * 100,
                2
            )

            for i in top3_idx
        ]


        # IMAGES

        images = [

            f"/static/images/crops/{crop.lower()}.jpg"

            for crop in crops
        ]


        # ADVICE

        fertilizer = fertilizer_advice(
            n,
            p,
            k
        )

        soil_info = soil_advice(ph)

        tips = get_general_tips()

        crop_specific = get_crop_tips(
            crops[0]
        )


        # SAVE HISTORY

        if 'user_id' in session:

            history = History(

                user_id=session['user_id'],

                crop=crops[0],

                confidence=confidence[0],

                n=n,

                p=p,

                k=k,

                ph=ph,

                state=state,

                district=district,

                soil=soil,

                temperature=temp,

                humidity=humidity,

                rainfall=rainfall,

                weather_condition=condition
            )


            db.session.add(history)

            db.session.commit()


        # RESPONSE

        return jsonify({

            "crops": crops,

            "confidence": confidence,

            "images": images,

            "weather": {

                "temperature": temp,

                "humidity": humidity,

                "rainfall": rainfall,

                "condition": condition
            },

            "fertilizer": fertilizer,

            "soil": soil_info,

            "tips": tips,

            "crop_tips": crop_specific
        })


    except Exception as e:

        return jsonify({

            "error": str(e)
        })



# =========================================
# MAIN
# =========================================

if __name__ == '__main__':

    app.run(

        debug=True,

        host='0.0.0.0',

        port=5000
    )