# -*- coding: utf-8 -*-
from kss._modules.hangulization.hangulize import *


class Latvian(Language):
    """For transcribing Latvian."""

    __iso639__ = {1: 'lv', 2: 'lav', 3: 'lav'}
    __tmp__ = ',;'

    vowels = u'aeiou'
    cs = 'bcCdDfgGhHkKlmnNprsStvzZ'
    vo = 'bdDgGhlmnNrvzZ'
    vl = 'cCfHkKpsSt'
    notation = Notation([
        (u'č', 'C'),
        (u'ģ', 'G'),
        (u'ķ', 'K'),
        (u'ļ{@}', 'lj'),
        (u'ļ', 'l'),
        ('{@}n{g|k}', 'N'),
        ('Ng{@|j|l|r}', 'N,g'),
        ('Ng', 'N,'),
        (u'ņ{@}', 'nj'),
        (u'ņ', 'n'),
        (u'š', 'S'),
        ('ch', 'H'),
        ('ts', 'c'),
        ('tS', 'C'),
        ('d{G|K}', None),
        ('t{G|K}', None),
        ('G', 'D'),
        ('K', 'C'),
        ('dz', 'X'),
        ('tz', 'X'),
        (u'dž', 'D'),
        (u'tž', 'D'),
        (u'ž', 'Z'),
        ('{c|C|D|s|S|X|z|Z}s$', None),
        ('y', 'i'),
        ('{s|S}je', 'Je'),
        ('{<cs>}je', 'e'),
        ('j{@}', 'J'),
        ('ij', 'i'),
        ('j', 'i'),
        ('{c|C|D|S|X|z|Z}J', None),
        ('qu', 'kv'),
        ('q', 'k'),
        ('w', 'v'),
        ('{@}v{<cs>}', 'u'),
        ('{@}v$', 'u'),
        ('x', 'ks'),
        ('bb', 'b'),
        ('dd', 'd'),
        ('ff', 'f'),
        ('gg', 'g'),
        ('hh', 'h'),
        ('kk', 'k'),
        ('ll', 'l'),
        ('mm', 'm,m'),
        ('nn', 'n,n'),
        ('pp', 'p'),
        ('rr', 'r'),
        ('ss', 's'),
        ('SS', 'S'),
        ('tt', 't'),
        ('vv', 'v'),
        ('zz', 'z'),
        ('ZZ', 'Z'),
        ('ds{<vo>}', 'X'),
        ('ds', 'c'),
        ('dS{<vo>}', 'Z'),
        ('dS', 'C'),
        ('bz{<vl>}', 'ps'),
        ('gz{<vl>}', 'ks'),
        ('bZ{<vl>}', 'pS'),
        ('gZ{<vl>}', 'kS'),
        ('b{<vl>}', 'p'),
        ('d{<vl>}', 't'),
        ('D{<vl>}', 'C'),
        ('g{<vl>}', 'k'),
        ('G{<vl>}', 'K'),
        ('X{<vl>}', 'c'),
        ('z{<vl>}', 's'),
        ('Z{<vl>}', 'S'),
        ('{@}k{<vl>}', 'k,'),
        ('{@}p{<vl>}', 'p,'),
        ('ts', 'c'),
        ('tS', 'C'),
        ('C{<cs>}', 'ci'),
        ('C$', 'ci'),
        ('D{<cs>}', 'zi'),
        ('D$', 'zi'),
        ('Z{<cs>}', 'zu'),
        ('Z$', 'zu'),
        ('S{<cs>}', 'sJu'),
        ('S$', 'sJu'),
        ('C', 'c'),
        ('D', 'z'),
        ('H', 'h'),
        ('S', 'sJ'),
        ('X', 'z'),
        ('Z', 'z'),
        ('^l', 'l;'),
        ('^m', 'm;'),
        ('^n', 'n;'),
        ('l$', 'l,'),
        ('m$', 'm,'),
        ('n$', 'n,'),
        ('l{@|J|m,|n,}', 'l;'),
        ('{,}l', 'l;'),
        ('m{@|J}', 'm;'),
        ('n{@|J}', 'n;'),
        ('l', 'l,'),
        ('m', 'm,'),
        ('n', 'n,'),
        (',,', ','),
        (',;', None),
        (',l,', 'l,'),
        (',m,', 'm,'),
        (',n,', 'n,'),
        ('l{m;|n;}', 'l,'),
        (';', None),
        ('b', Choseong(B)),
        ('c', Choseong(C)),
        ('d', Choseong(D)),
        ('f', Choseong(P)),
        ('g', Choseong(G)),
        ('h', Choseong(H)),
        ('k,', Jongseong(G)),
        ('k', Choseong(K)),
        ('^l', Choseong(L)),
        ('{,}l', Choseong(L)),
        ('l,', Jongseong(L)),
        ('l', Jongseong(L), Choseong(L)),
        ('m,', Jongseong(M)),
        ('m', Choseong(M)),
        ('n,', Jongseong(N)),
        ('n', Choseong(N)),
        ('N', Jongseong(NG)),
        ('p,', Jongseong(B)),
        ('p', Choseong(P)),
        ('r', Choseong(L)),
        ('s', Choseong(S)),
        ('t', Choseong(T)),
        ('v', Choseong(B)),
        ('z', Choseong(J)),
        ('Ja', Jungseong(YA)),
        ('Je', Jungseong(YE)),
        ('Ji', Jungseong(I)),
        ('Jo', Jungseong(YO)),
        ('Ju', Jungseong(YU)),
        ('a', Jungseong(A)),
        ('e', Jungseong(E)),
        ('i', Jungseong(I)),
        ('o', Jungseong(O)),
        ('u', Jungseong(U)),
    ])

    def normalize(self, string):
        return normalize_roman(string, {
            u'Č': u'č', u'Ģ': u'ģ', u'Ķ': u'ķ', u'Ļ': u'ļ', u'Ņ': u'ņ',
            u'Š': u'š', u'Ž': u'ž'
        })


__lang__ = Latvian
