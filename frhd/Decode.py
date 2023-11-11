
import re #need it

#These regexes match power ups, and power ups with rotation.
PUP_RE  = re.compile('(?P<type>(C|T|S|O)) (?P<x>-?\S*) (?P<y>-?[^ ,#])')
PUPR_RE = re.compile('(?P<type>(G|B)) (?P<x>-?\S*) (?P<y>-?\S*) (?P<rot>-?[^ ,#])')

def decline(ls): #Decode line
    ls = ls.split(' ')
    if len(ls) % 2 != 0:
        assert False, 'Invalid line'
    # ls = filter(None, ls)
    # print(ls)
    for obj in range(0,len(ls)):
        ls[obj] = b32d(ls[obj])
    return ls

def declinestr(str): #Line string(physics or scenery)
    lines = str.split(',')
    out = []
    for line in lines:
        line = decline(line)
        out.append(line)
    return out

def decpup(pup): #Decode powerup
    return PUP_RE.match(pup).groupdict()

def decpupr(pupr): #Decode powerup with rotation
    return PUPR_RE.match(pupr).groupdict()

def b32d(n): #Base 32 decode
    return int(n, 32)

if __name__ == '__main__':
    import pyperclip
    string = input('Enter a char: ')
    print(declinestr(string))
    pyperclip.copy(str(declinestr(string)))
