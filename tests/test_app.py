from app.app import app


def test_health_ok(monkeypatch):
    monkeypatch.setenv("APP_SECRET", "test-secret")
    resp = app.test_client().get("/health")
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "ok"


def test_health_without_secret(monkeypatch):
    monkeypatch.delenv("APP_SECRET", raising=False)
    resp = app.test_client().get("/health")
    assert resp.status_code == 503
