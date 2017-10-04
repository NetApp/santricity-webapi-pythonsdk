#!/usr/bin/env python
# coding: utf-8

"""
EApi.py

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


class EApi(object):

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient(context_path='/devmgr/v2')
            self.api_client = config.api_client
    
    
    def symbol_enable_asup(self, system_id, **kwargs):
            """
            This procedure is used to enable Autosupport.
            Documented return codes: ok, notImplemented. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_enable_asup(system_id, callback=callback_function)
    
    

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
                        " to method symbol_enable_asup" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_enable_asup`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/enableASUP'.replace('{format}', 'json')
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
    
    def symbol_enable_external_kms(self, system_id, body, **kwargs):
            """
            Enables external KMS.
            Documented return codes: ok, externalKmsEnabled, externalKmsFailed, externalKmsNotCompliant, externalKmsTimeout. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_enable_external_kms(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str body:  (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: WrappedLockKeyReturn
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
                        " to method symbol_enable_external_kms" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_enable_external_kms`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_enable_external_kms`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/enableExternalKMS'.replace('{format}', 'json')
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
                                                response_type='WrappedLockKeyReturn',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_enable_feature(self, system_id, body, **kwargs):
            """
            This procedure causes the \"premium\" features identified in the feature keys of the argument to be enabled.
            Documented return codes: ok, error, invalidSafeId, invalidSafeKey, invalidSafeCapability, invalidSafeVersion, perfTierSafeUpgradeDisabled, safeControllerNotSubjectToRaid6, premiumFeatureLimitExceedsMaximum, previouslyEnabledForEval, featureNotKeyable. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_enable_feature(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param FeatureKey body: A key for the \"premium\" feature to be enabled. This key must be obtained from an authorized source in order to be accepted by the array controller. (required)
    
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
                        " to method symbol_enable_feature" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_enable_feature`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_enable_feature`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/enableFeature'.replace('{format}', 'json')
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
    
    def symbol_enable_feature_evaluation(self, system_id, body, **kwargs):
            """
            Used to start an evaluation of a specified feature using the duration specified for the sub-model ID in the FBDT.
            Documented return codes: ok, noHeap, invalidSafeCapability, previouslyEnabledForEval, evalNotSupported, invalidCapability. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_enable_feature_evaluation(system_id, body, callback=callback_function)
    
    

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
                        " to method symbol_enable_feature_evaluation" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_enable_feature_evaluation`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_enable_feature_evaluation`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/enableFeatureEvaluation'.replace('{format}', 'json')
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
    
    def symbol_enable_flash_cache_volume(self, system_id, body, **kwargs):
            """
            This procedure creates a flash cache proxy linked to the referenced user RAID Volume and the flash cache High Level Volume. The flash cache attribute on the RAID Volume will be turned on.
            Documented return codes: ok, error, illegalParam, noHeap, volumeNotExist, volumeReconfiguring, tryAlternate, internalError, volumeFormatting, invalidVolumeref, volumeOffline, notFlashcacheVol, flashcacheDeleted, flashCacheInvalidBaseVol. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_enable_flash_cache_volume(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param VolumeFlashCacheDescriptor body: A reference to the user volume to link to the flash cache proxy, and a reference to the flash cache volume. (required)
    
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
                        " to method symbol_enable_flash_cache_volume" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_enable_flash_cache_volume`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_enable_flash_cache_volume`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/enableFlashCacheVolume'.replace('{format}', 'json')
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
    
    def symbol_establish_volume_copy(self, system_id, body, **kwargs):
            """
            This procedure establishes a volume copy.
            Documented return codes: ok, illegalParam, noHeap, tryAlternate, internalError, iconFailure, invalidCopyPriority, copyIncompatibleSource, copyIncompatibleTarget, copyGhostSource, copyGhostTarget, copyInvalidSourceRef, copyInvalidTargetRef, copyInvalidSourceState, copyInvalidTargetState, copySourceReconfig, copyTargetReconfig, copyTargetTooSmall, copyTargetLimit, maxVolumeCopysExceeded, copySourceReservation, copySourceFormat, copyTargetFormat, volcopyFeatureDisabled, copySourceZeroCapacity, copyApptagMismatch. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_establish_volume_copy(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param VolumeCopyCreationDescriptor body: The VolumeCopyCreationDescriptor for the volume copy. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: ReturnCodeWithRef
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
                        " to method symbol_establish_volume_copy" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_establish_volume_copy`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_establish_volume_copy`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/establishVolumeCopy'.replace('{format}', 'json')
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
                                                response_type='ReturnCodeWithRef',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_estimate_pit_rollback_repository_utilization(self, system_id, body, **kwargs):
            """
            This procedure will return the amount of repository capacity necessary to perform a rollback operation.
            Documented return codes: ok, invalidPitRef. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_estimate_pit_rollback_repository_utilization(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str body: A reference to a PiT (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: PITGroupRollbackUtilizationEstimateReturned
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
                        " to method symbol_estimate_pit_rollback_repository_utilization" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_estimate_pit_rollback_repository_utilization`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_estimate_pit_rollback_repository_utilization`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/estimatePITRollbackRepositoryUtilization'.replace('{format}', 'json')
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
                                                response_type='PITGroupRollbackUtilizationEstimateReturned',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_expand_concat_volume(self, system_id, body, **kwargs):
            """
            This procedure will expand a concatenated volume by adding another member RAID volume. Returns the ref for the new ConcatVolMember added.
            Documented return codes: ok, invalidProtection, invalidConcatVolMemberLabel, concatVolMemberTooSmall, concatMemberLimitExceeded, invalidMemberVol, memberVolMapped, invalidMemberVolState, incompatibleMemberVol, concatVolumeFailed, cannotExpandConcatMember, repositoryFull, insufficientExpansionSpace, invalidExpansionSize, incompatibleRepositorySecurity. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_expand_concat_volume(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param ConcatVolumeExpansionDescriptor body: A descriptor of the concat volume to be expanded. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: ReturnCodeWithRef
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
                        " to method symbol_expand_concat_volume" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_expand_concat_volume`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_expand_concat_volume`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/expandConcatVolume'.replace('{format}', 'json')
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
                                                response_type='ReturnCodeWithRef',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_expand_thin_volume_virtual_capacity(self, system_id, body, **kwargs):
            """
            This procedure will expand a thin volume's virtual capacity. It does not affect the repository volume's capacity.
            Documented return codes: ok, error, illegalParam, noHeap, tryAlternate, internalError, invalidVolumeref, illegalVolume, invalidVirtualCapacity. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_expand_thin_volume_virtual_capacity(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param ThinVolumeExpansionDescriptor body: An object containing all of the attributes necessary to expand a thin volume's virtual capacity. (required)
    
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
                        " to method symbol_expand_thin_volume_virtual_capacity" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_expand_thin_volume_virtual_capacity`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_expand_thin_volume_virtual_capacity`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/expandThinVolumeVirtualCapacity'.replace('{format}', 'json')
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
    
    def symbol_export_lock_key(self, system_id, body, **kwargs):
            """
            This procedure returns the WrappedLockKeyReturn union for the array.The WrappedLockKeyReturn contains the WrappedLockKey structure for the array it was exported from.
            No return codes have been documented for this API!

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_export_lock_key(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str body: The wrapped pass phrase used to encrypt the lock key. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: WrappedLockKeyReturn
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
                        " to method symbol_export_lock_key" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_export_lock_key`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_export_lock_key`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/exportLockKey'.replace('{format}', 'json')
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
                                                response_type='WrappedLockKeyReturn',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    
    def symbol_export_volume_group(self, system_id, body, **kwargs):
            """
            This procedure places the identified volume group in an \"exported\" state so that its drives may be removed and installed into another array.
            Documented return codes: ok, volumeGroupHasHotspare, volumeGroupReconfiguring, volumeGroupReconstructing, volumeGroupNotComplete, volumeGroupHasFailedDrives, volumeGroupHasNonOptimalVols, volumeGroupHasMirrorRelationship, volumeGroupHasVolcopyRelationship, volumeGroupHasMirroringMetadata, volumeGroupHasMappedVols, volumeGroupHasReservations, volumeGroupHasIncompatibleDacstores, volumeLimitExceeded, volumeGroupHasUnknownRaidLevel, volumeGroupHasUnsupportedRaidLevel, volumeGroupHasCloneOpportunity, volumeGroupHasInsufficientDrives, volumeGroupHasFailedVols, volumeGroupHasSnapshotRelationship, noNativeSstor, volumeInitializing, exportingDrivesDatabaseResynchronizing, exportingDrivesDatabaseFailed, volumeGroupHasArvmRelationship, volumeGroupHasPitgroupRelationship, volumeGroupHasPitviewRelationship, volumeGroupHasConcatRelationship. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_export_volume_group(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str body: A SYMbol VolumeGroupRef identifying the volume group to export. (required)
    
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
                        " to method symbol_export_volume_group" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_export_volume_group`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_export_volume_group`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/exportVolumeGroup'.replace('{format}', 'json')
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
    
    def symbol_external_kms_re_key(self, system_id, body, **kwargs):
            """
            Used to re-key the array with a new lock key.
            Documented return codes: ok, externalKmsFailed, externalKmsNotEnabled, externalKmsNotCompliant, externalKmsTimeout. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_external_kms_re_key(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str body: The wrapped pass phrase used to encrypt the lock key. (required)
    
            :param str controller: Controller selection
    
            :param bool verbose_error_response: 
    
            :return: WrappedLockKeyReturn
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
                        " to method symbol_external_kms_re_key" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_external_kms_re_key`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_external_kms_re_key`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/externalKMSReKey'.replace('{format}', 'json')
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
                                                response_type='WrappedLockKeyReturn',
                                                auth_settings=auth_settings,
                                                callback=params.get('callback'))
            return response
    









