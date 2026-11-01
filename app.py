import os
import smtplib
import traceback
from email.message import EmailMessage

from dotenv  import load_dotenv
from flask import Flask, render_template, request, redirect, session, url_for, jsonify
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "alert-system-development-key")

MODEL_FILE = "alert_model.pkl"
FEATURE_FILE = "feature_names.pkl"
TARGET_ENCODER_FILE = "target_encoder.pkl"
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS", "")
EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD", "")

model = None
MODEL_FEATURES = []
TARGET_ENCODER = None
FEATURE_ENCODERS = {}


def safe_float(value, default=0.0):
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def deterministic_token(value):
    text = "" if value is None else str(value).strip().lower()
    total = 0
    for idx, char in enumerate(text):
        total += (idx + 1) * ord(char)
    return total % 100000


def load_training_metadata():
    global model, MODEL_FEATURES, TARGET_ENCODER, FEATURE_ENCODERS

    try:
        model = joblib.load(MODEL_FILE)
        print("Model loaded successfully.")
    except Exception as e:
        print("ERROR LOADING MODEL:")
        print(e)
        model = None

    try:
        MODEL_FEATURES = list(joblib.load(FEATURE_FILE))
        print("MODEL FEATURES FOUND:")
        print(MODEL_FEATURES)
    except Exception as e:
        print("ERROR LOADING MODEL FEATURES:")
        print(e)
        MODEL_FEATURES = []

    try:
        TARGET_ENCODER = joblib.load(TARGET_ENCODER_FILE)
        print("Target encoder loaded successfully.")
    except Exception as e:
        print("ERROR LOADING TARGET ENCODER:")
        print(e)
        TARGET_ENCODER = None

    try:
        training_df = pd.read_csv("final_user_dataset_with_alert_stages.csv").drop_duplicates()
        for col in training_df.columns:
            if col == "alert_stage":
                continue
            if pd.api.types.is_numeric_dtype(training_df[col]):
                continue
            training_df[col] = training_df[col].fillna("Unknown").astype(str)

        for feature in MODEL_FEATURES:
            if feature in training_df.columns:
                encoder = LabelEncoder()
                encoder.fit(training_df[feature].astype(str))
                FEATURE_ENCODERS[feature] = encoder
    except Exception as e:
        print("ERROR BUILDING FEATURE ENCODERS:")
        print(e)


load_training_metadata()


def encode_feature_value(feature_name, value):
    if feature_name in FEATURE_ENCODERS:
        text_value = "" if value is None else str(value).strip()
        if text_value == "":
            return 0
        try:
            return int(FEATURE_ENCODERS[feature_name].transform([text_value])[0])
        except Exception:
            return deterministic_token(text_value)

    if value is None or str(value).strip() == "":
        return 0

    try:
        return float(value)
    except (TypeError, ValueError):
        return deterministic_token(value)


def send_alert_email(to_email, alert_message, session_count):
    if not EMAIL_ADDRESS or not EMAIL_APP_PASSWORD:
        print("EMAIL ALERT ERROR: Missing EMAIL_ADDRESS or EMAIL_APP_PASSWORD in .env")
        return False

    if not to_email:
        print("EMAIL ALERT ERROR: No recipient email supplied.")
        return False

    try:
        msg = EmailMessage()
        msg["Subject"] = "⚠️ FINAL ALERT Triggered"
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_email

        body = (
            f"Alert Message: {alert_message}\n"
            f"Session Count: {session_count}\n\n"
            "This is an automated alert from the Alert System."
        )
        msg.set_content(body)

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_APP_PASSWORD)
            server.send_message(msg)

        print(f"EMAIL ALERT SENT to {to_email}")
        return True

    except Exception:
        print("EMAIL ALERT ERROR:")
        traceback.print_exc()
        return False


