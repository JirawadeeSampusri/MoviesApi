# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.movie import Movie  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_controller_get_average_score_for_director(self):
        """Test case for controller_get_average_score_for_director

        Returns average score of all movie of this director.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/movie/v3/movies/{director_name}/score'.format(director_name='director_name_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_average_score_of_actor(self):
        """Test case for controller_get_average_score_of_actor

        Returns average score of all movie of this director.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/movie/v3/movies/{actor_1_name}/all-score'.format(actor_1_name='actor_1_name_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_best_movies(self):
        """Test case for controller_get_best_movies

        Returns a list movie that ahve imdb scor more than 9.5.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/movie/v3/movies/best-movies',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_movie_by_year(self):
        """Test case for controller_get_movie_by_year

        Returns full detail of the movies that have this title.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/movie/v3/movies/{title_year}'.format(title_year=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_movies(self):
        """Test case for controller_get_movies

        Returns a list movie.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/movie/v3/movies',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_movies_directed_by_director_name(self):
        """Test case for controller_get_movies_directed_by_director_name

        Returns a list of movies that this director has directed.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/movie/v3/movies/{director_name}'.format(director_name='director_name_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_movies_of_actor(self):
        """Test case for controller_get_movies_of_actor

        Returns a list of movies that this director has directed.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/movie/v3/movies/{actor_1_name}'.format(actor_1_name='actor_1_name_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
