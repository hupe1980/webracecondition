from webracecondition import Request

def test_request_method() -> None:
    request = Request("get", "/")
    assert request.method == "GET"

def test_request_params() -> None:
    request = Request("get", "/", params={"foo": "bar"})
    assert request.path == "/?foo=bar"

def test_request_params_no_params() -> None:
    request = Request("get", "/")
    assert request.path == "/"

def test_request_content_lenght() -> None:
    body = b"foo"
    request = Request("get", "/", raw_body=body)
    assert request.headers["content-length"] == str(len(body))

def test_request_content_lenght_empty_body() -> None:
    request = Request("get", "/")
    assert "content-length" not in request.headers

def test_request_cookies() -> None:
    request = Request("get", "/", cookies={"foo": "foo", "bar": "bar"})
    assert "cookie" in request.headers
    assert request.headers["cookie"] == "foo=foo; bar=bar"