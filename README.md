# 📚 CodeAlpha AI Projects - Complete README

## 📋 Project Overview

This repository contains **4 Artificial Intelligence projects** developed during my internship at **CodeAlpha**. Each project demonstrates different aspects of AI and machine learning, from natural language processing to computer vision.

---

## 🗂️ Project Structure

```
CodeAlpha_ArtificialIntelligence/
├── CodeAlpha_LanguageTranslationTool/
│   └── Translation_app.py
├── CodeAlpha_FAQ Chatbot/
│   └── Chatbot_app.py
├── CodeAlpha_Music Generator/
│   └── musicGenerator_app.py
├── CodeAlpha_objectDetectionandTracking/
│   └── ObjectDetection_final_fixed.py
├── requirements.txt
└── README.md
```

---

# 🌟 PROJECT 1: Language Translation Tool

### 📝 Description
A powerful language translation application that supports multiple languages with text-to-speech functionality. Uses free translation APIs to provide accurate translations between 20+ languages.

### ✨ Features
- **🌍 20+ Languages Supported** (English, Spanish, French, German, Japanese, etc.)
- **🔊 Text-to-Speech** - Listen to translations
- **📋 Copy Functionality** - One-click copy to clipboard
- **🎨 Modern UI** - Clean, user-friendly interface
- **⚡ Real-time Translation** - Instant results

### 🛠️ Technologies Used
- **Python 3.11**
- **Streamlit** - Web interface
- **MyMemory API** - Translation service
- **gTTS** - Text-to-Speech
- **Requests** - API calls

### 🚀 How to Run
```bash
cd "CodeAlpha_LanguageTranslationTool"
streamlit run Translation_app.py
```



### 💡 Usage Guide
1. Select source language (from)
2. Select target language (to)
3. Enter text to translate
4. Click "Translate"
5. Use "Listen" button for audio
6. Click "Copy" to copy translation

---

# 🤖 PROJECT 2: FAQ Chatbot

### 📝 Description
An intelligent FAQ chatbot that uses Natural Language Processing (NLP) to understand user queries and provide relevant answers about the CodeAlpha internship program.

### ✨ Features
- **🧠 NLP Understanding** - Uses TF-IDF and cosine similarity
- **💬 Interactive Chat Interface** - Real-time conversation
- **🔍 Smart Matching** - Finds most relevant FAQ
- **⚡ Quick Suggestions** - Pre-defined question buttons
- **📊 Chat History** - Maintains conversation context

### 🛠️ Technologies Used
- **Streamlit** - Web interface
- **NLTK** - Natural Language Toolkit
- **Scikit-learn** - TF-IDF Vectorizer & Cosine Similarity
- **Pandas** - Data manipulation

### 🚀 How to Run
```bash
cd "CodeAlpha_FAQ Chatbot"
streamlit run Chatbot_app.py
```



### 💡 Usage Guide
1. Type your question in the chat box
2. Press Enter or click Send
3. Bot will find the best matching answer
4. Use suggestion buttons for quick questions
5. View chat history for reference

### 📋 Sample Questions
- "What is CodeAlpha internship?"
- "How long is the internship?"
- "Do I get a certificate?"
- "What projects can I choose?"

---

# 🎵 PROJECT 3: Music Generator

### 📝 Description
An AI-powered music generator that creates original melodies using music theory and LSTM neural networks. Generates MIDI files that can be played or downloaded.

### ✨ Features
- **🎼 Multiple Scales** - Major, Minor, Pentatonic, Chromatic
- **🎹 Melody Generation** - Creates unique note sequences
- **📊 Visualization** - See melody patterns
- **💾 MIDI Export** - Download as MIDI files
- **⚡ Fast Training** - Quick demonstration model
- **🎚️ Customizable** - Adjust length, complexity, tempo

### 🛠️ Technologies Used
- **TensorFlow/Keras** - LSTM neural network
- **Music21** - Music theory and MIDI handling
- **MIDIUtil** - MIDI file creation
- **NumPy** - Numerical operations
- **Streamlit** - Web interface

### 🚀 How to Run
```bash
cd "CodeAlpha_Music Generator"
streamlit run musicGenerator_app.py
```



### 💡 Usage Guide
1. Select musical scale (C Major, A Minor, etc.)
2. Adjust melody length (4-32 notes)
3. Set tempo (60-180 BPM)
4. Click "Generate Melody"
5. View the generated notes
6. Download as MIDI file
7. Play using any MIDI player

### 🎚️ Parameters Explained
- **Scale** - Determines which notes are available
- **Length** - Number of notes in melody
- **Tempo** - Speed of playback (BPM)
- **Complexity** - How varied the melody is

---

# 🔍 PROJECT 4: Object Detection & Tracking

### 📝 Description
A real-time object detection and tracking application using YOLOv8. Can detect 80 different object classes in images and videos with high accuracy.

### ✨ Features
- **🎯 80+ Object Classes** - People, vehicles, animals, etc.
- **📷 Multiple Input Sources** - Images and videos
- **🎨 Visual Detection** - Bounding boxes with labels
- **📊 Analytics Dashboard** - Real-time statistics
- **💾 Export Results** - Download processed images
- **⚡ Multiple Models** - Nano, Small, Medium options
- **🔄 Fallback Mode** - Works with OpenCV if YOLO unavailable

