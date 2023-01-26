from src.model import sound_to_text, tiny_model


def test_whisper():
    model = tiny_model
    file_path = "data/test_data/meet.mp3"
    result = sound_to_text(model, file_path)
    assert result
