# coding: utf-8

"""
DCBXSummaryData.py

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


class DCBXSummaryData(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DCBXSummaryData - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'protocol_type': 'str',  # (required parameter)
            'priority': 'int',  # (required parameter)
            'priority_group_id': 'int',  # (required parameter)
            'link_bandwidth_percentage': 'int',  # (required parameter)
            'enabled': 'bool'
        }

        self.attribute_map = {
            'protocol_type': 'protocolType',  # (required parameter)
            'priority': 'priority',  # (required parameter)
            'priority_group_id': 'priorityGroupId',  # (required parameter)
            'link_bandwidth_percentage': 'linkBandwidthPercentage',  # (required parameter)
            'enabled': 'enabled'
        }

        self._protocol_type = None
        self._priority = None
        self._priority_group_id = None
        self._link_bandwidth_percentage = None
        self._enabled = None

    @property
    def protocol_type(self):
        """
        Gets the protocol_type of this DCBXSummaryData.
        This enumeration contains the known Ethernet Protocol types currently negotiated via DCBX.

        :return: The protocol_type of this DCBXSummaryData.
        :rtype: str
        :required/optional: required
        """
        return self._protocol_type

    @protocol_type.setter
    def protocol_type(self, protocol_type):
        """
        Sets the protocol_type of this DCBXSummaryData.
        This enumeration contains the known Ethernet Protocol types currently negotiated via DCBX.

        :param protocol_type: The protocol_type of this DCBXSummaryData.
        :type: str
        """
        allowed_values = ["unk", "fcoe", "fip", "iscsi", "__UNDEFINED"]
        if protocol_type not in allowed_values:
            raise ValueError(
                "Invalid value for `protocol_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._protocol_type = protocol_type

    @property
    def priority(self):
        """
        Gets the priority of this DCBXSummaryData.
        This object contains a priority number (0 - TLV_MAX_PROTOCOL_ENTRIES) assigned to the given protocol type.

        :return: The priority of this DCBXSummaryData.
        :rtype: int
        :required/optional: required
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this DCBXSummaryData.
        This object contains a priority number (0 - TLV_MAX_PROTOCOL_ENTRIES) assigned to the given protocol type.

        :param priority: The priority of this DCBXSummaryData.
        :type: int
        """
        self._priority = priority

    @property
    def priority_group_id(self):
        """
        Gets the priority_group_id of this DCBXSummaryData.
        This object contains a priority group ID assigned to the given priority number.

        :return: The priority_group_id of this DCBXSummaryData.
        :rtype: int
        :required/optional: required
        """
        return self._priority_group_id

    @priority_group_id.setter
    def priority_group_id(self, priority_group_id):
        """
        Sets the priority_group_id of this DCBXSummaryData.
        This object contains a priority group ID assigned to the given priority number.

        :param priority_group_id: The priority_group_id of this DCBXSummaryData.
        :type: int
        """
        self._priority_group_id = priority_group_id

    @property
    def link_bandwidth_percentage(self):
        """
        Gets the link_bandwidth_percentage of this DCBXSummaryData.
        This object contains the percentage of the link band-width assigned to the given priority group ID.

        :return: The link_bandwidth_percentage of this DCBXSummaryData.
        :rtype: int
        :required/optional: required
        """
        return self._link_bandwidth_percentage

    @link_bandwidth_percentage.setter
    def link_bandwidth_percentage(self, link_bandwidth_percentage):
        """
        Sets the link_bandwidth_percentage of this DCBXSummaryData.
        This object contains the percentage of the link band-width assigned to the given priority group ID.

        :param link_bandwidth_percentage: The link_bandwidth_percentage of this DCBXSummaryData.
        :type: int
        """
        self._link_bandwidth_percentage = link_bandwidth_percentage

    @property
    def enabled(self):
        """
        Gets the enabled of this DCBXSummaryData.
        This is the status of the given priority number.

        :return: The enabled of this DCBXSummaryData.
        :rtype: bool
        :required/optional: required
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this DCBXSummaryData.
        This is the status of the given priority number.

        :param enabled: The enabled of this DCBXSummaryData.
        :type: bool
        """
        self._enabled = enabled

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

