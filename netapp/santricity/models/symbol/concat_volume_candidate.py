# coding: utf-8

"""
ConcatVolumeCandidate.py

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


class ConcatVolumeCandidate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ConcatVolumeCandidate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'cand_type': 'str',  # (required parameter)
            'new_vol_candidate': 'ConcatVolumeNewVolumeCandidate',  
            'exist_vol_candidate': 'ConcatVolumeExistingVolumeCandidate',  
            'expansion_descriptor': 'ConcatVolumeDirectExpansionDescriptor'
        }

        self.attribute_map = {
            'cand_type': 'candType',  # (required parameter)
            'new_vol_candidate': 'newVolCandidate',  
            'exist_vol_candidate': 'existVolCandidate',  
            'expansion_descriptor': 'expansionDescriptor'
        }

        self._cand_type = None
        self._new_vol_candidate = None
        self._exist_vol_candidate = None
        self._expansion_descriptor = None

    @property
    def cand_type(self):
        """
        Gets the cand_type of this ConcatVolumeCandidate.
        This enumeration is used to specify the Concatenated Volume candidate type.

        :return: The cand_type of this ConcatVolumeCandidate.
        :rtype: str
        :required/optional: required
        """
        return self._cand_type

    @cand_type.setter
    def cand_type(self, cand_type):
        """
        Sets the cand_type of this ConcatVolumeCandidate.
        This enumeration is used to specify the Concatenated Volume candidate type.

        :param cand_type: The cand_type of this ConcatVolumeCandidate.
        :type: str
        """
        allowed_values = ["unknown", "newVol", "existingVols", "expansion", "__UNDEFINED"]
        if cand_type not in allowed_values:
            raise ValueError(
                "Invalid value for `cand_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._cand_type = cand_type

    @property
    def new_vol_candidate(self):
        """
        Gets the new_vol_candidate of this ConcatVolumeCandidate.
        This field is present only if the ConcatVolumeCandidateType value is equal to CONCAT_VOL_CANDIDATE_TYPE_NEW_VOL.

        :return: The new_vol_candidate of this ConcatVolumeCandidate.
        :rtype: ConcatVolumeNewVolumeCandidate
        :required/optional: optional
        """
        return self._new_vol_candidate

    @new_vol_candidate.setter
    def new_vol_candidate(self, new_vol_candidate):
        """
        Sets the new_vol_candidate of this ConcatVolumeCandidate.
        This field is present only if the ConcatVolumeCandidateType value is equal to CONCAT_VOL_CANDIDATE_TYPE_NEW_VOL.

        :param new_vol_candidate: The new_vol_candidate of this ConcatVolumeCandidate.
        :type: ConcatVolumeNewVolumeCandidate
        """
        self._new_vol_candidate = new_vol_candidate

    @property
    def exist_vol_candidate(self):
        """
        Gets the exist_vol_candidate of this ConcatVolumeCandidate.
        This field is present only if the ConcatVolumeCandidateType value is equal to CONCAT_VOL_CANDIDATE_TYPE_EXISTING_VOLS.

        :return: The exist_vol_candidate of this ConcatVolumeCandidate.
        :rtype: ConcatVolumeExistingVolumeCandidate
        :required/optional: optional
        """
        return self._exist_vol_candidate

    @exist_vol_candidate.setter
    def exist_vol_candidate(self, exist_vol_candidate):
        """
        Sets the exist_vol_candidate of this ConcatVolumeCandidate.
        This field is present only if the ConcatVolumeCandidateType value is equal to CONCAT_VOL_CANDIDATE_TYPE_EXISTING_VOLS.

        :param exist_vol_candidate: The exist_vol_candidate of this ConcatVolumeCandidate.
        :type: ConcatVolumeExistingVolumeCandidate
        """
        self._exist_vol_candidate = exist_vol_candidate

    @property
    def expansion_descriptor(self):
        """
        Gets the expansion_descriptor of this ConcatVolumeCandidate.
        This field is present only if the ConcatVolumeCandidateType value is equal to CONCAT_VOL_CANDIDATE_TYPE_EXPANSION.

        :return: The expansion_descriptor of this ConcatVolumeCandidate.
        :rtype: ConcatVolumeDirectExpansionDescriptor
        :required/optional: optional
        """
        return self._expansion_descriptor

    @expansion_descriptor.setter
    def expansion_descriptor(self, expansion_descriptor):
        """
        Sets the expansion_descriptor of this ConcatVolumeCandidate.
        This field is present only if the ConcatVolumeCandidateType value is equal to CONCAT_VOL_CANDIDATE_TYPE_EXPANSION.

        :param expansion_descriptor: The expansion_descriptor of this ConcatVolumeCandidate.
        :type: ConcatVolumeDirectExpansionDescriptor
        """
        self._expansion_descriptor = expansion_descriptor

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

