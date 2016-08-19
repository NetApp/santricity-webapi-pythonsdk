#NetApp SANtricity WebAPI - Python SDK


##Requirements

The NetApp SANtricity WebAPI - Python SDK client library requires Python 2.7 or later.

##Installation

###setuptools Installation

Installation of the Python bindings can be performed through [setuptools](http://pypi.python.org/pypi/setuptools).

Once downloaded, enter the following command:

```python
python setup.py install
```

###Manual Installation

If you chose not install the Python bindings through setuptools, you can perform the
installation manually by first downloading the latest release of the package. Once
downloaded, enter the following command to import the package:

```python
import netapp.santricity
```

###Getting started

To get started using the NetApp SANtricity WebAPI - Python SDK, access the ``api_client.py`` file and specify
the host URL for your REST service.

```python
#/usr/bin/python

from netapp.santricity.configuration import Configuration
from netapp.santricity.api_client import ApiClient
from netapp.santricity.api.v2.storage_systems_api import StorageSystemsApi
from netapp.santricity.models.v2.storage_system_response import StorageSystemResponse
from pprint import pprint

config = Configuration()
config.host = "http://localhost:8080" #
config.username = "rw"
config.password = "rw"

api_client = ApiClient()
config.api_client = api_client

storage_system = StorageSystemsApi(api_client=api_client)

ssr = storage_system.get_all_storage_systems()
```
