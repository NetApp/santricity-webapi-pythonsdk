# coding: utf-8

"""
DriveChannelPort.py

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


class DriveChannelPort(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DriveChannelPort - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'port_ref': 'str',  # (required parameter)
            'channel': 'int',  # (required parameter)
            'port_type': 'str',  # (required parameter)
            'parent_type': 'DriveChannelParent'
        }

        self.attribute_map = {
            'port_ref': 'portRef',  # (required parameter)
            'channel': 'channel',  # (required parameter)
            'port_type': 'portType',  # (required parameter)
            'parent_type': 'parentType'
        }

        self._port_ref = None
        self._channel = None
        self._port_type = None
        self._parent_type = None

    @property
    def port_ref(self):
        """
        Gets the port_ref of this DriveChannelPort.
        A reference to the drive channel port.

        :return: The port_ref of this DriveChannelPort.
        :rtype: str
        :required/optional: required
        """
        return self._port_ref

    @port_ref.setter
    def port_ref(self, port_ref):
        """
        Sets the port_ref of this DriveChannelPort.
        A reference to the drive channel port.

        :param port_ref: The port_ref of this DriveChannelPort.
        :type: str
        """
        self._port_ref = port_ref

    @property
    def channel(self):
        """
        Gets the channel of this DriveChannelPort.
        The Fibre Channel number of the port.

        :return: The channel of this DriveChannelPort.
        :rtype: int
        :required/optional: required
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """
        Sets the channel of this DriveChannelPort.
        The Fibre Channel number of the port.

        :param channel: The channel of this DriveChannelPort.
        :type: int
        """
        self._channel = channel

    @property
    def port_type(self):
        """
        Gets the port_type of this DriveChannelPort.
        The type of port (XBB/expansion/internal).

        :return: The port_type of this DriveChannelPort.
        :rtype: str
        :required/optional: required
        """
        return self._port_type

    @port_type.setter
    def port_type(self, port_type):
        """
        Sets the port_type of this DriveChannelPort.
        The type of port (XBB/expansion/internal).

        :param port_type: The port_type of this DriveChannelPort.
        :type: str
        """
        allowed_values = ["portUnknown", "port1", "port2", "port3", "port4", "port12", "port34", "port7", "minihubInout", "expansionOnly", "expansionAndInternal", "__UNDEFINED"]
        if port_type not in allowed_values:
            raise ValueError(
                "Invalid value for `port_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._port_type = port_type

    @property
    def parent_type(self):
        """
        Gets the parent_type of this DriveChannelPort.
        The parent type (minihub/controller).

        :return: The parent_type of this DriveChannelPort.
        :rtype: DriveChannelParent
        :required/optional: required
        """
        return self._parent_type

    @parent_type.setter
    def parent_type(self, parent_type):
        """
        Sets the parent_type of this DriveChannelPort.
        The parent type (minihub/controller).

        :param parent_type: The parent_type of this DriveChannelPort.
        :type: DriveChannelParent
        """
        self._parent_type = parent_type

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

