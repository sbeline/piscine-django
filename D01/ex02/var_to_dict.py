#!/usr/bin/env python3
# -*-coding:utf-8 -*

def var_to_dict():
    d = [
        ('Hendrix'      , '1942'),
        ('Allman'       , '1946'),
        ('King'         , '1925'),
        ('Clapton'      , '1945'),
        ('Johnson'      , '1911'),
        ('Berry'        , '1926'),
        ('Vaughan'      , '1954'),
        ('Cooder'       , '1947'),
        ('Page'         , '1944'),
        ('Richards'     , '1943'),
        ('Hammett'      , '1962'),
        ('Cobain'       , '1967'),
        ('Garcia'       , '1942'),
        ('Beck'         , '1944'),
        ('Santana'      , '1947'),
        ('Ramone'       , '1948'),
        ('White'        , '1975'),
        ('Frusciante'   , '1970'),
        ('Thompson'     , '1949'),
        ('Burton'       , '1939')
    ]
    mon_dictionnaire_invers = {}
    for v, keys in d:
        mon_dictionnaire_invers[v] = keys
        mon_dictionnaire = {}
    for keys, v in mon_dictionnaire_invers.items():
        test = mon_dictionnaire.setdefault(v, [])
        test.append(keys)

    for keys, v in mon_dictionnaire.items():
        print("{} : {}".format(keys, " ".join(v)))

if __name__ == '__main__':
	var_to_dict()
