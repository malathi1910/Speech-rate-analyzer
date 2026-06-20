import os
from datetime import datetime

import sounddevice as sd
from scipy.io.wavfile import write


SAMPLE_RATE = 16000


def record_audio(duration=30):
    os.makedirs("recordings", exist_ok=True)

    filename = datetime.now().strftime(
        "recordings/candidate_%Y%m%d_%H%M%S.wav"
    )

    print(f"\nRecording for {duration} seconds...")
    print("Speak now...\n")

    audio = sd.rec(
        int(duration * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    write(filename, SAMPLE_RATE, audio)

    print(f"Recording saved: {filename}")

    return filename
