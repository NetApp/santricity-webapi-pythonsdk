# coding: utf-8

"""
IscsiInterface.py

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


class IscsiInterface(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        IscsiInterface - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'channel': 'int',  # (required parameter)
            'channel_port_ref': 'str',  # (required parameter)
            'tcp_listen_port': 'int',  # (required parameter)
            'ipv4_enabled': 'bool',  # (required parameter)
            'ipv4_data': 'InternetProtocolV4Data',  # (required parameter)
            'interface_data': 'PhysicalInterfaceTypeData',  # (required parameter)
            'interface_ref': 'str',  # (required parameter)
            'ipv6_enabled': 'bool',  # (required parameter)
            'ipv6_data': 'InternetProtocolV6Data',  # (required parameter)
            'physical_location': 'Location',  # (required parameter)
            'protection_information_capable': 'bool',  # (required parameter)
            'is_i_pv6_capable': 'bool',  # (required parameter)
            'one_way_max_rate': 'int',  # (required parameter)
            'bidirectional_max_rate': 'int',  # (required parameter)
            'id': 'str'
        }

        self.attribute_map = {
            'channel': 'channel',  # (required parameter)
            'channel_port_ref': 'channelPortRef',  # (required parameter)
            'tcp_listen_port': 'tcpListenPort',  # (required parameter)
            'ipv4_enabled': 'ipv4Enabled',  # (required parameter)
            'ipv4_data': 'ipv4Data',  # (required parameter)
            'interface_data': 'interfaceData',  # (required parameter)
            'interface_ref': 'interfaceRef',  # (required parameter)
            'ipv6_enabled': 'ipv6Enabled',  # (required parameter)
            'ipv6_data': 'ipv6Data',  # (required parameter)
            'physical_location': 'physicalLocation',  # (required parameter)
            'protection_information_capable': 'protectionInformationCapable',  # (required parameter)
            'is_i_pv6_capable': 'isIPv6Capable',  # (required parameter)
            'one_way_max_rate': 'oneWayMaxRate',  # (required parameter)
            'bidirectional_max_rate': 'bidirectionalMaxRate',  # (required parameter)
            'id': 'id'
        }

        self._channel = None
        self._channel_port_ref = None
        self._tcp_listen_port = None
        self._ipv4_enabled = None
        self._ipv4_data = None
        self._interface_data = None
        self._interface_ref = None
        self._ipv6_enabled = None
        self._ipv6_data = None
        self._physical_location = None
        self._protection_information_capable = None
        self._is_i_pv6_capable = None
        self._one_way_max_rate = None
        self._bidirectional_max_rate = None
        self._id = None

    @property
    def channel(self):
        """
        Gets the channel of this IscsiInterface.
        The number of the channel controlled by this interface.

        :return: The channel of this IscsiInterface.
        :rtype: int
        :required/optional: required
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """
        Sets the channel of this IscsiInterface.
        The number of the channel controlled by this interface.

        :param channel: The channel of this IscsiInterface.
        :type: int
        """
        self._channel = channel

    @property
    def channel_port_ref(self):
        """
        Gets the channel_port_ref of this IscsiInterface.
        A reference to the channel port object associated with the channel controlled by this interface.

        :return: The channel_port_ref of this IscsiInterface.
        :rtype: str
        :required/optional: required
        """
        return self._channel_port_ref

    @channel_port_ref.setter
    def channel_port_ref(self, channel_port_ref):
        """
        Sets the channel_port_ref of this IscsiInterface.
        A reference to the channel port object associated with the channel controlled by this interface.

        :param channel_port_ref: The channel_port_ref of this IscsiInterface.
        :type: str
        """
        self._channel_port_ref = channel_port_ref

    @property
    def tcp_listen_port(self):
        """
        Gets the tcp_listen_port of this IscsiInterface.
        The number of the TCP port on which the target listens for incoming connections.

        :return: The tcp_listen_port of this IscsiInterface.
        :rtype: int
        :required/optional: required
        """
        return self._tcp_listen_port

    @tcp_listen_port.setter
    def tcp_listen_port(self, tcp_listen_port):
        """
        Sets the tcp_listen_port of this IscsiInterface.
        The number of the TCP port on which the target listens for incoming connections.

        :param tcp_listen_port: The tcp_listen_port of this IscsiInterface.
        :type: int
        """
        self._tcp_listen_port = tcp_listen_port

    @property
    def ipv4_enabled(self):
        """
        Gets the ipv4_enabled of this IscsiInterface.
        True if IPV4 is enabled for this interface; always true for iSER interface.

        :return: The ipv4_enabled of this IscsiInterface.
        :rtype: bool
        :required/optional: required
        """
        return self._ipv4_enabled

    @ipv4_enabled.setter
    def ipv4_enabled(self, ipv4_enabled):
        """
        Sets the ipv4_enabled of this IscsiInterface.
        True if IPV4 is enabled for this interface; always true for iSER interface.

        :param ipv4_enabled: The ipv4_enabled of this IscsiInterface.
        :type: bool
        """
        self._ipv4_enabled = ipv4_enabled

    @property
    def ipv4_data(self):
        """
        Gets the ipv4_data of this IscsiInterface.
        IPV4-related information for the interface.

        :return: The ipv4_data of this IscsiInterface.
        :rtype: InternetProtocolV4Data
        :required/optional: required
        """
        return self._ipv4_data

    @ipv4_data.setter
    def ipv4_data(self, ipv4_data):
        """
        Sets the ipv4_data of this IscsiInterface.
        IPV4-related information for the interface.

        :param ipv4_data: The ipv4_data of this IscsiInterface.
        :type: InternetProtocolV4Data
        """
        self._ipv4_data = ipv4_data

    @property
    def interface_data(self):
        """
        Gets the interface_data of this IscsiInterface.
        Information about the physical interface (e.g., Ethernet).

        :return: The interface_data of this IscsiInterface.
        :rtype: PhysicalInterfaceTypeData
        :required/optional: required
        """
        return self._interface_data

    @interface_data.setter
    def interface_data(self, interface_data):
        """
        Sets the interface_data of this IscsiInterface.
        Information about the physical interface (e.g., Ethernet).

        :param interface_data: The interface_data of this IscsiInterface.
        :type: PhysicalInterfaceTypeData
        """
        self._interface_data = interface_data

    @property
    def interface_ref(self):
        """
        Gets the interface_ref of this IscsiInterface.
        The unique identifier for a given instance of this structure.

        :return: The interface_ref of this IscsiInterface.
        :rtype: str
        :required/optional: required
        """
        return self._interface_ref

    @interface_ref.setter
    def interface_ref(self, interface_ref):
        """
        Sets the interface_ref of this IscsiInterface.
        The unique identifier for a given instance of this structure.

        :param interface_ref: The interface_ref of this IscsiInterface.
        :type: str
        """
        self._interface_ref = interface_ref

    @property
    def ipv6_enabled(self):
        """
        Gets the ipv6_enabled of this IscsiInterface.
        True if IPV6 is enabled for this interface; otherwise false.

        :return: The ipv6_enabled of this IscsiInterface.
        :rtype: bool
        :required/optional: required
        """
        return self._ipv6_enabled

    @ipv6_enabled.setter
    def ipv6_enabled(self, ipv6_enabled):
        """
        Sets the ipv6_enabled of this IscsiInterface.
        True if IPV6 is enabled for this interface; otherwise false.

        :param ipv6_enabled: The ipv6_enabled of this IscsiInterface.
        :type: bool
        """
        self._ipv6_enabled = ipv6_enabled

    @property
    def ipv6_data(self):
        """
        Gets the ipv6_data of this IscsiInterface.
        IPV6-related information for the interface.

        :return: The ipv6_data of this IscsiInterface.
        :rtype: InternetProtocolV6Data
        :required/optional: required
        """
        return self._ipv6_data

    @ipv6_data.setter
    def ipv6_data(self, ipv6_data):
        """
        Sets the ipv6_data of this IscsiInterface.
        IPV6-related information for the interface.

        :param ipv6_data: The ipv6_data of this IscsiInterface.
        :type: InternetProtocolV6Data
        """
        self._ipv6_data = ipv6_data

    @property
    def physical_location(self):
        """
        Gets the physical_location of this IscsiInterface.
        The physical location of the iSCSI interface. The parent reference in Location identifies the physical component (e.g., controller or host card) where the interface circuitry is located, and the position field is a firmware-assigned 1-relative number signifying \"1st iSCSI interface relative to the parent,\" \"2nd iSCSI interface relative to the parent,\" etc. This \"interface number\" is independent of the interface's channel association.

        :return: The physical_location of this IscsiInterface.
        :rtype: Location
        :required/optional: required
        """
        return self._physical_location

    @physical_location.setter
    def physical_location(self, physical_location):
        """
        Sets the physical_location of this IscsiInterface.
        The physical location of the iSCSI interface. The parent reference in Location identifies the physical component (e.g., controller or host card) where the interface circuitry is located, and the position field is a firmware-assigned 1-relative number signifying \"1st iSCSI interface relative to the parent,\" \"2nd iSCSI interface relative to the parent,\" etc. This \"interface number\" is independent of the interface's channel association.

        :param physical_location: The physical_location of this IscsiInterface.
        :type: Location
        """
        self._physical_location = physical_location

    @property
    def protection_information_capable(self):
        """
        Gets the protection_information_capable of this IscsiInterface.
        This field indicates whether or not the I/O interface is PI capable.

        :return: The protection_information_capable of this IscsiInterface.
        :rtype: bool
        :required/optional: required
        """
        return self._protection_information_capable

    @protection_information_capable.setter
    def protection_information_capable(self, protection_information_capable):
        """
        Sets the protection_information_capable of this IscsiInterface.
        This field indicates whether or not the I/O interface is PI capable.

        :param protection_information_capable: The protection_information_capable of this IscsiInterface.
        :type: bool
        """
        self._protection_information_capable = protection_information_capable

    @property
    def is_i_pv6_capable(self):
        """
        Gets the is_i_pv6_capable of this IscsiInterface.
        This flag is true if the interface is capable of IPv6 functionality.

        :return: The is_i_pv6_capable of this IscsiInterface.
        :rtype: bool
        :required/optional: required
        """
        return self._is_i_pv6_capable

    @is_i_pv6_capable.setter
    def is_i_pv6_capable(self, is_i_pv6_capable):
        """
        Sets the is_i_pv6_capable of this IscsiInterface.
        This flag is true if the interface is capable of IPv6 functionality.

        :param is_i_pv6_capable: The is_i_pv6_capable of this IscsiInterface.
        :type: bool
        """
        self._is_i_pv6_capable = is_i_pv6_capable

    @property
    def one_way_max_rate(self):
        """
        Gets the one_way_max_rate of this IscsiInterface.
        Maximum one way data rate in B/s

        :return: The one_way_max_rate of this IscsiInterface.
        :rtype: int
        :required/optional: required
        """
        return self._one_way_max_rate

    @one_way_max_rate.setter
    def one_way_max_rate(self, one_way_max_rate):
        """
        Sets the one_way_max_rate of this IscsiInterface.
        Maximum one way data rate in B/s

        :param one_way_max_rate: The one_way_max_rate of this IscsiInterface.
        :type: int
        """
        self._one_way_max_rate = one_way_max_rate

    @property
    def bidirectional_max_rate(self):
        """
        Gets the bidirectional_max_rate of this IscsiInterface.
        Maximum bi-directional data rate in B/s

        :return: The bidirectional_max_rate of this IscsiInterface.
        :rtype: int
        :required/optional: required
        """
        return self._bidirectional_max_rate

    @bidirectional_max_rate.setter
    def bidirectional_max_rate(self, bidirectional_max_rate):
        """
        Sets the bidirectional_max_rate of this IscsiInterface.
        Maximum bi-directional data rate in B/s

        :param bidirectional_max_rate: The bidirectional_max_rate of this IscsiInterface.
        :type: int
        """
        self._bidirectional_max_rate = bidirectional_max_rate

    @property
    def id(self):
        """
        Gets the id of this IscsiInterface.


        :return: The id of this IscsiInterface.
        :rtype: str
        :required/optional: optional
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this IscsiInterface.


        :param id: The id of this IscsiInterface.
        :type: str
        """
        self._id = id

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
