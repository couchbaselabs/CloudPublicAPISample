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

access_key=os.environ['cbc_access_key']
secret_key=os.environ['cbc_secret_key']
api_url=os.environ['cbc_api_url']



def cbc_api_get(api_endpoint):
    cbc_api_get_response = requests.get(api_url + api_endpoint, auth=CbcAPIAuth(access_key, secret_key))
    return _check_response(cbc_api_get_response)


def cbc_api_put(api_endpoint, request_body):
    cbc_api_put_response = requests.post(api_url + api_endpoint, json=request_body, auth=CbcAPIAuth(access_key, secret_key))
    return _check_response(cbc_api_put_response)


def cbc_api_del(api_endpoint):
    cbc_api_del_response = requests.delete(api_url + api_endpoint, auth=CbcAPIAuth(access_key, secret_key))
    return _check_response(cbc_api_del_response)


def _check_response(response):
    if response.status_code >= 500:
        print('[!] [{0}] Server Error'.format(response.status_code))
        return None
    elif response.status_code == 404:
        print('[!] [{0}] URL not found: [{1}]'.format(response.status_code, api_url))
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