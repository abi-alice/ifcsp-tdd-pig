from main import pig_latin

def test_pig_latin_happy():
    assert pig_latin("Hello World") == "ellohay orldway"
    assert pig_latin("phone") == "onephay"
    assert pig_latin("apple") == "appleyay"

def test_pig_latin_unhappy():
    assert pig_latin("abigail") != "bigailayay"
    assert pig_latin("programming") != "rogrammingpay"
    assert pig_latin("nice day") != "icenayayday"