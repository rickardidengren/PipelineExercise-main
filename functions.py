def IsPalindrom(input):
    s = input.replace(" ", "").lower()
    backwards = ""
    for part in s:
        backwards = part + backwards


    return backwards == s


# ålder      18      20
# location Krogen Systemet
# promilleHalt < 1.0
def canIBuyBeer(age,location,promilleHalt):
    if promilleHalt > 1.0:
        return False
    if location == "S" and age < 19:
        return False
    if location == "K" and age < 18:
        return False
    return True


def IsValidEmail(input):
    if not  '@' in input:
        return False
    lastPoint = input.rfind('.')
    if lastPoint == -1:
        return False
    antalEfter = len(input) - lastPoint -1
    if antalEfter == 2 or antalEfter == 3:
        return True
    return False
