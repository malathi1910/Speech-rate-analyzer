from pydub import AudioSegment, silence


def get_speaking_duration(
    audio_path,
    min_silence_len=800,
    silence_offset=16
):
    audio = AudioSegment.from_file(audio_path)

    silence_threshold = audio.dBFS - silence_offset

    non_silent_segments = silence.detect_nonsilent(
        audio,
        min_silence_len=min_silence_len,
        silence_thresh=silence_threshold
    )

    speaking_duration_ms = sum(
        end - start
        for start, end in non_silent_segments
    )

    return speaking_duration_ms / 1000.0
