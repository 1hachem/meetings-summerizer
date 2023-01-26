import whisper

tiny_model = whisper.load_model("tiny")


def sound_to_text(model, file_path):
    result = model.transcribe(file_path)
    return result["text"]
