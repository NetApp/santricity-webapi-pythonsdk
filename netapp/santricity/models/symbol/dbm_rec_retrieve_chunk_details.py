# coding: utf-8

"""
DbmRecRetrieveChunkDetails.py

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


class DbmRecRetrieveChunkDetails(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DbmRecRetrieveChunkDetails - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'structure_integrity_check': 'str',  # (required parameter)
            'total_image_size': 'int',  # (required parameter)
            'timestamp': 'int',  # (required parameter)
            'config_gen': 'int',  # (required parameter)
            'chunk_data': 'str',  # (required parameter)
            'source_location': 'str',  # (required parameter)
            'config_type': 'str'
        }

        self.attribute_map = {
            'structure_integrity_check': 'structureIntegrityCheck',  # (required parameter)
            'total_image_size': 'totalImageSize',  # (required parameter)
            'timestamp': 'timestamp',  # (required parameter)
            'config_gen': 'configGen',  # (required parameter)
            'chunk_data': 'chunkData',  # (required parameter)
            'source_location': 'sourceLocation',  # (required parameter)
            'config_type': 'configType'
        }

        self._structure_integrity_check = None
        self._total_image_size = None
        self._timestamp = None
        self._config_gen = None
        self._chunk_data = None
        self._source_location = None
        self._config_type = None

    @property
    def structure_integrity_check(self):
        """
        Gets the structure_integrity_check of this DbmRecRetrieveChunkDetails.
        Indicates whether the overall image has a structural fault or if the integrity wasn't checked prior to retrieval.

        :return: The structure_integrity_check of this DbmRecRetrieveChunkDetails.
        :rtype: str
        :required/optional: required
        """
        return self._structure_integrity_check

    @structure_integrity_check.setter
    def structure_integrity_check(self, structure_integrity_check):
        """
        Sets the structure_integrity_check of this DbmRecRetrieveChunkDetails.
        Indicates whether the overall image has a structural fault or if the integrity wasn't checked prior to retrieval.

        :param structure_integrity_check: The structure_integrity_check of this DbmRecRetrieveChunkDetails.
        :type: str
        """
        allowed_values = ["skipped", "passed", "failed", "__UNDEFINED"]
        if structure_integrity_check not in allowed_values:
            raise ValueError(
                "Invalid value for `structure_integrity_check`, must be one of {0}"
                .format(allowed_values)
            )
        self._structure_integrity_check = structure_integrity_check

    @property
    def total_image_size(self):
        """
        Gets the total_image_size of this DbmRecRetrieveChunkDetails.
        The size of the image that will be retrieved.

        :return: The total_image_size of this DbmRecRetrieveChunkDetails.
        :rtype: int
        :required/optional: required
        """
        return self._total_image_size

    @total_image_size.setter
    def total_image_size(self, total_image_size):
        """
        Sets the total_image_size of this DbmRecRetrieveChunkDetails.
        The size of the image that will be retrieved.

        :param total_image_size: The total_image_size of this DbmRecRetrieveChunkDetails.
        :type: int
        """
        self._total_image_size = total_image_size

    @property
    def timestamp(self):
        """
        Gets the timestamp of this DbmRecRetrieveChunkDetails.
        Indicates when the image was retrieved.

        :return: The timestamp of this DbmRecRetrieveChunkDetails.
        :rtype: int
        :required/optional: required
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this DbmRecRetrieveChunkDetails.
        Indicates when the image was retrieved.

        :param timestamp: The timestamp of this DbmRecRetrieveChunkDetails.
        :type: int
        """
        self._timestamp = timestamp

    @property
    def config_gen(self):
        """
        Gets the config_gen of this DbmRecRetrieveChunkDetails.
        The value of the configuration gen number when the image was retrieved.

        :return: The config_gen of this DbmRecRetrieveChunkDetails.
        :rtype: int
        :required/optional: required
        """
        return self._config_gen

    @config_gen.setter
    def config_gen(self, config_gen):
        """
        Sets the config_gen of this DbmRecRetrieveChunkDetails.
        The value of the configuration gen number when the image was retrieved.

        :param config_gen: The config_gen of this DbmRecRetrieveChunkDetails.
        :type: int
        """
        self._config_gen = config_gen

    @property
    def chunk_data(self):
        """
        Gets the chunk_data of this DbmRecRetrieveChunkDetails.
        The data chunk.

        :return: The chunk_data of this DbmRecRetrieveChunkDetails.
        :rtype: str
        :required/optional: required
        """
        return self._chunk_data

    @chunk_data.setter
    def chunk_data(self, chunk_data):
        """
        Sets the chunk_data of this DbmRecRetrieveChunkDetails.
        The data chunk.

        :param chunk_data: The chunk_data of this DbmRecRetrieveChunkDetails.
        :type: str
        """
        self._chunk_data = chunk_data

    @property
    def source_location(self):
        """
        Gets the source_location of this DbmRecRetrieveChunkDetails.
        Defines which storage device to read the image from. Repeated here to ensure all chunks were read from the same place.

        :return: The source_location of this DbmRecRetrieveChunkDetails.
        :rtype: str
        :required/optional: required
        """
        return self._source_location

    @source_location.setter
    def source_location(self, source_location):
        """
        Sets the source_location of this DbmRecRetrieveChunkDetails.
        Defines which storage device to read the image from. Repeated here to ensure all chunks were read from the same place.

        :param source_location: The source_location of this DbmRecRetrieveChunkDetails.
        :type: str
        """
        allowed_values = ["unknown", "dacstoreDisks", "onboardRpa", "hostImage", "__UNDEFINED"]
        if source_location not in allowed_values:
            raise ValueError(
                "Invalid value for `source_location`, must be one of {0}"
                .format(allowed_values)
            )
        self._source_location = source_location

    @property
    def config_type(self):
        """
        Gets the config_type of this DbmRecRetrieveChunkDetails.
        Which record types to check.

        :return: The config_type of this DbmRecRetrieveChunkDetails.
        :rtype: str
        :required/optional: required
        """
        return self._config_type

    @config_type.setter
    def config_type(self, config_type):
        """
        Sets the config_type of this DbmRecRetrieveChunkDetails.
        Which record types to check.

        :param config_type: The config_type of this DbmRecRetrieveChunkDetails.
        :type: str
        """
        allowed_values = ["configNone", "traditionalConfig", "configAll", "partialConfig", "__UNDEFINED"]
        if config_type not in allowed_values:
            raise ValueError(
                "Invalid value for `config_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._config_type = config_type

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

