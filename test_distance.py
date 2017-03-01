import distance

def test_parameters():
    dist=distance.distance(5,5,5,5)


def test_valid_input():
    w=4
    dist=distance.distance(5,w,4,4)


def test_return_type():
    dist=distance.distance(5,5,5,5)
    assert dist.is_integer()
