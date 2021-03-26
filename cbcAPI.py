# -*- coding: utf-8 -*-

# Generic/Built-in
import requests
import json
import os


# Other Libs



# Owned
from cbcAPIAuth import CbcAPIAuth

__author__ = 'Jonathan Giffard'
__copyright__ = 'Copyright 2021, Couchbase'
__credits__ = ['Jonathan Giffard']
__license__ = 'GPL 3.0'
__version__ = '0.1.0'
__maintainer__ = 'Jonathan Giffard'
__email__ = 'jonathan.giffard@couchbase.com'
__status__ = 'Dev'

# Get the environmental variables that hold
# the values we will need


def _cbc_api_get_environ():
    # Return value, set to None

    api_access_info = None

    # Read the values from the environmental variables
    api_access_info_values  = {'access_key': os.environ.get('cbc_access_key'),
                       'secret_key': os.environ.get('cbc_secret_key'),
                       'api_base_url': os.environ.get('cbc_base_url')
                       }

    # Check we got all of the values
    # It's a None if the environment variable was not set
    if api_access_info_values['access_key'] is not None:
        if api_access_info_values['secret_key'] is not None:
            if api_access_info_values['api_base_url'] is not None:
                api_access_info = api_access_info_values
            else:
                api_access_info = None
                print('Environmental variable api_base_url is missing or empty')
        else:
            print('Environmental variable secret_key is missing or empty')
    else:
        print('Environmental variable access_key is missing or empty')

    return api_access_info


def cbc_api_get(api_endpoint):

    api_access_values = _cbc_api_get_environ()

    cbc_api_checked_response = None

    if api_access_values is not None:
        cbc_api_get_response = requests.get(api_access_values['api_base_url'] + api_endpoint, auth=CbcAPIAuth(api_access_values['access_key'], api_access_values['secret_key']))

        cbc_api_checked_response = _check_response(cbc_api_get_response)

    return cbc_api_checked_response


def cbc_api_put(api_endpoint, request_body):

    cbc_api_checked_response = None

    api_access_values = _cbc_api_get_environ()

    if api_access_values is not None:
        cbc_api_put_response = requests.post(api_access_values['api_base_url'] + api_endpoint, json=request_body, auth=CbcAPIAuth(api_access_values['access_key'], api_access_values['secret_key']))

        cbc_api_checked_response = _check_response(cbc_api_put_response)

    return cbc_api_checked_response


def cbc_api_del(api_endpoint):

    cbc_api_checked_response = None

    api_access_values = _cbc_api_get_environ()

    if api_access_values is not None:
        cbc_api_del_response = requests.delete(api_access_values['api_base_url'] + api_endpoint, auth=CbcAPIAuth(api_access_values['access_key'], api_access_values['secret_key']))

        cbc_api_checked_response = _check_response(cbc_api_del_response)


    return cbc_api_checked_response


def _check_response(response):
    if response.status_code >= 500:
        print('[!] [{0}] Server Error'.format(response.status_code))
        return None
    elif response.status_code == 404:
        print('[!] [{0}] URL not found: [{1}]'.format(response.status_code, api_base_url))
        return None
    elif response.status_code == 401:
        print('[!] [{0}] Authentication Failed'.format(response.status_code))
        return None
    elif response.status_code >= 400:
        print('[!] [{0}] Bad Request'.format(response.status_code))
        print(response.content)
        return None
    elif response.status_code >= 300:
        print('[!] [{0}] Unexpected redirect.'.format(response.status_code))
        return None
    elif response.status_code == 200:
        return json.loads(response.content)
    elif response.status_code == 204:
        return response.content
    else:
        print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(response.status_code, response.content))
        return None


