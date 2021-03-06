# coding: utf-8

"""
ControllerNetworkSettings.py

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


class ControllerNetworkSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ControllerNetworkSettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'ipv4_default_router_address': 'str',  # (required parameter)
            'ipv6_default_router_address': 'IpV6AddressData',  # (required parameter)
            'ipv6_candidate_default_router_addresses': 'list[IpV6AddressData]',  # (required parameter)
            'remote_access_enabled': 'bool',  # (required parameter)
            'dns_properties': 'ControllerDNSProperties',  # (required parameter)
            'ntp_properties': 'ControllerNTPProperties'
        }

        self.attribute_map = {
            'ipv4_default_router_address': 'ipv4DefaultRouterAddress',  # (required parameter)
            'ipv6_default_router_address': 'ipv6DefaultRouterAddress',  # (required parameter)
            'ipv6_candidate_default_router_addresses': 'ipv6CandidateDefaultRouterAddresses',  # (required parameter)
            'remote_access_enabled': 'remoteAccessEnabled',  # (required parameter)
            'dns_properties': 'dnsProperties',  # (required parameter)
            'ntp_properties': 'ntpProperties'
        }

        self._ipv4_default_router_address = None
        self._ipv6_default_router_address = None
        self._ipv6_candidate_default_router_addresses = None
        self._remote_access_enabled = None
        self._dns_properties = None
        self._ntp_properties = None

    @property
    def ipv4_default_router_address(self):
        """
        Gets the ipv4_default_router_address of this ControllerNetworkSettings.
        The IPV4 static default router address for the controller (sometimes referred to as the \"gateway address\").

        :return: The ipv4_default_router_address of this ControllerNetworkSettings.
        :rtype: str
        :required/optional: required
        """
        return self._ipv4_default_router_address

    @ipv4_default_router_address.setter
    def ipv4_default_router_address(self, ipv4_default_router_address):
        """
        Sets the ipv4_default_router_address of this ControllerNetworkSettings.
        The IPV4 static default router address for the controller (sometimes referred to as the \"gateway address\").

        :param ipv4_default_router_address: The ipv4_default_router_address of this ControllerNetworkSettings.
        :type: str
        """
        self._ipv4_default_router_address = ipv4_default_router_address

    @property
    def ipv6_default_router_address(self):
        """
        Gets the ipv6_default_router_address of this ControllerNetworkSettings.
        The IPV6 static default router address and associated data for the controller.

        :return: The ipv6_default_router_address of this ControllerNetworkSettings.
        :rtype: IpV6AddressData
        :required/optional: required
        """
        return self._ipv6_default_router_address

    @ipv6_default_router_address.setter
    def ipv6_default_router_address(self, ipv6_default_router_address):
        """
        Sets the ipv6_default_router_address of this ControllerNetworkSettings.
        The IPV6 static default router address and associated data for the controller.

        :param ipv6_default_router_address: The ipv6_default_router_address of this ControllerNetworkSettings.
        :type: IpV6AddressData
        """
        self._ipv6_default_router_address = ipv6_default_router_address

    @property
    def ipv6_candidate_default_router_addresses(self):
        """
        Gets the ipv6_candidate_default_router_addresses of this ControllerNetworkSettings.
        The set of IPV6 candidate default router addresses for the controller.

        :return: The ipv6_candidate_default_router_addresses of this ControllerNetworkSettings.
        :rtype: list[IpV6AddressData]
        :required/optional: required
        """
        return self._ipv6_candidate_default_router_addresses

    @ipv6_candidate_default_router_addresses.setter
    def ipv6_candidate_default_router_addresses(self, ipv6_candidate_default_router_addresses):
        """
        Sets the ipv6_candidate_default_router_addresses of this ControllerNetworkSettings.
        The set of IPV6 candidate default router addresses for the controller.

        :param ipv6_candidate_default_router_addresses: The ipv6_candidate_default_router_addresses of this ControllerNetworkSettings.
        :type: list[IpV6AddressData]
        """
        self._ipv6_candidate_default_router_addresses = ipv6_candidate_default_router_addresses

    @property
    def remote_access_enabled(self):
        """
        Gets the remote_access_enabled of this ControllerNetworkSettings.
        True if enabled for remote access

        :return: The remote_access_enabled of this ControllerNetworkSettings.
        :rtype: bool
        :required/optional: required
        """
        return self._remote_access_enabled

    @remote_access_enabled.setter
    def remote_access_enabled(self, remote_access_enabled):
        """
        Sets the remote_access_enabled of this ControllerNetworkSettings.
        True if enabled for remote access

        :param remote_access_enabled: The remote_access_enabled of this ControllerNetworkSettings.
        :type: bool
        """
        self._remote_access_enabled = remote_access_enabled

    @property
    def dns_properties(self):
        """
        Gets the dns_properties of this ControllerNetworkSettings.
        DNS configuration information.

        :return: The dns_properties of this ControllerNetworkSettings.
        :rtype: ControllerDNSProperties
        :required/optional: required
        """
        return self._dns_properties

    @dns_properties.setter
    def dns_properties(self, dns_properties):
        """
        Sets the dns_properties of this ControllerNetworkSettings.
        DNS configuration information.

        :param dns_properties: The dns_properties of this ControllerNetworkSettings.
        :type: ControllerDNSProperties
        """
        self._dns_properties = dns_properties

    @property
    def ntp_properties(self):
        """
        Gets the ntp_properties of this ControllerNetworkSettings.
        NTP configuration information.

        :return: The ntp_properties of this ControllerNetworkSettings.
        :rtype: ControllerNTPProperties
        :required/optional: required
        """
        return self._ntp_properties

    @ntp_properties.setter
    def ntp_properties(self, ntp_properties):
        """
        Sets the ntp_properties of this ControllerNetworkSettings.
        NTP configuration information.

        :param ntp_properties: The ntp_properties of this ControllerNetworkSettings.
        :type: ControllerNTPProperties
        """
        self._ntp_properties = ntp_properties

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

