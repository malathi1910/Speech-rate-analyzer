import whisper


_model = None


def load_model():
    global _model

    if _model is None:
        print("Loading Whisper model...")
        _model = whisper.load_model("medium")

    return _model


def transcribe_audio(audio_path):
    model = load_model()

    result = model.transcribe(
        audio_path,
        language="en",
        fp16=False
    )

    return result["text"]
