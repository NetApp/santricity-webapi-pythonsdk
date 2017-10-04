#!/usr/bin/env python
# coding: utf-8

"""
StorageSystemsApi.py

  The Clear BSD License

  Copyright (c) – 2016, NetApp, Inc. All rights reserved.

  Redistribution and use in source and binary forms, with or without modification, are permitted (subject to the limitations in the disclaimer below) provided that the following conditions are met:

  * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

  * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

  * Neither the name of NetApp, Inc. nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

  NO EXPRESS OR IMPLIED LICENSES TO ANY PARTY'S PATENT RIGHTS ARE GRANTED BY THIS LICENSE. THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from ....santricity.configuration import Configuration
from ....santricity.api_client import ApiClient


class StorageSystemsApi(object):

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient(context_path='/devmgr/v2')
            self.api_client = config.api_client
    
    
    def cancel_discovery_operation(self, **kwargs):
            """
            Cancel discovery operation
            Proxy Only. Cancel a running discovery operation.

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.cancel_discovery_operation(callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :return: None
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = []
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method cancel_discovery_operation" % key
                    )
                params[key] = val
            del params['kwargs']

    

            resource_path = '/discovery'.replace('{format}', 'json')
            path_params = {}
    

            query_params = {}
    

            header_params = {}
    

            form_params = []
            local_var_files = {}
    

            body_params = None
    

            # HTTP header `Accept`
            header_params['Accept'] = self.api_client.\
                select_header_accept(['application/json'])
            if not header_params['Accept']:
                del header_params['Accept']

            # HTTP header `Content-Type`
            header_params['Content-Type'] = self.api_client.\
                select_header_content_type(['application/json'])

            # Authentication setting
            auth_settings = ['basicAuth']

            response = self.api_client.call_api(resource_path, 'DELETE',
                                                path_params,
                                                query_params,
                                                header_params,
                                                body=body_params,
                                                post_params=form_params,
                                                files=local_var_files,
                                                response_type=None,
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def configure_ethernet_interfaces(self, system_id, **kwargs):
            """
            Configure the ethernet management connections on a controller
            Mode: Both Embedded and Proxy. Update the ethernet management connection configuration. <br> This operation can lead to an inaccessible controller if performed incorrectly or if incorrect ip addresses, gateway addresses, etc, are provided. Configuration is performed by connecting to the alternate controller, so it must be accessible for the operation to succeed.

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.configure_ethernet_interfaces(system_id, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param ManagementConfigurationRequest body: 
    
            :return: ManagementInterface
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method configure_ethernet_interfaces" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `configure_ethernet_interfaces`")
    
    
    
    

            resource_path = '/storage-systems/{system-id}/configuration/ethernet-interfaces'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    

            header_params = {}
    

            form_params = []
            local_var_files = {}
    

            body_params = None
    
            if 'body' in params:
                body_params = params['body']
    

            # HTTP header `Accept`
            header_params['Accept'] = self.api_client.\
                select_header_accept(['application/json'])
            if not header_params['Accept']:
                del header_params['Accept']

            # HTTP header `Content-Type`
            header_params['Content-Type'] = self.api_client.\
                select_header_content_type(['application/json'])

            # Authentication setting
            auth_settings = ['basicAuth']

            response = self.api_client.call_api(resource_path, 'POST',
                                                path_params,
                                                query_params,
                                                header_params,
                                                body=body_params,
                                                post_params=form_params,
                                                files=local_var_files,
                                                response_type='ManagementInterface',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def discover_storage_devices(self, **kwargs):
            """
            Discover StorageDevices on the network
            Mode: Proxy only. Initiate a discovery operation on a range of IP addresses. Retrieve the results using a GET.

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.discover_storage_devices(callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param DiscoveryStartRequest body: 
    
            :return: DiscoverResponse
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['body']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method discover_storage_devices" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
    

            resource_path = '/discovery'.replace('{format}', 'json')
            path_params = {}
    

            query_params = {}
    

            header_params = {}
    

            form_params = []
            local_var_files = {}
    

            body_params = None
    
            if 'body' in params:
                body_params = params['body']
    

            # HTTP header `Accept`
            header_params['Accept'] = self.api_client.\
                select_header_accept(['application/json'])
            if not header_params['Accept']:
                del header_params['Accept']

            # HTTP header `Content-Type`
            header_params['Content-Type'] = self.api_client.\
                select_header_content_type(['application/json'])

            # Authentication setting
            auth_settings = ['basicAuth']

            response = self.api_client.call_api(resource_path, 'POST',
                                                path_params,
                                                query_params,
                                                header_params,
                                                body=body_params,
                                                post_params=form_params,
                                                files=local_var_files,
                                                response_type='DiscoverResponse',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def enable_feature_pack(self, system_id, key_file, **kwargs):
            """
            Enable a feature pack.
            Mode: Both Embedded and Proxy. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.enable_feature_pack(system_id, key_file, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param file key_file: The bundle key file (required)
    
            :return: None
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'key_file']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method enable_feature_pack" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `enable_feature_pack`")
    
    
    
            # verify the required parameter 'key_file' is set
            if ('key_file' not in params) or (params['key_file'] is None):
                raise ValueError("Missing the required parameter `key_file` when calling `enable_feature_pack`")
    
    

            resource_path = '/storage-systems/{system-id}/feature-pack'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    

            header_params = {}
    

            form_params = []
            local_var_files = {}
    
            if 'key_file' in params:
                local_var_files['keyFile'] = params['key_file']
    

            body_params = None
    

            # HTTP header `Accept`
            header_params['Accept'] = self.api_client.\
                select_header_accept(['application/json'])
            if not header_params['Accept']:
                del header_params['Accept']

            # HTTP header `Content-Type`
            header_params['Content-Type'] = self.api_client.\
                select_header_content_type(['multipart/form-data'])

            # Authentication setting
            auth_settings = ['basicAuth']

            response = self.api_client.call_api(resource_path, 'POST',
                                                path_params,
                                                query_params,
                                                header_params,
                                                body=body_params,
                                                post_params=form_params,
                                                files=local_var_files,
                                                response_type=None,
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def enable_premium_feature(self, system_id, **kwargs):
            """
            Enable a premium feature.
            Mode: Both Embedded and Proxy. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.enable_premium_feature(system_id, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param file key_file: The premium feature key file
    
            :return: None
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'key_file']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method enable_premium_feature" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `enable_premium_feature`")
    
    
    
    

            resource_path = '/storage-systems/{system-id}/premium-feature'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    

            header_params = {}
    

            form_params = []
            local_var_files = {}
    
            if 'key_file' in params:
                local_var_files['keyFile'] = params['key_file']
    

            body_params = None
    

            # HTTP header `Accept`
            header_params['Accept'] = self.api_client.\
                select_header_accept(['application/json'])
            if not header_params['Accept']:
                del header_params['Accept']

            # HTTP header `Content-Type`
            header_params['Content-Type'] = self.api_client.\
                select_header_content_type(['multipart/form-data'])

            # Authentication setting
            auth_settings = ['basicAuth']

            response = self.api_client.call_api(resource_path, 'POST',
                                                path_params,
                                                query_params,
                                                header_params,
                                                body=body_params,
                                                post_params=form_params,
                                                files=local_var_files,
                                                response_type=None,
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def get_all_folders(self, **kwargs):
            """
            Get all Folders
            Mode: Proxy only. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.get_all_folders(callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :return: list[Folder]
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = []
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method get_all_folders" % key
                    )
                params[key] = val
            del params['kwargs']

    

            resource_path = '/folders'.replace('{format}', 'json')
            path_params = {}
    

            query_params = {}
    

            header_params = {}
    

            form_params = []
            local_var_files = {}
    

            body_params = None
    

            # HTTP header `Accept`
            header_params['Accept'] = self.api_client.\
                select_header_accept(['application/json'])
            if not header_params['Accept']:
                del header_params['Accept']

            # HTTP header `Content-Type`
            header_params['Content-Type'] = self.api_client.\
                select_header_content_type(['application/json'])

            # Authentication setting
            auth_settings = ['basicAuth']

            response = self.api_client.call_api(resource_path, 'GET',
                                                path_params,
                                                query_params,
                                                header_params,
                                                body=body_params,
                                                post_params=form_params,
                                                files=local_var_files,
                                                response_type='list[Folder]',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def get_all_storage_systems(self, **kwargs):
            """
            Get list of storage-systems
            Mode: Both Embedded and Proxy. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.get_all_storage_systems(callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :return: list[StorageSystemResponse]
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = []
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method get_all_storage_systems" % key
                    )
                params[key] = val
            del params['kwargs']

    

            resource_path = '/storage-systems'.replace('{format}', 'json')
            path_params = {}
    

            query_params = {}
    

            header_params = {}
    

            form_params = []
            local_var_files = {}
    

            body_params = None
    

            # HTTP header `Accept`
            header_params['Accept'] = self.api_client.\
                select_header_accept(['application/json'])
            if not header_params['Accept']:
                del header_params['Accept']

            # HTTP header `Content-Type`
            header_params['Content-Type'] = self.api_client.\
                select_header_content_type(['application/json'])

            # Authentication setting
            auth_settings = ['basicAuth']

            response = self.api_client.call_api(resource_path, 'GET',
                                                path_params,
                                                query_params,
                                                header_params,
                                                body=body_params,
                                                post_params=form_params,
                                                files=local_var_files,
                                                response_type='list[StorageSystemResponse]',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def get_discovery_results(self, **kwargs):
            """
            Get discovery results
            Mode: Proxy only. Retrieve the results of a discovery operation on a range of IP addresses. Recent previous results can be retrieved using their requestId.

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.get_discovery_results(callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param int request_id: 
    
            :return: DiscoverResponse
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['request_id']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method get_discovery_results" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
    

            resource_path = '/discovery'.replace('{format}', 'json')
            path_params = {}
    

            query_params = {}
    
            if 'request_id' in params:
                query_params['requestId'] = params['request_id']
    

            header_params = {}
    

            form_params = []
            local_var_files = {}
    

            body_params = None
    

            # HTTP header `Accept`
            header_params['Accept'] = self.api_client.\
                select_header_accept(['application/json'])
            if not header_params['Accept']:
                del header_params['Accept']

            # HTTP header `Content-Type`
            header_params['Content-Type'] = self.api_client.\
                select_header_content_type(['application/json'])

            # Authentication setting
            auth_settings = ['basicAuth']

            response = self.api_client.call_api(resource_path, 'GET',
                                                path_params,
                                                query_params,
                                                header_params,
                                                body=body_params,
                                                post_params=form_params,
                                                files=local_var_files,
                                                response_type='DiscoverResponse',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def get_ethernet_interfaces(self, system_id, **kwargs):
            """
            Get the list of ethernet interfaces
            Mode: Both Embedded and Proxy. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.get_ethernet_interfaces(system_id, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :return: list[ManagementInterface]
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method get_ethernet_interfaces" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `get_ethernet_interfaces`")
    
    

            resource_path = '/storage-systems/{system-id}/configuration/ethernet-interfaces'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    

            header_params = {}
    

            form_params = []
            local_var_files = {}
    

            body_params = None
    

            # HTTP header `Accept`
            header_params['Accept'] = self.api_client.\
                select_header_accept(['application/json'])
            if not header_params['Accept']:
                del header_params['Accept']

            # HTTP header `Content-Type`
            header_params['Content-Type'] = self.api_client.\
                select_header_content_type(['application/json'])

            # Authentication setting
            auth_settings = ['basicAuth']

            response = self.api_client.call_api(resource_path, 'GET',
                                                path_params,
                                                query_params,
                                                header_params,
                                                body=body_params,
                                                post_params=form_params,
                                                files=local_var_files,
                                                response_type='list[ManagementInterface]',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def get_filtered_object_graph(self, system_id, **kwargs):
            """
            Retrieve one or more elements from the ObjectGraph using an XPath expression.
            Mode: Both Embedded and Proxy. This method is used to query the ObjectGraph for one or more elements. <br/> <b>Examples:</b> <br/> <ul><li>Retrieve the list of drives: /drive </li> <li>Locate all instances of an attribute called \"id\": //id </li> <li>Find a thinVolume with an id of \"1\": /highLevelVolBundle/thinVolume[id=\"1\"]</li><li>Find all thin volumes and volumes inefficiently: //volume | //thinVolume</li><li>Get the NSVRAM version from saData: /sa/saData/nvsramVersion</li></ul><b>References: </b> http://www.w3schools.com/xsl/xpath_intro.asp

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.get_filtered_object_graph(system_id, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str query: 
    
            :return: list[object]
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'query']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method get_filtered_object_graph" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `get_filtered_object_graph`")
    
    
    
    

            resource_path = '/storage-systems/{system-id}/graph/xpath-filter'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'query' in params:
                query_params['query'] = params['query']
    

            header_params = {}
    

            form_params = []
            local_var_files = {}
    

            body_params = None
    

            # HTTP header `Accept`
            header_params['Accept'] = self.api_client.\
                select_header_accept(['application/json'])
            if not header_params['Accept']:
                del header_params['Accept']

            # HTTP header `Content-Type`
            header_params['Content-Type'] = self.api_client.\
                select_header_content_type(['application/json'])

            # Authentication setting
            auth_settings = ['basicAuth']

            response = self.api_client.call_api(resource_path, 'GET',
                                                path_params,
                                                query_params,
                                                header_params,
                                                body=body_params,
                                                post_params=form_params,
                                                files=local_var_files,
                                                response_type='list[object]',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def get_folder(self, folder_id, **kwargs):
            """
            Get a Folder
            Mode: Proxy only. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.get_folder(folder_id, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str folder_id:  (required)
    
            :return: Folder
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['folder_id']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method get_folder" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'folder_id' is set
            if ('folder_id' not in params) or (params['folder_id'] is None):
                raise ValueError("Missing the required parameter `folder_id` when calling `get_folder`")
    
    

            resource_path = '/folders/{folder-id}'.replace('{format}', 'json')
            path_params = {}
    
            if 'folder_id' in params:
                path_params['folder-id'] = params['folder_id']
    

            query_params = {}
    

            header_params = {}
    

            form_params = []
            local_var_files = {}
    

            body_params = None
    

            # HTTP header `Accept`
            header_params['Accept'] = self.api_client.\
                select_header_accept(['application/json'])
            if not header_params['Accept']:
                del header_params['Accept']

            # HTTP header `Content-Type`
            header_params['Content-Type'] = self.api_client.\
                select_header_content_type(['application/json'])

            # Authentication setting
            auth_settings = ['basicAuth']

            response = self.api_client.call_api(resource_path, 'GET',
                                                path_params,
                                                query_params,
                                                header_params,
                                                body=body_params,
                                                post_params=form_params,
                                                files=local_var_files,
                                                response_type='Folder',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def get_lockdown_status_response(self, system_id, **kwargs):
            """
            Retrieve information about the storage system lockdown status.
            Mode: Both Embedded and Proxy. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.get_lockdown_status_response(system_id, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :return: LockdownStatusResponse
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method get_lockdown_status_response" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `get_lockdown_status_response`")
    
    

            resource_path = '/storage-systems/{system-id}/lockdownstatus'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    

            header_params = {}
    

            form_params = []
            local_var_files = {}
    

            body_params = None
    

            # HTTP header `Accept`
            header_params['Accept'] = self.api_client.\
                select_header_accept(['application/json'])
            if not header_params['Accept']:
                del header_params['Accept']

            # HTTP header `Content-Type`
            header_params['Content-Type'] = self.api_client.\
                select_header_content_type(['application/json'])

            # Authentication setting
            auth_settings = ['basicAuth']

            response = self.api_client.call_api(resource_path, 'GET',
                                                path_params,
                                                query_params,
                                                header_params,
                                                body=body_params,
                                                post_params=form_params,
                                                files=local_var_files,
                                                response_type='LockdownStatusResponse',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def get_object_graph(self, system_id, **kwargs):
            """
            Retrieve the ObjectGraph, which contains all configuration details for the storage-system.
            Mode: Both Embedded and Proxy. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.get_object_graph(system_id, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :return: ObjectBundle
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method get_object_graph" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `get_object_graph`")
    
    

            resource_path = '/storage-systems/{system-id}/graph'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    

            header_params = {}
    

            form_params = []
            local_var_files = {}
    

            body_params = None
    

            # HTTP header `Accept`
            header_params['Accept'] = self.api_client.\
                select_header_accept(['application/json'])
            if not header_params['Accept']:
                del header_params['Accept']

            # HTTP header `Content-Type`
            header_params['Content-Type'] = self.api_client.\
                select_header_content_type(['application/json'])

            # Authentication setting
            auth_settings = ['basicAuth']

            response = self.api_client.call_api(resource_path, 'GET',
                                                path_params,
                                                query_params,
                                                header_params,
                                                body=body_params,
                                                post_params=form_params,
                                                files=local_var_files,
                                                response_type='ObjectBundle',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def get_password_status(self, system_id, **kwargs):
            """
            Get the password status of the StorageDevice
            Mode: Both Embedded and Proxy. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.get_password_status(system_id, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :return: PasswordStatusResponse
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method get_password_status" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `get_password_status`")
    
    

            resource_path = '/storage-systems/{system-id}/passwords'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    

            header_params = {}
    

            form_params = []
            local_var_files = {}
    

            body_params = None
    

            # HTTP header `Accept`
            header_params['Accept'] = self.api_client.\
                select_header_accept(['application/json'])
            if not header_params['Accept']:
                del header_params['Accept']

            # HTTP header `Content-Type`
            header_params['Content-Type'] = self.api_client.\
                select_header_content_type(['application/json'])

            # Authentication setting
            auth_settings = ['basicAuth']

            response = self.api_client.call_api(resource_path, 'GET',
                                                path_params,
                                                query_params,
                                                header_params,
                                                body=body_params,
                                                post_params=form_params,
                                                files=local_var_files,
                                                response_type='PasswordStatusResponse',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def get_storage_device_with_folder(self, folder_id, **kwargs):
            """
            Get StorageDevices associated with a Folder
            Mode: Proxy only. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.get_storage_device_with_folder(folder_id, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str folder_id:  (required)
    
            :return: list[str]
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['folder_id']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method get_storage_device_with_folder" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'folder_id' is set
            if ('folder_id' not in params) or (params['folder_id'] is None):
                raise ValueError("Missing the required parameter `folder_id` when calling `get_storage_device_with_folder`")
    
    

            resource_path = '/folders/{folder-id}/storage-devices'.replace('{format}', 'json')
            path_params = {}
    
            if 'folder_id' in params:
                path_params['folder-id'] = params['folder_id']
    

            query_params = {}
    

            header_params = {}
    

            form_params = []
            local_var_files = {}
    

            body_params = None
    

            # HTTP header `Accept`
            header_params['Accept'] = self.api_client.\
                select_header_accept(['application/json'])
            if not header_params['Accept']:
                del header_params['Accept']

            # HTTP header `Content-Type`
            header_params['Content-Type'] = self.api_client.\
                select_header_content_type(['application/json'])

            # Authentication setting
            auth_settings = ['basicAuth']

            response = self.api_client.call_api(resource_path, 'GET',
                                                path_params,
                                                query_params,
                                                header_params,
                                                body=body_params,
                                                post_params=form_params,
                                                files=local_var_files,
                                                response_type='list[str]',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def get_storage_system(self, system_id, **kwargs):
            """
            Get a specific storage-system
            Mode: Both Embedded and Proxy. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.get_storage_system(system_id, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :return: StorageSystemResponse
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method get_storage_system" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `get_storage_system`")
    
    

            resource_path = '/storage-systems/{system-id}'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    

            header_params = {}
    

            form_params = []
            local_var_files = {}
    

            body_params = None
    

            # HTTP header `Accept`
            header_params['Accept'] = self.api_client.\
                select_header_accept(['application/json'])
            if not header_params['Accept']:
                del header_params['Accept']

            # HTTP header `Content-Type`
            header_params['Content-Type'] = self.api_client.\
                select_header_content_type(['application/json'])

            # Authentication setting
            auth_settings = ['basicAuth']

            response = self.api_client.call_api(resource_path, 'GET',
                                                path_params,
                                                query_params,
                                                header_params,
                                                body=body_params,
                                                post_params=form_params,
                                                files=local_var_files,
                                                response_type='StorageSystemResponse',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def get_storage_system_capabilities(self, system_id, **kwargs):
            """
            Get StorageDevice capabilities.
            Mode: Both Embedded and Proxy. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.get_storage_system_capabilities(system_id, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :return: CapabilitiesResponse
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method get_storage_system_capabilities" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `get_storage_system_capabilities`")
    
    

            resource_path = '/storage-systems/{system-id}/capabilities'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    

            header_params = {}
    

            form_params = []
            local_var_files = {}
    

            body_params = None
    

            # HTTP header `Accept`
            header_params['Accept'] = self.api_client.\
                select_header_accept(['application/json'])
            if not header_params['Accept']:
                del header_params['Accept']

            # HTTP header `Content-Type`
            header_params['Content-Type'] = self.api_client.\
                select_header_content_type(['application/json'])

            # Authentication setting
            auth_settings = ['basicAuth']

            response = self.api_client.call_api(resource_path, 'GET',
                                                path_params,
                                                query_params,
                                                header_params,
                                                body=body_params,
                                                post_params=form_params,
                                                files=local_var_files,
                                                response_type='CapabilitiesResponse',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def new_folder(self, **kwargs):
            """
            Create a Folder
            Mode: Proxy only. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.new_folder(callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param FolderCreateRequest body: 
    
            :return: Folder
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['body']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method new_folder" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
    

            resource_path = '/folders'.replace('{format}', 'json')
            path_params = {}
    

            query_params = {}
    

            header_params = {}
    

            form_params = []
            local_var_files = {}
    

            body_params = None
    
            if 'body' in params:
                body_params = params['body']
    

            # HTTP header `Accept`
            header_params['Accept'] = self.api_client.\
                select_header_accept(['application/json'])
            if not header_params['Accept']:
                del header_params['Accept']

            # HTTP header `Content-Type`
            header_params['Content-Type'] = self.api_client.\
                select_header_content_type(['application/json'])

            # Authentication setting
            auth_settings = ['basicAuth']

            response = self.api_client.call_api(resource_path, 'POST',
                                                path_params,
                                                query_params,
                                                header_params,
                                                body=body_params,
                                                post_params=form_params,
                                                files=local_var_files,
                                                response_type='Folder',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def new_storage_system(self, **kwargs):
            """
            Add a storage-system
            This endpoint allows you to add additional storage-systems under management using their IP address[es].

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.new_storage_system(callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param StorageSystemCreateRequest body: 
    
            :return: AddStorageSystemReturn
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['body']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method new_storage_system" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
    

            resource_path = '/storage-systems'.replace('{format}', 'json')
            path_params = {}
    

            query_params = {}
    

            header_params = {}
    

            form_params = []
            local_var_files = {}
    

            body_params = None
    
            if 'body' in params:
                body_params = params['body']
    

            # HTTP header `Accept`
            header_params['Accept'] = self.api_client.\
                select_header_accept(['application/json'])
            if not header_params['Accept']:
                del header_params['Accept']

            # HTTP header `Content-Type`
            header_params['Content-Type'] = self.api_client.\
                select_header_content_type(['application/json'])

            # Authentication setting
            auth_settings = ['basicAuth']

            response = self.api_client.call_api(resource_path, 'POST',
                                                path_params,
                                                query_params,
                                                header_params,
                                                body=body_params,
                                                post_params=form_params,
                                                files=local_var_files,
                                                response_type='AddStorageSystemReturn',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def remove_feature_pack(self, system_id, **kwargs):
            """
            Remove all feature packs.
            Mode: Both Embedded and Proxy. \n\nWARNING: Removal of feature packs is an offline operation. Failure to quiesce IO prior to performing this operation may result in loss of access to data or loss of data. \n\nWhen used in embedded mode a client may not receive a response from this operation.

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.remove_feature_pack(system_id, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :return: None
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method remove_feature_pack" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `remove_feature_pack`")
    
    

            resource_path = '/storage-systems/{system-id}/feature-pack'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    

            header_params = {}
    

            form_params = []
            local_var_files = {}
    

            body_params = None
    

            # HTTP header `Accept`
            header_params['Accept'] = self.api_client.\
                select_header_accept(['application/json'])
            if not header_params['Accept']:
                del header_params['Accept']

            # HTTP header `Content-Type`
            header_params['Content-Type'] = self.api_client.\
                select_header_content_type(['application/json'])

            # Authentication setting
            auth_settings = ['basicAuth']

            response = self.api_client.call_api(resource_path, 'DELETE',
                                                path_params,
                                                query_params,
                                                header_params,
                                                body=body_params,
                                                post_params=form_params,
                                                files=local_var_files,
                                                response_type=None,
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def remove_folder(self, folder_id, **kwargs):
            """
            Delete a Folder
            Mode: Proxy only. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.remove_folder(folder_id, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str folder_id:  (required)
    
            :return: CallResponse
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['folder_id']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method remove_folder" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'folder_id' is set
            if ('folder_id' not in params) or (params['folder_id'] is None):
                raise ValueError("Missing the required parameter `folder_id` when calling `remove_folder`")
    
    

            resource_path = '/folders/{folder-id}'.replace('{format}', 'json')
            path_params = {}
    
            if 'folder_id' in params:
                path_params['folder-id'] = params['folder_id']
    

            query_params = {}
    

            header_params = {}
    

            form_params = []
            local_var_files = {}
    

            body_params = None
    

            # HTTP header `Accept`
            header_params['Accept'] = self.api_client.\
                select_header_accept(['application/json'])
            if not header_params['Accept']:
                del header_params['Accept']

            # HTTP header `Content-Type`
            header_params['Content-Type'] = self.api_client.\
                select_header_content_type(['application/json'])

            # Authentication setting
            auth_settings = ['basicAuth']

            response = self.api_client.call_api(resource_path, 'DELETE',
                                                path_params,
                                                query_params,
                                                header_params,
                                                body=body_params,
                                                post_params=form_params,
                                                files=local_var_files,
                                                response_type='CallResponse',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def remove_premium_feature(self, system_id, capability, **kwargs):
            """
            Remove a premium feature.
            Mode: Both Embedded and Proxy. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.remove_premium_feature(system_id, capability, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str capability: Capability to remove. (required)
    
            :return: None
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'capability']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method remove_premium_feature" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `remove_premium_feature`")
    
    
    
            # verify the required parameter 'capability' is set
            if ('capability' not in params) or (params['capability'] is None):
                raise ValueError("Missing the required parameter `capability` when calling `remove_premium_feature`")
    
    

            resource_path = '/storage-systems/{system-id}/premium-feature'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'capability' in params:
                query_params['capability'] = params['capability']
    

            header_params = {}
    

            form_params = []
            local_var_files = {}
    

            body_params = None
    

            # HTTP header `Accept`
            header_params['Accept'] = self.api_client.\
                select_header_accept(['application/json'])
            if not header_params['Accept']:
                del header_params['Accept']

            # HTTP header `Content-Type`
            header_params['Content-Type'] = self.api_client.\
                select_header_content_type(['application/json'])

            # Authentication setting
            auth_settings = ['basicAuth']

            response = self.api_client.call_api(resource_path, 'DELETE',
                                                path_params,
                                                query_params,
                                                header_params,
                                                body=body_params,
                                                post_params=form_params,
                                                files=local_var_files,
                                                response_type=None,
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def remove_storage_system(self, system_id, **kwargs):
            """
            Remove one or more storage-systems
            The path is a comma-separated list of IDs. The identifiers of any storage-systems were failed to remove are provided in the response error response.

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.remove_storage_system(system_id, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :return: None
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method remove_storage_system" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `remove_storage_system`")
    
    

            resource_path = '/storage-systems/{system-id}'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    

            header_params = {}
    

            form_params = []
            local_var_files = {}
    

            body_params = None
    

            # HTTP header `Accept`
            header_params['Accept'] = self.api_client.\
                select_header_accept(['application/json'])
            if not header_params['Accept']:
                del header_params['Accept']

            # HTTP header `Content-Type`
            header_params['Content-Type'] = self.api_client.\
                select_header_content_type(['application/json'])

            # Authentication setting
            auth_settings = ['basicAuth']

            response = self.api_client.call_api(resource_path, 'DELETE',
                                                path_params,
                                                query_params,
                                                header_params,
                                                body=body_params,
                                                post_params=form_params,
                                                files=local_var_files,
                                                response_type=None,
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def set_password(self, system_id, **kwargs):
            """
            Set the password of the StorageDevice
            Mode: Both Embedded and Proxy. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.set_password(system_id, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param PasswordSetRequest body: 
    
            :return: None
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method set_password" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `set_password`")
    
    
    
    

            resource_path = '/storage-systems/{system-id}/passwords'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    

            header_params = {}
    

            form_params = []
            local_var_files = {}
    

            body_params = None
    
            if 'body' in params:
                body_params = params['body']
    

            # HTTP header `Accept`
            header_params['Accept'] = self.api_client.\
                select_header_accept(['application/json'])
            if not header_params['Accept']:
                del header_params['Accept']

            # HTTP header `Content-Type`
            header_params['Content-Type'] = self.api_client.\
                select_header_content_type(['application/json'])

            # Authentication setting
            auth_settings = ['basicAuth']

            response = self.api_client.call_api(resource_path, 'POST',
                                                path_params,
                                                query_params,
                                                header_params,
                                                body=body_params,
                                                post_params=form_params,
                                                files=local_var_files,
                                                response_type=None,
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def update_folder(self, folder_id, **kwargs):
            """
            Update a Folder
            Mode: Proxy only. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.update_folder(folder_id, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str folder_id:  (required)
    
            :param FolderUpdateRequest body: 
    
            :return: Folder
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['folder_id', 'body']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method update_folder" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'folder_id' is set
            if ('folder_id' not in params) or (params['folder_id'] is None):
                raise ValueError("Missing the required parameter `folder_id` when calling `update_folder`")
    
    
    
    

            resource_path = '/folders/{folder-id}'.replace('{format}', 'json')
            path_params = {}
    
            if 'folder_id' in params:
                path_params['folder-id'] = params['folder_id']
    

            query_params = {}
    

            header_params = {}
    

            form_params = []
            local_var_files = {}
    

            body_params = None
    
            if 'body' in params:
                body_params = params['body']
    

            # HTTP header `Accept`
            header_params['Accept'] = self.api_client.\
                select_header_accept(['application/json'])
            if not header_params['Accept']:
                del header_params['Accept']

            # HTTP header `Content-Type`
            header_params['Content-Type'] = self.api_client.\
                select_header_content_type(['application/json'])

            # Authentication setting
            auth_settings = ['basicAuth']

            response = self.api_client.call_api(resource_path, 'POST',
                                                path_params,
                                                query_params,
                                                header_params,
                                                body=body_params,
                                                post_params=form_params,
                                                files=local_var_files,
                                                response_type='Folder',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def update_storage_device_name(self, system_id, **kwargs):
            """
            Set the name of the StorageDevice
            Mode: Both Embedded and Proxy. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.update_storage_device_name(system_id, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param StorageSystemConfigUpdateRequest body: 
    
            :return: StorageSystemConfigResponse
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method update_storage_device_name" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `update_storage_device_name`")
    
    
    
    

            resource_path = '/storage-systems/{system-id}/configuration'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    

            header_params = {}
    

            form_params = []
            local_var_files = {}
    

            body_params = None
    
            if 'body' in params:
                body_params = params['body']
    

            # HTTP header `Accept`
            header_params['Accept'] = self.api_client.\
                select_header_accept(['application/json'])
            if not header_params['Accept']:
                del header_params['Accept']

            # HTTP header `Content-Type`
            header_params['Content-Type'] = self.api_client.\
                select_header_content_type(['application/json'])

            # Authentication setting
            auth_settings = ['basicAuth']

            response = self.api_client.call_api(resource_path, 'POST',
                                                path_params,
                                                query_params,
                                                header_params,
                                                body=body_params,
                                                post_params=form_params,
                                                files=local_var_files,
                                                response_type='StorageSystemConfigResponse',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def update_storage_system(self, system_id, update_request, **kwargs):
            """
            Update a storage-system
            Mode: Both Embedded and Proxy. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.update_storage_system(system_id, update_request, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param StorageSystemUpdateRequest update_request: Update request (required)
    
            :return: StorageSystemResponse
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'update_request']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method update_storage_system" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `update_storage_system`")
    
    
    
            # verify the required parameter 'update_request' is set
            if ('update_request' not in params) or (params['update_request'] is None):
                raise ValueError("Missing the required parameter `update_request` when calling `update_storage_system`")
    
    

            resource_path = '/storage-systems/{system-id}'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    

            header_params = {}
    

            form_params = []
            local_var_files = {}
    

            body_params = None
    
            if 'update_request' in params:
                body_params = params['update_request']
    

            # HTTP header `Accept`
            header_params['Accept'] = self.api_client.\
                select_header_accept(['application/json'])
            if not header_params['Accept']:
                del header_params['Accept']

            # HTTP header `Content-Type`
            header_params['Content-Type'] = self.api_client.\
                select_header_content_type(['application/json'])

            # Authentication setting
            auth_settings = ['basicAuth']

            response = self.api_client.call_api(resource_path, 'POST',
                                                path_params,
                                                query_params,
                                                header_params,
                                                body=body_params,
                                                post_params=form_params,
                                                files=local_var_files,
                                                response_type='StorageSystemResponse',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def validate_storage_system_password(self, system_id, **kwargs):
            """
            Validate the stored password for a storage-system
            Mode: Both Embedded and Proxy. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.validate_storage_system_password(system_id, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :return: None
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method validate_storage_system_password" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `validate_storage_system_password`")
    
    

            resource_path = '/storage-systems/{system-id}/validatePassword'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    

            header_params = {}
    

            form_params = []
            local_var_files = {}
    

            body_params = None
    

            # HTTP header `Accept`
            header_params['Accept'] = self.api_client.\
                select_header_accept(['application/json'])
            if not header_params['Accept']:
                del header_params['Accept']

            # HTTP header `Content-Type`
            header_params['Content-Type'] = self.api_client.\
                select_header_content_type(['application/json'])

            # Authentication setting
            auth_settings = ['basicAuth']

            response = self.api_client.call_api(resource_path, 'POST',
                                                path_params,
                                                query_params,
                                                header_params,
                                                body=body_params,
                                                post_params=form_params,
                                                files=local_var_files,
                                                response_type=None,
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    









