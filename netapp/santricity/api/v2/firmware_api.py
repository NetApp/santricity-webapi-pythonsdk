#!/usr/bin/env python
# coding: utf-8

"""
FirmwareApi.py

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


class FirmwareApi(object):

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient(context_path='/devmgr/v2')
            self.api_client = config.api_client
    
    
    def activate_staged_controller_firmware(self, system_id, **kwargs):
            """
            Activate staged controller firmware
            Mode: Proxy only. Activate Controller Firmware that was previous staged for a later upgrade operation. This operation will begin activation of the uploaded package.

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.activate_staged_controller_firmware(system_id, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param CfwActivationRequest body: 
    
            :return: CfwUpgradeResponse
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
                        " to method activate_staged_controller_firmware" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `activate_staged_controller_firmware`")
    
    
    
    

            resource_path = '/storage-systems/{system-id}/cfw-upgrade/activate'.replace('{format}', 'json')
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
                                                response_type='CfwUpgradeResponse',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def activate_staged_firmware(self, **kwargs):
            """
            Activates previously staged firmware.
            Mode: Embedded only. A successful activation will shut the web server down which may result in the request to timeout, be canceled, or return with a 503 Service Unavailable before the success response could be returned.

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.activate_staged_firmware(callback=callback_function)
    
    

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
                        " to method activate_staged_firmware" % key
                    )
                params[key] = val
            del params['kwargs']

    

            resource_path = '/firmware/embedded-firmware/activate'.replace('{format}', 'json')
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
    
    def begin_compatibility_check(self, **kwargs):
            """
            Begin a firmware compatibility check operation
            Mode: Proxy only. This endpoint allows a user to request all firmware and nvsram files that are compatible with a StorageSystem, or list of StorageSystems.

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.begin_compatibility_check(callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param FirmwareCompatibilityRequest body: 
    
            :return: FirmwareCompatibilityResponse
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
                        " to method begin_compatibility_check" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
    

            resource_path = '/firmware/compatibility-check'.replace('{format}', 'json')
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
                                                response_type='FirmwareCompatibilityResponse',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def cancel_compatibility_check(self, **kwargs):
            """
            Cancel a firmware compatibility check operation
            Mode: Proxy only. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.cancel_compatibility_check(callback=callback_function)
    
    

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
                        " to method cancel_compatibility_check" % key
                    )
                params[key] = val
            del params['kwargs']

    

            resource_path = '/firmware/compatibility-check'.replace('{format}', 'json')
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
    
    def cancel_health_check(self, **kwargs):
            """
            Cancel a running health check
            Mode: Both Embedded and Proxy. This operation may take some time to cancel, as pending operations must be completed first.

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.cancel_health_check(callback=callback_function)
    
    

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
                        " to method cancel_health_check" % key
                    )
                params[key] = val
            del params['kwargs']

    

            resource_path = '/health-check'.replace('{format}', 'json')
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
    
    def check_embedded_firmware_bundle_compatibility(self, system_id, **kwargs):
            """
            Performs a compatibility check on a controller firmware bundle. Speed up process by sending only first 8KB of file.
            Mode: Embedded only. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.check_embedded_firmware_bundle_compatibility(system_id, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id:  (required)
    
            :param file file: 
    
            :return: EmbeddedCompatibilityCheckResponse
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'file']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method check_embedded_firmware_bundle_compatibility" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `check_embedded_firmware_bundle_compatibility`")
    
    
    
    

            resource_path = '/firmware/embedded-firmware/{system-id}/bundle-compatibility-check'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    

            header_params = {}
    

            form_params = []
            local_var_files = {}
    
            if 'file' in params:
                local_var_files['file'] = params['file']
    

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
                                                response_type='EmbeddedCompatibilityCheckResponse',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def check_embedded_nvsram_compatibility(self, system_id, **kwargs):
            """
            Performs a compatibility check on a NVSRAM file.
            Mode: Embedded only. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.check_embedded_nvsram_compatibility(system_id, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id:  (required)
    
            :param file file: 
    
            :return: EmbeddedCompatibilityCheckResponse
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'file']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method check_embedded_nvsram_compatibility" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `check_embedded_nvsram_compatibility`")
    
    
    
    

            resource_path = '/firmware/embedded-firmware/{system-id}/nvsram-compatibility-check'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    

            header_params = {}
    

            form_params = []
            local_var_files = {}
    
            if 'file' in params:
                local_var_files['file'] = params['file']
    

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
                                                response_type='EmbeddedCompatibilityCheckResponse',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def clear_staged_firmware(self, system_id, **kwargs):
            """
            Clear staged firmware details on the array
            Mode: Proxy only. Clear staged firmware details on the storage array

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.clear_staged_firmware(system_id, callback=callback_function)
    
    

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
                        " to method clear_staged_firmware" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `clear_staged_firmware`")
    
    

            resource_path = '/storage-systems/{system-id}/cfw-upgrade/staged'.replace('{format}', 'json')
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
    
    def get_all_firmware_files(self, **kwargs):
            """
            Get the list of firmware files
            Mode: Proxy only. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.get_all_firmware_files(callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :return: list[CFWPackageMetadata]
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
                        " to method get_all_firmware_files" % key
                    )
                params[key] = val
            del params['kwargs']

    

            resource_path = '/firmware/cfw-files'.replace('{format}', 'json')
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
                                                response_type='list[CFWPackageMetadata]',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def get_compatibility_check_results(self, **kwargs):
            """
            Request status of a firmware compatibility check operation
            Mode: Proxy only. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.get_compatibility_check_results(callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param int request_id: Retrieve result of a previously submitted request.
    
            :return: FirmwareCompatibilityResponse
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
                        " to method get_compatibility_check_results" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
    

            resource_path = '/firmware/compatibility-check'.replace('{format}', 'json')
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
                                                response_type='FirmwareCompatibilityResponse',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def get_controller_firmware_upgrade_status(self, system_id, **kwargs):
            """
            Retrieve status of a Controller Firmware upgrade operation
            Mode: Proxy only. Retrieve the status of a running controller firmware or nvsram upgrade operation.

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.get_controller_firmware_upgrade_status(system_id, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :return: CfwUpgradeResponse
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
                        " to method get_controller_firmware_upgrade_status" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `get_controller_firmware_upgrade_status`")
    
    

            resource_path = '/storage-systems/{system-id}/cfw-upgrade'.replace('{format}', 'json')
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
                                                response_type='CfwUpgradeResponse',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def get_embedded_firmware_information(self, **kwargs):
            """
            Get last successful firmware upgrade timestamps and firmware upgrade logs
            Mode: Embedded only. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.get_embedded_firmware_information(callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param bool cfw_upgrade: Controller Firmware Upgrade
    
            :param bool iom_upgrade: IOM Firmware Upgrade
    
            :param bool drive_upgrade: Drive Firmware Upgrade
    
            :param bool nvsram_upgrade: NVSRAM Upgrade
    
            :param bool include_logs: Include firmware log 
    
            :return: EmbeddedFirmwareResponse
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['cfw_upgrade', 'iom_upgrade', 'drive_upgrade', 'nvsram_upgrade', 'include_logs']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method get_embedded_firmware_information" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
    
    
    
    
    
    
    
    
    

            resource_path = '/firmware/embedded-firmware'.replace('{format}', 'json')
            path_params = {}
    

            query_params = {}
    
            if 'cfw_upgrade' in params:
                query_params['cfwUpgrade'] = params['cfw_upgrade']
    
            if 'iom_upgrade' in params:
                query_params['iomUpgrade'] = params['iom_upgrade']
    
            if 'drive_upgrade' in params:
                query_params['driveUpgrade'] = params['drive_upgrade']
    
            if 'nvsram_upgrade' in params:
                query_params['nvsramUpgrade'] = params['nvsram_upgrade']
    
            if 'include_logs' in params:
                query_params['includeLogs'] = params['include_logs']
    

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
                                                response_type='EmbeddedFirmwareResponse',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def get_firmware_details(self, system_id, **kwargs):
            """
            Retrieve details on the current firmware
            Mode: Embedded only. Retrieve the list of code modules and versions of the firmware on the storage array.

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.get_firmware_details(system_id, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id:  (required)
    
            :return: CurrentFirmwareResponse
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
                        " to method get_firmware_details" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `get_firmware_details`")
    
    

            resource_path = '/firmware/embedded-firmware/{system-id}/versions'.replace('{format}', 'json')
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
                                                response_type='CurrentFirmwareResponse',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def get_firmware_file(self, filename, **kwargs):
            """
            Get a specific firmware file
            Mode: Proxy only. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.get_firmware_file(filename, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str filename:  (required)
    
            :return: CFWPackageMetadata
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['filename']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method get_firmware_file" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'filename' is set
            if ('filename' not in params) or (params['filename'] is None):
                raise ValueError("Missing the required parameter `filename` when calling `get_firmware_file`")
    
    

            resource_path = '/firmware/cfw-files/{filename}'.replace('{format}', 'json')
            path_params = {}
    
            if 'filename' in params:
                path_params['filename'] = params['filename']
    

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
                                                response_type='CFWPackageMetadata',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def get_health_check_status(self, **kwargs):
            """
            Get health check status
            This endpoint should be utilized to retrieve the results of the health check. There are multiple parts to the health check process. If a critical portion fails, the entire check will be set to failed. If an invalid password is detected or a controller cannot be contacted, the check will return without completing additional unnecessary steps.

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.get_health_check_status(callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param int request_id: Retrieve result of a previously submitted request.
    
            :return: HealthCheckResponse
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
                        " to method get_health_check_status" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
    

            resource_path = '/health-check'.replace('{format}', 'json')
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
                                                response_type='HealthCheckResponse',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def get_iom_service_information(self, **kwargs):
            """
            Get IOM service information
            Mode: Embedded only. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.get_iom_service_information(callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :return: IomServiceInfoResponse
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
                        " to method get_iom_service_information" % key
                    )
                params[key] = val
            del params['kwargs']

    

            resource_path = '/firmware/embedded-firmware/iom/service'.replace('{format}', 'json')
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
                                                response_type='IomServiceInfoResponse',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def get_staged_controller_firmware_details(self, system_id, **kwargs):
            """
            Retrieve details on the staged firmware
            Mode: Embedded only. Retrieve the list of code modules and versions of the firmware staged on the storage array.

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.get_staged_controller_firmware_details(system_id, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id:  (required)
    
            :return: StagedFirmwareResponse
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
                        " to method get_staged_controller_firmware_details" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `get_staged_controller_firmware_details`")
    
    

            resource_path = '/firmware/embedded-firmware/{system-id}/staged'.replace('{format}', 'json')
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
                                                response_type='StagedFirmwareResponse',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def get_staged_firmware_details(self, system_id, **kwargs):
            """
            Retrieve details on the staged firmware
            Mode: Proxy only. Retrieve the list of code modules and versions of the firmware staged on the storage array.

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.get_staged_firmware_details(system_id, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :return: StagedFirmwareResponse
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
                        " to method get_staged_firmware_details" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `get_staged_firmware_details`")
    
    

            resource_path = '/storage-systems/{system-id}/cfw-upgrade/staged'.replace('{format}', 'json')
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
                                                response_type='StagedFirmwareResponse',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def remove_firmware_file(self, filename, **kwargs):
            """
            Delete an uploaded firmware file
            Mode: Proxy only. Delete an uploaded firmware file by providing the filename. If the file is locked the file will be scheduled for deletion on service shutdown.

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.remove_firmware_file(filename, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str filename:  (required)
    
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

            all_params = ['filename']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method remove_firmware_file" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'filename' is set
            if ('filename' not in params) or (params['filename'] is None):
                raise ValueError("Missing the required parameter `filename` when calling `remove_firmware_file`")
    
    

            resource_path = '/firmware/upload/{filename}'.replace('{format}', 'json')
            path_params = {}
    
            if 'filename' in params:
                path_params['filename'] = params['filename']
    

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
    
    def remove_staged_firmware(self, system_id, **kwargs):
            """
            Clear staged firmware details on the array
            Mode: Embedded only. Clear staged firmware details on the storage array

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.remove_staged_firmware(system_id, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id:  (required)
    
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
                        " to method remove_staged_firmware" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `remove_staged_firmware`")
    
    

            resource_path = '/firmware/embedded-firmware/{system-id}/staged'.replace('{format}', 'json')
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
    
    def start_controller_firmware_upgrade(self, system_id, **kwargs):
            """
            Initiate a Controller Firmware upgrade operation
            Mode: Proxy only. Start a controller firmware or nvsram upgrade operation.

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.start_controller_firmware_upgrade(system_id, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param CfwUpgradeRequest body: 
    
            :return: InitialAsyncResponse
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
                        " to method start_controller_firmware_upgrade" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `start_controller_firmware_upgrade`")
    
    
    
    

            resource_path = '/storage-systems/{system-id}/cfw-upgrade'.replace('{format}', 'json')
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
                                                response_type='InitialAsyncResponse',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def start_health_check(self, **kwargs):
            """
            Begin a health check
            Mode: Both Embedded and Proxy. The health checks are designed to test whether or not a StorageSystem is stable enough to safely allow a firmware upgrade operation to proceed. They can also be used in a generic fashion to probe a large number of StorageSystems for issues requiring attention.

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.start_health_check(callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param HealthCheckRequest body: 
    
            :return: InitialAsyncResponse
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
                        " to method start_health_check" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
    

            resource_path = '/health-check'.replace('{format}', 'json')
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
                                                response_type='InitialAsyncResponse',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def update_iom_service_information(self, **kwargs):
            """
            Updates the IOM service configuration
            Mode: Embedded only. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.update_iom_service_information(callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param IomServiceUpdateRequest body: 
    
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

            all_params = ['body']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method update_iom_service_information" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
    

            resource_path = '/firmware/embedded-firmware/iom/service'.replace('{format}', 'json')
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
                                                response_type=None,
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def upload_embedded_firmware_file(self, **kwargs):
            """
            Upload a firmware file.
            Mode: Embedded only. Upload endpoint for firmware that is not staged but directly loaded to the controller. This endpoint only applies when running embedded, not as a proxy.. File can be named the veosimage or the nvsramimage

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.upload_embedded_firmware_file(callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param bool staged: set to true to indicate to stage
    
            :param bool nvsram: set to true to NVSRAM is included, and if so it must be first.  If this is true and a DLP file is included, it must be  first.  If not,  an error is generated
    
            :param file nvsramfile: 
    
            :param file dlpfile: 
    
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

            all_params = ['staged', 'nvsram', 'nvsramfile', 'dlpfile']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method upload_embedded_firmware_file" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
    
    
    
    
    
    
    

            resource_path = '/firmware/embedded-firmware'.replace('{format}', 'json')
            path_params = {}
    

            query_params = {}
    
            if 'staged' in params:
                query_params['staged'] = params['staged']
    
            if 'nvsram' in params:
                query_params['nvsram'] = params['nvsram']
    

            header_params = {}
    

            form_params = []
            local_var_files = {}
    
            if 'nvsramfile' in params:
                local_var_files['nvsramfile'] = params['nvsramfile']
    
            if 'dlpfile' in params:
                local_var_files['dlpfile'] = params['dlpfile']
    

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
    
    def upload_firmware_file(self, firmware_file, **kwargs):
            """
            Upload a firmware file.
            Mode: Proxy only. The firmware file will be uploaded to the server and will be available for firmware upgrade operations. It is recommended to keep the file names the same as they were named by the company. Some file types require this and will fail of renamed

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.upload_firmware_file(firmware_file, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param file firmware_file: The firmware file (required)
    
            :param bool validate: Validate firmware file
    
            :return: FileInfo
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['firmware_file', 'validate']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method upload_firmware_file" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'firmware_file' is set
            if ('firmware_file' not in params) or (params['firmware_file'] is None):
                raise ValueError("Missing the required parameter `firmware_file` when calling `upload_firmware_file`")
    
    
    
    

            resource_path = '/firmware/upload'.replace('{format}', 'json')
            path_params = {}
    

            query_params = {}
    
            if 'validate' in params:
                query_params['validate'] = params['validate']
    

            header_params = {}
    

            form_params = []
            local_var_files = {}
    
            if 'firmware_file' in params:
                local_var_files['firmwareFile'] = params['firmware_file']
    

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
                                                response_type='FileInfo',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def upload_nvsram_file(self, system_id, **kwargs):
            """
            Upload a nvsram file.
            Mode: Embedded only. Upload endpoint for nvsram to download to the controller. Controllers will reboot when operation completes

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.upload_nvsram_file(system_id, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id:  (required)
    
            :param file nvsramimage: 
    
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

            all_params = ['system_id', 'nvsramimage']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method upload_nvsram_file" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `upload_nvsram_file`")
    
    
    
    

            resource_path = '/firmware/embedded-firmware/{system-id}/nvsram'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    

            header_params = {}
    

            form_params = []
            local_var_files = {}
    
            if 'nvsramimage' in params:
                local_var_files['nvsramimage'] = params['nvsramimage']
    

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
    









