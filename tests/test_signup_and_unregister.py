def test_signup_success(client):
    email = "new@mergington.edu"
    r = client.post("/activities/Chess Club/signup", params={"email": email})
    assert r.status_code == 200
    assert email in r.json().get("message", "")


def test_signup_already(client):
    r = client.post("/activities/Chess Club/signup", params={"email": "michael@mergington.edu"})
    assert r.status_code == 400


def test_signup_nonexistent(client):
    r = client.post("/activities/NoSuch/signup", params={"email": "someone@example.com"})
    assert r.status_code == 404


def test_unregister_success(client):
    r = client.delete("/activities/Chess Club/unregister", params={"email": "michael@mergington.edu"})
    assert r.status_code == 200


def test_unregister_not_registered(client):
    r = client.delete("/activities/Chess Club/unregister", params={"email": "nobody@example.com"})
    assert r.status_code == 400
