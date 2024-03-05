import pyab3p


def test_del_wont_crash() -> None:
    ab3p = pyab3p.Ab3p()
    del ab3p
