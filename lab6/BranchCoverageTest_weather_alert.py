
import pytest
from weather_alert import wind_alert, rain_alert, heat_alert, overall_alert


def test_wind_branches():
    assert wind_alert(89) == "warning"
    assert wind_alert(62) == "watch"
    assert wind_alert(39) == "advisory"
    assert wind_alert(38) == "none"


def test_rain_branches():
    assert rain_alert(50, True) == "warning"
    assert rain_alert(50, False) == "watch"
    assert rain_alert(10, True) == "watch"
    assert rain_alert(10, False) == "advisory"
    assert rain_alert(9, False) == "none"


def test_heat_branches():
    assert heat_alert(45, 40) == "warning"
    assert heat_alert(40, 40) == "watch"
    assert heat_alert(35, 40) == "advisory"
    assert heat_alert(34, 40) == "none"

    assert heat_alert(44, 50) == "warning"
    assert heat_alert(39, 50) == "watch"
    assert heat_alert(34, 50) == "advisory"
    assert heat_alert(33, 50) == "none"


def test_overall_alert_branches():
    assert overall_alert([]) == "none"
    assert overall_alert(["advisory"]) == "advisory"
    assert overall_alert(["watch", "advisory"]) == "watch"
    assert overall_alert(["warning", "watch"]) == "warning"
    assert overall_alert(["none", "none"]) == "none"


def test_unknown_alert_branch():
    with pytest.raises(ValueError, match="unknown alert"):
        overall_alert(["storm"])
