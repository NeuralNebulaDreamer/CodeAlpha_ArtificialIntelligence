import subprocess
import sys
import os


def install_packages():
    packages = [
        'requests',
        'gtts',
        'pygame',
        'nltk',
        'scikit-learn',
        'numpy',
        'tensorflow',
        'midiutil',
        'opencv-python',
        'Pillow',
        'streamlit'
    ]

    for package in packages:
        print(f"\n📦 Installing {package}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"✅ Successfully installed {package}")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install {package}: {e}")

    # Download NLTK data
    print("\n📚 Downloading NLTK data...")
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')
    nltk.download('punkt_tab')

    print("\n🎉 All installations complete!")


if __name__ == "__main__":
    install_packages()