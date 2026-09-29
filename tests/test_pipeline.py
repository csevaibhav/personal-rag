from src.pipeline import answer_query


def test_answer_query_returns_a_string():
    result = answer_query("what is my degree?")
    assert isinstance(result, str)
    assert "what is my degree?" in result
