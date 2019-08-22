from module_tracker import tracker


def test_tracking_with_glob():
    assert tracker.track_glob("tests/test_data/**/*.py") == sorted(
        ["ast", "glob", "flask", "flask_cors", "tensorflow", "torch", "test_data"]
    )
