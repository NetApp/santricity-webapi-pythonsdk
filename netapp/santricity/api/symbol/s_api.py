#!/usr/bin/env python
# coding: utf-8

"""
SApi.py

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


class SApi(object):

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient(context_path='/devmgr/v2')
            self.api_client = config.api_client
    
    
    def symbol_scan_volume(self, system_id, body, **kwargs):
            """
            This procedure causes a scan of the specified volume over the specified extent. The scan stops on any media or parity error encountered and reports the error. The procedure can also be used to repair media errors and parity errors.
            Documented return codes: ok, illegalParam, noHeap, tryAlternate, invalidVolumeref, volumeOffline, volumeNotOptimal, parityScanFailed, parityRepairFailed, mediaRepairFailed. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_scan_volume(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param VolumeScanDescriptor body: A VolumeScanDescriptor that specifies the volume and extent to be scanned and contains indicators to enable repairing of media and parity errors. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: ParityScanResponse
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_scan_volume" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_scan_volume`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_scan_volume`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/scanVolume'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='ParityScanResponse',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_secure_disk_pool(self, system_id, body, **kwargs):
            """
            This procedure converts the specified disk pool to a secure volume group.
            Documented return codes: ok. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_secure_disk_pool(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str body: An object containing all of the required attributes to convert the specified disk pool to a secure volume group. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_secure_disk_pool" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_secure_disk_pool`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_secure_disk_pool`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/secureDiskPool'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_secure_volume_group(self, system_id, body, **kwargs):
            """
            This procedure converts the specified volume group to a secure volume group.
            Documented return codes: ok, notImplemented, invalidVolumegroupref, volsInVgUsingNonSecureCapableFlashcache, volsInVgUsingSecureDisabledFlashcache. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_secure_volume_group(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str body: The VolumeGroupRef identifier for the volume to be secured. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_secure_volume_group" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_secure_volume_group`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_secure_volume_group`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/secureVolumeGroup'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_send_drive_firmware(self, system_id, body, **kwargs):
            """
            This procedure sends chunks to the parallel drive firmware download process.
            Documented return codes: ok, error, illegalParam, noHeap, invalidRequest, invalidOffset, overrun, invalidChunksize, invalidSetid, validationError, controllerInServiceMode. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_send_drive_firmware(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param DriveFirmwareChunkDescriptor body: This object contains information about the DriveFirmwareChunkDescriptor. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_send_drive_firmware" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_send_drive_firmware`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_send_drive_firmware`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/sendDriveFirmware'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_alarm(self, system_id, body, **kwargs):
            """
            This procedure sets the allowed alarm controls.
            Documented return codes: ok, error, illegalParam. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_alarm(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param AlarmUpdateDescriptor body: An AlarmUpdateDescriptor object that indicates the alarm to modify and the alarm control to activate. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_alarm" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_alarm`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_alarm`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setAlarm'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_asup_status(self, system_id, body, **kwargs):
            """
            This procedure is used to set the current Autosupport status values.
            Documented return codes: ok, notImplemented. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_asup_status(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param AsupStatus body:  (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_asup_status" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_asup_status`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_asup_status`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setAsupStatus'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_async_mirror_group_params(self, system_id, body, **kwargs):
            """
            This procedure will change the parameters of an Async Mirror Group.
            Documented return codes: ok, invalidWarnThreshold, arvmGroupUserLabelExists, arvmGroupHasIncompleteMember, invalidSyncPriority, invalidRecoveryPointAlertThreshold, invalidSyncAlertThreshold, arvmOrphanGroup, arvmOrphanMember, arvmInvalidSyncInterval, remoteInternalError, arvmRemoteGroupUserLabelExists, arvmRemoteGroupDoesNotExist, remoteDatabaseError. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_async_mirror_group_params(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param AsyncMirrorGroupParamsUpdateDescriptor body: An object containing the Asynchronous Mirror Group parameters. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_async_mirror_group_params" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_async_mirror_group_params`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_async_mirror_group_params`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setAsyncMirrorGroupParams'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_auto_load_balancing(self, system_id, body, **kwargs):
            """
            This procedure enables or disables the auto load balancing capability on this array.
            Documented return codes: ok, noHeap, databaseError. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_auto_load_balancing(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param AutoLoadBalancingControlDescriptor body: Input descriptor indicating whether auto load balancing is to be enabled or disabled (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_auto_load_balancing" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_auto_load_balancing`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_auto_load_balancing`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setAutoLoadBalancing'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_auto_resync(self, system_id, body, **kwargs):
            """
            This procedure sets the allowable options for the auto resynchronization.
            Documented return codes: ok, illegalParam, noHeap, internalError, iconFailure, invalidVolumeref, ghostVolume, invalidMirrorvol, rvmVersionMismatch, rvmOperNotAllowedOnSec. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_auto_resync(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param MirrorAutoResyncDescriptor body: This object determines whether auto resynchronization is allowed. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_auto_resync" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_auto_resync`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_auto_resync`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setAutoResync'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_battery_params(self, system_id, body, **kwargs):
            """
            This procedure sets the battery parameters for the given battery.
            Documented return codes: ok, illegalParam, noHeap, volumeNotExist, tryAlternate, internalError, noVolumes. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_battery_params(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param BatteryParamsUpdateDescriptor body: A descriptor object that specifies the battery properties. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_battery_params" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_battery_params`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_battery_params`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setBatteryParams'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_cache_mirroring_protection_information(self, system_id, body, **kwargs):
            """
            This procedure allows checking of protection information of cache mirroring to be enabled or disabled, if this feature is supported. There is a capability enumeration that indicates whether or not this feature is supported.
            Documented return codes: ok. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_cache_mirroring_protection_information(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param CacheMirroringProtectionInformationDescriptor body: A CacheMirroringProtectionInformationDescriptor containing the arguments for the call. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_cache_mirroring_protection_information" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_cache_mirroring_protection_information`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_cache_mirroring_protection_information`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setCacheMirroringProtectionInformation'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_cluster_performance_limitation_values(self, system_id, body, **kwargs):
            """
            This procedure allows the user to limit the performance of a host cluster. The limitations that can be set are throughput (MB/s) and IOPs.
            Documented return codes: ok. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_cluster_performance_limitation_values(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param ClusterPerformanceLimitationValuesDescriptor body: The procedure takes as input a structure containing the limitations on the performance of the cluster. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_cluster_performance_limitation_values" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_cluster_performance_limitation_values`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_cluster_performance_limitation_values`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setClusterPerformanceLimitationValues'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_controller_nvsram(self, system_id, body, **kwargs):
            """
            This procedure is used to modify a portion of the controller's NVSRAM. Note that the NVSRAM data is changed only on the controller to which this request is directed.
            Documented return codes: ok, error, illegalParam, noHeap, nvramError, invalidRegionid. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_controller_nvsram(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param NVSRAMUpdateDescriptor body: An NVSRAMUpdateDescriptor object that specifies the region to be modified, the starting byte offset within the region, and the size and value of the new data to be stored into NVSRAM. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_controller_nvsram" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_controller_nvsram`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_controller_nvsram`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setControllerNVSRAM'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_controller_service_mode(self, system_id, body, **kwargs):
            """
            This procedure places a controller in Service Mode. It replaces the obsolete setControllerToPassive procedure. The command is serviced by the controller opposite to controllerRef.
            Documented return codes: ok, illegalParam, noHeap, tryAlternate, modesenseError. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_controller_service_mode(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str body: The value of the controller reference for the controller to be placed in service mode. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_controller_service_mode" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_controller_service_mode`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_controller_service_mode`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setControllerServiceMode'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_controller_time(self, system_id, body, **kwargs):
            """
            This procedure allows the client to set the clock of the controller to the specified value. Note that the clock value is only set on the controller to which this request is directed. If the client wishes to set the clock value on each controller, then an independent request of this form should be directed to each controller.
            Documented return codes: ok, illegalParam. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_controller_time(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param int body: A 64-bit integer value that represents the new clock value to be set on the controller. The integer specifies the time value as the number of seconds that have elapsed since 12:00AM GMT on January 1, 1970. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_controller_time" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_controller_time`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_controller_time`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setControllerTime'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_controller_to_active(self, system_id, body, **kwargs):
            """
            This procedure causes the specified controller to be transitioned into the active state. If the controller was previously active, no visible changes will occur as a result of this operation. If it was previously passive or in service mode, it will be made active. After this transition occurs, it will be possible to assign ownership of volume groups to the controller so that it may participate in standard I/O operations.
            Documented return codes: ok, error, illegalParam, noHeap, internalError, invalidRequest, iconFailure, cacheSyncFailure, invalidControllerref, modesenseError. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_controller_to_active(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str body: The value of the controller reference for the controller that is to be made active. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_controller_to_active" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_controller_to_active`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_controller_to_active`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setControllerToActive'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_controller_to_failed(self, system_id, body, **kwargs):
            """
            This procedure marks the specified controller as being failed. Furthermore, the alternate of the specified controller will force the failed controller into a reset state (if possible).
            Documented return codes: ok, error, illegalParam, noHeap, tryAlternate, internalError, invalidRequest, iconFailure, cacheSyncFailure, invalidControllerref, modesenseError, controllerInServiceMode. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_controller_to_failed(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str body: The value of the controller reference for the controller that is to be marked failed. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_controller_to_failed" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_controller_to_failed`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_controller_to_failed`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setControllerToFailed'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_controller_to_optimal(self, system_id, body, **kwargs):
            """
            This procedure causes the specified controller's state to be set to optimal. If the controller was previously in the failed state, it will be reactivated. If necessary, the alternate controller will also remove any forced reset signal being applied to the specified controller.
            Documented return codes: ok, error, illegalParam, noHeap, internalError, invalidRequest, iconFailure, cacheSyncFailure, invalidControllerref, modesenseError. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_controller_to_optimal(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str body: The value of the controller reference for the controller to be set to the optimal state. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_controller_to_optimal" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_controller_to_optimal`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_controller_to_optimal`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setControllerToOptimal'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_controller_to_passive(self, system_id, body, **kwargs):
            """
            This procedure causes the specified controller to be transitioned to the passive state. All volume groups owned by the controller will be transitioned to the alternate controller, which remains in the active state.
            Documented return codes: obsolete. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_controller_to_passive(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str body: The value of the controller reference for the controller that is to be made passive. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_controller_to_passive" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_controller_to_passive`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_controller_to_passive`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setControllerToPassive'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_disk_pool_priority(self, system_id, body, **kwargs):
            """
            This procedure will set the Disk Pool Reconstruction and Background Operation priorities.
            Documented return codes: ok. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_disk_pool_priority(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param DiskPoolPriorityUpdateDescriptor body: An object containing all of the attributes required to set priorities for a Disk Pool. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_disk_pool_priority" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_disk_pool_priority`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_disk_pool_priority`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setDiskPoolPriority'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_disk_pool_reserved_drive_count(self, system_id, body, **kwargs):
            """
            This procedure will set the Disk Pool Reserved Drive Count value.
            Documented return codes: ok. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_disk_pool_reserved_drive_count(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param DiskPoolReservedDriveCountUpdateDescriptor body: An object containing all of the attributes required to set a reserved drive count value on a disk pool. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_disk_pool_reserved_drive_count" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_disk_pool_reserved_drive_count`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_disk_pool_reserved_drive_count`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setDiskPoolReservedDriveCount'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_disk_pool_threshold(self, system_id, body, **kwargs):
            """
            This procedure will set the Disk Pool Utilization Threshold values.
            Documented return codes: ok, invalidCriticalThreshold. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_disk_pool_threshold(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param DiskPoolThresholdUpdateDescriptor body: An object containing all of the attributes required to set utilization threshold values for a Disk Pool. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_disk_pool_threshold" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_disk_pool_threshold`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_disk_pool_threshold`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setDiskPoolThreshold'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_disk_pool_to_complete(self, system_id, body, **kwargs):
            """
            This procedure forces the Disk Pool to a complete (optimal) state. This may be necessary if a drive is missing and the drive is not going to be replaced.
            Documented return codes: ok. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_disk_pool_to_complete(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str body: A reference to the Disk Pool to complete. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_disk_pool_to_complete" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_disk_pool_to_complete`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_disk_pool_to_complete`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setDiskPoolToComplete'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_disk_pool_user_label(self, system_id, body, **kwargs):
            """
            This procedure is used to set the user assigned label for the disk pool.
            Documented return codes: ok, illegalParam. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_disk_pool_user_label(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param VolumeGroupLabelUpdateDescriptor body: A DiskPoolLabelUpdateDescriptor structure that contains the user label and a reference to the volume group to update. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_disk_pool_user_label" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_disk_pool_user_label`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_disk_pool_user_label`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setDiskPoolUserLabel'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_drive_channel_state(self, system_id, body, **kwargs):
            """
            This procedure sets the drive channel state to either degraded or optimal.
            Documented return codes: ok. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_drive_channel_state(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param DriveChannelStateDescriptor body: This object contains information on how to request a drive channel state change from the array. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_drive_channel_state" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_drive_channel_state`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_drive_channel_state`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setDriveChannelState'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_drive_physical_security_id(self, system_id, body, **kwargs):
            """
            This procedure is used to set the Physical Security ID for a drive. The PSID is required in order to set a FIPS drive back to factory settings if the previous PSID is lost. In that case, the drive must be set back to factory settings in order to be used.
            Documented return codes: ok. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_drive_physical_security_id(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param DrivePhysicalSecurityIdDescriptor body: The input structure contains a reference to the drive and the Physical Security ID string. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_drive_physical_security_id" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_drive_physical_security_id`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_drive_physical_security_id`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setDrivePhysicalSecurityID'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_drive_temperature_polling_interval(self, system_id, body, **kwargs):
            """
            This procedure set the interval in minutes between automatic polls of drive temperatures. For interval > 0, automatic polling is enabled at the specified interval. For interval == 0, automatic polling is disabled. Each polling event will update the driveTemperature field in each Drive structure in the ObjectBundle.
            Documented return codes: ok. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_drive_temperature_polling_interval(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param int body: Polling interval in minutes. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_drive_temperature_polling_interval" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_drive_temperature_polling_interval`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_drive_temperature_polling_interval`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setDriveTemperaturePollingInterval'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_drive_to_failed(self, system_id, body, **kwargs):
            """
            This procedure marks the specified drive as being failed. In general, this will also impact the operational state of the volume group to which the drive is assigned, plus all volumes defined on that volume group. The precise impact on the states of these other objects may vary, as it depends on the RAID level of the volumes, as well as the states of the other drives in the volume group.
            Documented return codes: ok, error, illegalParam, noHeap, driveNotExist, tryAlternate, invalidDriveref, databaseError, invalidDriveState, takeRecoveryActionsFirst. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_drive_to_failed(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str body: The value of the drive reference for the drive that is to be marked failed. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_drive_to_failed" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_drive_to_failed`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_drive_to_failed`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setDriveToFailed'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_drive_to_optimal(self, system_id, body, **kwargs):
            """
            This procedure forces the specified drive to the optimal state, including clearing the PFA condition for the drive, if any. Returning the drive to optimal may cause volumes on the associated volume group to be returned to the optimal state as well. This is a potentially dangerous operation, since a failed drive is usually accompanied by some form of parity inconsistency. Forcing a drive from the failed state to the optimal state may disrupt the controller's normal methods of providing availability in a degraded state, and may thus result in corrupted data being returned on ensuing data transfers to the host system.
            Documented return codes: ok, illegalParam, noHeap, tryAlternate, background, invalidDriveref, invalidDriveState. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_drive_to_optimal(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str body: The value of the drive reference for the drive to be returned to the optimal state. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_drive_to_optimal" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_drive_to_optimal`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_drive_to_optimal`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setDriveToOptimal'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_external_kms_parameters(self, system_id, body, **kwargs):
            """
            Sets parameters necessary to communicate with an external key management server.
            Documented return codes: ok. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_external_kms_parameters(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param ExternalKMSParametersSetDescriptor body:  (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_external_kms_parameters" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_external_kms_parameters`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_external_kms_parameters`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setExternalKMSParameters'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_flash_cache_params(self, system_id, body, **kwargs):
            """
            This procedure sets the parameters on a given flash cache.
            Documented return codes: ok, illegalParam, noHeap, internalError, flashcacheInvalidConfigType, notFlashcacheVol, flashcacheDeleted, flashcacheFailed, flashcacheDegradedState. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_flash_cache_params(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param FlashCacheParamsUpdateDescriptor body: A flash cache reference, configuration type, and whether or not flash cache should be enabled on new volumes. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_flash_cache_params" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_flash_cache_params`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_flash_cache_params`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setFlashCacheParams'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_function_state(self, system_id, body, **kwargs):
            """
            This procedure is used to get the state of a function, enable or disable the function, or revert the function back to its default value.
            Documented return codes: ok. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_function_state(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param FunctionStateDescriptor body: The function ID and the action to be performed. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: FunctionStateReturned
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_function_state" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_function_state`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_function_state`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setFunctionState'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='FunctionStateReturned',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_high_resolution_sampling(self, system_id, body, **kwargs):
            """
            This procedure enables or disables high resolution statistics gathering.
            Documented return codes: ok. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_high_resolution_sampling(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param HighResolutionRequestDescriptor body: None. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: HighResolutionReturned
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_high_resolution_sampling" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_high_resolution_sampling`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_high_resolution_sampling`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setHighResolutionSampling'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='HighResolutionReturned',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_host_interface_params(self, system_id, body, **kwargs):
            """
            This procedure updates the I/O interface parameters for the controller to which the request is directed.
            Documented return codes: ok, error, noHeap, tryAlternate, nvramError, invalidControllerref, invalidFibreid. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_host_interface_params(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param InterfaceUpdateDescriptor body: An InterfaceUpdateDescriptor object that provides new values for the host I/O interface parameters. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_host_interface_params" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_host_interface_params`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_host_interface_params`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setHostInterfaceParams'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_host_port_properties(self, system_id, body, **kwargs):
            """
            This procedure sets selected HostPort properties, as specified by the input argument. It is a replacement for the deprecated moveHostPort, renameHostPort.
            Documented return codes: ok, requestFailedDueToPiRestrictions. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_host_port_properties(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param HostPortPropertiesUpdateDescriptor body: A HostPortPropertiesUpdateDescriptor structure which indicates the affected host port, which properties to set, and what values to set for them. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_host_port_properties" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_host_port_properties`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_host_port_properties`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setHostPortProperties'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_host_port_type(self, system_id, body, **kwargs):
            """
            Changes the \"host port type\" attribute of a given HostPort object. Changing an individual host port type will cause all host port types to be changed if SPM is not enabled. This procedure does not apply to iSCSI; for iSCSI, the host type is set at the host level.
            Documented return codes: ok, illegalParam, partNodeNonexistent. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_host_port_type(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param HostPortTypeUpdateDescriptor body: A HostPortTypeUpdateDescriptor object that identifies the HostPort to be modified, and also provides the new type index value that specifies the type of the host port. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_host_port_type" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_host_port_type`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_host_port_type`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setHostPortType'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_host_ports_attributes(self, system_id, body, **kwargs):
            """
            This procedure sets selected HostPorts attributes, as specified by the input argument. It is meant to operate on a group of ports, for example all the ports on a host interface card or base board.
            Documented return codes: ok. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_host_ports_attributes(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param HostPortsAttributesUpdateDescriptor body: A HostPortsAttributesUpdateDescriptor structure containing the arguments for the procedure call. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_host_ports_attributes" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_host_ports_attributes`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_host_ports_attributes`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setHostPortsAttributes'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_host_properties(self, system_id, body, **kwargs):
            """
            This procedure sets selected host properties as indicated by the input argument. It is a replacement for the deprecated moveHost, renameHost.
            Documented return codes: ok. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_host_properties(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param HostPropertiesUpdateDescriptor body: A HostPropertiesUpdateDescriptor, indicating the affected Host, which properties to set, and what values to set them to. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_host_properties" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_host_properties`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_host_properties`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setHostProperties'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_host_specific_nvsram(self, system_id, body, **kwargs):
            """
            This procedure updates the NVSRAM for the Host Specific region.
            Documented return codes: ok, error, illegalParam, noHeap, nvramError, invalidRegionid, invalidHostTypeIndex. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_host_specific_nvsram(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param HostSpecificNVSRAMUpdateDescriptor body: A HostSpecificNVSRAMUpdateDescriptor object that specifies the region ID (in this case 0xF2), the host index for a specific host, the starting offset within the region, the number of bytes, and the values to be written. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_host_specific_nvsram" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_host_specific_nvsram`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_host_specific_nvsram`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setHostSpecificNVSRAM'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_ib_statistics_baseline(self, system_id, **kwargs):
            """
            This procedure, from the client's perspective, resets the InfiniBand baselined statistical counters to zero. It is a logical reset in the sense that the raw counts maintained in hardware and firmware are not actually reset; instead the firmware makes a snapshot of the current counter values and uses that to report deltas in counts when the statistics are fetched. The new baseline time is applied to both controllers, so that their counts are in sync with one another. If one controller resets without the other resetting, the counters become effectively out of sync and the client is made aware of this fact by the timestamp data reported along with the statistics.
            Documented return codes: ok. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_ib_statistics_baseline(system_id, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_ib_statistics_baseline" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_ib_statistics_baseline`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setIbStatisticsBaseline'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_initiator_properties(self, system_id, body, **kwargs):
            """
            This procedure sets selected Initiator properties as indicated by the input argument.
            Documented return codes: ok, invalidAuthMethod, invalidSecret, secretAlreadyInUse, requestFailedDueToPiRestrictions. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_initiator_properties(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param InitiatorPropertiesUpdateDescriptor body: An InitiatorPropertiesUpdateDescriptor, indicating which Initiator properties to set and what values to set them to. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_initiator_properties" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_initiator_properties`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_initiator_properties`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setInitiatorProperties'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_iscsi_entity_properties(self, system_id, body, **kwargs):
            """
            This procedure sets selected iSCSI entity properties for the storage array as indicated by the input argument.
            Documented return codes: ok, isnsDhcpNotSupported. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_iscsi_entity_properties(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param IscsiEntityPropertiesUpdateDescriptor body: An IscsiEntityPropertiesUpdateDescriptor, indicating which iSCSI entity properties to set and what values to set them to. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_iscsi_entity_properties" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_iscsi_entity_properties`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_iscsi_entity_properties`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setIscsiEntityProperties'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_iscsi_interface_properties(self, system_id, body, **kwargs):
            """
            This procedure sets selected properties of a controller iSCSI interface, as indicated by the input argument.
            Documented return codes: ok, invalidInterfaceref, duplicateIscsiIpAddress, portSpeedConflict. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_iscsi_interface_properties(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param IscsiInterfacePropertiesUpdateDescriptor body: An IscsiInterfacePropertiesUpdateDescriptor, indicating the affected iSCSI interface, which properties to set, and what values to set them to. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_iscsi_interface_properties" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_iscsi_interface_properties`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_iscsi_interface_properties`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setIscsiInterfaceProperties'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_iscsi_statistics_baseline(self, system_id, **kwargs):
            """
            This procedure, from the client's perspective, resets the iSCSI statistical counters to zero. It is a logical reset in the sense that the raw counts maintained in hardware and firmware are not actually reset; instead the firmware makes a snapshot of the current counter values and uses that to report deltas in counts when the statistics are fetched. The new baseline time is applied to both controllers, so that their counts are in sync with one another. If one controller resets without the other resetting, the counters become effectively out of sync and the client is made aware of this fact by the timestamp data reported along with the statistics.
            Documented return codes: ok. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_iscsi_statistics_baseline(system_id, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_iscsi_statistics_baseline" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_iscsi_statistics_baseline`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setIscsiStatisticsBaseline'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_key_value_tag_mapping(self, system_id, body, **kwargs):
            """
            This procedure persists the association between the Key-Value tags and the Volumes (or Workloads). This procedure is used both for creating the initial mappings and to update. Each execution will remove any existing mappings and replace them with the mappings defined within the argument list.
            Documented return codes: ok. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_key_value_tag_mapping(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param KeyValueTagMappingSetDescriptorList body: The input is a list of mappings, each mapping consists of a Volume Reference and a Key-Value Pair reference. This method will create the initial associations and can be used to perform a replacement of those associations. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_key_value_tag_mapping" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_key_value_tag_mapping`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_key_value_tag_mapping`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setKeyValueTagMapping'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_lock_key(self, system_id, **kwargs):
            """
            This procedure is used in conjunction with the createLockKey procedure. This request may be issued to change the existing array lock key or to set an array lock key after a database adoption. The procedure commits the lock key generated by the createLockKey procedure to the drives and to the controllers.
            Documented return codes: ok, volumeNotOptimal, driveSecurityEnabledFailed, lockkeyFailed, noFdeDrives, keyDoesNotExist. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_lock_key(system_id, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_lock_key" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_lock_key`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setLockKey'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_network_parameters(self, system_id, body, **kwargs):
            """
            This procedure updates the network parameters.
            Documented return codes: ok, illegalParam, noHeap, tryAlternate, background. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_network_parameters(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param EthernetParamsUpdateDescriptor body: An EthernetParamsUpdateDescriptor object that specifies the controller IP address, the gateway IP address, the network subnet mask, and bootp enable/disable. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_network_parameters" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_network_parameters`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_network_parameters`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setNetworkParameters'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_nvme_host_interface_properties(self, system_id, body, **kwargs):
            """
            This procedure sets the properties of a NVMe over Fabrics Host Interface port.
            Documented return codes: ok, invalidInterfaceref, invalidIpAddress. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_nvme_host_interface_properties(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param NVMeInterfacePropertiesUpdateDescriptor body: NVMe over Fabrics Host Interface Properties (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_nvme_host_interface_properties" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_nvme_host_interface_properties`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_nvme_host_interface_properties`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setNVMeHostInterfaceProperties'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_nvmeof_statistics_baseline(self, system_id, **kwargs):
            """
            This procedure, from the client's perspective, resets the NVMe over Fabrics baselined statistical counters to zero. It is a logical reset in the sense that the raw counts maintained in hardware and firmware are not actually reset; instead the firmware makes a snapshot of the current counter values and uses that to report deltas in counts when the statistics are fetched. The new baseline time is applied to both storage controllers, so that their counts are in sync with one another. If one storage controller resets without the other resetting, the counters become effectively out of sync and the client is made aware of this fact by the timestamp data reported along with the statistics.
            Documented return codes: ok. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_nvmeof_statistics_baseline(system_id, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_nvmeof_statistics_baseline" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_nvmeof_statistics_baseline`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setNVMeoFStatisticsBaseline'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_pit_consistency_group_params(self, system_id, body, **kwargs):
            """
            This procedure will modify the attributes of a PiT consistency group.
            Documented return codes: ok, invalidRollbackPriority, invalidWarnThreshold, invalidPitConsistencyGroupLabel, invalidPitAutoDeleteLimit, invalidPitRepositoryFullPolicy, attributeFixedByArvm, pitGroupsFeatureDisabled. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_pit_consistency_group_params(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param PITConsistencyGroupParamsUpdateDescriptor body: Descriptor for the consistency group parameters to be updated. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_pit_consistency_group_params" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_pit_consistency_group_params`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_pit_consistency_group_params`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setPITConsistencyGroupParams'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_pit_consistency_group_view_params(self, system_id, body, **kwargs):
            """
            This procedure changes the user-settable parameters on a PITConsistencyGroupView.
            Documented return codes: ok. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_pit_consistency_group_view_params(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param PITConsistencyGroupViewParamsUpdateDescriptor body: An object containing the required user-settable attributes to set on a PiT Consistency Group View. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_pit_consistency_group_view_params" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_pit_consistency_group_view_params`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_pit_consistency_group_view_params`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setPITConsistencyGroupViewParams'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_pit_group_params(self, system_id, body, **kwargs):
            """
            This procedure will update the changeable parameters of a PiT Group.
            Documented return codes: ok, invalidBasevol, invalidRollbackPriority, invalidWarnThreshold, baseVolumeFailed, invalidPitGroupLabel, invalidPitAutoDeleteLimit, invalidPitRepositoryFullPolicy, invalidPitGroupRef, pitGroupInConsistencyGroup, attributeFixedByArvm, pitGroupsFeatureDisabled. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_pit_group_params(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param PITGroupParamsUpdateDescriptor body: Structure containing PiT parameter data. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_pit_group_params" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_pit_group_params`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_pit_group_params`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setPITGroupParams'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_pit_view_params(self, system_id, body, **kwargs):
            """
            This procedure will change the attributes of an existing PiT View.
            Documented return codes: ok, invalidWarnThreshold, pitViewInConsistencyGroup, pitGroupsFeatureDisabled. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_pit_view_params(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param PITViewParamsUpdateDescriptor body: Descriptor for the PiT View parameters to be updated. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_pit_view_params" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_pit_view_params`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_pit_view_params`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setPITViewParams'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_remote_target_properties(self, system_id, body, **kwargs):
            """
            This procedure sets the selected remote target properties as indicated by the input arguments.
            Documented return codes: ok, invalidAuthMethod, invalidSecret, secretAlreadyInUse. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_remote_target_properties(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param InitiatorTargetPropertiesUpdateDescriptor body: The updated settings for the new target initiator identified in the descriptor. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_remote_target_properties" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_remote_target_properties`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_remote_target_properties`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setRemoteTargetProperties'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_rlogin_capability(self, system_id, body, **kwargs):
            """
            This procedure allows rlogin to the controller to be enabled or disabled.
            Documented return codes: ok, illegalParam, noHeap, tryAlternate, background. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_rlogin_capability(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param RloginUpdateDescriptor body: The RloginUpdateDescriptor object is used for specifying the remote login capability of the controller (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_rlogin_capability" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_rlogin_capability`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_rlogin_capability`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setRloginCapability'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_rls_baseline(self, system_id, **kwargs):
            """
            This procedure sets the RLS baseline for all devices. The baseline is used to indicate the difference in error counts from when the baseline was established and the time at which the RLS data is requested.
            Documented return codes: ok, dstNotFibre. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_rls_baseline(system_id, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_rls_baseline" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_rls_baseline`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setRLSBaseline'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_sa_cache_params(self, system_id, body, **kwargs):
            """
            This procedure updates the cache parameters that are maintained on a per-array basis, across all controllers in the array.
            Documented return codes: ok, illegalParam, noHeap, volumeNotExist, volumeReconfiguring, tryAlternate, internalError, invalidCacheblksize, invalidFlushThreshold, invalidFlushAmount, noVolumes, controllerInServiceMode. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_sa_cache_params(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param SACacheParamsUpdateDescriptor body: An SACacheParamsUpdateDescriptor object that provides new values for the storage array cache management parameters. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_sa_cache_params" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_sa_cache_params`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_sa_cache_params`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setSACacheParams'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_sa_media_scan_period(self, system_id, body, **kwargs):
            """
            This procedure sets the target media scan period for background media scans to the value specified by the caller. The period is specified in units of days, and governs the approximate time required for a complete media scan of all volumes and drives in the system. The allowed period values can be determined by checking the appropriate fields of the FeatureParameters object for the storage array.
            Documented return codes: ok, error, illegalParam, tryAlternate, invalidScanperiod, controllerInServiceMode. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_sa_media_scan_period(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param int body: The desired media scan period, expressed in units of days. This value must be within the valid range of media scan periods supported the controller. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_sa_media_scan_period" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_sa_media_scan_period`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_sa_media_scan_period`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setSAMediaScanPeriod'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_sa_tray_positions(self, system_id, body, **kwargs):
            """
            This procedure is used by the client to request that the controller store (in nonvolatile storage) a TrayPositionList object that provides information about the relative physical positions of the storage array's trays within their enclosing rack(s) or container(s).
            Documented return codes: ok, error, illegalParam, noHeap, invalidTrayposLength. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_sa_tray_positions(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param TrayPositionList body: The TrayPositionList object to be stored for future retrieval. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_sa_tray_positions" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_sa_tray_positions`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_sa_tray_positions`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setSATrayPositions'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_sa_user_label(self, system_id, body, **kwargs):
            """
            This procedure is used by a client to modify the user-assigned label for the storage array. The label value is stored in non-volatile storage and returned to the client as part of the SAInfo object.
            Documented return codes: ok, error, illegalParam, invalidLabel. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_sa_user_label(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str body: The new user-assigned label for the storage array. This value is presented to the controller as a variable-length opaque byte array. However, the intention is that the byte array will contain a string value in double-byte character set format, with each two bytes representing one character value. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_sa_user_label" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_sa_user_label`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_sa_user_label`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setSAUserLabel'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_sa_view_password(self, system_id, body, **kwargs):
            """
            This procedure is used to set the initial view array password or change an existing view array password.
            Documented return codes: ok, authFailPassword, adminPasswordNotSet. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_sa_view_password(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param EncryptedPassword body:  (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_sa_view_password" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_sa_view_password`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_sa_view_password`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setSAViewPassword'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_simplex_mode(self, system_id, body, **kwargs):
            """
            This procedure is used to enable and disable Simplex mode.
            Documented return codes: ok, illegalParam, noHeap, tryAlternate, notImplemented, internalError, iconFailure, mirrorsPresent. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_simplex_mode(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str body: An enumeration object that describes the controller's redundancy mode. Use CTRL_REDUNDANCY_MODE_DUPLEX to set the redundancy mode to duplex and CTRL_REDUNDANCY_MODE_SIMPLEX to set the redundancy mode to simplex. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_simplex_mode" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_simplex_mode`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_simplex_mode`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setSimplexMode'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_snapshot_params(self, system_id, body, **kwargs):
            """
            This procedure is used to set various snapshot parameters including the repository warning threshold, the repository full policy, and the rollback operation priority.
            Documented return codes: ok, illegalParam, noHeap, tryAlternate, internalError, invalidVolumeref, snapNotAvailable, ghostVolume, invalidRollbackPriority, invalidWarnThreshold. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_snapshot_params(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param SnapshotParamsUpdateDescriptor body: A SnapshotParamsUpdateDescriptor object that specifies the various snapshot parameters. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_snapshot_params" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_snapshot_params`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_snapshot_params`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setSnapshotParams'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_snmp_community_params(self, system_id, body, **kwargs):
            """
            This procedure is used to modify an existing SNMP community.
            Documented return codes: ok. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_snmp_community_params(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param SNMPCommunityParamsUpdateDescriptorList body:  (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_snmp_community_params" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_snmp_community_params`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_snmp_community_params`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setSNMPCommunityParams'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_snmp_system_variables(self, system_id, body, **kwargs):
            """
            This procedure is used to set values of user-settable SNMP system variables.
            Documented return codes: ok. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_snmp_system_variables(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param SNMPSystemVariablesUpdateDescriptor body:  (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_snmp_system_variables" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_snmp_system_variables`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_snmp_system_variables`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setSNMPSystemVariables'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_snmp_trap_destination_params(self, system_id, body, **kwargs):
            """
            This procedure is used to modify an existing SNMP trap destination.
            Documented return codes: ok. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_snmp_trap_destination_params(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param SNMPTrapDestinationParamsUpdateDescriptorList body:  (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_snmp_trap_destination_params" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_snmp_trap_destination_params`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_snmp_trap_destination_params`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setSNMPTrapDestinationParams'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_storage_array_properties(self, system_id, body, **kwargs):
            """
            This procedure sets selected properties for the storage array that is the recipient of the call.
            Documented return codes: ok, illegalParam. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_storage_array_properties(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param StorageArrayPropertiesUpdateDescriptor body: A StorageArrayPropertiesUpdateDescriptor, indicating which properties to set and what values to set them to. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_storage_array_properties" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_storage_array_properties`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_storage_array_properties`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setStorageArrayProperties'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_target_properties(self, system_id, body, **kwargs):
            """
            This procedure sets selected Target properties as indicated by the input argument.
            Documented return codes: ok, invalidAuthMethod, invalidSecret, secretAlreadyInUse. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_target_properties(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param TargetPropertiesUpdateDescriptor body: A TargetPropertiesUpdateDescriptor, indicating the affected Target, which properties to set and what values to set them to. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_target_properties" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_target_properties`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_target_properties`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setTargetProperties'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_thin_volume_capacity_threshold(self, system_id, body, **kwargs):
            """
            This procedure will set a thin volume's capacity threshold warning level.
            Documented return codes: ok, internalError, invalidVolumeref, invalidWarnThreshold, illegalVolume, thresholdBelowUsedCapacity, thinVolumeParametersCannotBeModified. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_thin_volume_capacity_threshold(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param ThinVolumeThresholdUpdateDescriptor body: An object containing all of the required attributes for setting the capacity threshold warning level on a thin volume. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_thin_volume_capacity_threshold" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_thin_volume_capacity_threshold`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_thin_volume_capacity_threshold`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setThinVolumeCapacityThreshold'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_thin_volume_expansion_policy(self, system_id, body, **kwargs):
            """
            This procedure will set a thin volume's repository volume expansion policy.
            Documented return codes: ok, internalError, invalidVolumeref, illegalVolume, invalidExpansionPolicy, thinVolumeParametersCannotBeModified. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_thin_volume_expansion_policy(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param ThinVolumeExpansionPolicyUpdateDescriptor body: An object containing all of the required attributes needed to set the repository volume expansion policy for a thin volume. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_thin_volume_expansion_policy" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_thin_volume_expansion_policy`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_thin_volume_expansion_policy`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setThinVolumeExpansionPolicy'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_thin_volume_provisioned_capacity_quota(self, system_id, body, **kwargs):
            """
            This procedure will set a thin volume's provisioned capacity quota. This is the maximum value to which a thin volume's repository can grow.
            Documented return codes: ok, tryAlternate, internalError, invalidVolumeref, illegalVolume, invalidProvisionedCapacityQuota, invalidExpansionPolicy, invalidExpansionOperation, thinVolumeParametersCannotBeModified. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_thin_volume_provisioned_capacity_quota(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param ThinVolumeCapacityQuotaUpdateDescriptor body: An object containing all of the required attributes needed to set a thin volume's provisioned capacity quota. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_thin_volume_provisioned_capacity_quota" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_thin_volume_provisioned_capacity_quota`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_thin_volume_provisioned_capacity_quota`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setThinVolumeProvisionedCapacityQuota'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_thin_volume_reporting_policy(self, system_id, body, **kwargs):
            """
            This procedure changes the reporting policy of a thin volume. The reporting policy controls how a thin volume is reported to the host on the SCSI interface, i.e., as a thin volume that supports unmap commands or as a thick volume.
            Documented return codes: ok. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_thin_volume_reporting_policy(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param ThinVolumeReportingPolicyUpdateDescriptor body: A ThinVolumeReportingPolicyUpdateDescriptor structure containing the arguments for the procedure call. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_thin_volume_reporting_policy" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_thin_volume_reporting_policy`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_thin_volume_reporting_policy`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setThinVolumeReportingPolicy'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_tray_attributes(self, system_id, body, **kwargs):
            """
            This procedure sets arbitrary \"attribute data\" for a specified tray enclosure. Only the attributes specified in the argument are affected by this operation. The old data in an affected attribute is completely overwritten by the new attribute data.
            Documented return codes: ok, error, illegalParam, noHeap, invalidRequest, invalidRequestForEnclosure. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_tray_attributes(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param TrayAttributeUpdateDescriptor body: A TrayAttributeUpdateDescriptor indicating which tray is to receive the attribute data, along with a list of elements defining new attribute data to be written. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_tray_attributes" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_tray_attributes`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_tray_attributes`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setTrayAttributes'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_vol_xfer_alert_delay_period(self, system_id, body, **kwargs):
            """
            This procedure is used to set the delay period before a volume transfer alert is issued.
            Documented return codes: ok, error, illegalParam. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_vol_xfer_alert_delay_period(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param int body: The delay period in seconds from 0 to 3600. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_vol_xfer_alert_delay_period" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_vol_xfer_alert_delay_period`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_vol_xfer_alert_delay_period`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setVolXferAlertDelayPeriod'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_volume_cache_params(self, system_id, body, **kwargs):
            """
            This procedure updates the caching parameters for a particular volume as specified in the argument structure.
            Documented return codes: ok, error, illegalParam, noHeap, volumeNotExist, volumeReconfiguring, tryAlternate, internalError, invalidRequest, volumeFormatting, invalidVolumeref, volumeOffline, invalidCacheModifier, invalidReadahead, ghostVolume, cacheParametersNotChangeable. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_volume_cache_params(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param VolumeCacheParamsUpdateDescriptor body: A VolumeCacheParamsUpdateDescriptor object that specifies the volume whose cache parameters are to be updated, as well as the new parameter values themselves. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_volume_cache_params" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_volume_cache_params`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_volume_cache_params`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setVolumeCacheParams'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_volume_copy_params(self, system_id, body, **kwargs):
            """
            This procedure modifies the parameters of a volume copy.
            Documented return codes: ok, illegalParam, noHeap, volumeNotExist, internalError, invalidCopyPriority, invalidVolumecopyref, copyChangeFailed, copyGhostTarget, copyTargetReservation. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_volume_copy_params(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param VolumeCopyParamsUpdateDescriptor body: A VolumeCopyParamsUpdateDescriptor object that identifies the copy request and a set of attributes to be used to update the existing attributes. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_volume_copy_params" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_volume_copy_params`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_volume_copy_params`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setVolumeCopyParams'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_volume_group_to_offline(self, system_id, body, **kwargs):
            """
            This procedure marks a volume group offline. When this operation completes, all volumes in the volume group will be inaccessible for I/O operations. The drives that comprise the volume group can be removed from the storage array and, if desired, inserted into a different storage array.
            Documented return codes: ok, error, illegalParam, noHeap, driveNotUnassigned, volumeReconfiguring, tryAlternate, invalidRequest, invalidVolumeref, driveNotOptimal, driveRemoved, duplicateDrives, numdrivesAdditional, numdrivesGroup. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_volume_group_to_offline(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str body: The value of the volume group reference for the volume group to be placed offline. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_volume_group_to_offline" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_volume_group_to_offline`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_volume_group_to_offline`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setVolumeGroupToOffline'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_volume_group_to_online(self, system_id, body, **kwargs):
            """
            This procedure marks a volume group online. It is typically used when the drives assigned to a volume group have been transported from one storage array to another. After the last such drive has been inserted into the new storage array, it is necessary to manually mark the volume group online. When this operation completes, assuming the drives are all functioning properly, the volumes defined in the volume group will become accessible for I/O operations.
            Documented return codes: ok, error, illegalParam, noHeap, driveNotUnassigned, volumeReconfiguring, tryAlternate, invalidRequest, invalidVolumeref, driveNotOptimal, duplicateDrives, numdrivesAdditional, numdrivesGroup. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_volume_group_to_online(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str body: The value of the volume group reference for the volume group to be placed online. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_volume_group_to_online" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_volume_group_to_online`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_volume_group_to_online`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setVolumeGroupToOnline'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_volume_group_user_label(self, system_id, body, **kwargs):
            """
            Sets the user assigned label for the volume group specified in the VolumeGroupLabelUpdate structure.
            Documented return codes: ok, illegalParam. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_volume_group_user_label(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param VolumeGroupLabelUpdateDescriptor body: A VolumeGroupUserLabelUpdateDescriptor structure that contains the user label and a reference to the volume group to update. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_volume_group_user_label" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_volume_group_user_label`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_volume_group_user_label`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setVolumeGroupUserLabel'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_volume_list_online(self, system_id, body, **kwargs):
            """
            Places the set of volumes online.
            Documented return codes: ok, noHeap, volumeNotExist, internalError, invalidVolumeref, volumeNotOptimal. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_volume_list_online(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param AbstractVolRefList body: The list AbstractVolRefList of volumes to be placed online. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: VolumeListReturned
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_volume_list_online" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_volume_list_online`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_volume_list_online`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setVolumeListOnline'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='VolumeListReturned',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_volume_media_scan_params(self, system_id, body, **kwargs):
            """
            This procedure sets the media scan parameters for a particular volume. Each volume can be configured to either participate in media scans or not. Furthermore, if a volume is configured to participate, it can be further configured so that parity validation either occurs during the media scan or is skipped. The client uses this procedure to set these configuration options on a per-volume basis.
            Documented return codes: ok, error, illegalParam, noHeap, tryAlternate, invalidVolumeref, volumeOffline, ghostVolume, ssdMediaScanNotAllowed. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_volume_media_scan_params(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param VolumeMediaScanParamsUpdateDescriptor body: A VolumeMediaScanParamsUpdateDescriptor object that identifies the volume to be modified, as well as the media scan settings to be used for the volume. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_volume_media_scan_params" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_volume_media_scan_params`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_volume_media_scan_params`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setVolumeMediaScanParams'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_volume_params(self, system_id, body, **kwargs):
            """
            This procedure updates various parameters (outside of cache-related parameters) for a particular volume as specified in the argument structure.
            Documented return codes: ok, illegalParam, noHeap, volumeNotExist, tryAlternate, invalidRequest, invalidVolumeref, volumeOffline, invalidReconpriority, ghostVolume. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_volume_params(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param VolumeParamsUpdateDescriptor body: A VolumeParamsUpdateDescriptor object that specifies the volume whose parameters are to be updated, as well as the new parameter values themselves. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_volume_params" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_volume_params`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_volume_params`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setVolumeParams'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_volume_properties(self, system_id, body, **kwargs):
            """
            This procedure is used for setting new values of certain volume properties. It supports setting some properties while leaving others unchanged.
            Documented return codes: ok, error, illegalParam, noHeap, volumeNotExist, tryAlternate, internalError, invalidVolumeref, volumeOffline, volumeNotOptimal, invalidReconpriority, volumeNotConfigurable. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_volume_properties(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param VolumePropertiesUpdateDescriptor body: A VolumePropertiesUpdateDescriptor structure specifying which properties to change and what their new values should be. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_volume_properties" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_volume_properties`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_volume_properties`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setVolumeProperties'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_set_volume_user_label(self, system_id, body, **kwargs):
            """
            This procedure is used by a client to modify the user-assigned label for a volume. The label value is stored in non-volatile storage and returned to the client as part of the Volume or SnapshotVolume object when the client requests this information from the controller.
            Documented return codes: ok, error, illegalParam, noHeap, tryAlternate, invalidVolumeref, volumeOffline, invalidLabel, ghostVolume, volumeNotConfigurable. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_set_volume_user_label(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param VolumeLabelUpdateDescriptor body: A VolumeLabelUpdateDescriptor object that contains the new user-assigned label for the volume. This value is presented to the controller as a variable-length opaque byte array. However, the intention is that the byte array will contain a string value in double-byte character set format, with each two bytes representing one character value. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_set_volume_user_label" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_set_volume_user_label`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_set_volume_user_label`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/setVolumeUserLabel'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_start_base_controller_diagnostic(self, system_id, body, **kwargs):
            """
            Starts a base controller diagnostic test on the controller.
            Documented return codes: ok, illegalParam, diagInProgress, ctrlNotInServiceMode. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_start_base_controller_diagnostic(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param FruDiagDescriptor body: A structure containing the test type for the procedure call. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_start_base_controller_diagnostic" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_start_base_controller_diagnostic`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_start_base_controller_diagnostic`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/startBaseControllerDiagnostic'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_start_cache_backup_device_diagnostic(self, system_id, body, **kwargs):
            """
            Starts a cache backup device diagnostic test on the controller
            Documented return codes: ok, illegalParam, diagInProgress, ctrlNotInServiceMode, cacheBackupDevNotExist. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_start_cache_backup_device_diagnostic(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param FruDiagDescriptor body: A structure containing the test type and slot number for the procedure call. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_start_cache_backup_device_diagnostic" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_start_cache_backup_device_diagnostic`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_start_cache_backup_device_diagnostic`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/startCacheBackupDeviceDiagnostic'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_start_cache_memory_diagnostic(self, system_id, body, **kwargs):
            """
            Starts a cache memory diagnostic test on the controller
            Documented return codes: ok, illegalParam, diagInProgress, ctrlNotInServiceMode. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_start_cache_memory_diagnostic(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param FruDiagDescriptor body: A structure containing the test type for the controller. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_start_cache_memory_diagnostic" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_start_cache_memory_diagnostic`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_start_cache_memory_diagnostic`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/startCacheMemoryDiagnostic'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_start_cg_rollback(self, system_id, body, **kwargs):
            """
            This procedure will initiate a rollback on a specified PiT on all members of a consistency group (all members that have the specified PiT may not necessarily be all of them).
            Documented return codes: ok, repositoryOffline, pitGroupsFeatureDisabled. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_start_cg_rollback(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param PITConsistencyGroupRollbackStartDescriptor body: Descriptor for the consistency group rollback to be started. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_start_cg_rollback" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_start_cg_rollback`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_start_cg_rollback`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/startCGRollback'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_start_channel_diagnostics(self, system_id, body, **kwargs):
            """
            This procedure initiates a drive channel fault isolation diagnostic test. It returns a status code immediately and the requested tests proceed asynchronously. Any SYMbol request, other than getChannelDiagnosticsResults, cancelChannelDiagnostics, bindToController, and getSAData that is received while the test is running is rejected immediately. Since some SYMbol procedures do not provide a return code, the method of indicating the request rejection is specialized and entails the following: The RPC header that is returned to the client will consist of an RPC response of type \"reply message.\" The reply will have a general status of \"accepted,\" indicating the request was accepted by the controller for processing. The specific \"accepted request status\" value will be 0x80000001, which is an indication that the request could not be processed due to a diagnostic activity.
            Documented return codes: ok, invalidRequest, channelDiagsLockErr, channelDiagsNotQuiesced, channelDiagsAltCommFailed, channelDiagsChanSetupFailed, channelDiagsDeviceBypassFailed. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_start_channel_diagnostics(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param ChannelDiagnosticDescriptor body: A ChannelDiagnosticDescriptor structure that contains all of the arguments needed to define the test to perform. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_start_channel_diagnostics" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_start_channel_diagnostics`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_start_channel_diagnostics`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/startChannelDiagnostics'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_start_channel_identification(self, system_id, body, **kwargs):
            """
            This procedure causes visual indicators to be activated on the specified channel. The indicators will remain active until the stopIdentification procedure is invoked.
            Documented return codes: ok, error, illegalParam, noHeap, noChannel. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_start_channel_identification(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param int body: An integer value specifying the channel number. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_start_channel_identification" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_start_channel_identification`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_start_channel_identification`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/startChannelIdentification'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_start_disk_pool_expansion(self, system_id, body, **kwargs):
            """
            This procedure initiates a long-running operation to expand the capacity of a Disk Pool by adding one or more drives to it.
            Documented return codes: ok, exceedDiskPoolCapacity, exceedMaxVolumeCapacity. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_start_disk_pool_expansion(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param DiskPoolExpansionDescriptor body: A reference to the Disk Pool to expand and the drives to use for the expansion. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_start_disk_pool_expansion" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_start_disk_pool_expansion`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_start_disk_pool_expansion`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/startDiskPoolExpansion'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_start_disk_pool_reduction(self, system_id, body, **kwargs):
            """
            This procedure initiates a long-running operation to reduce the capacity of a Disk Pool by removing one or more drives from it.
            Documented return codes: ok, drivesNotAvailableForRemoval. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_start_disk_pool_reduction(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param DiskPoolReductionDescriptor body:  (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_start_disk_pool_reduction" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_start_disk_pool_reduction`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_start_disk_pool_reduction`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/startDiskPoolReduction'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_start_drive_firmware_download(self, system_id, body, **kwargs):
            """
            This procedure starts the parallel drive firmware download process.
            Documented return codes: ok, error, busy, illegalParam, noHeap, downloadNotPermitted, spawnError, downloadInProgress, sodInProgress, invalidDrives, invalidSetsize. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_start_drive_firmware_download(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param DriveFirmwareDownload body: This object contains the list of drives to download and an indicator of whether or not to perform the download keeping the volumes online. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: DriveFirmwareStatus
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_start_drive_firmware_download" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_start_drive_firmware_download`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_start_drive_firmware_download`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/startDriveFirmwareDownload'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='DriveFirmwareStatus',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_start_drive_identification(self, system_id, body, **kwargs):
            """
            This procedure causes visual indicators to be activated on the physical drives specified in the argument list to allow an end-user to visually identify the drives. The indicators will remain active until the stopIdentification procedure is invoked.
            Documented return codes: ok, error, illegalParam, noHeap. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_start_drive_identification(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param DriveRefList body: A list of drive reference objects that specifies the drives whose visual indicators are to be activated. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_start_drive_identification" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_start_drive_identification`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_start_drive_identification`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/startDriveIdentification'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_start_drive_reconstruction(self, system_id, body, **kwargs):
            """
            This procedure initiates the reconstruction of a failed drive in a degraded RAID volume. The procedure returns once the reconstruction has started. If the indicated failed drive has an integrated hot spare serving in its place, then this procedure will initiate the copyback from the hot spare to the failed drive.
            Documented return codes: ok, error, illegalParam, noHeap, volumeReconfiguring, tryAlternate, invalidRequest, invalidDriveref, invalidRaidlevel, reconstructionInProgress, copybackInProgress. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_start_drive_reconstruction(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str body: The value of the drive reference for the drive on which reconstruction is to begin. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_start_drive_reconstruction" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_start_drive_reconstruction`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_start_drive_reconstruction`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/startDriveReconstruction'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_start_flash_cache_analytics(self, system_id, body, **kwargs):
            """
            This procedure starts collecting analytics data for flash cache. It resets analytics counters and begins capturing cache data.
            Documented return codes: ok, error, illegalParam, internalError, invalidVolumeref, notFlashcacheVol. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_start_flash_cache_analytics(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str body:  (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_start_flash_cache_analytics" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_start_flash_cache_analytics`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_start_flash_cache_analytics`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/startFlashCacheAnalytics'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_start_host_card_diagnostic(self, system_id, body, **kwargs):
            """
            Starts a host card diagnostic test on the controller
            Documented return codes: ok, illegalParam, diagInProgress, ctrlNotInServiceMode. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_start_host_card_diagnostic(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param FruDiagDescriptor body: A structure containing the test type and slot number for the procedure call. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_start_host_card_diagnostic" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_start_host_card_diagnostic`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_start_host_card_diagnostic`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/startHostCardDiagnostic'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_start_performance_monitor(self, system_id, **kwargs):
            """
            This procedure returns the success of starting statistic data collection.
            Documented return codes: ok. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_start_performance_monitor(system_id, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_start_performance_monitor" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_start_performance_monitor`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/startPerformanceMonitor'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_start_pit_rollback(self, system_id, body, **kwargs):
            """
            This procedure will initiate a rollback on a specified list of PiTs. Note that this list could be a subset of a set of consistency group PiTs.
            Documented return codes: ok, repositoryOffline, invalidPitRef, pitGroupsFeatureDisabled. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_start_pit_rollback(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param PITRefList body: A list of references to PiTs for which to start the rollback. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_start_pit_rollback" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_start_pit_rollback`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_start_pit_rollback`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/startPITRollback'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_start_raw_data_restore(self, system_id, body, **kwargs):
            """
            starts a raw data restore operation.
            Documented return codes: ok, busy, noHeap, tryAlternate, rawdataTransferBadType, rawdataTransferAlreadyStarted, rawdataTransferReadError, rawdataTransferNoDrives, rawdataTransferInvalidImage, dbmDbSourceUnavailable, dbmRestoreSourceMismatch. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_start_raw_data_restore(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param RawDataRestoreStartDesc body: Specifies the controller ref, data transfer type and transfer-type-specific parameters for the restore operation. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: RawDataRestoreResult
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_start_raw_data_restore" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_start_raw_data_restore`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_start_raw_data_restore`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/startRawDataRestore'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='RawDataRestoreResult',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_start_raw_data_retrieve(self, system_id, body, **kwargs):
            """
            This procedure starts a raw data retrieval operation.
            Documented return codes: ok, busy, noHeap, invalidControllerref, rawdataTransferBadType, rawdataTransferAlreadyStarted, rawdataTransferNoDrives, dqRetrieveNothingToTransfer, dplCoreDumpInvalidTag, coredumpBackupInProgress. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_start_raw_data_retrieve(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param RawDataRetrieveStartDesc body: The controller ref and transfer-type-specific details of the retrieval. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: RawDataRetrieveStartResult
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_start_raw_data_retrieve" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_start_raw_data_retrieve`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_start_raw_data_retrieve`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/startRawDataRetrieve'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='RawDataRetrieveStartResult',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_start_sa_identification(self, system_id, **kwargs):
            """
            This procedure causes visual indicators to be activated on the physical storage array unit to allow an end-user to visually identify the storage array. The indicators will remain active until the stopIdentification procedure is invoked.
            Documented return codes: ok, noHeap. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_start_sa_identification(system_id, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_start_sa_identification" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_start_sa_identification`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/startSAIdentification'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_start_snapshot_rollback(self, system_id, body, **kwargs):
            """
            This procedure is used to initiate a snapshot rollback (to base) on one or more snapshots.
            Documented return codes: ok, rollbackStartFailure. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_start_snapshot_rollback(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param SnapshotRefList body: A reference to the snapshots to roll back. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_start_snapshot_rollback" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_start_snapshot_rollback`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_start_snapshot_rollback`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/startSnapshotRollback'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_start_ssd_block_allocation_scan(self, system_id, body, **kwargs):
            """
            This procedure starts a slow background scan of the free or both free and allocated blocks for the requested devices. Background scan is long running and can be checked using the getSSDBlockAllocationScanStatus procedure.
            Documented return codes: ok. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_start_ssd_block_allocation_scan(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param StartSSDBlockAllocationScanDescriptor body: A StartSSDBlockAllocationScanDescriptor specifying details of the start request. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_start_ssd_block_allocation_scan" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_start_ssd_block_allocation_scan`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_start_ssd_block_allocation_scan`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/startSSDBlockAllocationScan'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_start_sync_mirror(self, system_id, body, **kwargs):
            """
            This procedure starts the synchronization process on a mirror.
            Documented return codes: ok, illegalParam, volumeNotExist, tryAlternate, internalError, invalidVolumeref, ghostVolume, invalidMirrorvol, mirrorVolNotPrimary. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_start_sync_mirror(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str body: The value of the mirror that is to be synchronized. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_start_sync_mirror" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_start_sync_mirror`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_start_sync_mirror`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/startSyncMirror'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_start_tray_identification(self, system_id, body, **kwargs):
            """
            This procedure causes visual indicators to be activated on the physical storage array unit to allow an end-user to visually identify the trays. The indicators will remain active until the stopIdentification procedure is invoked.
            Documented return codes: ok, invalidTrayref. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_start_tray_identification(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param TrayRefList body: A list of the trays. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_start_tray_identification" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_start_tray_identification`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_start_tray_identification`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/startTrayIdentification'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_start_volume_copy(self, system_id, body, **kwargs):
            """
            This procedure takes as its input a VolumeCopyRef and causes a copy operation to be initiated from the beginning of the Source volume. A failure status is returned if the Source and Target volumes do not meet compatibility requirements.
            Documented return codes: ok, illegalParam, noHeap, volumeNotExist, tryAlternate, internalError, iconFailure, invalidVolumecopyref, copyActive, copyIncompatibleSource, copyIncompatibleTarget, copyGhostSource, copyGhostTarget, copyInvalidSourceState, copyInvalidTargetState, copySourceReconfig, copyTargetReconfig, copyTargetTooSmall, copyTargetLimit, copySourceReservation, copySourceFormat, copyTargetFormat, copyStartFailed, copySourceZeroCapacity, copyApptagMismatch. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_start_volume_copy(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str body: A descriptor object that identifies the volumes to perform the copy operation. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_start_volume_copy" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_start_volume_copy`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_start_volume_copy`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/startVolumeCopy'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_start_volume_expansion(self, system_id, body, **kwargs):
            """
            This procedure checks to make sure the additional capacity is available and then starts a DVE or DCE/DVE operation.
            Documented return codes: ok, error, illegalParam, noHeap, driveNotUnassigned, volumeReconfiguring, tryAlternate, internalError, invalidRequest, volumeFormatting, invalidVolumeref, invalidDriveref, volumeOffline, volumeNotOptimal, invalidExpansionList, driveNotOptimal, duplicateDrives, numdrivesAdditional, numdrivesGroup, driveTooSmall, ghostVolume, cannotReconfigure, drivesDacstoresOverlap, volumeHasAsyncMirror, insufficientCache. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_start_volume_expansion(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param VolumeExpansionDescriptor body: A VolumeExpansionDescriptor object that identifies the volume to be expanded, plus the drive or drives to be added to the volume. All drives specified for this operation must be in the unassigned state initially. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_start_volume_expansion" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_start_volume_expansion`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_start_volume_expansion`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/startVolumeExpansion'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_start_volume_format(self, system_id, body, **kwargs):
            """
            This procedure causes the specified volume to be formatted. All data that is currently present on the volume will be irretrievably lost as a result of this operation. Once a format operation starts, the volume's action field will be changed to VOL_ACTION_INITIALIZING; the getVolumeActionProgress procedure can then be used to monitor the progress of the operation. Volume format operations are typically required only when reviving a volume that has been marked failed for some reason. Newly-created volumes need not be explicitly formatted using this procedure.
            Documented return codes: ok, busy, illegalParam, noHeap, volumeNotExist, volumeReconfiguring, tryAlternate, reservationConflict, internalError, invalidRequest, invalidVolumeref, volumeOffline, ghostVolume, cannotFormatVolume. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_start_volume_format(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str body: The value of the volume reference for the volume that is to be reformatted. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_start_volume_format" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_start_volume_format`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_start_volume_format`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/startVolumeFormat'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_start_volume_group_defrag(self, system_id, body, **kwargs):
            """
            This procedure initiates a long-running operation to defragment a volume group by shifting the physical storage location of each volume in the volume group to eliminate any free extents that reside between defined volumes. Note that all volumes remain fully accessible and online during this transition. While the operation is in progress, the client can make calls to the getVolumeActionProgress procedure to determine how much progress has been made in completing the operation for each affected volume. The end result of a volume group defragment operation is that free extents that existed between defined volumes will be eliminated, and a single large free extent (if any) will appear at the end of the volume group.
            Documented return codes: ok, error, illegalParam, noHeap, driveNotUnassigned, volumeReconfiguring, tryAlternate, invalidRequest, volumeFormatting, invalidVolumegroupref, volumeOffline, volumeNotOptimal, driveNotOptimal, duplicateDrives, numdrivesAdditional, numdrivesGroup, driveTooSmall, cannotReconfigure, drivesDacstoresOverlap, reconfigLogSpaceError, insufficientCache. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_start_volume_group_defrag(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str body: The value of a volume group reference for the volume group that is to be defragmented. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_start_volume_group_defrag" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_start_volume_group_defrag`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_start_volume_group_defrag`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/startVolumeGroupDefrag'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_start_volume_group_expansion(self, system_id, body, **kwargs):
            """
            This procedure initiates a long-running operation to expand the capacity of a volume group by adding one or more drives to it. An expansion of this form requires that the controller transparently move the data of existing volumes within the volume group; volumes remain fully accessible and online during this transition. While the operation is in progress, the client can make calls to the getVolumeActionProgress procedure to determine how much progress has been made in completing the operation for each affected volume. The end result of a volume group expansion is the appearance of a new (or enlarged) free extent at the end of the volume group. The free extent can then be used to create new volumes as desired by the user.
            Documented return codes: ok, error, illegalParam, noHeap, driveNotUnassigned, volumeReconfiguring, tryAlternate, invalidRequest, volumeFormatting, invalidVolumegroupref, invalidDriveref, volumeOffline, volumeNotOptimal, invalidExpansionList, driveNotOptimal, duplicateDrives, numdrivesAdditional, numdrivesGroup, driveTooSmall, cannotReconfigure, drivesDacstoresOverlap, volumeHasAsyncMirror, reconfigLogSpaceError, insufficientCache. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_start_volume_group_expansion(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param VolumeGroupExpansionDescriptor body: A VolumeGroupExpansionDescriptor object that identifies the volume group to be expanded, plus the drive or drives to be added to the volume group. All drives specified for this operation must be in the unassigned state initially. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_start_volume_group_expansion" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_start_volume_group_expansion`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_start_volume_group_expansion`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/startVolumeGroupExpansion'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_start_volume_parity_check(self, system_id, body, **kwargs):
            """
            Initiates an explicit parity check operation. This is a background task that verifies the correctness of all parity/redundancy data for the volume. Only one such operation may be active at any time on a given controller. After initiating the operation with this procedure, the operation's progress can be checked via the getParityCheckProgress procedure. This procedure is deprecated. The scanVolume procedure should be used instead.
            Documented return codes: ok, noHeap, tryAlternate, background, invalidVolumeref, volumeOffline, volumeNotOptimal, invalidRaidlevel, parityScanInProgress, ghostVolume. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_start_volume_parity_check(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str body: The AbstractVolRef of the volume on which the operation is to be performed. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_start_volume_parity_check" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_start_volume_parity_check`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_start_volume_parity_check`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/startVolumeParityCheck'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_start_volume_raid_migration(self, system_id, body, **kwargs):
            """
            This procedure initiates a long-running operation to change the RAID level of a volume group (and thus all volumes in the volume group) from one supported value to another. While the operation is in progress, the client can make calls to the getVolumeActionProgress procedure to determine how much progress has been made in completing the operation for each affected volume.
            Documented return codes: ok, error, illegalParam, noHeap, driveNotUnassigned, volumeReconfiguring, tryAlternate, invalidRequest, volumeFormatting, invalidVolumegroupref, volumeOffline, invalidRaidlevel, driveNotOptimal, duplicateDrives, numdrivesAdditional, numdrivesGroup, cannotReconfigure, drivesDacstoresOverlap, insufficientCache. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_start_volume_raid_migration(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param VolumeRAIDMigrationDescriptor body: A VolumeRAIDMigrationDescriptor object that identifies the volume group and the new RAID level to be used. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_start_volume_raid_migration" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_start_volume_raid_migration`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_start_volume_raid_migration`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/startVolumeRAIDMigration'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_start_volume_segment_sizing(self, system_id, body, **kwargs):
            """
            This procedure initiates a long-running operation to change the segment size (i.e. stripe depth) of a volume from one supported value to another. While the operation is in progress, the client can make calls to the getVolumeActionProgress procedure to determine how much progress has been made in completing the operation.
            Documented return codes: ok, error, illegalParam, noHeap, volumeReconfiguring, tryAlternate, reservationConflict, invalidRequest, volumeFormatting, invalidVolumeref, volumeOffline, invalidSegmentsize, ghostVolume, cannotReconfigure, drivesDacstoresOverlap, insufficientCache. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_start_volume_segment_sizing(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param VolumeSegmentSizingDescriptor body: A VolumeSegmentSizingDescriptor object that identifies the volume and the new segment size to be used. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_start_volume_segment_sizing" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_start_volume_segment_sizing`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_start_volume_segment_sizing`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/startVolumeSegmentSizing'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_state_capture(self, system_id, body, **kwargs):
            """
            This procedure is used to capture current controller conditions as specified by the function being passed through the variable string input.
            Documented return codes: ok. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_state_capture(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str body: A character string indicating the function being called and up to 2 function arguments. The individual elements of the string are separated by commas. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: ReturnCodeWithOpaqueData
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_state_capture" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_state_capture`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_state_capture`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/stateCapture'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='ReturnCodeWithOpaqueData',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_stop_channel_diagnostics(self, system_id, **kwargs):
            """
            This procedure cancels a running channel diagnostic test sequence that was initiated by the startChannelDiagnostics procedure. It is possible to retrieve the (partial) results of a canceled test by calling getChannelDiagnosticsResults.
            Documented return codes: ok. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_stop_channel_diagnostics(system_id, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_stop_channel_diagnostics" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_stop_channel_diagnostics`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/stopChannelDiagnostics'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_stop_drive_firmware_download(self, system_id, **kwargs):
            """
            This procedure stops the parallel drive firmware download process.
            Documented return codes: ok, error, illegalParam, tryAlternate, invalidRequest. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_stop_drive_firmware_download(system_id, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_stop_drive_firmware_download" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_stop_drive_firmware_download`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/stopDriveFirmwareDownload'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_stop_flash_cache_analytics(self, system_id, body, **kwargs):
            """
            This procedure stops the collection of analytics data for flash cache. It disables the collection of cache hits.
            Documented return codes: ok, error, illegalParam, internalError, invalidVolumeref, notFlashcacheVol. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_stop_flash_cache_analytics(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str body:  (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_stop_flash_cache_analytics" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_stop_flash_cache_analytics`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_stop_flash_cache_analytics`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/stopFlashCacheAnalytics'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_stop_identification(self, system_id, **kwargs):
            """
            This procedure cancels the effects of any prior startDriveIdentification, startSAIdentification, startChannelIdentification and/or startTrayIdentification operations by deactivating all visual indicators.
            Documented return codes: ok. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_stop_identification(system_id, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_stop_identification" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_stop_identification`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/stopIdentification'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_stop_iscsi_session(self, system_id, body, **kwargs):
            """
            This procedure forcibly terminates an iSCSI session.
            Documented return codes: ok. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_stop_iscsi_session(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param int body: An TargetSessionIdentifyingHandle object indicating which session to terminate. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_stop_iscsi_session" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_stop_iscsi_session`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_stop_iscsi_session`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/stopIscsiSession'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_stop_performance_monitor(self, system_id, **kwargs):
            """
            This procedure returns the success of stopping statistic data collection.
            Documented return codes: ok. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_stop_performance_monitor(system_id, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_stop_performance_monitor" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_stop_performance_monitor`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/stopPerformanceMonitor'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_stop_pit_consistency_group_view(self, system_id, body, **kwargs):
            """
            This procedure will stop the specified PITConsistencyGroupView (and thus all of its associated member views).
            Documented return codes: ok, operationFailedVolumeCopyClone. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_stop_pit_consistency_group_view(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param PITConsistencyGroupViewStopDescriptor body: An object containing all of the attributes required to stop a PiT Consistency Group View. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_stop_pit_consistency_group_view" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_stop_pit_consistency_group_view`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_stop_pit_consistency_group_view`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/stopPITConsistencyGroupView'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_stop_pit_view(self, system_id, body, **kwargs):
            """
            This procedure will stop an existing PiT View.
            Documented return codes: ok, operationFailedVolumeCopyClone. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_stop_pit_view(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str body: Reference to PiT View to be stopped. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_stop_pit_view" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_stop_pit_view`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_stop_pit_view`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/stopPITView'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_stop_volume_copy(self, system_id, body, **kwargs):
            """
            This procedure halts the active copy.
            Documented return codes: ok, illegalParam, noHeap, volumeNotExist, tryAlternate, internalError, invalidVolumecopyref, copyInactive, copyStopFailed. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_stop_volume_copy(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str body: The VolumeCopyRef object to halt the active copy. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_stop_volume_copy" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_stop_volume_copy`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_stop_volume_copy`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/stopVolumeCopy'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_suspend_async_mirror_group(self, system_id, body, **kwargs):
            """
            This procedure will suspend an Async Mirror Group.
            Documented return codes: ok, arvmGroupDoesNotExist, arvmRecoveryPointDeletionRequired, arvmGroupNotPrimary, arvmMemberFailed, arvmSuspendFailure, arvmOrphanGroup, remoteInternalError, arvmRemoteGroupDoesNotExist, remoteDatabaseError, arvmRemoteSuspendFailure. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_suspend_async_mirror_group(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param AsyncMirrorGroupSuspendDescriptor body: A descriptor that lists the AMG on which the synchronization is to be suspended. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: AsyncMirrorGroupActionResult
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_suspend_async_mirror_group" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_suspend_async_mirror_group`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_suspend_async_mirror_group`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/suspendAsyncMirrorGroup'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='AsyncMirrorGroupActionResult',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_suspend_consistency_group(self, system_id, body, **kwargs):
            """
            This procedure suspends the communications for all mirrors in a Write Consistency group with a specified group number.
            Documented return codes: ok, noHeap, internalError, iconFailure, rvmQuiescenceInProgress, legacyRvmAsyncModeUnsupported. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_suspend_consistency_group(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str body: This object contains information about the write consistency group object. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_suspend_consistency_group" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_suspend_consistency_group`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_suspend_consistency_group`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/suspendConsistencyGroup'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_suspend_flash_cache(self, system_id, body, **kwargs):
            """
            This procedure suspends caching on the specified flash cache.
            Documented return codes: ok, error, illegalParam, noHeap, volumeNotExist, internalError, invalidVolumeref, flashcacheAlreadySuspended, notFlashcacheVol, flashcacheDeleted. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_suspend_flash_cache(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str body: The flash cache reference. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_suspend_flash_cache" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_suspend_flash_cache`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_suspend_flash_cache`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/suspendFlashCache'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_suspend_mirror(self, system_id, body, **kwargs):
            """
            This procedure suspends the communication between a mirror pair.
            Documented return codes: ok, illegalParam, noHeap, tryAlternate, internalError, iconFailure, invalidVolumeref, ghostVolume, invalidMirrorvol, rvmVersionMismatch, rvmOperNotAllowedOnSec, mirrorAlreadySuspended. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_suspend_mirror(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str body: This object contains information identifying the Mirror Proxy Volume to be removed. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_suspend_mirror" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_suspend_mirror`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_suspend_mirror`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/suspendMirror'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_suspend_mirror_list(self, system_id, body, **kwargs):
            """
            This procedure suspends the communication between all mirrored pairs specified in the MirrorVolumeList.
            Documented return codes: ok, noHeap, internalError, iconFailure, rvmQuiescenceInProgress. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_suspend_mirror_list(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param MirrorVolumeList body: This object contains information identifying the list of Mirror Volumes to suspend. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: str
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_suspend_mirror_list" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_suspend_mirror_list`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_suspend_mirror_list`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/suspendMirrorList'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='str',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_synchronize_async_mirror_group(self, system_id, body, **kwargs):
            """
            This procedure will start a manual resynchronization on an Async Mirror Group.
            Documented return codes: ok, arvmGroupDoesNotExist, arvmRecoveryPointDeletionRequired, arvmGroupNotPrimary, arvmSynchronizeFailure, arvmInvalidAmgRequestWhileSuspended, arvmManualSyncAlreadyInProgress, arvmManualSyncRetryTooSoon, arvmOrphanGroup, remoteInternalError, arvmRemoteGroupDoesNotExist, remoteDatabaseError, arvmRemoteSynchronizeFailure, arvmExpansionSynchronizationInProgress. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_synchronize_async_mirror_group(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param AsyncMirrorGroupSynchronizeDescriptor body: A reference to the Asynchronous Mirror Group to synchronize. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: AsyncMirrorGroupActionResult
                     If the method is called asynchronously,
                     returns the request thread.
            :raises: ValueError
                       If the required params are not provided or if the response data format is unknown.
                     TypeError:
                        When the data type of response data is different from what we are expecting
                     ApiException:
                        Occurs when we get a HTTP error code (422 and above).

            """

            all_params = ['system_id', 'body', 'controller', 'verbose_error_response']
            all_params.append('callback')

            params = locals()
            for key, val in iteritems(params['kwargs']):
                if key not in all_params:
                    raise TypeError(
                        "Got an unexpected keyword argument '%s'"
                        " to method symbol_synchronize_async_mirror_group" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_synchronize_async_mirror_group`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_synchronize_async_mirror_group`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/synchronizeAsyncMirrorGroup'.replace('{format}', 'json')
            path_params = {}
    
            if 'system_id' in params:
                path_params['system-id'] = params['system_id']
    

            query_params = {}
    
            if 'controller' in params:
                query_params['controller'] = params['controller']
    
            if 'verbose_error_response' in params:
                query_params['verboseErrorResponse'] = params['verbose_error_response']
    

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
                                                response_type='AsyncMirrorGroupActionResult',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    









