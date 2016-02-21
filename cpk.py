from browser import document

cp437table = '\x00\u263a\u263b\u2665\u2666\u2663\u2660\u2022\u25d8\u25cb\u25d9\u2642\u2640\u266a\u266b\u263c\u25ba\u25c4\u2195\u203c\xb6\xa7\u25ac\u21a8\u2191\u2193\u2192\u2190\u221f\u2194\u25b2\u25bc !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\u2302\xc7\xfc\xe9\xe2\xe4\xe0\xe5\xe7\xea\xeb\xe8\xef\xee\xec\xc4\xc5\xc9\xe6\xc6\xf4\xf6\xf2\xfb\xf9\xff\xd6\xdc\xa2\xa3\xa5\u20a7\u0192\xe1\xed\xf3\xfa\xf1\xd1\xaa\xba\xbf\u2310\xac\xbd\xbc\xa1\xab\xbb\u2591\u2592\u2593\u2502\u2524\u2561\u2562\u2556\u2555\u2563\u2551\u2557\u255d\u255c\u255b\u2510\u2514\u2534\u252c\u251c\u2500\u253c\u255e\u255f\u255a\u2554\u2569\u2566\u2560\u2550\u256c\u2567\u2568\u2564\u2565\u2559\u2558\u2552\u2553\u256b\u256a\u2518\u250c\u2588\u2584\u258c\u2590\u2580\u03b1\xdf\u0393\u03c0\u03a3\u03c3\xb5\u03c4\u03a6\u0398\u03a9\u03b4\u221e\u03c6\u03b5\u2229\u2261\xb1\u2265\u2264\u2320\u2321\xf7\u2248\xb0\u2219\xb7\u221a\u207f\xb2\u25a0\xa0'
asciitable = ''.join(map(chr, range(128)))
jellytable = '\xa1\xa2\xa3\xa4\xa5\xa6\xa9\xac\xae\xb5\xbd\xbf\u20ac\xc6\xc7\xd0\xd1\xd7\xd8\u0152\xde\xdf\xe6\xe7\xf0\u0131\u0237\xf1\xf7\xf8\u0153\xfe !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\xb6\xb0\xb9\xb2\xb3\u2074\u2075\u2076\u2077\u2078\u2079\u207a\u207b\u207c\u207d\u207e\u0181\u0187\u018a\u0191\u0193\u0198\u2c6e\u019d\u01a4\u01ac\u01b2\u0224\u0253\u0188\u0257\u0192\u0260\u0266\u0199\u0271\u0272\u01a5\u02a0\u027c\u0282\u01ad\u028b\u0225\u1ea0\u1e04\u1e0c\u1eb8\u1e24\u1eca\u1e32\u1e36\u1e42\u1e46\u1ecc\u1e5a\u1e62\u1e6c\u1ee4\u1e7e\u1e88\u1ef4\u1e92\u0226\u1e02\u010a\u1e0a\u0116\u1e1e\u0120\u1e22\u0130\u013f\u1e40\u1e44\u022e\u1e56\u1e58\u1e60\u1e6a\u1e86\u1e8a\u1e8e\u017b\u1ea1\u1e05\u1e0d\u1eb9\u1e25\u1ecb\u1e33\u1e37\u1e43\u1e47\u1ecd\u1e5b\u1e63\u1e6d\u1ee5\u1e7f\u1e89\u1ef5\u1e93\u0227\u1e03\u010b\u1e0b\u0117\u1e1f\u0121\u1e23\u0140\u1e41\u1e45\u022f\u1e57\u1e59\u1e61\u1e6b\u1e87\u1e8b\u1e8f\u017c\xab\xbb\u2018\u2019\u201c\u201d'

codepages = {
    "cp437":cp437table,
    "ascii":asciitable,
    "jelly":jellytable
}

supported_pages = [
'ascii', 'cp037', 'cp1006', 'cp1026', 'cp1140', 'cp1250',
'cp1251', 'cp1252', 'cp1253', 'cp1254', 'cp1255', 'cp1256', 'cp1257', 'cp1258',
'cp424', 'cp437', 'cp500', 'cp720', 'cp737', 'cp775', 'cp850', 'cp852',
'cp855', 'cp856', 'cp857', 'cp858', 'cp860', 'cp861', 'cp862', 'cp863',
'cp864', 'cp865', 'cp866', 'cp869', 'cp874', 'cp875', 'iso8859_1',
'iso8859_10', 'iso8859_13', 'iso8859_14', 'iso8859_15', 'iso8859_16',
'iso8859_2', 'iso8859_3', 'iso8859_4', 'iso8859_5', 'iso8859_6', 'iso8859_7',
'iso8859_8', 'iso8859_9', 'jelly', 'koi8_r', 'koi8_u', 'mac_cyrillic',
'mac_greek', 'mac_iceland', 'mac_latin2', 'mac_roman', 'mac_turkish', 'ptcp154'
]

for enc in supported_pages:
    document["codepage"].html += '<option value="{}"{}>{}</option>'.format(
        enc,
        'selected' if enc == 'ascii' else '',
        enc.upper().replace('_', '-')
    )

codepage = codepages["ascii"]

def changePage(ev):
    global codepage
    global codepages
    codepage = codepages[ev.target.value] if ev.target.value in codepages else bytes(range(256)).decode(ev.target.value)
    loadButtons()

def addtext(ev):
    document["out"].html += ev.target.html

def clear(ev):
    document["out"].html = ''

def loadButtons():
    global codepage
    document["buttons"].html = '<tr><th style="padding:3px"></th>\n{}\n</tr>'.format('\n'.join(map('<th style="padding:3px">_{0:1x}</th>'.format, range(16))))

    for i in range(16):
        r = ''
        for j in range(16):
            if i*16+j >= len(codepage):
                break
            ch = codepage[i*16+j]
            ch = "NUL" if ch == "\x00" else "SP" if ch == " " else ch
            r += '<td><button type="button" class="btn btn-xs btn-default" style="font-family:monospace" style="padding:3px">{}</button></td>\n'.format(ch)
        document["buttons"].html += '<tr>\n<th style="padding:3px">{0:1x}_</th>\n{1}</tr>'.format(i, r)

    for btn in document.get(selector='button'):
        btn.bind('click', addtext)

    document["clear"].unbind('click')
    document["clear"].bind('click', clear)

loadButtons()
document["codepage"].bind('change', changePage)
