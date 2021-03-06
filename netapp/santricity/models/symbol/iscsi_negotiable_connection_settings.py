# coding: utf-8

"""
IscsiNegotiableConnectionSettings.py

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


class IscsiNegotiableConnectionSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        IscsiNegotiableConnectionSettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'max_receive_data_segment_length': 'int',  # (required parameter)
            'header_digest_method': 'list[str]',  # (required parameter)
            'data_digest_method': 'list[str]',  # (required parameter)
            'receiving_markers': 'bool',  # (required parameter)
            'auth_method': 'list[str]'
        }

        self.attribute_map = {
            'max_receive_data_segment_length': 'maxReceiveDataSegmentLength',  # (required parameter)
            'header_digest_method': 'headerDigestMethod',  # (required parameter)
            'data_digest_method': 'dataDigestMethod',  # (required parameter)
            'receiving_markers': 'receivingMarkers',  # (required parameter)
            'auth_method': 'authMethod'
        }

        self._max_receive_data_segment_length = None
        self._header_digest_method = None
        self._data_digest_method = None
        self._receiving_markers = None
        self._auth_method = None

    @property
    def max_receive_data_segment_length(self):
        """
        Gets the max_receive_data_segment_length of this IscsiNegotiableConnectionSettings.
        The maximum data payload size supported for command or data PDUs able to be received on this connection.

        :return: The max_receive_data_segment_length of this IscsiNegotiableConnectionSettings.
        :rtype: int
        :required/optional: required
        """
        return self._max_receive_data_segment_length

    @max_receive_data_segment_length.setter
    def max_receive_data_segment_length(self, max_receive_data_segment_length):
        """
        Sets the max_receive_data_segment_length of this IscsiNegotiableConnectionSettings.
        The maximum data payload size supported for command or data PDUs able to be received on this connection.

        :param max_receive_data_segment_length: The max_receive_data_segment_length of this IscsiNegotiableConnectionSettings.
        :type: int
        """
        self._max_receive_data_segment_length = max_receive_data_segment_length

    @property
    def header_digest_method(self):
        """
        Gets the header_digest_method of this IscsiNegotiableConnectionSettings.
        The iSCSI header digest scheme in use within this connection. This field is an array of at most two elements so that, when reporting default settings, both primary and secondary methods can be reported, which are at array indexes 0 and 1 respectively. When used to report current settings, the array is sized at one.

        :return: The header_digest_method of this IscsiNegotiableConnectionSettings.
        :rtype: list[str]
        :required/optional: required
        """
        return self._header_digest_method

    @header_digest_method.setter
    def header_digest_method(self, header_digest_method):
        """
        Sets the header_digest_method of this IscsiNegotiableConnectionSettings.
        The iSCSI header digest scheme in use within this connection. This field is an array of at most two elements so that, when reporting default settings, both primary and secondary methods can be reported, which are at array indexes 0 and 1 respectively. When used to report current settings, the array is sized at one.

        :param header_digest_method: The header_digest_method of this IscsiNegotiableConnectionSettings.
        :type: list[str]
        """
        self._header_digest_method = header_digest_method

    @property
    def data_digest_method(self):
        """
        Gets the data_digest_method of this IscsiNegotiableConnectionSettings.
        The iSCSI data digest scheme in use within this connection. The same method is followed as for header digest in reporting default versus current settings.

        :return: The data_digest_method of this IscsiNegotiableConnectionSettings.
        :rtype: list[str]
        :required/optional: required
        """
        return self._data_digest_method

    @data_digest_method.setter
    def data_digest_method(self, data_digest_method):
        """
        Sets the data_digest_method of this IscsiNegotiableConnectionSettings.
        The iSCSI data digest scheme in use within this connection. The same method is followed as for header digest in reporting default versus current settings.

        :param data_digest_method: The data_digest_method of this IscsiNegotiableConnectionSettings.
        :type: list[str]
        """
        self._data_digest_method = data_digest_method

    @property
    def receiving_markers(self):
        """
        Gets the receiving_markers of this IscsiNegotiableConnectionSettings.
        True if this connection is receiving markers in in its incoming data stream.

        :return: The receiving_markers of this IscsiNegotiableConnectionSettings.
        :rtype: bool
        :required/optional: required
        """
        return self._receiving_markers

    @receiving_markers.setter
    def receiving_markers(self, receiving_markers):
        """
        Sets the receiving_markers of this IscsiNegotiableConnectionSettings.
        True if this connection is receiving markers in in its incoming data stream.

        :param receiving_markers: The receiving_markers of this IscsiNegotiableConnectionSettings.
        :type: bool
        """
        self._receiving_markers = receiving_markers

    @property
    def auth_method(self):
        """
        Gets the auth_method of this IscsiNegotiableConnectionSettings.
        The authentication method being used on this connection, as communicated during the login phase. The same method is followed as for header digest in reporting default versus current settings.

        :return: The auth_method of this IscsiNegotiableConnectionSettings.
        :rtype: list[str]
        :required/optional: required
        """
        return self._auth_method

    @auth_method.setter
    def auth_method(self, auth_method):
        """
        Sets the auth_method of this IscsiNegotiableConnectionSettings.
        The authentication method being used on this connection, as communicated during the login phase. The same method is followed as for header digest in reporting default versus current settings.

        :param auth_method: The auth_method of this IscsiNegotiableConnectionSettings.
        :type: list[str]
        """
        self._auth_method = auth_method

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

