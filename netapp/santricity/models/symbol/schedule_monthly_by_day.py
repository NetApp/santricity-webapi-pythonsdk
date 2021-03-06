# coding: utf-8

"""
ScheduleMonthlyByDay.py

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


class ScheduleMonthlyByDay(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ScheduleMonthlyByDay - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'day_of_week': 'str',  # (required parameter)
            'daily_schedule': 'DailySchedule',  # (required parameter)
            'week_number': 'int',  # (required parameter)
            'months_of_year': 'list[str]'
        }

        self.attribute_map = {
            'day_of_week': 'dayOfWeek',  # (required parameter)
            'daily_schedule': 'dailySchedule',  # (required parameter)
            'week_number': 'weekNumber',  # (required parameter)
            'months_of_year': 'monthsOfYear'
        }

        self._day_of_week = None
        self._daily_schedule = None
        self._week_number = None
        self._months_of_year = None

    @property
    def day_of_week(self):
        """
        Gets the day_of_week of this ScheduleMonthlyByDay.
        The day of the week. This is NOT a bit mask.

        :return: The day_of_week of this ScheduleMonthlyByDay.
        :rtype: str
        :required/optional: required
        """
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, day_of_week):
        """
        Sets the day_of_week of this ScheduleMonthlyByDay.
        The day of the week. This is NOT a bit mask.

        :param day_of_week: The day_of_week of this ScheduleMonthlyByDay.
        :type: str
        """
        allowed_values = ["notSpecified", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "__UNDEFINED"]
        if day_of_week not in allowed_values:
            raise ValueError(
                "Invalid value for `day_of_week`, must be one of {0}"
                .format(allowed_values)
            )
        self._day_of_week = day_of_week

    @property
    def daily_schedule(self):
        """
        Gets the daily_schedule of this ScheduleMonthlyByDay.
        Conveys time information, including time of day, recurrence and occurrence frequency.

        :return: The daily_schedule of this ScheduleMonthlyByDay.
        :rtype: DailySchedule
        :required/optional: required
        """
        return self._daily_schedule

    @daily_schedule.setter
    def daily_schedule(self, daily_schedule):
        """
        Sets the daily_schedule of this ScheduleMonthlyByDay.
        Conveys time information, including time of day, recurrence and occurrence frequency.

        :param daily_schedule: The daily_schedule of this ScheduleMonthlyByDay.
        :type: DailySchedule
        """
        self._daily_schedule = daily_schedule

    @property
    def week_number(self):
        """
        Gets the week_number of this ScheduleMonthlyByDay.
        The week number during the month. For example, 1 = first, 2 = second, etc., and 5 = last.

        :return: The week_number of this ScheduleMonthlyByDay.
        :rtype: int
        :required/optional: required
        """
        return self._week_number

    @week_number.setter
    def week_number(self, week_number):
        """
        Sets the week_number of this ScheduleMonthlyByDay.
        The week number during the month. For example, 1 = first, 2 = second, etc., and 5 = last.

        :param week_number: The week_number of this ScheduleMonthlyByDay.
        :type: int
        """
        self._week_number = week_number

    @property
    def months_of_year(self):
        """
        Gets the months_of_year of this ScheduleMonthlyByDay.
        This is a bit mask. Values from the MonthOfYear enumeration should be added (or OR'ed) together to set this value.

        :return: The months_of_year of this ScheduleMonthlyByDay.
        :rtype: list[str]
        :required/optional: required
        """
        return self._months_of_year

    @months_of_year.setter
    def months_of_year(self, months_of_year):
        """
        Sets the months_of_year of this ScheduleMonthlyByDay.
        This is a bit mask. Values from the MonthOfYear enumeration should be added (or OR'ed) together to set this value.

        :param months_of_year: The months_of_year of this ScheduleMonthlyByDay.
        :type: list[str]
        """
        self._months_of_year = months_of_year

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