### 🛠️ Technologies Used
- **YOLOv8** - State-of-the-art object detection
- **OpenCV** - Image processing
- **Streamlit** - Web interface
- **Plotly** - Interactive charts
- **Pandas** - Data analysis
- **Pillow** - Image handling

### 🚀 How to Run
```bash
cd "CodeAlpha_objectDetectionandTracking"
streamlit run ObjectDetection_final_fixed.py
```


### 💡 Usage Guide
1. **Load Model** - Click "Load Model" in sidebar
2. **Choose Input** - Select Image or Video mode
3. **Upload File** - Upload image/video
4. **Detect** - Click "Detect Objects"
5. **View Results** - See detections with bounding boxes
6. **Download** - Save processed image

### 🎚️ Model Options
| Model | Speed | Accuracy | Use Case |
|-------|-------|----------|----------|
| Nano (yolov8n) | Fastest | Good | Quick tests |
| Small (yolov8s) | Balanced | Better | General use |
| Medium (yolov8m) | Slower | Best | High accuracy needed |
| OpenCV Fallback | Fast | Basic | No YOLO available |

### 📊 Detected Classes
- People, vehicles, animals
- Household items
- Electronics
- Sports equipment
- Food items
- And many more (80+ classes)

---

## 🔧 Installation & Setup

### Prerequisites
- Python 3.11 or higher
- pip package manager
- Virtual environment (recommended)

### Step-by-Step Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd CodeAlpha_ArtificialIntelligence
```

2. **Create virtual environment**
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### requirements.txt
```txt
# Core packages
streamlit>=1.28.0
numpy==1.24.3
pandas>=2.0.0
Pillow>=10.0.0

# Project 1: Translation
requests>=2.31.0
gtts>=2.5.1

# Project 2: Chatbot
nltk>=3.8.1
scikit-learn>=1.3.0

# Project 3: Music Generator
tensorflow>=2.13.0
music21>=8.1.0
midiutil>=1.2.1

# Project 4: Object Detection
opencv-python>=4.8.0
ultralytics>=8.0.0
plotly>=5.17.0
```

---

## 🎯 Project Completion Checklist

### Task 1: Language Translation Tool ✅
- [x] Multi-language support
- [x] Text-to-speech
- [x] Copy functionality
- [x] User-friendly interface

### Task 2: FAQ Chatbot ✅
- [x] NLP preprocessing
- [x] Similarity matching
- [x] Interactive chat
- [x] Suggestion buttons

### Task 3: Music Generator ✅
- [x] LSTM model
- [x] MIDI generation
- [x] Multiple scales
- [x] Downloadable output

### Task 4: Object Detection and Tracking ✅
- [x] YOLOv8 integration
- [x] Multiple input sources
- [x] Object Tracking frame to frame
- [x] Real-time detection
- [x] Analytics dashboard

---

## 📱 Demo Videos

### Project 1: Translation Tool
[Link to LinkedIn video]

### Project 2: FAQ Chatbot
[Link to LinkedIn video]

### Project 3: Music Generator
[Link to LinkedIn video]

### Project 4: Object Detection
[Link to LinkedIn video]

---

## 🤝 Contributing

This project was created for internship submission. Feel free to fork and enhance!

---

## 📞 Contact

- **Internship**: CodeAlpha
- **Website**: [www.codealpha.tech](https://www.codealpha.tech)
- **WhatsApp**: +91 8052293611
- **Email**: services@codealpha.tech

---

## 📄 License

This project is submitted as part of the CodeAlpha internship program. All rights reserved.

---

## 🙏 Acknowledgments

- **CodeAlpha** for the internship opportunity
- **Open Source Libraries** for making AI accessible
- **My Mentors** for guidance and support

---

## 🏆 Certificate Eligibility

✅ Completed **4 out of 4 tasks**
- Minimum required: 2 tasks
- Submitted: 4 tasks
- Status: **Eligible for Certificate**

---

## 📊 Quick Start Commands

```bash
# Translation Tool
cd "CodeAlpha_LanguageTranslationTool"
streamlit run Translation_app.py

# FAQ Chatbot
cd "CodeAlpha_FAQ Chatbot"
streamlit run Chatbot_app.py

# Music Generator
cd "CodeAlpha_Music Generator"
streamlit run musicGenerator_app.py

# Object Detection
cd "CodeAlpha_objectDetectionandTracking"
streamlit run ObjectDetection_final_fixed.py
```

---

## 🎨 Color Legend

| Color | Meaning |
|-------|---------|
| 🟢 Green | Success/Active |
| 🟡 Yellow | Warning/Loading |
| 🔴 Red | Error/Stop |
| 🔵 Blue | Information |
| 🟣 Purple | AI/ML Features |

---

## 🔄 Version History

- **v1.0.0** - Initial submission
- **v1.1.0** - Fixed object detection issues
- **v1.2.0** - Added Streamlit interfaces
- **v1.3.0** - Enhanced UI/UX

---

## 📝 Notes

- First run of object detection will download YOLO models (may take a few minutes)
- Translation tool requires internet connection
- Music generator creates original melodies each time
- Chatbot uses local NLP (no internet needed)

---

**Made with ❤️ for CodeAlpha Internship**
