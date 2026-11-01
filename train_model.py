# ==========================================
# GLOBAL ALERT SYSTEM - MODEL TRAINING
# ==========================================

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# ==========================================
# 1. LOAD DATASET
# ==========================================
print("\nLoading dataset...")

df = pd.read_csv("final_user_dataset_with_alert_stages.csv")

print("\nDataset loaded successfully!")

print("\nFirst 5 rows:")
print(df.head())


# ==========================================
# 2. DATASET INFORMATION
# ==========================================

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Columns:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())


# ==========================================
# 3. REMOVE DUPLICATES
# ==========================================

df = df.drop_duplicates()

print("\nDuplicates removed successfully!")


# ==========================================
# 4. FILL MISSING VALUES
# ==========================================

# ==========================================
# 4. FILL MISSING VALUES
# ==========================================

print("\nHandling missing values...")

for col in df.columns:

    # Numerical columns
    if pd.api.types.is_numeric_dtype(df[col]):

        df[col] = df[col].fillna(
            df[col].median()
        )

    # Text / categorical columns
    else:

        df[col] = df[col].fillna(
            "Unknown"
        )

print("\nMissing values handled successfully!")


# ==========================================
# 5. DEFINE TARGET COLUMN
# ==========================================

TARGET_COLUMN = "alert_stage"

if TARGET_COLUMN not in df.columns:
    print(f"\nERROR: Target column '{TARGET_COLUMN}' not found!")
    print("Available columns are:")
    print(df.columns.tolist())
    exit()


# ==========================================
# 6. SEPARATE FEATURES AND TARGET
# ==========================================

X = df.drop(TARGET_COLUMN, axis=1)
y = df[TARGET_COLUMN]

print("\nFeatures used for training:")
print(X.columns.tolist())

print("\nTarget column:")
print(TARGET_COLUMN)


# ==========================================
# 7. REMOVE ID / SERIAL NUMBER COLUMNS
# ==========================================

columns_to_remove = []

for col in X.columns:

    col_lower = col.lower()

    if (
        "id" in col_lower
        or "name" in col_lower
        or "timestamp" in col_lower
        or "date" in col_lower
        or "time" in col_lower
    ):
        columns_to_remove.append(col)


if columns_to_remove:

    print("\nRemoving unnecessary columns:")
    print(columns_to_remove)

    X = X.drop(columns=columns_to_remove)


# ==========================================
# 8. ENCODE ALL CATEGORICAL COLUMNS
# ==========================================

print("\nEncoding categorical columns...")

for col in X.columns:

    if X[col].dtype == "object":

        print(f"Encoding: {col}")

        le = LabelEncoder()

        X[col] = le.fit_transform(
            X[col].astype(str)
        )


# ==========================================
# 9. FINAL CHECK FOR TEXT COLUMNS
# ==========================================

remaining_text_columns = X.select_dtypes(
    include=["object"]
).columns.tolist()

print("\nRemaining text columns:")
print(remaining_text_columns)


# ==========================================
# 10. CONVERT ALL VALUES TO NUMERIC
# ==========================================

for col in X.columns:

    X[col] = pd.to_numeric(
        X[col],
        errors="coerce"
    )


# ==========================================
# 11. HANDLE ANY NEW MISSING VALUES
# ==========================================

X = X.fillna(0)


print("\nFinal Data Types:")
print(X.dtypes)


# ==========================================
# 12. ENCODE TARGET COLUMN
# ==========================================

target_encoder = LabelEncoder()

y = target_encoder.fit_transform(
    y.astype(str)
)

print("\nTarget Classes:")
print(target_encoder.classes_)


# ==========================================
# 13. TRAIN TEST SPLIT
# ==========================================

print("\nSplitting dataset...")

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.2,

    random_state=42,

    stratify=y
)


# ==========================================
# 14. CREATE RANDOM FOREST MODEL
# ==========================================

print("\nTraining Random Forest Model...")

model = RandomForestClassifier(

    n_estimators=200,

    random_state=42,

    n_jobs=-1
)


# ==========================================
# 15. TRAIN MODEL
# ==========================================

model.fit(
    X_train,
    y_train
)


# ==========================================
# 16. MAKE PREDICTIONS
# ==========================================

print("\nMaking predictions...")

y_pred = model.predict(X_test)


# ==========================================
# 17. MODEL ACCURACY
# ==========================================

accuracy = accuracy_score(
    y_test,
    y_pred
)

print("\n==========================================")
print("MODEL RESULTS")
print("==========================================")

print(f"\nModel Accuracy: {accuracy * 100:.2f}%")


# ==========================================
# 18. CLASSIFICATION REPORT
# ==========================================

print("\nClassification Report:")

print(

    classification_report(
        y_test,
        y_pred,
        zero_division=0
    )
)


# ==========================================
# 19. SAVE MODEL
# ==========================================

joblib.dump(
    model,
    "alert_model.pkl"
)

print("\nModel saved successfully!")

print("File created: alert_model.pkl")


# ==========================================
# 20. SAVE TARGET ENCODER
# ==========================================

joblib.dump(
    target_encoder,
    "target_encoder.pkl"
)

print("Target encoder saved successfully!")

print("File created: target_encoder.pkl")


# ==========================================
# 21. SAVE FEATURE NAMES
# ==========================================

joblib.dump(
    list(X.columns),
    "feature_names.pkl"
)

print("Feature names saved successfully!")

print("File created: feature_names.pkl")


# ==========================================
# FINAL SUCCESS MESSAGE
# ==========================================

print("\n==========================================")
print("GLOBAL ALERT SYSTEM")
print("MODEL TRAINING COMPLETED SUCCESSFULLY!")
print("==========================================")

print(f"\nFinal Accuracy: {accuracy * 100:.2f}%")

print("\nGenerated Files:")

print("1. alert_model.pkl")
print("2. target_encoder.pkl")
print("3. feature_names.pkl")

print("\nNow you can run app.py")