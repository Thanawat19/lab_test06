import sys
sys.path.insert(0, '../LAB_TEST06')
from core import config

def test_appname():
    expected_result = "Awesome API"
    actual_result = config.settings.app_name
    assert expected_result == actual_result

def test_host():
    expected_result = "cluster0.fvspk.mongodb.net"
    actual_result = config.settings.host
    assert expected_result == actual_result

def test_username():
    expected_result = "Thanawat19"
    actual_result = config.settings.user_name
    assert expected_result == actual_result

def test_password():
    expected_result = "1234"
    actual_result = config.settings.pass_word
    assert expected_result == actual_result