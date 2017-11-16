# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class InlineResponse2008(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name: str=None, state: str=None, created_at: date=None, last_modified_at: date=None):
        """
        InlineResponse2008 - a model defined in Swagger

        :param name: The name of this InlineResponse2008.
        :type name: str
        :param state: The state of this InlineResponse2008.
        :type state: str
        :param created_at: The created_at of this InlineResponse2008.
        :type created_at: date
        :param last_modified_at: The last_modified_at of this InlineResponse2008.
        :type last_modified_at: date
        """
        self.swagger_types = {
            'name': str,
            'state': str,
            'created_at': date,
            'last_modified_at': date
        }

        self.attribute_map = {
            'name': 'name',
            'state': 'state',
            'created_at': 'createdAt',
            'last_modified_at': 'lastModifiedAt'
        }

        self._name = name
        self._state = state
        self._created_at = created_at
        self._last_modified_at = last_modified_at

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2008':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_8 of this InlineResponse2008.
        :rtype: InlineResponse2008
        """
        return deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """
        Gets the name of this InlineResponse2008.

        :return: The name of this InlineResponse2008.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """
        Sets the name of this InlineResponse2008.

        :param name: The name of this InlineResponse2008.
        :type name: str
        """

        self._name = name

    @property
    def state(self) -> str:
        """
        Gets the state of this InlineResponse2008.

        :return: The state of this InlineResponse2008.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str):
        """
        Sets the state of this InlineResponse2008.

        :param state: The state of this InlineResponse2008.
        :type state: str
        """
        allowed_values = ["PUBLISHED", "UNPUBLISHED", "DELETED"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def created_at(self) -> date:
        """
        Gets the created_at of this InlineResponse2008.

        :return: The created_at of this InlineResponse2008.
        :rtype: date
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: date):
        """
        Sets the created_at of this InlineResponse2008.

        :param created_at: The created_at of this InlineResponse2008.
        :type created_at: date
        """

        self._created_at = created_at

    @property
    def last_modified_at(self) -> date:
        """
        Gets the last_modified_at of this InlineResponse2008.

        :return: The last_modified_at of this InlineResponse2008.
        :rtype: date
        """
        return self._last_modified_at

    @last_modified_at.setter
    def last_modified_at(self, last_modified_at: date):
        """
        Sets the last_modified_at of this InlineResponse2008.

        :param last_modified_at: The last_modified_at of this InlineResponse2008.
        :type last_modified_at: date
        """

        self._last_modified_at = last_modified_at

