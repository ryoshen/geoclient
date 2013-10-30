#!/usr/bin/python

# Copyright 2013 Xu Shen
#

"""
Unit tests for geoclient.

"""

import unittest
from geoclient import GeoClient

APP_KEY = "You should have an app_key."
APP_ID = "You should have an app_id, too."


class Test(unittest.TestCase):

    """Unit tests for geoclient"""

    def test_address(self):
        """Test geoclient address()"""

        house_number = "314"
        street = "WEST  100 STREET"
        borough = "manhattan"
        gclient = GeoClient(APP_KEY, APP_ID)
        result = gclient.address(house_number, street, borough)
        self.assertEquals(result['address']['bbl'], '1018887502')
        self.assertEquals(result['address']['buildingIdentificationNumber'],
                          '1057093')
        self.assertEquals(result['address']['firstStreetNameNormalized'], street)
        self.assertEquals(result['address']['houseNumber'], house_number)

    def test_bbl(self):
        """Test geoclient bbl()"""

        borough = "manhattan"
        lot = "1"
        block = "1889"
        gclient = GeoClient(APP_KEY, APP_ID)
        result = gclient.bbl(borough, lot, block)
        self.assertEquals(result['bbl']['bbl'], '1000011889')
        self.assertEquals(result['bbl']['bblTaxBlock'], '00001')

    def test_bin(self):
        """Test geoclient bin()"""

        building_identification_number = '1079043'
        gclient = GeoClient(APP_KEY, APP_ID)
        result = gclient.bin(bin=building_identification_number)
        self.assertEquals(result['bin']['bbl'], '1000670001')
        self.assertEquals(result['bin']['buildingIdentificationNumber'], '1079043')

if __name__ == '__main__':
    unittest.main()
