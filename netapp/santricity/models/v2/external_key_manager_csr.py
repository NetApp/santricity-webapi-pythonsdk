# coding: utf-8

"""
ExternalKeyManagerCSR.py

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


class ExternalKeyManagerCSR(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ExternalKeyManagerCSR - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'common_name': 'str',  # (required parameter)
            'organization_name': 'str',  # (required parameter)
            'organizational_unit_name': 'str',  
            'locality_name': 'str',  # (required parameter)
            'state_province_name': 'str',  
            'country_name': 'str'
        }

        self.attribute_map = {
            'common_name': 'commonName',  # (required parameter)
            'organization_name': 'organizationName',  # (required parameter)
            'organizational_unit_name': 'organizationalUnitName',  
            'locality_name': 'localityName',  # (required parameter)
            'state_province_name': 'stateProvinceName',  
            'country_name': 'countryName'
        }

        self._common_name = None
        self._organization_name = None
        self._organizational_unit_name = None
        self._locality_name = None
        self._state_province_name = None
        self._country_name = None

    @property
    def common_name(self):
        """
        Gets the common_name of this ExternalKeyManagerCSR.
        Typically pre-populated with the storage array name

        :return: The common_name of this ExternalKeyManagerCSR.
        :rtype: str
        :required/optional: required
        """
        return self._common_name

    @common_name.setter
    def common_name(self, common_name):
        """
        Sets the common_name of this ExternalKeyManagerCSR.
        Typically pre-populated with the storage array name

        :param common_name: The common_name of this ExternalKeyManagerCSR.
        :type: str
        """
        self._common_name = common_name

    @property
    def organization_name(self):
        """
        Gets the organization_name of this ExternalKeyManagerCSR.
        The full legal name of the organization

        :return: The organization_name of this ExternalKeyManagerCSR.
        :rtype: str
        :required/optional: required
        """
        return self._organization_name

    @organization_name.setter
    def organization_name(self, organization_name):
        """
        Sets the organization_name of this ExternalKeyManagerCSR.
        The full legal name of the organization

        :param organization_name: The organization_name of this ExternalKeyManagerCSR.
        :type: str
        """
        self._organization_name = organization_name

    @property
    def organizational_unit_name(self):
        """
        Gets the organizational_unit_name of this ExternalKeyManagerCSR.
        The division of the organization handling the certificate

        :return: The organizational_unit_name of this ExternalKeyManagerCSR.
        :rtype: str
        :required/optional: optional
        """
        return self._organizational_unit_name

    @organizational_unit_name.setter
    def organizational_unit_name(self, organizational_unit_name):
        """
        Sets the organizational_unit_name of this ExternalKeyManagerCSR.
        The division of the organization handling the certificate

        :param organizational_unit_name: The organizational_unit_name of this ExternalKeyManagerCSR.
        :type: str
        """
        self._organizational_unit_name = organizational_unit_name

    @property
    def locality_name(self):
        """
        Gets the locality_name of this ExternalKeyManagerCSR.
        City or Locality for the organization

        :return: The locality_name of this ExternalKeyManagerCSR.
        :rtype: str
        :required/optional: required
        """
        return self._locality_name

    @locality_name.setter
    def locality_name(self, locality_name):
        """
        Sets the locality_name of this ExternalKeyManagerCSR.
        City or Locality for the organization

        :param locality_name: The locality_name of this ExternalKeyManagerCSR.
        :type: str
        """
        self._locality_name = locality_name

    @property
    def state_province_name(self):
        """
        Gets the state_province_name of this ExternalKeyManagerCSR.
        The full name of the state or province for the organization

        :return: The state_province_name of this ExternalKeyManagerCSR.
        :rtype: str
        :required/optional: optional
        """
        return self._state_province_name

    @state_province_name.setter
    def state_province_name(self, state_province_name):
        """
        Sets the state_province_name of this ExternalKeyManagerCSR.
        The full name of the state or province for the organization

        :param state_province_name: The state_province_name of this ExternalKeyManagerCSR.
        :type: str
        """
        self._state_province_name = state_province_name

    @property
    def country_name(self):
        """
        Gets the country_name of this ExternalKeyManagerCSR.
        The two letter country ISO code for the organization

        :return: The country_name of this ExternalKeyManagerCSR.
        :rtype: str
        :required/optional: required
        """
        return self._country_name

    @country_name.setter
    def country_name(self, country_name):
        """
        Sets the country_name of this ExternalKeyManagerCSR.
        The two letter country ISO code for the organization

        :param country_name: The country_name of this ExternalKeyManagerCSR.
        :type: str
        """
        self._country_name = country_name

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

