import requests


# Checking access to the application
def test_access():
    r = requests.get("http://127.0.0.1:5000")
    assert r.ok, "Unreached."
