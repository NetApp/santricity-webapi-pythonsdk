# coding: utf-8

"""
DiscreteTimeSeries.py

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


class DiscreteTimeSeries(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DiscreteTimeSeries - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'controller_ref': 'str',  # (required parameter)
            'wrap_count': 'int',  # (required parameter)
            'series': 'list[int]'
        }

        self.attribute_map = {
            'controller_ref': 'controllerRef',  # (required parameter)
            'wrap_count': 'wrapCount',  # (required parameter)
            'series': 'series'
        }

        self._controller_ref = None
        self._wrap_count = None
        self._series = None

    @property
    def controller_ref(self):
        """
        Gets the controller_ref of this DiscreteTimeSeries.
        A reference to the controller that provided the statistics.

        :return: The controller_ref of this DiscreteTimeSeries.
        :rtype: str
        :required/optional: required
        """
        return self._controller_ref

    @controller_ref.setter
    def controller_ref(self, controller_ref):
        """
        Sets the controller_ref of this DiscreteTimeSeries.
        A reference to the controller that provided the statistics.

        :param controller_ref: The controller_ref of this DiscreteTimeSeries.
        :type: str
        """
        self._controller_ref = controller_ref

    @property
    def wrap_count(self):
        """
        Gets the wrap_count of this DiscreteTimeSeries.
        The number of times the controller memory buffer for holding the observations has wrapped before being retrieved by the client.

        :return: The wrap_count of this DiscreteTimeSeries.
        :rtype: int
        :required/optional: required
        """
        return self._wrap_count

    @wrap_count.setter
    def wrap_count(self, wrap_count):
        """
        Sets the wrap_count of this DiscreteTimeSeries.
        The number of times the controller memory buffer for holding the observations has wrapped before being retrieved by the client.

        :param wrap_count: The wrap_count of this DiscreteTimeSeries.
        :type: int
        """
        self._wrap_count = wrap_count

    @property
    def series(self):
        """
        Gets the series of this DiscreteTimeSeries.
        The array of observations.

        :return: The series of this DiscreteTimeSeries.
        :rtype: list[int]
        :required/optional: required
        """
        return self._series

    @series.setter
    def series(self, series):
        """
        Sets the series of this DiscreteTimeSeries.
        The array of observations.

        :param series: The series of this DiscreteTimeSeries.
        :type: list[int]
        """
        self._series = series

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
