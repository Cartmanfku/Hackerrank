
import re

table_hex = [
    -1,-1,-1,-1, -1,-1,-1,-1, -1,-1,-1,-1, -1,-1,-1,-1,
    -1,-1,-1,-1, -1,-1,-1,-1, -1,-1,-1,-1, -1,-1,-1,-1,
    -1,-1,-1,-1, -1,-1,-1,-1, -1,-1,-1,-1, -1,-1,-1,-1,
    0, 1, 2, 3,  4, 5, 6, 7,  8, 9,-1,-1, -1,-1,-1,-1,
    -1,10,11,12, 13,14,15,-1, -1,-1,-1,-1, -1,-1,-1,-1,
    -1,-1,-1,-1, -1,-1,-1,-1, -1,-1,-1,-1, -1,-1,-1,-1,
    -1,10,11,12, 13,14,15,-1, -1,-1,-1,-1, -1,-1,-1,-1,
    -1,-1,-1,-1, -1,-1,-1,-1, -1,-1,-1,-1, -1,-1,-1,-1
]


def a2b_hex(t):
    result = []

    def pairs_gen(s):
        while s:
            try:
                yield table_hex[ord(s[0])], table_hex[ord(s[1])]
            except IndexError:
                if len(s):
                    raise TypeError('Odd-length string')
                return
            s = s[2:]

    for a, b in pairs_gen(t):
        if a < 0 or b < 0:
            raise TypeError('Non-hexadecimal digit found')
        result.append(chr((a << 4) + b))
    return ''.join(result)
    

unhexlify = a2b_hex

# Base32 encoding/decoding must be done in Python
_b32alphabet = {
    0: 'A',  9: 'J', 18: 'S', 27: '3',
    1: 'B', 10: 'K', 19: 'T', 28: '4',
    2: 'C', 11: 'L', 20: 'U', 29: '5',
    3: 'D', 12: 'M', 21: 'V', 30: '6',
    4: 'E', 13: 'N', 22: 'W', 31: '7',
    5: 'F', 14: 'O', 23: 'X',
    6: 'G', 15: 'P', 24: 'Y',
    7: 'H', 16: 'Q', 25: 'Z',
    8: 'I', 17: 'R', 26: '2',
    }

_b32rev = dict([(v, long(k)) for k, v in _b32alphabet.items()])

def b32decode(s):
    padchars = 0
    mo = re.search('(?P<pad>[=]*)$', s)
    if mo:
        padchars = len(mo.group('pad'))
        if padchars > 0:
            s = s[:-padchars]
    # Now decode the full quanta
    parts = []
    acc = 0
    shift = 35
    for c in s:
        val = _b32rev.get(c)
        if val is None:
            raise TypeError('Non-base32 digit found')
        acc += _b32rev[c] << shift
        shift -= 5
        if shift < 0:
            parts.append(unhexlify('%010x' % acc))
            acc = 0
            shift = 35
    # Process the last, partial quanta
    last = unhexlify('%010x' % acc)
    if padchars == 0:
        last = ''                       # No characters
    elif padchars == 1:
        last = last[:-1]
    elif padchars == 3:
        last = last[:-2]
    elif padchars == 4:
        last = last[:-3]
    elif padchars == 6:
        last = last[:-4]
    else:
        raise TypeError('Incorrect padding')
    parts.append(last)
    return ''.join(parts)

table_b2a_base64 = \
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def b2a_base64(s):
    length = len(s)
    final_length = length % 3

    def triples_gen(s):
        while s:
            try:
                yield ord(s[0]), ord(s[1]), ord(s[2])
            except IndexError:
                s += '\0\0'
                yield ord(s[0]), ord(s[1]), ord(s[2])
                return
            s = s[3:]

    
    a = triples_gen(s[ :length - final_length])

    result = [''.join(
        [table_b2a_base64[( A >> 2                    ) & 0x3F],
         table_b2a_base64[((A << 4) | ((B >> 4) & 0xF)) & 0x3F],
         table_b2a_base64[((B << 2) | ((C >> 6) & 0x3)) & 0x3F],
         table_b2a_base64[( C                         ) & 0x3F]])
              for A, B, C in a]

    final = s[length - final_length:]
    if final_length == 0:
        snippet = ''
    elif final_length == 1:
        a = ord(final[0])
        snippet = table_b2a_base64[(a >> 2 ) & 0x3F] + \
                  table_b2a_base64[(a << 4 ) & 0x3F] + '=='
    else:
        a = ord(final[0])
        b = ord(final[1])
        snippet = table_b2a_base64[(a >> 2) & 0x3F] + \
                  table_b2a_base64[((a << 4) | (b >> 4) & 0xF) & 0x3F] + \
                  table_b2a_base64[(b << 2) & 0x3F] + '='
    return ''.join(result) + snippet + '\n'

def b64encode(s):
    encoded = b2a_base64(s)[:-1]
    return encoded
    

t = int(raw_input())
for i in range(0,t):
    s = raw_input()
    d = b32decode(s)
    print b64encode(d)