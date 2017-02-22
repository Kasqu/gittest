#!/usr/bin/env python
# -*- coding: utf-8 -*-
#wersja funkcyjna

def utworzKonto():
    return {'bilans': 0 } #słownik, zmienna lokalna

def wplata(konto, ile):
    konto['bilans'] += ile
    return konto['bilans']

def wyplata(konto, ile):
    konto['bilans'] -= ile
    return konto['bilans']

osoba1 = utworzKonto()
osoba2 = utworzKonto()

ile = int(raw_input("Wpłata: "))
print "stan konta:", wplata(osoba1, ile)

ile = int(raw_input("Wpłata: "))
print "stan konta:", wplata(osoba2, ile)

ile = int(raw_input("Wypłata: "))
print "stan konta:", wyplata(osoba1, ile)

ile = int(raw_input("Wypłata: "))
print "stan konta:", wyplata(osoba2, ile)




