# Test all imports
print("Testing imports...")

try:
    import requests
    print("✅ requests")
except:
    print("❌ requests")

try:
    from gtts import gTTS
    print("✅ gtts")
except:
    print("❌ gtts")

try:
    import pygame
    print("✅ pygame")
except:
    print("❌ pygame")

try:
    import nltk
    print("✅ nltk")
except:
    print("❌ nltk")

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    print("✅ scikit-learn")
except:
    print("❌ scikit-learn")

try:
    import numpy as np
    print("✅ numpy")
except:
    print("❌ numpy")

try:
    import tensorflow as tf
    print("✅ tensorflow")
except:
    print("❌ tensorflow")

try:
    from midiutil import MIDIFile
    print("✅ midiutil")
except:
    print("❌ midiutil")

try:
    import cv2
    print("✅ opencv-python")
except:
    print("❌ opencv-python")

try:
    from PIL import Image
    print("✅ Pillow")
except:
    print("❌ Pillow")

try:
    import streamlit
    print("✅ streamlit")
except:
    print("❌streamlit")