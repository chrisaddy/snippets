from is_a_number import tokenize, check


def test_tokenizer():
    number = "one hundred fifty-five"

    assert tokenize(number) == ["one", "hundred", "fifty", "five"]

    # this is grammatically incorrect, but common enough to test for
    number = "one hundred and fifty-five"

    assert tokenize(number) == ["one", "hundred", "fifty", "five"]

    number = "eight million seven"

    

def test_one_five_hundred():
    assert not check("one five hundred")
    
