#!/usr/bin/python

# Copyright 2013 Xu Shen

"""
An easy-to-use Python wrapper for the Geoclient API

"""

import urllib
import urllib2

try:
    import simplejson as json
except ImportError:
    import json

VERSION = '1.0.0'
__all__ = ['GeoClient', 'GeoClientError']


def fetch_json(query_url, params={}, headers={}):
    """Retrieve a JSON object from a (parameterized) URL.

    :param query_url: The base URL to query
    :type query_url: string
    :param params: Dictionary mapping (string) query parameters to values
    :type params: dict
    :param headers: Dictionary giving (string) HTTP headers and values
    :type headers: dict
    :return: A `(url, json_obj)` tuple, where `url` is the final,
    parameterized, encoded URL fetched, and `json_obj` is the data
    fetched from that URL as a JSON-format object.
    :rtype: (string, dict or array)

    """
    encoded_params = urllib.urlencode(params)
    url = query_url + encoded_params
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    return url, json.load(response)


class GeoClientError(Exception):
    """Base class for errors in the :mod:`geoclient` module.

    Methods of the :class:`GeoClient` raise this when something goes wrong.

    """
    #: See https://api.cityofnewyork.us/geoclient/v1/doc
    #: Section 2.1 for information on the meaning of these status code
    G_GEO_SUCCESS = 200
    G_GEO_MISSING_QUERY = 400
    G_GEO_UNAVAILABLE_URL = 404
    G_GEO_UNKNOWN_ADDRESS = 500

    _STATUS_MESSAGES = {
        G_GEO_SUCCESS: 'G_GEO_SUCCESS',
        G_GEO_MISSING_QUERY: 'G_GEO_MISSING_QUERY',
        G_GEO_UNAVAILABLE_URL: 'G_GEO_UNAVAILABLE_URL',
        G_GEO_UNKNOWN_ADDRESS: 'G_GEO_UNKNOWN_ADDRESS',
    }

    def __init__(self, status, url=None, response=None):
        """Create an exception with a status and optional full response.

        :param status: Either a ``G_GEO_`` code or a string explaining the
         exception.
        :type status: int or string
        :param url: The query URL that resulted in the error, if any.
        :type url: string
        :param response: The actual response returned from Geoclient, if any.
        :type response: dict

        """
        Exception.__init__(self, status)        # Exception is an old-school class
        self.status = status
        self.response = response
        self.url = url

    def __str__(self):
        """Return a string representation of this :exc:`GeoClientError`."""
        if self.status in self._STATUS_MESSAGES:
            if self.response is not None and 'responseDetails' in self.response:
                return_value = 'Error %d: %s' % (self.status, self.response['responseDetails'])
            else:
                return_value = 'Error %d: %s' % (self.status, self._STATUS_MESSAGES[self.status])
        else:
            return_value = str(self.status)
        return return_value

    def __unicode__(self):
        """Return a unicode representation of this :exc:`GeoClientError`."""
        return unicode(self.__str__())

STATUS_OK = GeoClientError.G_GEO_SUCCESS


class GeoClient(object):
    """
    An easy-to-use Python wrapper for the GeoClient APIs.
    """

    _QUERY_URL = "https://api.cityofnewyork.us/geoclient/v1/"
    _ADDRESS_QUERY_URL = _QUERY_URL + 'address.json?'
    _BBL_QUERY_URL = _QUERY_URL + 'bbl.json?'
    _BIN_QUERY_URL = _QUERY_URL + 'bin.json?'

    def __init__(self, app_key='', app_id=''):
        """
        Create a new :class:`GeoClient` object using the given `app_key` and
        `app_id`.

        :param app_key: Geoclient API key
        :type app_key: string
        :param app_id: Geoclient API id
        :type app_id: string

        Geoclient requires API users to register for an API key and an API id
        before using the geocoding service.

        """
        self.app_key = app_key
        self.app_id = app_id

    def address(self, house_number='', street='', borough=''):       # pylint: disable-msg=C0103,R0913
        """
        Given a string address `query`, return a dictionary of information about
        that location, including its latitude and longitude.

        :param house_number: House number of the address
        :type house_number: string
        :param street: Street name or 7-digit street code
        :type street: string
        :param borough: borough of new york, must be one of Manhattan, Bronx,
         Brooklyn, Queens and Staten Island
        :type borough: string
        :returns: `geocoder return value`_ dictionary
        :rtype: dict
        :raises GeoClientError: if there is something wrong with the query.

        More information on the types and meaning of the parameters can be found
        at the `GeoClient`__ site.

        __ https://api.cityofnewyork.us/geoclient/v1/doc

        """
        if house_number is None or street is None or borough is None:
            raise GeoClientError('All parameters must be provided.')
        params = {
            'houseNumber': house_number,
            'street': street,
            'borough': borough,
            'app_key': self.app_key,
            'app_id': self.app_id,
        }
        url, response = fetch_json(self._ADDRESS_QUERY_URL, params=params)
        return response

    def bbl(self, borough='', block='', lot=''):
        """
        Given a string address `query`, return a dictionary of information about
        that location, including its latitude and longitude.

        :param borough: Borough of new york, must be one of Manhattan, Bronx,
         Brooklyn, Queens and Staten Island
        :type borough: string
        :param block: Tax block
        :type block: string
        :param lot: Tax lot
        :type lot: string
        :returns: `geocoder return value`_ dictionary
        :rtype: dict
        :raises GeoClientError: if there is something wrong with the query.

        More information on the types and meaning of the parameters can be found
        at the `GeoClient`__ site.

        __ https://api.cityofnewyork.us/geoclient/v1/doc

        """
        if borough is None or block is None or lot is None:
            raise GeoClientError('All parameters must be provided.')
        params = {
            'borough': borough,
            'block': block,
            'lot': lot,
            'app_key': self.app_key,
            'app_id': self.app_id,
        }
        url, response = fetch_json(self._BBL_QUERY_URL, params=params)
        return response

    def bin(self, bin=''):
        """
        Given a building identification number, return a dictionary of
        information.

        :param bin: Building identification number.
        :type bin: string
        :returns: `geocoder return value`_ dictionary
        :rtype: dict
        :raises GeoClientError: if there is something wrong with the query.

        More information on the types and meaning of the parameters can be found
        at the `GeoClient`__ site.

        __ https://api.cityofnewyork.us/geoclient/v1/doc

        """
        if bin is None:
            raise GeoClientError('Building Identification Number must be provided.')
        params = {
            'bin': bin,
            'app_key': self.app_key,
            'app_id': self.app_id,
        }
        url, response = fetch_json(self._BIN_QUERY_URL, params=params)
        return response

if __name__ == "__main__":
    import sys

    def main(argv):
        """
        Geocodes a location given on the command line.
        """

        if len(argv) < 2 or len(argv) > 4:
            print main.__doc__
            sys.exit(1)

        query = argv[1]
        if len(argv) == 4:
            app_key = argv[2]
            app_id = argv[3]
        else:
            app_key = raw_input("GeoClient APP key: ")
            app_id = raw_input("GeoClient APP ID: ")

        gclient = GeoClient(app_key, app_id)
        try:
            result = gclient.geocode(query)
        except GeoClientError, err:
            sys.stderr.write('%s\n%s\nResponse:\n' % (err.url, err))
            json.dump(err.response, sys.stderr, indent=4)
            sys.exit(1)
        json.dump(result, sys.stdout, indent=4)
        sys.stdout.write('\n')

    main(sys.argv)
