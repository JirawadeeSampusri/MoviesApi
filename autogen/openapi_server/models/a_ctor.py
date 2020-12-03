# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class ACtor(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, director_name=None, imdb_avg_score=None):  # noqa: E501
        """ACtor - a model defined in OpenAPI

        :param director_name: The director_name of this ACtor.  # noqa: E501
        :type director_name: str
        :param imdb_avg_score: The imdb_avg_score of this ACtor.  # noqa: E501
        :type imdb_avg_score: float
        """
        self.openapi_types = {
            'director_name': str,
            'imdb_avg_score': float
        }

        self.attribute_map = {
            'director_name': 'director_name',
            'imdb_avg_score': 'imdb_avg_score'
        }

        self._director_name = director_name
        self._imdb_avg_score = imdb_avg_score

    @classmethod
    def from_dict(cls, dikt) -> 'ACtor':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ACtor of this ACtor.  # noqa: E501
        :rtype: ACtor
        """
        return util.deserialize_model(dikt, cls)

    @property
    def director_name(self):
        """Gets the director_name of this ACtor.


        :return: The director_name of this ACtor.
        :rtype: str
        """
        return self._director_name

    @director_name.setter
    def director_name(self, director_name):
        """Sets the director_name of this ACtor.


        :param director_name: The director_name of this ACtor.
        :type director_name: str
        """

        self._director_name = director_name

    @property
    def imdb_avg_score(self):
        """Gets the imdb_avg_score of this ACtor.


        :return: The imdb_avg_score of this ACtor.
        :rtype: float
        """
        return self._imdb_avg_score

    @imdb_avg_score.setter
    def imdb_avg_score(self, imdb_avg_score):
        """Sets the imdb_avg_score of this ACtor.


        :param imdb_avg_score: The imdb_avg_score of this ACtor.
        :type imdb_avg_score: float
        """

        self._imdb_avg_score = imdb_avg_score
