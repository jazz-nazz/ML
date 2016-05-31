#!/usr/bin/python2.7
# -*- coding: utf-8 -*

import os

DATADIR = ""
DATAFILE = "beatles-discography.csv"


def parse_file(datafile):
    data = []
    with open(datafile, "r") as f:
        for nLine, line in enumerate(f):
            print line
            if not nLine:
                dictKeys = [elem.strip() for elem in line.split(',')]
            else:
                data.append(dict(zip(dictKeys, [elem.strip() for elem in line.split(',')])))
            if nLine == 10:
                break

    return data


def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    assert d[0] == firstline
    assert d[9] == tenthline


test()