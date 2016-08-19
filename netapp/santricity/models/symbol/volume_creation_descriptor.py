# coding: utf-8

"""
VolumeCreationDescriptor.py

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


class VolumeCreationDescriptor(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        VolumeCreationDescriptor - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'candidate': 'VolumeCandidate',  # (required parameter)
            'label': 'str',  # (required parameter)
            'manager': 'str',  # (required parameter)
            'capacity': 'int',  # (required parameter)
            'segment_size': 'int',  # (required parameter)
            'read_ahead': 'int',  # (required parameter)
            'write_zeros': 'bool',  # (required parameter)
            'no_mapping': 'bool',  # (required parameter)
            'volume_group_label': 'str',  # (required parameter)
            'protection_type': 'str'
        }

        self.attribute_map = {
            'candidate': 'candidate',  # (required parameter)
            'label': 'label',  # (required parameter)
            'manager': 'manager',  # (required parameter)
            'capacity': 'capacity',  # (required parameter)
            'segment_size': 'segmentSize',  # (required parameter)
            'read_ahead': 'readAhead',  # (required parameter)
            'write_zeros': 'writeZeros',  # (required parameter)
            'no_mapping': 'noMapping',  # (required parameter)
            'volume_group_label': 'volumeGroupLabel',  # (required parameter)
            'protection_type': 'protectionType'
        }

        self._candidate = None
        self._label = None
        self._manager = None
        self._capacity = None
        self._segment_size = None
        self._read_ahead = None
        self._write_zeros = None
        self._no_mapping = None
        self._volume_group_label = None
        self._protection_type = None

    @property
    def candidate(self):
        """
        Gets the candidate of this VolumeCreationDescriptor.
        The volume candidate object that is to be used as the basis for the new volume.

        :return: The candidate of this VolumeCreationDescriptor.
        :rtype: VolumeCandidate
        :required/optional: required
        """
        return self._candidate

    @candidate.setter
    def candidate(self, candidate):
        """
        Sets the candidate of this VolumeCreationDescriptor.
        The volume candidate object that is to be used as the basis for the new volume.

        :param candidate: The candidate of this VolumeCreationDescriptor.
        :type: VolumeCandidate
        """
        self._candidate = candidate

    @property
    def label(self):
        """
        Gets the label of this VolumeCreationDescriptor.
        The user-assigned label to be used as the name of the new volume.

        :return: The label of this VolumeCreationDescriptor.
        :rtype: str
        :required/optional: required
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this VolumeCreationDescriptor.
        The user-assigned label to be used as the name of the new volume.

        :param label: The label of this VolumeCreationDescriptor.
        :type: str
        """
        self._label = label

    @property
    def manager(self):
        """
        Gets the manager of this VolumeCreationDescriptor.
        The controller reference value of the controller that will be assigned as the owner of the newly-created volume.

        :return: The manager of this VolumeCreationDescriptor.
        :rtype: str
        :required/optional: required
        """
        return self._manager

    @manager.setter
    def manager(self, manager):
        """
        Sets the manager of this VolumeCreationDescriptor.
        The controller reference value of the controller that will be assigned as the owner of the newly-created volume.

        :param manager: The manager of this VolumeCreationDescriptor.
        :type: str
        """
        self._manager = manager

    @property
    def capacity(self):
        """
        Gets the capacity of this VolumeCreationDescriptor.
        The desired capacity of the new volume. Note that the controller may be forced to make the actual volume slightly larger than the requested size to account for arrangement of parity data, etc. If the resulting size is still smaller than the size of the volume candidate, then a new free extent will be created in addition to the new volume to account for the unused capacity.

        :return: The capacity of this VolumeCreationDescriptor.
        :rtype: int
        :required/optional: required
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Sets the capacity of this VolumeCreationDescriptor.
        The desired capacity of the new volume. Note that the controller may be forced to make the actual volume slightly larger than the requested size to account for arrangement of parity data, etc. If the resulting size is still smaller than the size of the volume candidate, then a new free extent will be created in addition to the new volume to account for the unused capacity.

        :param capacity: The capacity of this VolumeCreationDescriptor.
        :type: int
        """
        self._capacity = capacity

    @property
    def segment_size(self):
        """
        Gets the segment_size of this VolumeCreationDescriptor.
        The desired segment size for the new volume in bytes. This must be one of the supported segment sizes, as specified in the FeatureParameters object returned by the controller. Alternatively, a value of zero can be specified to indicate that the controller should select a reasonable segment size based on the usage hint provided in the volume creation request.

        :return: The segment_size of this VolumeCreationDescriptor.
        :rtype: int
        :required/optional: required
        """
        return self._segment_size

    @segment_size.setter
    def segment_size(self, segment_size):
        """
        Sets the segment_size of this VolumeCreationDescriptor.
        The desired segment size for the new volume in bytes. This must be one of the supported segment sizes, as specified in the FeatureParameters object returned by the controller. Alternatively, a value of zero can be specified to indicate that the controller should select a reasonable segment size based on the usage hint provided in the volume creation request.

        :param segment_size: The segment_size of this VolumeCreationDescriptor.
        :type: int
        """
        self._segment_size = segment_size

    @property
    def read_ahead(self):
        """
        Gets the read_ahead of this VolumeCreationDescriptor.
        A true (non-zero) / false (zero) indicator of whether or not automatic cache read-ahead is enabled.

        :return: The read_ahead of this VolumeCreationDescriptor.
        :rtype: int
        :required/optional: required
        """
        return self._read_ahead

    @read_ahead.setter
    def read_ahead(self, read_ahead):
        """
        Sets the read_ahead of this VolumeCreationDescriptor.
        A true (non-zero) / false (zero) indicator of whether or not automatic cache read-ahead is enabled.

        :param read_ahead: The read_ahead of this VolumeCreationDescriptor.
        :type: int
        """
        self._read_ahead = read_ahead

    @property
    def write_zeros(self):
        """
        Gets the write_zeros of this VolumeCreationDescriptor.
        A true value is an indication that the client wants the controller to initialize the new volume with all zeros. If this option is selected, the volume will be created and immediately transitioned to the formatting state. This operation can take an extended period of time to complete, and the volume will not be available during the process. A false value indicates that no zeroing is required; the volume will become available immediately, although a background initialization process will be running at the same time.

        :return: The write_zeros of this VolumeCreationDescriptor.
        :rtype: bool
        :required/optional: required
        """
        return self._write_zeros

    @write_zeros.setter
    def write_zeros(self, write_zeros):
        """
        Sets the write_zeros of this VolumeCreationDescriptor.
        A true value is an indication that the client wants the controller to initialize the new volume with all zeros. If this option is selected, the volume will be created and immediately transitioned to the formatting state. This operation can take an extended period of time to complete, and the volume will not be available during the process. A false value indicates that no zeroing is required; the volume will become available immediately, although a background initialization process will be running at the same time.

        :param write_zeros: The write_zeros of this VolumeCreationDescriptor.
        :type: bool
        """
        self._write_zeros = write_zeros

    @property
    def no_mapping(self):
        """
        Gets the no_mapping of this VolumeCreationDescriptor.
        A true value indicates that the volume should not have a LUN mapping automatically created for it. Rather, a subsequent Storage Partitions operation will be required to establish such a mapping and allow host I/O accesses to be conveyed to the new volume. A false value indicates that a default mapping should be created for the new volume.

        :return: The no_mapping of this VolumeCreationDescriptor.
        :rtype: bool
        :required/optional: required
        """
        return self._no_mapping

    @no_mapping.setter
    def no_mapping(self, no_mapping):
        """
        Sets the no_mapping of this VolumeCreationDescriptor.
        A true value indicates that the volume should not have a LUN mapping automatically created for it. Rather, a subsequent Storage Partitions operation will be required to establish such a mapping and allow host I/O accesses to be conveyed to the new volume. A false value indicates that a default mapping should be created for the new volume.

        :param no_mapping: The no_mapping of this VolumeCreationDescriptor.
        :type: bool
        """
        self._no_mapping = no_mapping

    @property
    def volume_group_label(self):
        """
        Gets the volume_group_label of this VolumeCreationDescriptor.
        The label to assign to the new volume group, if any. This field is only used when the candidate selection type is CANDIDATE_SEL_MANUAL or CANDIDATE_SEL_COUNT.

        :return: The volume_group_label of this VolumeCreationDescriptor.
        :rtype: str
        :required/optional: required
        """
        return self._volume_group_label

    @volume_group_label.setter
    def volume_group_label(self, volume_group_label):
        """
        Sets the volume_group_label of this VolumeCreationDescriptor.
        The label to assign to the new volume group, if any. This field is only used when the candidate selection type is CANDIDATE_SEL_MANUAL or CANDIDATE_SEL_COUNT.

        :param volume_group_label: The volume_group_label of this VolumeCreationDescriptor.
        :type: str
        """
        self._volume_group_label = volume_group_label

    @property
    def protection_type(self):
        """
        Gets the protection_type of this VolumeCreationDescriptor.
        This field specifies which protection type should be used for the volume being created.

        :return: The protection_type of this VolumeCreationDescriptor.
        :rtype: str
        :required/optional: required
        """
        return self._protection_type

    @protection_type.setter
    def protection_type(self, protection_type):
        """
        Sets the protection_type of this VolumeCreationDescriptor.
        This field specifies which protection type should be used for the volume being created.

        :param protection_type: The protection_type of this VolumeCreationDescriptor.
        :type: str
        """
        allowed_values = ["type0Protection", "type1Protection", "type2Protection", "type3Protection", "__UNDEFINED"]
        if protection_type not in allowed_values:
            raise ValueError(
                "Invalid value for `protection_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._protection_type = protection_type

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
