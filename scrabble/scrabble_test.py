# Generate 7 letters
# choose word
# is word valid
# + score


from scrabble import Scrabble

my_scrabble = Scrabble()

def test_letter_score():
    assert my_scrabble.letter_score("E") == 1
    assert my_scrabble.letter_score("D") == 2
    assert my_scrabble.letter_score("C") == 3
    assert my_scrabble.letter_score("H") == 4
    assert my_scrabble.letter_score("K") == 5
    assert my_scrabble.letter_score("J") == 8
    assert my_scrabble.letter_score("Q") == 10


def test_generate_letters():
    assert my_scrabble.generate_letters() == 7



def test_word():
    assert my_scrabble.word() == True


def test_score_calculator():
    assert my_scrabble.score_calculator("CACTUS") == 10
    assert my_scrabble.score_calculator("ROOM") == 6
    assert my_scrabble.score_calculator("ZEBRA") == 16
    assert my_scrabble.score_calculator("FARM") == 9
    assert my_scrabble.score_calculator("JOG") == 11


#def test_replace():
