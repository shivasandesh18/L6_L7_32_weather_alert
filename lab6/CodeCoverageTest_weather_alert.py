
import pytest
from weather_alert import wind_alert, rain_alert, heat_alert, overall_alert


def test_wind_alert_levels():
    assert wind_alert(10) == "none"
    assert wind_alert(39) == "advisory"
    assert wind_alert(62) == "watch"
    assert wind_alert(89) == "warning"


def test_rain_alert_levels():
    assert rain_alert(5, False) == "none"
    assert rain_alert(10, False) == "advisory"
    assert rain_alert(10, True) == "watch"
    assert rain_alert(50, False) == "watch"
    assert rain_alert(50, True) == "warning"


def test_heat_alert_levels():
    assert heat_alert(20, 40) == "none"
    assert heat_alert(35, 40) == "advisory"
    assert heat_alert(40, 40) == "watch"
    assert heat_alert(45, 40) == "warning"
    assert heat_alert(33, 50) == "none"
    assert heat_alert(35, 50) == "advisory"


def test_overall_alert_levels():
    assert overall_alert([]) == "none"
    assert overall_alert(["advisory"]) == "advisory"
    assert overall_alert(["watch", "advisory"]) == "watch"
    assert overall_alert(["warning", "watch"]) == "warning"
    assert overall_alert(["none", "none"]) == "none"


def test_unknown_alert():
    with pytest.raises(ValueError, match="unknown alert"):
        overall_alert(["storm"])
