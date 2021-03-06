# coding: utf-8

"""
Minihub.py

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


class Minihub(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Minihub - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'minihub_ref': 'str',  # (required parameter)
            'status': 'str',  # (required parameter)
            'physical_location': 'Location',  # (required parameter)
            'minihub_data': 'MinihubTypeData',  # (required parameter)
            'current_speed': 'str',  # (required parameter)
            'max_speed': 'str',  # (required parameter)
            'channel': 'int',  # (required parameter)
            'port_list': 'PortList',  # (required parameter)
            'vendor_name': 'str',  # (required parameter)
            'part_number': 'str',  # (required parameter)
            'serial_number': 'str',  # (required parameter)
            'fru_type': 'str',  # (required parameter)
            'manufacturer_date': 'int',  # (required parameter)
            'reserved1': 'str',  
            'reserved2': 'str',  
            'rtr_attributes': 'RTRAttributes'
        }

        self.attribute_map = {
            'minihub_ref': 'minihubRef',  # (required parameter)
            'status': 'status',  # (required parameter)
            'physical_location': 'physicalLocation',  # (required parameter)
            'minihub_data': 'minihubData',  # (required parameter)
            'current_speed': 'currentSpeed',  # (required parameter)
            'max_speed': 'maxSpeed',  # (required parameter)
            'channel': 'channel',  # (required parameter)
            'port_list': 'portList',  # (required parameter)
            'vendor_name': 'vendorName',  # (required parameter)
            'part_number': 'partNumber',  # (required parameter)
            'serial_number': 'serialNumber',  # (required parameter)
            'fru_type': 'fruType',  # (required parameter)
            'manufacturer_date': 'manufacturerDate',  # (required parameter)
            'reserved1': 'reserved1',  
            'reserved2': 'reserved2',  
            'rtr_attributes': 'rtrAttributes'
        }

        self._minihub_ref = None
        self._status = None
        self._physical_location = None
        self._minihub_data = None
        self._current_speed = None
        self._max_speed = None
        self._channel = None
        self._port_list = None
        self._vendor_name = None
        self._part_number = None
        self._serial_number = None
        self._fru_type = None
        self._manufacturer_date = None
        self._reserved1 = None
        self._reserved2 = None
        self._rtr_attributes = None

    @property
    def minihub_ref(self):
        """
        Gets the minihub_ref of this Minihub.
        The reference for this physical minihub.

        :return: The minihub_ref of this Minihub.
        :rtype: str
        :required/optional: required
        """
        return self._minihub_ref

    @minihub_ref.setter
    def minihub_ref(self, minihub_ref):
        """
        Sets the minihub_ref of this Minihub.
        The reference for this physical minihub.

        :param minihub_ref: The minihub_ref of this Minihub.
        :type: str
        """
        self._minihub_ref = minihub_ref

    @property
    def status(self):
        """
        Gets the status of this Minihub.
        The operational status of the minihub.

        :return: The status of this Minihub.
        :rtype: str
        :required/optional: required
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Minihub.
        The operational status of the minihub.

        :param status: The status of this Minihub.
        :type: str
        """
        allowed_values = ["optimal", "failed", "unsupported", "unknown", "__UNDEFINED"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status`, must be one of {0}"
                .format(allowed_values)
            )
        self._status = status

    @property
    def physical_location(self):
        """
        Gets the physical_location of this Minihub.
        The physical location of the minihub. Note that the tray reference identifies the enclosure containing the minihub, but the slot information does not apply to this component.

        :return: The physical_location of this Minihub.
        :rtype: Location
        :required/optional: required
        """
        return self._physical_location

    @physical_location.setter
    def physical_location(self, physical_location):
        """
        Sets the physical_location of this Minihub.
        The physical location of the minihub. Note that the tray reference identifies the enclosure containing the minihub, but the slot information does not apply to this component.

        :param physical_location: The physical_location of this Minihub.
        :type: Location
        """
        self._physical_location = physical_location

    @property
    def minihub_data(self):
        """
        Gets the minihub_data of this Minihub.
        Information returned is based on the minihub type.

        :return: The minihub_data of this Minihub.
        :rtype: MinihubTypeData
        :required/optional: required
        """
        return self._minihub_data

    @minihub_data.setter
    def minihub_data(self, minihub_data):
        """
        Sets the minihub_data of this Minihub.
        Information returned is based on the minihub type.

        :param minihub_data: The minihub_data of this Minihub.
        :type: MinihubTypeData
        """
        self._minihub_data = minihub_data

    @property
    def current_speed(self):
        """
        Gets the current_speed of this Minihub.
        The current speed of the minihub.

        :return: The current_speed of this Minihub.
        :rtype: str
        :required/optional: required
        """
        return self._current_speed

    @current_speed.setter
    def current_speed(self, current_speed):
        """
        Sets the current_speed of this Minihub.
        The current speed of the minihub.

        :param current_speed: The current_speed of this Minihub.
        :type: str
        """
        allowed_values = ["speedUnknown", "speed1gig", "speed2gig", "speed4gig", "speed10gig", "speed15gig", "speed3gig", "speed10meg", "speed100meg", "speed2pt5Gig", "speed5gig", "speed20gig", "speed30gig", "speed60gig", "speed8gig", "speed6gig", "speed40gig", "speed16gig", "speed56gig", "speed12gig", "speed25gig", "speed32gig", "speed100gig", "__UNDEFINED"]
        if current_speed not in allowed_values:
            raise ValueError(
                "Invalid value for `current_speed`, must be one of {0}"
                .format(allowed_values)
            )
        self._current_speed = current_speed

    @property
    def max_speed(self):
        """
        Gets the max_speed of this Minihub.
        The maximum speed of the minihub.

        :return: The max_speed of this Minihub.
        :rtype: str
        :required/optional: required
        """
        return self._max_speed

    @max_speed.setter
    def max_speed(self, max_speed):
        """
        Sets the max_speed of this Minihub.
        The maximum speed of the minihub.

        :param max_speed: The max_speed of this Minihub.
        :type: str
        """
        allowed_values = ["speedUnknown", "speed1gig", "speed2gig", "speed4gig", "speed10gig", "speed15gig", "speed3gig", "speed10meg", "speed100meg", "speed2pt5Gig", "speed5gig", "speed20gig", "speed30gig", "speed60gig", "speed8gig", "speed6gig", "speed40gig", "speed16gig", "speed56gig", "speed12gig", "speed25gig", "speed32gig", "speed100gig", "__UNDEFINED"]
        if max_speed not in allowed_values:
            raise ValueError(
                "Invalid value for `max_speed`, must be one of {0}"
                .format(allowed_values)
            )
        self._max_speed = max_speed

    @property
    def channel(self):
        """
        Gets the channel of this Minihub.
        The channel number that this minihub is associated with.

        :return: The channel of this Minihub.
        :rtype: int
        :required/optional: required
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """
        Sets the channel of this Minihub.
        The channel number that this minihub is associated with.

        :param channel: The channel of this Minihub.
        :type: int
        """
        self._channel = channel

    @property
    def port_list(self):
        """
        Gets the port_list of this Minihub.
        Detailed information for each port of the minihub. This field is deprecated.

        :return: The port_list of this Minihub.
        :rtype: PortList
        :required/optional: required
        """
        return self._port_list

    @port_list.setter
    def port_list(self, port_list):
        """
        Sets the port_list of this Minihub.
        Detailed information for each port of the minihub. This field is deprecated.

        :param port_list: The port_list of this Minihub.
        :type: PortList
        """
        self._port_list = port_list

    @property
    def vendor_name(self):
        """
        Gets the vendor_name of this Minihub.
        The vendor name of the minihub.

        :return: The vendor_name of this Minihub.
        :rtype: str
        :required/optional: required
        """
        return self._vendor_name

    @vendor_name.setter
    def vendor_name(self, vendor_name):
        """
        Sets the vendor_name of this Minihub.
        The vendor name of the minihub.

        :param vendor_name: The vendor_name of this Minihub.
        :type: str
        """
        self._vendor_name = vendor_name

    @property
    def part_number(self):
        """
        Gets the part_number of this Minihub.
        The part number of the minihub.

        :return: The part_number of this Minihub.
        :rtype: str
        :required/optional: required
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """
        Sets the part_number of this Minihub.
        The part number of the minihub.

        :param part_number: The part_number of this Minihub.
        :type: str
        """
        self._part_number = part_number

    @property
    def serial_number(self):
        """
        Gets the serial_number of this Minihub.
        The serial number of the minihub.

        :return: The serial_number of this Minihub.
        :rtype: str
        :required/optional: required
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """
        Sets the serial_number of this Minihub.
        The serial number of the minihub.

        :param serial_number: The serial_number of this Minihub.
        :type: str
        """
        self._serial_number = serial_number

    @property
    def fru_type(self):
        """
        Gets the fru_type of this Minihub.
        The field replaceable unit type of the minihub.

        :return: The fru_type of this Minihub.
        :rtype: str
        :required/optional: required
        """
        return self._fru_type

    @fru_type.setter
    def fru_type(self, fru_type):
        """
        Sets the fru_type of this Minihub.
        The field replaceable unit type of the minihub.

        :param fru_type: The fru_type of this Minihub.
        :type: str
        """
        self._fru_type = fru_type

    @property
    def manufacturer_date(self):
        """
        Gets the manufacturer_date of this Minihub.
        The date the minihub was manufactured.

        :return: The manufacturer_date of this Minihub.
        :rtype: int
        :required/optional: required
        """
        return self._manufacturer_date

    @manufacturer_date.setter
    def manufacturer_date(self, manufacturer_date):
        """
        Sets the manufacturer_date of this Minihub.
        The date the minihub was manufactured.

        :param manufacturer_date: The manufacturer_date of this Minihub.
        :type: int
        """
        self._manufacturer_date = manufacturer_date

    @property
    def reserved1(self):
        """
        Gets the reserved1 of this Minihub.


        :return: The reserved1 of this Minihub.
        :rtype: str
        :required/optional: optional
        """
        return self._reserved1

    @reserved1.setter
    def reserved1(self, reserved1):
        """
        Sets the reserved1 of this Minihub.


        :param reserved1: The reserved1 of this Minihub.
        :type: str
        """
        self._reserved1 = reserved1

    @property
    def reserved2(self):
        """
        Gets the reserved2 of this Minihub.


        :return: The reserved2 of this Minihub.
        :rtype: str
        :required/optional: optional
        """
        return self._reserved2

    @reserved2.setter
    def reserved2(self, reserved2):
        """
        Sets the reserved2 of this Minihub.


        :param reserved2: The reserved2 of this Minihub.
        :type: str
        """
        self._reserved2 = reserved2

    @property
    def rtr_attributes(self):
        """
        Gets the rtr_attributes of this Minihub.
        The CRU type of the minihub plus its ready-to-remove attributes, which are based on the CRU type

        :return: The rtr_attributes of this Minihub.
        :rtype: RTRAttributes
        :required/optional: required
        """
        return self._rtr_attributes

    @rtr_attributes.setter
    def rtr_attributes(self, rtr_attributes):
        """
        Sets the rtr_attributes of this Minihub.
        The CRU type of the minihub plus its ready-to-remove attributes, which are based on the CRU type

        :param rtr_attributes: The rtr_attributes of this Minihub.
        :type: RTRAttributes
        """
        self._rtr_attributes = rtr_attributes

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

