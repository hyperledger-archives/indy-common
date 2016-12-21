from sovrin_common.util import randomString


def testRandomString():
    r1 = randomString()
    assert r1 is not None
    r2 = randomString()
    assert r2 is not None
    assert r1 != r2