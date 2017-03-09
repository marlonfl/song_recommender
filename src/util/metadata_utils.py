def equals(song1, song2):
    s1 = song1.lower()
    s2 = song2.lower()

    if s1 == s2:
        return True
    elif s1.split("-")[0] == s2.split("-")[0]:
        title1 = s1.split("-")[1].split("(")[0]
        title2 = s2.split("-")[1].split("(")[0]
        return title1 == title2
    else:
        return False


if __name__ == "__main__":
    assert(equals("test", "test"))
    assert(equals("Test - Test(Original Mix)", "tesT - TEst("))
    assert(not equals("abc - e", "abc - f"))
    assert(not equals("asd - asd", "wewe - ags"))
