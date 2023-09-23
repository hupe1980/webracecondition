from webracecondition import Request

def test_request_method() -> None:
    request = Request("get", "/")
    assert request.method == "GET"