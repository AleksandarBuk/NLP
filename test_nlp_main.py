from nlp_logic.nlp_main import search_wikipedia, summarize_wikipedia, get_text_blob, get_phrases

def test_get_phrase():
    assert "bryant" in get_phrases("Lakers") 