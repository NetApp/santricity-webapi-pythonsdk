# coding: utf-8

"""
ThinVolumeUpdateRequest.py

 The Clear BSD License

 Copyright (c) – 2016, NetApp, Inc. All rights reserved.

 Redistribution and use in source and binary forms, with or without modification, are permitted (subject to the limitations in the disclaimer below) provided that the following conditions are met:

 * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

 * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

 * Neither the name of NetApp, Inc. nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

 NO EXPRESS OR IMPLIED LICENSES TO ANY PARTY'S PATENT RIGHTS ARE GRANTED BY THIS LICENSE. THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from pprint import pformat
from six import iteritems


class ThinVolumeUpdateRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ThinVolumeUpdateRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',  
            'growth_alert_threshold': 'int',  
            'flash_cache': 'bool',  
            'meta_tags': 'list[VolumeMetadataItem]',  
            'expansion_policy': 'str',  
            'owning_controller_id': 'str',  
            'cache_settings': 'ThinVolumeCacheSettings',  
            'scan_settings': 'VolumeMediaScanParams'
        }

        self.attribute_map = {
            'name': 'name',  
            'growth_alert_threshold': 'growthAlertThreshold',  
            'flash_cache': 'flashCache',  
            'meta_tags': 'metaTags',  
            'expansion_policy': 'expansionPolicy',  
            'owning_controller_id': 'owningControllerId',  
            'cache_settings': 'cacheSettings',  
            'scan_settings': 'scanSettings'
        }

        self._name = None
        self._growth_alert_threshold = None
        self._flash_cache = None
        self._meta_tags = None
        self._expansion_policy = None
        self._owning_controller_id = None
        self._cache_settings = None
        self._scan_settings = None

    @property
    def name(self):
        """
        Gets the name of this ThinVolumeUpdateRequest.
        The user-label to assign to the volume.

        :return: The name of this ThinVolumeUpdateRequest.
        :rtype: str
        :required/optional: optional
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ThinVolumeUpdateRequest.
        The user-label to assign to the volume.

        :param name: The name of this ThinVolumeUpdateRequest.
        :type: str
        """
        self._name = name

    @property
    def growth_alert_threshold(self):
        """
        Gets the growth_alert_threshold of this ThinVolumeUpdateRequest.
        The repository utilization warning threshold (in percent).

        :return: The growth_alert_threshold of this ThinVolumeUpdateRequest.
        :rtype: int
        :required/optional: optional
        """
        return self._growth_alert_threshold

    @growth_alert_threshold.setter
    def growth_alert_threshold(self, growth_alert_threshold):
        """
        Sets the growth_alert_threshold of this ThinVolumeUpdateRequest.
        The repository utilization warning threshold (in percent).

        :param growth_alert_threshold: The growth_alert_threshold of this ThinVolumeUpdateRequest.
        :type: int
        """
        self._growth_alert_threshold = growth_alert_threshold

    @property
    def flash_cache(self):
        """
        Gets the flash_cache of this ThinVolumeUpdateRequest.
        If true, add the volume to the flashCache if one is defined. If false, remove from the flashCache if one exists.

        :return: The flash_cache of this ThinVolumeUpdateRequest.
        :rtype: bool
        :required/optional: optional
        """
        return self._flash_cache

    @flash_cache.setter
    def flash_cache(self, flash_cache):
        """
        Sets the flash_cache of this ThinVolumeUpdateRequest.
        If true, add the volume to the flashCache if one is defined. If false, remove from the flashCache if one exists.

        :param flash_cache: The flash_cache of this ThinVolumeUpdateRequest.
        :type: bool
        """
        self._flash_cache = flash_cache

    @property
    def meta_tags(self):
        """
        Gets the meta_tags of this ThinVolumeUpdateRequest.
        Optional array of Meta Data tags for the volume.  

        :return: The meta_tags of this ThinVolumeUpdateRequest.
        :rtype: list[VolumeMetadataItem]
        :required/optional: optional
        """
        return self._meta_tags

    @meta_tags.setter
    def meta_tags(self, meta_tags):
        """
        Sets the meta_tags of this ThinVolumeUpdateRequest.
        Optional array of Meta Data tags for the volume.  

        :param meta_tags: The meta_tags of this ThinVolumeUpdateRequest.
        :type: list[VolumeMetadataItem]
        """
        self._meta_tags = meta_tags

    @property
    def expansion_policy(self):
        """
        Gets the expansion_policy of this ThinVolumeUpdateRequest.
        Thin Volume expansion policy.      If automatic, the thin volume will be expanded automatically when capacity is exceeded,      if manual, the volume must be expanded manually.

        :return: The expansion_policy of this ThinVolumeUpdateRequest.
        :rtype: str
        :required/optional: optional
        """
        return self._expansion_policy

    @expansion_policy.setter
    def expansion_policy(self, expansion_policy):
        """
        Sets the expansion_policy of this ThinVolumeUpdateRequest.
        Thin Volume expansion policy.      If automatic, the thin volume will be expanded automatically when capacity is exceeded,      if manual, the volume must be expanded manually.

        :param expansion_policy: The expansion_policy of this ThinVolumeUpdateRequest.
        :type: str
        """
        allowed_values = ["unknown", "manual", "automatic", "__UNDEFINED", None]
        if expansion_policy not in allowed_values:
            raise ValueError(
                "Invalid value for `expansion_policy`, must be one of {0}"
                .format(allowed_values)
            )
        self._expansion_policy = expansion_policy

    @property
    def owning_controller_id(self):
        """
        Gets the owning_controller_id of this ThinVolumeUpdateRequest.
        Set the preferred owning controller

        :return: The owning_controller_id of this ThinVolumeUpdateRequest.
        :rtype: str
        :required/optional: optional
        """
        return self._owning_controller_id

    @owning_controller_id.setter
    def owning_controller_id(self, owning_controller_id):
        """
        Sets the owning_controller_id of this ThinVolumeUpdateRequest.
        Set the preferred owning controller

        :param owning_controller_id: The owning_controller_id of this ThinVolumeUpdateRequest.
        :type: str
        """
        self._owning_controller_id = owning_controller_id

    @property
    def cache_settings(self):
        """
        Gets the cache_settings of this ThinVolumeUpdateRequest.
        Configure cache settings for the volume

        :return: The cache_settings of this ThinVolumeUpdateRequest.
        :rtype: ThinVolumeCacheSettings
        :required/optional: optional
        """
        return self._cache_settings

    @cache_settings.setter
    def cache_settings(self, cache_settings):
        """
        Sets the cache_settings of this ThinVolumeUpdateRequest.
        Configure cache settings for the volume

        :param cache_settings: The cache_settings of this ThinVolumeUpdateRequest.
        :type: ThinVolumeCacheSettings
        """
        self._cache_settings = cache_settings

    @property
    def scan_settings(self):
        """
        Gets the scan_settings of this ThinVolumeUpdateRequest.
        Configure scan settings with regard to the controller's background media scan operation

        :return: The scan_settings of this ThinVolumeUpdateRequest.
        :rtype: VolumeMediaScanParams
        :required/optional: optional
        """
        return self._scan_settings

    @scan_settings.setter
    def scan_settings(self, scan_settings):
        """
        Sets the scan_settings of this ThinVolumeUpdateRequest.
        Configure scan settings with regard to the controller's background media scan operation

        :param scan_settings: The scan_settings of this ThinVolumeUpdateRequest.
        :type: VolumeMediaScanParams
        """
        self._scan_settings = scan_settings

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        if self is None:
           return None
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if self is None or other is None:
            return None
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

