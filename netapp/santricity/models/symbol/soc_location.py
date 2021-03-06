# coding: utf-8

"""
SocLocation.py

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


class SocLocation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SocLocation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'channel_type': 'str',  # (required parameter)
            'channel': 'int',  # (required parameter)
            'soc': 'int',  # (required parameter)
            'port': 'int',  # (required parameter)
            'controller_slot': 'int'
        }

        self.attribute_map = {
            'channel_type': 'channelType',  # (required parameter)
            'channel': 'channel',  # (required parameter)
            'soc': 'soc',  # (required parameter)
            'port': 'port',  # (required parameter)
            'controller_slot': 'controllerSlot'
        }

        self._channel_type = None
        self._channel = None
        self._soc = None
        self._port = None
        self._controller_slot = None

    @property
    def channel_type(self):
        """
        Gets the channel_type of this SocLocation.
        The channel type.

        :return: The channel_type of this SocLocation.
        :rtype: str
        :required/optional: required
        """
        return self._channel_type

    @channel_type.setter
    def channel_type(self, channel_type):
        """
        Sets the channel_type of this SocLocation.
        The channel type.

        :param channel_type: The channel_type of this SocLocation.
        :type: str
        """
        allowed_values = ["hostside", "driveside", "management", "__UNDEFINED"]
        if channel_type not in allowed_values:
            raise ValueError(
                "Invalid value for `channel_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._channel_type = channel_type

    @property
    def channel(self):
        """
        Gets the channel of this SocLocation.
        The channel type.

        :return: The channel of this SocLocation.
        :rtype: int
        :required/optional: required
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """
        Sets the channel of this SocLocation.
        The channel type.

        :param channel: The channel of this SocLocation.
        :type: int
        """
        self._channel = channel

    @property
    def soc(self):
        """
        Gets the soc of this SocLocation.
        The SOC index, 0-based.

        :return: The soc of this SocLocation.
        :rtype: int
        :required/optional: required
        """
        return self._soc

    @soc.setter
    def soc(self, soc):
        """
        Sets the soc of this SocLocation.
        The SOC index, 0-based.

        :param soc: The soc of this SocLocation.
        :type: int
        """
        self._soc = soc

    @property
    def port(self):
        """
        Gets the port of this SocLocation.
        The port number, 1-based

        :return: The port of this SocLocation.
        :rtype: int
        :required/optional: required
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this SocLocation.
        The port number, 1-based

        :param port: The port of this SocLocation.
        :type: int
        """
        self._port = port

    @property
    def controller_slot(self):
        """
        Gets the controller_slot of this SocLocation.
        The controller slot number, 1 or 2

        :return: The controller_slot of this SocLocation.
        :rtype: int
        :required/optional: required
        """
        return self._controller_slot

    @controller_slot.setter
    def controller_slot(self, controller_slot):
        """
        Sets the controller_slot of this SocLocation.
        The controller slot number, 1 or 2

        :param controller_slot: The controller_slot of this SocLocation.
        :type: int
        """
        self._controller_slot = controller_slot

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

