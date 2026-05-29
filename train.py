import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier


# =====================================================
# LOAD DATASET
# =====================================================

df = pd.read_csv("data/crop_data.csv")


# =====================================================
# CLEAN DATA
# =====================================================

# lowercase column names
df.columns = df.columns.str.lower()

# remove duplicate rows
df.drop_duplicates(inplace=True)

# fill missing values
df = df.ffill()


# =====================================================
# RENAME COLUMNS
# =====================================================

df.rename(columns={

    'nitrogen': 'n',

    'phosphorus': 'p',

    'potassium': 'k',

    'label': 'label'

}, inplace=True)


# =====================================================
# REQUIRED FEATURES
# =====================================================

features = [

    'n',
    'p',
    'k',
    'temperature',
    'humidity',
    'ph',
    'rainfall'
]


# =====================================================
# REMOVE OUTLIERS
# =====================================================

for col in features:

    q1 = df[col].quantile(0.25)

    q3 = df[col].quantile(0.75)

    iqr = q3 - q1

    lower = q1 - 1.5 * iqr

    upper = q3 + 1.5 * iqr

    df = df[
        (df[col] >= lower) &
        (df[col] <= upper)
    ]


# =====================================================
# LABEL ENCODING
# =====================================================

label_encoder = LabelEncoder()

df['label'] = label_encoder.fit_transform(
    df['label']
)


# =====================================================
# INPUT / OUTPUT
# =====================================================

X = df[features]

y = df['label']


# =====================================================
# TRAIN TEST SPLIT
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.2,

    random_state=42,

    stratify=y
)


# =====================================================
# RANDOM FOREST MODEL
# =====================================================

rf_model = RandomForestClassifier(

    n_estimators=700,

    max_depth=25,

    min_samples_split=2,

    min_samples_leaf=1,

    random_state=42
)


# =====================================================
# EXTRA TREES MODEL
# =====================================================

et_model = ExtraTreesClassifier(

    n_estimators=700,

    random_state=42
)


# =====================================================
# TRAIN MODELS
# =====================================================

rf_model.fit(X_train, y_train)

et_model.fit(X_train, y_train)


# =====================================================
# PREDICTIONS
# =====================================================

rf_pred = rf_model.predict(X_test)

et_pred = et_model.predict(X_test)


# =====================================================
# ACCURACY
# =====================================================

rf_acc = accuracy_score(y_test, rf_pred)

et_acc = accuracy_score(y_test, et_pred)


print(f"Random Forest Accuracy: {rf_acc * 100:.2f}%")

print(f"Extra Trees Accuracy: {et_acc * 100:.2f}%")


# =====================================================
# BEST MODEL
# =====================================================

best_model = rf_model

best_accuracy = rf_acc


if et_acc > best_accuracy:

    best_model = et_model

    best_accuracy = et_acc


print(f"Best Accuracy: {best_accuracy * 100:.2f}%")


# =====================================================
# SAVE MODEL
# =====================================================

joblib.dump(

    best_model,

    'model/crop_model.pkl'
)


joblib.dump(

    label_encoder,

    'model/label_encoder.pkl'
)


print("Model saved successfully!")


# =====================================================
# SAMPLE TEST
# =====================================================

sample = np.array([[

    90,      # N
    42,      # P
    43,      # K
    26.5,    # temperature
    80,      # humidity
    6.5,     # ph
    202      # rainfall

]])


prediction = best_model.predict(sample)

crop = label_encoder.inverse_transform(
    prediction
)

print("Predicted Crop:", crop[0])