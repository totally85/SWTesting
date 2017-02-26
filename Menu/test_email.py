#https://www.youtube.com/watch?v=l32bsaIDoWk

import emailVerifier

def test_email():
    isReal = emailVerifier.verifyEmail("jam1250@msstate.edu")
    assert isReal == True