def run_prediction_logic(payload):
    if model is None:
        raise Exception("Model is not loaded.")

    if not MODEL_FEATURES:
        raise Exception("Model feature list is empty. Check feature_names.pkl.")

    country = str(payload.get("country", "") or "")
    state = str(payload.get("state", "") or "")
    role = str(payload.get("role", "") or "")
    domain = str(payload.get("domain", "") or "")
    app_name = str(payload.get("app_name") or payload.get("app") or "")
    email = str(payload.get("email", "") or "")
    user_id = str(payload.get("user_id", "") or "")

    session_count = safe_float(payload.get("session_count", 0), 0.0)
    alert_sent = safe_float(payload.get("alert_sent", 0), 0.0)
    alert_message = str(payload.get("alert_message", "") or "")
    usage_minutes = safe_float(payload.get("usage_minutes", 0), 0.0)

    feature_values = {}
    for feature in MODEL_FEATURES:
        if feature == "country":
            feature_values[feature] = encode_feature_value(feature, country)
        elif feature == "state":
            feature_values[feature] = encode_feature_value(feature, state)
        elif feature == "role":
            feature_values[feature] = encode_feature_value(feature, role)
        elif feature == "domain":
            feature_values[feature] = encode_feature_value(feature, domain)
        elif feature == "app":
            feature_values[feature] = encode_feature_value(feature, app_name)
        elif feature == "app_name":
            feature_values[feature] = encode_feature_value(feature, app_name)
        elif feature == "session_count":
            feature_values[feature] = session_count
        elif feature == "alert_sent":
            feature_values[feature] = alert_sent
        elif feature == "alert_message":
            feature_values[feature] = encode_feature_value(feature, alert_message)
        elif feature == "usage_minutes":
            feature_values[feature] = usage_minutes
        else:
            feature_values[feature] = 0

    input_df = pd.DataFrame([feature_values], columns=MODEL_FEATURES)
    input_df = input_df.replace([float("inf"), float("-inf")], 0)
    input_df = input_df.fillna(0)
    for col in input_df.columns:
        input_df[col] = pd.to_numeric(input_df[col], errors="coerce")
    input_df = input_df.fillna(0).astype(float)

    print("\n==============================")
    print("MODEL EXPECTED FEATURES:")
    print(MODEL_FEATURES)
    print("\nFINAL INPUT:")
    print(input_df)

    prediction = model.predict(input_df)[0]
    prediction_result = str(prediction)

    if TARGET_ENCODER is not None and hasattr(TARGET_ENCODER, "inverse_transform"):
        try:
            prediction_result = str(TARGET_ENCODER.inverse_transform([int(prediction)])[0])
        except Exception:
            pass

    print("\nPREDICTION RESULT:")
    print(prediction_result)

    if str(prediction_result).strip().upper() == "FINAL_ALERT":
        if email:
            try:
                email_sent = send_alert_email(
                    email,
                    alert_message or "Final alert triggered",
                    int(session_count),
                )
            except Exception:
                print("EMAIL ALERT ERROR:")
                traceback.print_exc()
                email_sent = False
        else:
            print("EMAIL ALERT ERROR: No email provided in form.")
            email_sent = False
    else:
        email_sent = False

    username = str(payload.get("name", "") or "").strip()
    if not username:
        username = email.split("@", 1)[0] if "@" in email else (user_id or "Global User")

    session["prediction_data"] = {
        "username": username,
        "email": email,
        "country": country or "Unknown",
        "state": state or "Unknown",
        "role": role or "Unknown",
        "app_name": app_name or "Unknown",
        "session_count": int(session_count),
        "alert_message": alert_message or "No alert message provided.",
        "prediction": prediction_result,
        "email_status": "sent" if email_sent else (
            "not_sent" if prediction_result != "FINAL_ALERT" else "failed"
        ),
    }

    return {
        "success": True,
        "user_id": user_id,
        "predicted_stage": prediction_result,
        "confidence": 0.0 if not hasattr(model, "predict_proba") else float(max(model.predict_proba(input_df)[0])),
        "probabilities": {},
        "current_usage": usage_minutes,
    }


# ==========================================
# HOME PAGE
# ==========================================

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/visualization")
def visualization():
    prediction_data = session.get("prediction_data")
    if not prediction_data:
        return render_template("visualization.html", prediction_data=None)

    return render_template("visualization.html", prediction_data=prediction_data)


# ==========================================
# PREDICT ROUTE
# ==========================================

@app.route("/api/v1/prediction/predict", methods=["POST"])
def api_predict():
    try:
        payload = request.get_json(silent=True) or request.form.to_dict()
        result = run_prediction_logic(payload)
        return jsonify(result)
    except Exception as e:
        print("\n==============================")
        print("API PREDICTION ERROR")
        print("==============================")
        traceback.print_exc()
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/predict", methods=["POST"])
def predict():
    try:
        payload = request.form.to_dict()
        result = run_prediction_logic(payload)
        return redirect(url_for("visualization"))
    except Exception as e:
        print("\n==============================")
        print("PREDICTION ERROR")
        print("==============================")
        traceback.print_exc()
        error_message = str(e)
        return render_template(
            "index.html",
            prediction=f"Error: {error_message}"
        )


# ==========================================
# RUN APP
# ==========================================

if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )