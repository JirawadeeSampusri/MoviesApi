# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.actor import Actor  # noqa: E501
from openapi_server.models.average_each_year import AverageEachYear  # noqa: E501
from openapi_server.models.director import Director  # noqa: E501
from openapi_server.models.movie import Movie  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_controller_find_most_score_of_year(self):
        """Test case for controller_find_most_score_of_year

        Returns a list movie.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/movie/v3/movies/MostYearScore',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

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

    def test_controller_get_average_score_for_each_director(self):
        """Test case for controller_get_average_score_for_each_director

        Returns a list movie.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/movie/v3/movies/EachDirectorScore',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_average_score_for_each_director_in_each_year(self):
        """Test case for controller_get_average_score_for_each_director_in_each_year

        Returns a list movie.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/movie/v3/movies/{title_year}/EachDirectorScore'.format(title_year=56),
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
            '/movie/v3/movies/{actor_name}/all-score'.format(actor_name='actor_name_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_average_score_of_movies_in_each_year(self):
        """Test case for controller_get_average_score_of_movies_in_each_year

        Returns a list movie.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/movie/v3/movies/EachYearScore',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_average_score_of_movies_in_that_year(self):
        """Test case for controller_get_average_score_of_movies_in_that_year

        Returns full detail of the movies that have this title.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/movie/v3/movies/{title_year}/year-score'.format(title_year=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_best_director(self):
        """Test case for controller_get_best_director

        Returns a list movie.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/movie/v3/movies/BestDirector',
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

    def test_controller_get_movie_detail_by_movie_title(self):
        """Test case for controller_get_movie_detail_by_movie_title

        Returns full detail of the movies that have this title.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/movie/v3/movies/{movie_title}'.format(movie_title='movie_title_example'),
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

    def test_controller_get_movies_from_actor(self):
        """Test case for controller_get_movies_from_actor

        Returns a list of movies that this director has directed.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/movie/v3/movies/{actor_name}'.format(actor_name='actor_name_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
