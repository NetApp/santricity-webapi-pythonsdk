# coding: utf-8

"""
ParentRelativeLocation.py

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


class ParentRelativeLocation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ParentRelativeLocation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'component_type': 'str',  # (required parameter)
            'relative_position': 'int'
        }

        self.attribute_map = {
            'component_type': 'componentType',  # (required parameter)
            'relative_position': 'relativePosition'
        }

        self._component_type = None
        self._relative_position = None

    @property
    def component_type(self):
        """
        Gets the component_type of this ParentRelativeLocation.
        The type of component.

        :return: The component_type of this ParentRelativeLocation.
        :rtype: str
        :required/optional: required
        """
        return self._component_type

    @component_type.setter
    def component_type(self, component_type):
        """
        Sets the component_type of this ParentRelativeLocation.
        The type of component.

        :param component_type: The component_type of this ParentRelativeLocation.
        :type: str
        """
        allowed_values = ["unknown", "drive", "powerSply", "fan", "minihub", "tempSensor", "channel", "esm", "controller", "battery", "enclosure", "ups", "chip", "volume", "volumeGrp", "portCru", "interconnectCru", "supportCru", "alarm", "channelPort", "sfpPort", "hostBoard", "newFormat", "ctlrSfp", "ctlrSoc", "initiator", "target", "isnsServer", "hostIoCard", "cacheBackupDevice", "cacheMemDimm", "host", "hostPort", "drawer", "relative", "schedule", "asyncMirrorGroup", "diskPool", "pit", "pitConsistencyGroup", "cgpit", "cgview", "flashCache", "snmpCommunity", "snmpTrapDestination", "fcTarget", "blankOne", "blankTwo", "fanOnlyCru", "psuCru", "nvmeInitiator", "__UNDEFINED"]
        if component_type not in allowed_values:
            raise ValueError(
                "Invalid value for `component_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._component_type = component_type

    @property
    def relative_position(self):
        """
        Gets the relative_position of this ParentRelativeLocation.
        The relative position within the component's parent.

        :return: The relative_position of this ParentRelativeLocation.
        :rtype: int
        :required/optional: required
        """
        return self._relative_position

    @relative_position.setter
    def relative_position(self, relative_position):
        """
        Sets the relative_position of this ParentRelativeLocation.
        The relative position within the component's parent.

        :param relative_position: The relative_position of this ParentRelativeLocation.
        :type: int
        """
        self._relative_position = relative_position

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

