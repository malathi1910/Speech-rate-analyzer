# Speech Rate Analyzer using Whisper

A Python application that records audio from a microphone, transcribes speech using OpenAI Whisper, calculates **Words Per Minute (WPM)**, and saves the results in a JSON file.

---

## 📌 Project Overview

The Speech Rate Analyzer measures a speaker's speaking speed by:

* Recording audio for a specified duration
* Converting speech to text using Whisper
* Calculating the total number of words spoken
* Computing Words Per Minute (WPM)
* Saving the results for future analysis

This project demonstrates the integration of **audio processing**, **speech recognition**, and **data analysis** using Python.

---

## ✨ Features

* 🎤 Record audio directly from the microphone
* 📝 Transcribe audio using OpenAI Whisper
* ⏱️ Calculate speaking duration
* 📊 Compute Words Per Minute (WPM)
* 📄 Save results in JSON format
* 📁 Store audio recordings automatically
* 🧩 Modular code structure for easy maintenance

---

## 🛠️ Tech Stack

* Python 3.x
* OpenAI Whisper
* SoundDevice
* NumPy
* SciPy

---

## 📂 Project Structure

```text
speech-rate-analyzer/
│
├── main.py
├── requirements.txt
├── README.md
│
├── recordings/
│   └── candidate_YYYYMMDD_HHMMSS.wav
│
├── output/
│   └── result.json
│
└── utils/
    ├── recorder.py
    ├── transcriber.py
    ├── duration_calculator.py
    └── wpm_calculator.py
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/speech-rate-analyzer.git
cd speech-rate-analyzer
```

### 2. Create and Activate a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the application:

```bash
python main.py
```

Enter the recording duration when prompted:

```text
Enter recording duration in seconds: 30
```

The application will:

1. Record audio from the microphone
2. Save the audio file
3. Transcribe the recording using Whisper
4. Calculate speaking duration
5. Compute WPM
6. Save the results to a JSON file

---

## 🧮 WPM Calculation

```text
WPM = Total Number of Words / Speaking Duration (in minutes)
```

Example:

* Total words spoken: 105
* Speaking duration: 30 seconds (0.5 minutes)

```text
WPM = 105 / 0.5 = 210
```

---

## 📄 Sample Output

### Console Output

```text
Step 1: Getting duration
Enter recording duration in seconds: 30

Step 2: Recording audio
Recording for 30 seconds...
Speak now...

Recording saved: recordings/candidate_20260619_204256.wav

Step 3: Transcribing audio
Loading Whisper model...

Step 4: Transcript received
So can you explain to me what is machine learning like I'm a 5 year old?

Step 5: Calculating speaking duration
Speaking duration: 30.00

Step 6: Calculating WPM
WPM: 210

Step 7: Saving result
Step 8: Saved successfully
```

### `output/result.json`

```json
{
  "words_per_minute": 210
}
```

---

## 🔮 Future Enhancements

* Calculate actual speech duration using Voice Activity Detection (VAD)
* Support multiple Whisper model sizes
* Add a web interface using Streamlit or Gradio
* Track speaking performance over time
* Export results to CSV or PDF
* Add error handling and unit tests

---


