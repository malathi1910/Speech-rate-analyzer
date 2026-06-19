import json
import os

from utils.recorder import record_audio
from utils.transcriber import transcribe_audio
from utils.duration_calculator import get_speaking_duration
from utils.wpm_calculator import calculate_wpm


def main():
    try:
        os.makedirs("output", exist_ok=True)

        print("Step 1: Getting duration")
        duration = int(input("Enter recording duration in seconds: "))

        print("Step 2: Recording audio")
        audio_path = record_audio(duration)
        print(f"Audio saved at: {audio_path}")

        print("Step 3: Transcribing audio")
        transcript = transcribe_audio(audio_path)

        print("Step 4: Transcript received")
        print(transcript)

        print("Step 5: Calculating speaking duration")
        speaking_duration = get_speaking_duration(audio_path)

        print(f"Speaking duration: {speaking_duration:.2f}")

        print("Step 6: Calculating WPM")
        wpm = calculate_wpm(transcript, speaking_duration)

        print(f"WPM: {wpm}")

        result = {
            "words_per_minute": wpm
        }

        print("Step 7: Saving result")

        output_path = "output/result.json"

        with open(output_path, "w") as file:
            json.dump(result, file, indent=2)

        print("Step 8: Saved successfully")
        print(json.dumps(result, indent=2))

    except Exception as e:
        print(f"\nERROR: {e}")


if __name__ == "__main__":
    main()
