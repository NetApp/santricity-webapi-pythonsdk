# coding: utf-8

"""
MappableObject.py

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


class MappableObject(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        MappableObject - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'object_type': 'str',  
            'wwn': 'str',  
            'total_size_in_bytes': 'int',  
            'current_controller_id': 'str',  
            'list_of_mappings': 'list[LUNMapping]',  
            'mapped': 'bool',  # (required parameter)
            'preferred_controller_id': 'str',  
            'name': 'str',  
            'id': 'str'
        }

        self.attribute_map = {
            'object_type': 'objectType',  
            'wwn': 'wwn',  
            'total_size_in_bytes': 'totalSizeInBytes',  
            'current_controller_id': 'currentControllerId',  
            'list_of_mappings': 'listOfMappings',  
            'mapped': 'mapped',  # (required parameter)
            'preferred_controller_id': 'preferredControllerId',  
            'name': 'name',  
            'id': 'id'
        }

        self._object_type = None
        self._wwn = None
        self._total_size_in_bytes = None
        self._current_controller_id = None
        self._list_of_mappings = None
        self._mapped = None
        self._preferred_controller_id = None
        self._name = None
        self._id = None

    @property
    def object_type(self):
        """
        Gets the object_type of this MappableObject.


        :return: The object_type of this MappableObject.
        :rtype: str
        :required/optional: optional
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this MappableObject.


        :param object_type: The object_type of this MappableObject.
        :type: str
        """
        allowed_values = ["unknown", "volume", "pool", "host", "lunMapping", "hostGroup", "thinVolume", "drive", "volumeCopy", "pit", "pitView", "snapshotGroup", "snapshot", "accessVolume", "legacySnapshot", "hostType", "metadataTag", "managementUrl", "folder", "asyncMirrorGroup", "asyncMirrorGroupMember", "asyncMirrorGroupIncompleteMember", "consistencyGroup", "consistencyGroupView", "fan", "battery", "storageSystem", "controller", "powerSupply", "minihub", "esm", "drawer", "hostBoard", "interconnectCRU", "cacheBackupDevice", "tray", "supportCRU", "hostPort", "initiator", "snapshotSchedule", "thermalSensor", "sfp", "flashCache", "featureAttribute", "featureState", "lockKeyId", "remoteVolume", "mirrorVolume", "vaultMirrorVolume", "vaultMirrorGroup", "metadataVolume", "sasPort", "sasExpander", "channelPort", "speedNegError", "snmpAgentBundle", "stagedFirmware", "workload", None]
        if object_type not in allowed_values:
            raise ValueError(
                "Invalid value for `object_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._object_type = object_type

    @property
    def wwn(self):
        """
        Gets the wwn of this MappableObject.


        :return: The wwn of this MappableObject.
        :rtype: str
        :required/optional: optional
        """
        return self._wwn

    @wwn.setter
    def wwn(self, wwn):
        """
        Sets the wwn of this MappableObject.


        :param wwn: The wwn of this MappableObject.
        :type: str
        """
        self._wwn = wwn

    @property
    def total_size_in_bytes(self):
        """
        Gets the total_size_in_bytes of this MappableObject.


        :return: The total_size_in_bytes of this MappableObject.
        :rtype: int
        :required/optional: optional
        """
        return self._total_size_in_bytes

    @total_size_in_bytes.setter
    def total_size_in_bytes(self, total_size_in_bytes):
        """
        Sets the total_size_in_bytes of this MappableObject.


        :param total_size_in_bytes: The total_size_in_bytes of this MappableObject.
        :type: int
        """
        self._total_size_in_bytes = total_size_in_bytes

    @property
    def current_controller_id(self):
        """
        Gets the current_controller_id of this MappableObject.


        :return: The current_controller_id of this MappableObject.
        :rtype: str
        :required/optional: optional
        """
        return self._current_controller_id

    @current_controller_id.setter
    def current_controller_id(self, current_controller_id):
        """
        Sets the current_controller_id of this MappableObject.


        :param current_controller_id: The current_controller_id of this MappableObject.
        :type: str
        """
        self._current_controller_id = current_controller_id

    @property
    def list_of_mappings(self):
        """
        Gets the list_of_mappings of this MappableObject.


        :return: The list_of_mappings of this MappableObject.
        :rtype: list[LUNMapping]
        :required/optional: optional
        """
        return self._list_of_mappings

    @list_of_mappings.setter
    def list_of_mappings(self, list_of_mappings):
        """
        Sets the list_of_mappings of this MappableObject.


        :param list_of_mappings: The list_of_mappings of this MappableObject.
        :type: list[LUNMapping]
        """
        self._list_of_mappings = list_of_mappings

    @property
    def mapped(self):
        """
        Gets the mapped of this MappableObject.


        :return: The mapped of this MappableObject.
        :rtype: bool
        :required/optional: required
        """
        return self._mapped

    @mapped.setter
    def mapped(self, mapped):
        """
        Sets the mapped of this MappableObject.


        :param mapped: The mapped of this MappableObject.
        :type: bool
        """
        self._mapped = mapped

    @property
    def preferred_controller_id(self):
        """
        Gets the preferred_controller_id of this MappableObject.


        :return: The preferred_controller_id of this MappableObject.
        :rtype: str
        :required/optional: optional
        """
        return self._preferred_controller_id

    @preferred_controller_id.setter
    def preferred_controller_id(self, preferred_controller_id):
        """
        Sets the preferred_controller_id of this MappableObject.


        :param preferred_controller_id: The preferred_controller_id of this MappableObject.
        :type: str
        """
        self._preferred_controller_id = preferred_controller_id

    @property
    def name(self):
        """
        Gets the name of this MappableObject.


        :return: The name of this MappableObject.
        :rtype: str
        :required/optional: optional
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this MappableObject.


        :param name: The name of this MappableObject.
        :type: str
        """
        self._name = name

    @property
    def id(self):
        """
        Gets the id of this MappableObject.


        :return: The id of this MappableObject.
        :rtype: str
        :required/optional: optional
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MappableObject.


        :param id: The id of this MappableObject.
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

