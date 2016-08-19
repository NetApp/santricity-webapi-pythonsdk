# coding: utf-8

"""
AsupResponse.py

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


class AsupResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AsupResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'enabled': 'bool',  # (required parameter)
            'schedule_type': 'int',  # (required parameter)
            'weekdays': 'list[int]',  # (required parameter)
            'months': 'list[int]',  # (required parameter)
            'scheduled_days': 'list[int]',  # (required parameter)
            'delivery_type': 'int',  # (required parameter)
            'destination_http_addr': 'str',  # (required parameter)
            'destination_smtp_addr': 'str',  # (required parameter)
            'http_delivery_type': 'int',  # (required parameter)
            'proxy_host_addr': 'str',  
            'proxy_host_port': 'str',  
            'auth_required': 'bool',  
            'auth_user_name': 'str',  
            'auth_password': 'str',  
            'proxy_script': 'str',  
            'mail_server': 'str',  
            'mail_sender_addr': 'str',  
            'mail_reply_addr': 'str',  
            'log': 'str',  
            'sequence': 'int'
        }

        self.attribute_map = {
            'enabled': 'enabled',  # (required parameter)
            'schedule_type': 'scheduleType',  # (required parameter)
            'weekdays': 'weekdays',  # (required parameter)
            'months': 'months',  # (required parameter)
            'scheduled_days': 'scheduledDays',  # (required parameter)
            'delivery_type': 'deliveryType',  # (required parameter)
            'destination_http_addr': 'destinationHttpAddr',  # (required parameter)
            'destination_smtp_addr': 'destinationSmtpAddr',  # (required parameter)
            'http_delivery_type': 'httpDeliveryType',  # (required parameter)
            'proxy_host_addr': 'proxyHostAddr',  
            'proxy_host_port': 'proxyHostPort',  
            'auth_required': 'authRequired',  
            'auth_user_name': 'authUserName',  
            'auth_password': 'authPassword',  
            'proxy_script': 'proxyScript',  
            'mail_server': 'mailServer',  
            'mail_sender_addr': 'mailSenderAddr',  
            'mail_reply_addr': 'mailReplyAddr',  
            'log': 'log',  
            'sequence': 'sequence'
        }

        self._enabled = None
        self._schedule_type = None
        self._weekdays = None
        self._months = None
        self._scheduled_days = None
        self._delivery_type = None
        self._destination_http_addr = None
        self._destination_smtp_addr = None
        self._http_delivery_type = None
        self._proxy_host_addr = None
        self._proxy_host_port = None
        self._auth_required = None
        self._auth_user_name = None
        self._auth_password = None
        self._proxy_script = None
        self._mail_server = None
        self._mail_sender_addr = None
        self._mail_reply_addr = None
        self._log = None
        self._sequence = None

    @property
    def enabled(self):
        """
        Gets the enabled of this AsupResponse.
        AutoSupport is enabled or disabled

        :return: The enabled of this AsupResponse.
        :rtype: bool
        :required/optional: required
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this AsupResponse.
        AutoSupport is enabled or disabled

        :param enabled: The enabled of this AsupResponse.
        :type: bool
        """
        self._enabled = enabled

    @property
    def schedule_type(self):
        """
        Gets the schedule_type of this AsupResponse.
        The schedule frequency

        :return: The schedule_type of this AsupResponse.
        :rtype: int
        :required/optional: required
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        """
        Sets the schedule_type of this AsupResponse.
        The schedule frequency

        :param schedule_type: The schedule_type of this AsupResponse.
        :type: int
        """
        self._schedule_type = schedule_type

    @property
    def weekdays(self):
        """
        Gets the weekdays of this AsupResponse.
        Days of the week

        :return: The weekdays of this AsupResponse.
        :rtype: list[int]
        :required/optional: required
        """
        return self._weekdays

    @weekdays.setter
    def weekdays(self, weekdays):
        """
        Sets the weekdays of this AsupResponse.
        Days of the week

        :param weekdays: The weekdays of this AsupResponse.
        :type: list[int]
        """
        self._weekdays = weekdays

    @property
    def months(self):
        """
        Gets the months of this AsupResponse.
        Months

        :return: The months of this AsupResponse.
        :rtype: list[int]
        :required/optional: required
        """
        return self._months

    @months.setter
    def months(self, months):
        """
        Sets the months of this AsupResponse.
        Months

        :param months: The months of this AsupResponse.
        :type: list[int]
        """
        self._months = months

    @property
    def scheduled_days(self):
        """
        Gets the scheduled_days of this AsupResponse.
        Days of the month

        :return: The scheduled_days of this AsupResponse.
        :rtype: list[int]
        :required/optional: required
        """
        return self._scheduled_days

    @scheduled_days.setter
    def scheduled_days(self, scheduled_days):
        """
        Sets the scheduled_days of this AsupResponse.
        Days of the month

        :param scheduled_days: The scheduled_days of this AsupResponse.
        :type: list[int]
        """
        self._scheduled_days = scheduled_days

    @property
    def delivery_type(self):
        """
        Gets the delivery_type of this AsupResponse.
        Delivery method

        :return: The delivery_type of this AsupResponse.
        :rtype: int
        :required/optional: required
        """
        return self._delivery_type

    @delivery_type.setter
    def delivery_type(self, delivery_type):
        """
        Sets the delivery_type of this AsupResponse.
        Delivery method

        :param delivery_type: The delivery_type of this AsupResponse.
        :type: int
        """
        self._delivery_type = delivery_type

    @property
    def destination_http_addr(self):
        """
        Gets the destination_http_addr of this AsupResponse.
        Destination HTTP address

        :return: The destination_http_addr of this AsupResponse.
        :rtype: str
        :required/optional: required
        """
        return self._destination_http_addr

    @destination_http_addr.setter
    def destination_http_addr(self, destination_http_addr):
        """
        Sets the destination_http_addr of this AsupResponse.
        Destination HTTP address

        :param destination_http_addr: The destination_http_addr of this AsupResponse.
        :type: str
        """
        self._destination_http_addr = destination_http_addr

    @property
    def destination_smtp_addr(self):
        """
        Gets the destination_smtp_addr of this AsupResponse.
        Destination SMTP address

        :return: The destination_smtp_addr of this AsupResponse.
        :rtype: str
        :required/optional: required
        """
        return self._destination_smtp_addr

    @destination_smtp_addr.setter
    def destination_smtp_addr(self, destination_smtp_addr):
        """
        Sets the destination_smtp_addr of this AsupResponse.
        Destination SMTP address

        :param destination_smtp_addr: The destination_smtp_addr of this AsupResponse.
        :type: str
        """
        self._destination_smtp_addr = destination_smtp_addr

    @property
    def http_delivery_type(self):
        """
        Gets the http_delivery_type of this AsupResponse.
        Http delivery method

        :return: The http_delivery_type of this AsupResponse.
        :rtype: int
        :required/optional: required
        """
        return self._http_delivery_type

    @http_delivery_type.setter
    def http_delivery_type(self, http_delivery_type):
        """
        Sets the http_delivery_type of this AsupResponse.
        Http delivery method

        :param http_delivery_type: The http_delivery_type of this AsupResponse.
        :type: int
        """
        self._http_delivery_type = http_delivery_type

    @property
    def proxy_host_addr(self):
        """
        Gets the proxy_host_addr of this AsupResponse.
        Proxy server address

        :return: The proxy_host_addr of this AsupResponse.
        :rtype: str
        :required/optional: optional
        """
        return self._proxy_host_addr

    @proxy_host_addr.setter
    def proxy_host_addr(self, proxy_host_addr):
        """
        Sets the proxy_host_addr of this AsupResponse.
        Proxy server address

        :param proxy_host_addr: The proxy_host_addr of this AsupResponse.
        :type: str
        """
        self._proxy_host_addr = proxy_host_addr

    @property
    def proxy_host_port(self):
        """
        Gets the proxy_host_port of this AsupResponse.
        Proxy server port

        :return: The proxy_host_port of this AsupResponse.
        :rtype: str
        :required/optional: optional
        """
        return self._proxy_host_port

    @proxy_host_port.setter
    def proxy_host_port(self, proxy_host_port):
        """
        Sets the proxy_host_port of this AsupResponse.
        Proxy server port

        :param proxy_host_port: The proxy_host_port of this AsupResponse.
        :type: str
        """
        self._proxy_host_port = proxy_host_port

    @property
    def auth_required(self):
        """
        Gets the auth_required of this AsupResponse.
        Authentication required

        :return: The auth_required of this AsupResponse.
        :rtype: bool
        :required/optional: optional
        """
        return self._auth_required

    @auth_required.setter
    def auth_required(self, auth_required):
        """
        Sets the auth_required of this AsupResponse.
        Authentication required

        :param auth_required: The auth_required of this AsupResponse.
        :type: bool
        """
        self._auth_required = auth_required

    @property
    def auth_user_name(self):
        """
        Gets the auth_user_name of this AsupResponse.
        Authentication username

        :return: The auth_user_name of this AsupResponse.
        :rtype: str
        :required/optional: optional
        """
        return self._auth_user_name

    @auth_user_name.setter
    def auth_user_name(self, auth_user_name):
        """
        Sets the auth_user_name of this AsupResponse.
        Authentication username

        :param auth_user_name: The auth_user_name of this AsupResponse.
        :type: str
        """
        self._auth_user_name = auth_user_name

    @property
    def auth_password(self):
        """
        Gets the auth_password of this AsupResponse.
        Authentication password

        :return: The auth_password of this AsupResponse.
        :rtype: str
        :required/optional: optional
        """
        return self._auth_password

    @auth_password.setter
    def auth_password(self, auth_password):
        """
        Sets the auth_password of this AsupResponse.
        Authentication password

        :param auth_password: The auth_password of this AsupResponse.
        :type: str
        """
        self._auth_password = auth_password

    @property
    def proxy_script(self):
        """
        Gets the proxy_script of this AsupResponse.
        Proxy configuration script

        :return: The proxy_script of this AsupResponse.
        :rtype: str
        :required/optional: optional
        """
        return self._proxy_script

    @proxy_script.setter
    def proxy_script(self, proxy_script):
        """
        Sets the proxy_script of this AsupResponse.
        Proxy configuration script

        :param proxy_script: The proxy_script of this AsupResponse.
        :type: str
        """
        self._proxy_script = proxy_script

    @property
    def mail_server(self):
        """
        Gets the mail_server of this AsupResponse.
        SMTP mail server

        :return: The mail_server of this AsupResponse.
        :rtype: str
        :required/optional: optional
        """
        return self._mail_server

    @mail_server.setter
    def mail_server(self, mail_server):
        """
        Sets the mail_server of this AsupResponse.
        SMTP mail server

        :param mail_server: The mail_server of this AsupResponse.
        :type: str
        """
        self._mail_server = mail_server

    @property
    def mail_sender_addr(self):
        """
        Gets the mail_sender_addr of this AsupResponse.
        Sender email address

        :return: The mail_sender_addr of this AsupResponse.
        :rtype: str
        :required/optional: optional
        """
        return self._mail_sender_addr

    @mail_sender_addr.setter
    def mail_sender_addr(self, mail_sender_addr):
        """
        Sets the mail_sender_addr of this AsupResponse.
        Sender email address

        :param mail_sender_addr: The mail_sender_addr of this AsupResponse.
        :type: str
        """
        self._mail_sender_addr = mail_sender_addr

    @property
    def mail_reply_addr(self):
        """
        Gets the mail_reply_addr of this AsupResponse.
        Reply email address

        :return: The mail_reply_addr of this AsupResponse.
        :rtype: str
        :required/optional: optional
        """
        return self._mail_reply_addr

    @mail_reply_addr.setter
    def mail_reply_addr(self, mail_reply_addr):
        """
        Sets the mail_reply_addr of this AsupResponse.
        Reply email address

        :param mail_reply_addr: The mail_reply_addr of this AsupResponse.
        :type: str
        """
        self._mail_reply_addr = mail_reply_addr

    @property
    def log(self):
        """
        Gets the log of this AsupResponse.
        Log entries

        :return: The log of this AsupResponse.
        :rtype: str
        :required/optional: optional
        """
        return self._log

    @log.setter
    def log(self, log):
        """
        Sets the log of this AsupResponse.
        Log entries

        :param log: The log of this AsupResponse.
        :type: str
        """
        self._log = log

    @property
    def sequence(self):
        """
        Gets the sequence of this AsupResponse.
        Bundle sequence number

        :return: The sequence of this AsupResponse.
        :rtype: int
        :required/optional: optional
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """
        Sets the sequence of this AsupResponse.
        Bundle sequence number

        :param sequence: The sequence of this AsupResponse.
        :type: int
        """
        self._sequence = sequence

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
