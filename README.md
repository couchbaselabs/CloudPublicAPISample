# CloudPublicAPISample

_For Couchbase Server 5.0 see [this branch](https://github.com/couchbaselabs/try-cb-python/tree/5.0) for latest changes to authentication_

# Couchbase Python travel-sample Application REST Backend
This is a sample application for getting started with Couchbase Cloud Public API . 
The application lists the cloud connections

![Application](app.png)

## Prerequisites
The following pieces need to be in place in order to run the application.

* Admission into the Restricted Beta
* Access and Secret Keys for authentication to the API
* Python 3.0 or greater

## Running the application
To download the application you can either download [the archive](https://github.com/couchbaselabs/CloudPublicAPISameple) or clone the repository:

```
$ git clone https://github.com/couchbaselabs/CloudPublicAPISameple
```

The application uses several Python libraries that need to be installed, this are listed in _requirements.txt_ and can be automatically loaded using the _pip_ command:
```
$ pip install -r requirements.txt
```

Launch the application by running the _cloudAPISample.py_ file from a terminal.
 
```
$ python cloudAPISample.py
```
