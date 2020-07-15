from sci_calc import SciCalc

my_sci_calc = SciCalc()


def test_find_sqrt():
    assert my_sci_calc.find_sqrt(100) == 10.0

