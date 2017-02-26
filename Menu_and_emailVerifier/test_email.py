#https://www.youtube.com/watch?v=l32bsaIDoWk

import emailVerifier

def test_email():
    isReal = emailVerifier.verifyEmail("blah.com")
    assert isReal == False