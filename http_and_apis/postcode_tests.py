from postcode_class import Postcode

my_house = Postcode("CV1 2BP")

def test_get_address():
    assert my_house.get_address("DY9 0YH") == 200
    assert my_house.get_address("DY9 0YHJIJ") == {'status': 404, 'error': 'Invalid postcode'}


