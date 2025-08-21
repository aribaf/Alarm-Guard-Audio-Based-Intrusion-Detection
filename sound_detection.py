import sounddevice as sd
from scipy.io.wavfile import write
import librosa
import numpy as np
import joblib
import os

# Load the pre-trained sound classifier model
MODEL_PATH = 'sound_classifier.pkl'
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Error: {MODEL_PATH} not found. Ensure the model file is in the working directory.")

model = joblib.load(MODEL_PATH)
print("Sound classifier model loaded successfully.")

def record_audio(duration=5, fs=44100, output_file='temp.wav'):
    """
    Records audio for a given duration and saves it as a WAV file.

    Args:
        duration (int): Recording duration in seconds.
        fs (int): Sampling frequency in Hz.
        output_file (str): Path to save the recorded audio.

    Returns:
        str: Path to the saved audio file.
    """
    print(f"Recording audio for {duration} seconds...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()  # Wait for the recording to finish
    write(output_file, fs, (audio * 32767).astype(np.int16))
    print(f"Audio recorded and saved to {output_file}.")
    return output_file

def extract_features(file_path):
    """
    Extracts MFCC features from an audio file.

    Args:
        file_path (str): Path to the audio file.

    Returns:
        np.ndarray: Extracted MFCC features as a mean vector.
    """
    try:
        y, sr = librosa.load(file_path, sr=None)
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        return np.mean(mfcc.T, axis=0)
    except Exception as e:
        print(f"Error extracting features from {file_path}: {e}")
        return None

def detect_specific_sound(file_path):
    """
    Detects if the specific sound is present in the audio file.

    Args:
        file_path (str): Path to the audio file.

    Returns:
        bool: True if the specific sound is detected, False otherwise.
    """
    print("Analyzing audio for specific sound...")
    features = extract_features(file_path)
    if features is not None:
        prediction = model.predict([features])
        return prediction[0] == 1
    else:
        print("Feature extraction failed. Cannot classify the sound.")
        return False
