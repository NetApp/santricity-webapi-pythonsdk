# coding: utf-8

"""
ValidateConfigurationFileResponseItem.py

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


class ValidateConfigurationFileResponseItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ValidateConfigurationFileResponseItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'row': 'int',  
            'type': 'str',  
            'value': 'str'
        }

        self.attribute_map = {
            'row': 'row',  
            'type': 'type',  
            'value': 'value'
        }

        self._row = None
        self._type = None
        self._value = None

    @property
    def row(self):
        """
        Gets the row of this ValidateConfigurationFileResponseItem.
        The 1 based row identifier.  Row 0 is the header row and is not returned

        :return: The row of this ValidateConfigurationFileResponseItem.
        :rtype: int
        :required/optional: optional
        """
        return self._row

    @row.setter
    def row(self, row):
        """
        Sets the row of this ValidateConfigurationFileResponseItem.
        The 1 based row identifier.  Row 0 is the header row and is not returned

        :param row: The row of this ValidateConfigurationFileResponseItem.
        :type: int
        """
        self._row = row

    @property
    def type(self):
        """
        Gets the type of this ValidateConfigurationFileResponseItem.
        The configuration item type

        :return: The type of this ValidateConfigurationFileResponseItem.
        :rtype: str
        :required/optional: optional
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ValidateConfigurationFileResponseItem.
        The configuration item type

        :param type: The type of this ValidateConfigurationFileResponseItem.
        :type: str
        """
        allowed_values = ["systemSerialNumber", "controllerAPort1IP4", "controllerAPort2IP4", "controllerBPort1IP4", "controllerBPort2IP4", "controllerAPort1IP6", "controllerAPort2IP6", "controllerBPort1IP6", "controllerBPort2IP6", "controllerAPort1Netmask4", "controllerAPort2Netmask4", "controllerBPort1Netmask4", "controllerBPort2Netmask4", "controllerAPort1Netmask6", "controllerAPort2Netmask6", "controllerBPort1Netmask6", "controllerBPort2Netmask6", "controllerAIPv4GW", "controllerAIPv6GW", "controllerBIPv4GW", "controllerBIPv6GW", "systemLabel", "saPassword", "systemKey", "metaData", None]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type`, must be one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def value(self):
        """
        Gets the value of this ValidateConfigurationFileResponseItem.
        The data found for the row

        :return: The value of this ValidateConfigurationFileResponseItem.
        :rtype: str
        :required/optional: optional
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this ValidateConfigurationFileResponseItem.
        The data found for the row

        :param value: The value of this ValidateConfigurationFileResponseItem.
        :type: str
        """
        self._value = value

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

