from app.calc import uptime_percent


def test_all_up():
    assert uptime_percent(100, 100) == 100.0


def test_rounding():
    assert uptime_percent(1, 3) == 33.33


def test_no_checks_yet():
    assert uptime_percent(0, 0) == 0.0
