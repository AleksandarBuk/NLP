from nlp_logic.nlp_main import get_phrases

def test_get_phrases():
    phrases = get_phrases("Lakers")
    assert "bryant" in phrases, f"Expected 'bryant' in phrases, but got: {phrases}"