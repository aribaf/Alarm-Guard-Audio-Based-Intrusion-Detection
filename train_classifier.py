import os
import librosa
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score
import joblib



def extract_features(file_path):
    """Extracts MFCC features from an audio file."""
    y, sr = librosa.load(file_path, sr=None)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return np.mean(mfcc.T, axis=0)

def preprocess_data(data_dir):
    """Loads audio files and prepares feature-label pairs."""
    features, labels = [], []
    for label, class_name in enumerate(os.listdir(data_dir)):
        class_path = os.path.join(data_dir, class_name)
        if os.path.isdir(class_path):
            for file_name in os.listdir(class_path):
                file_path = os.path.join(class_path, file_name)
                features.append(extract_features(file_path))
                labels.append(label)
    return np.array(features), np.array(labels)

# Prepare the data
features, labels = preprocess_data('./data')

# Check if there are enough samples
if len(features) < 2:
    raise ValueError("Not enough data samples to split. Ensure you have at least two samples.")

# Train the model
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, 'sound_classifier.pkl')
print("Sound classifier saved.")

# Test the model
accuracy = accuracy_score(y_test, model.predict(X_test))
print(f"Model Accuracy: {accuracy:.2f}")
