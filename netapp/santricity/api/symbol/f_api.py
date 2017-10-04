#!/usr/bin/env python
# coding: utf-8

"""
FApi.py

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


class FApi(object):

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient(context_path='/devmgr/v2')
            self.api_client = config.api_client
    
    
    def symbol_fail_back_volume_ownership(self, system_id, body, **kwargs):
            """
            This procedure will perform an immediate fail-back of volume current ownership to the preferred owner.
            Documented return codes: ok, noHeap. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_fail_back_volume_ownership(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param VolumeOwnershipFailBackRequestDescriptor body: Descriptor containing input parameters for fail back request operation. (required)
    
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
                        " to method symbol_fail_back_volume_ownership" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_fail_back_volume_ownership`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_fail_back_volume_ownership`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/failBackVolumeOwnership'.replace('{format}', 'json')
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
    
    def symbol_force_disk_pool_to_optimal(self, system_id, body, **kwargs):
            """
            This procedure attempts to revive the given disk pool.
            Documented return codes: ok. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_force_disk_pool_to_optimal(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str body: An object containing all of the required attributes to revive the given disk pool. (required)
    
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
                        " to method symbol_force_disk_pool_to_optimal" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_force_disk_pool_to_optimal`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_force_disk_pool_to_optimal`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/forceDiskPoolToOptimal'.replace('{format}', 'json')
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
    
    def symbol_force_volume_group(self, system_id, body, **kwargs):
            """
            This procedure applies to a volume group for which successful migration of drives from the source array to the target array could not be completed due to hardware errors. It causes the identified volume group to move to a state called the \"forced\" state, from which it is still permissible to perform an import operation on the volume group.
            Documented return codes: ok, volumeGroupHasHotspare, volumeGroupReconfiguring, volumeGroupReconstructing, volumeGroupHasFailedDrives, volumeGroupHasNonOptimalVols, volumeGroupHasMirrorRelationship, volumeGroupHasVolcopyRelationship, volumeGroupHasMirroringMetadata, volumeGroupHasMappedVols, volumeGroupHasReservations, volumeGroupHasIncompatibleDacstores, volumeLimitExceeded, volumeGroupHasUnknownRaidLevel, volumeGroupHasUnsupportedRaidLevel, volumeGroupHasCloneOpportunity, volumeGroupHasInsufficientDrives, volumeGroupHasFailedVols, volumeGroupNotContingent, legacyVg, vgNotForceable, driveSpinUpError, volumeGroupHasIncompatibleDrive. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_force_volume_group(system_id, body, callback=callback_function)
    
    

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
                        " to method symbol_force_volume_group" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_force_volume_group`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_force_volume_group`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/forceVolumeGroup'.replace('{format}', 'json')
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
    
    def symbol_force_volume_group_to_optimal(self, system_id, body, **kwargs):
            """
            This is a potentially dangerous operation, since it causes data to be made available to the I/O host even though that data may have become corrupted due to device failures that occurred in the past.
            Documented return codes: ok, error, illegalParam, noHeap, volumeReconfiguring, tryAlternate, background, invalidVolumegroupref. 

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please define a `callback` function
            to be invoked when receiving the response.
            >>> def callback_function(response):
            >>>     pprint(response)
            >>>
    
            >>> thread = api.symbol_force_volume_group_to_optimal(system_id, body, callback=callback_function)
    
    

            :param callback function: The callback function
                for asynchronous request. (optional)
    
            :param str system_id: The unique identifier of the storage-system. This may be the id or the WWN. (required)
    
            :param str body: The value of the VolumeGroupRef for the volume group that is being restored to the optimal state. (required)
    
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
                        " to method symbol_force_volume_group_to_optimal" % key
                    )
                params[key] = val
            del params['kwargs']

    
    
            # verify the required parameter 'system_id' is set
            if ('system_id' not in params) or (params['system_id'] is None):
                raise ValueError("Missing the required parameter `system_id` when calling `symbol_force_volume_group_to_optimal`")
    
    
    
            # verify the required parameter 'body' is set
            if ('body' not in params) or (params['body'] is None):
                raise ValueError("Missing the required parameter `body` when calling `symbol_force_volume_group_to_optimal`")
    
    
    
    
    
    

            resource_path = '/storage-systems/{system-id}/symbol/forceVolumeGroupToOptimal'.replace('{format}', 'json')
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
    









