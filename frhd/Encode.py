
def encline(points):   #encode line.
	return [[' '.join([b32e(point) for point in points]) + ',']]

def encpup(x,y,pupcode):
    #encode powerup without rotation
    return [['%s %s %s,' % (pupcode,b32e(x),b32e(y))]]

def encpupr(x,y,rot,pupcode):
    #encode powerup with rotation
    return [['%s %s %s %s,' % (pupcode,b32e(x),b32e(y),b32e(rot))]]

def encpupportal(x1, y1, x2, y2):
    #encode portal
    return [['W %s %s %s %s,' % (b32e(x1),b32e(y1),b32e(x2),b32e(y2))]]

def b32e(numbera):
    #encode number. I struggled to find the right alphabet that frhd used for their encoding
    """Encode number in freerider base32."""

    alphabet = '0123456789abcdefghijklmnopqrstuv' #DO NOT CHANGE
    number = abs(numbera)
    base32 = ''
    while number:
        number, i = divmod(number, 32)
        base32 = alphabet[i] + base32
    if numbera < 0:
        base32 = '-'+base32
    return base32 or alphabet[0]
