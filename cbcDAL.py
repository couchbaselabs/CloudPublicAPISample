# -*- coding: utf-8 -*-

# Generic/Built-in


from requests.auth import AuthBase

# Other Libs
import maya



# Owned
from cbcAPI import cbc_api_get, cbc_api_put, cbc_api_del


__author__ = 'Jonathan Giffard'
__copyright__ = 'Copyright 2021, Couchbase'
__credits__ = ['Jonathan Giffard']
__license__ = 'GPL 3.0'
__version__ = '0.1.0'
__maintainer__ = 'Jonathan Giffard'
__email__ = 'jonathan.giffard@couchbase.com'
__status__ = 'Dev'


def list_clouds():

    list_of_clouds = cbc_api_get('/v2/clouds')

    # Did we get a list?
    if list_of_clouds != None:

        cloud_list = []

        for cloud in list_of_clouds['data']:
            # Builds up a row to display in a table
            # Table is generated by _pretty_table
            # Use maya to convert createAt to a more friendly date / time
            cloud_list.append([cloud['name'],cloud['provider'] + ' ' + cloud['providerSettings']['awsRegion'], maya.parse(cloud['createdAt']), cloud['id']])

        # Send the table header & rows to _pretty_table
        # and print the output from it

    return cloud_list


def get_api_status():

    api_status = cbc_api_get('/v2/status')

    return(api_status["status"])





