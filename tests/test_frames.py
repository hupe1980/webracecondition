from webracecondition import create_request_frames, has_end_stream_set

def test_create_request_frames_with_body() -> None:
    stream = create_request_frames(
        scheme="https",
        host="localhost",
        port="443",
        method="POST",
        path="/",
        stream_id=1,
        body=b"foo",
    )

    last_frame = stream.frames[len(stream.frames)-1]
    
    assert last_frame.payload.data == b"foo"
    assert has_end_stream_set(last_frame)
    

