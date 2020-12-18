import connexion
import six

from openapi_server.models.actor import Actor  # noqa: E501
from openapi_server.models.average_each_year import AverageEachYear  # noqa: E501
from openapi_server.models.director import Director  # noqa: E501
from openapi_server.models.movie import Movie  # noqa: E501
from openapi_server import util


def controller_find_most_score_of_year():  # noqa: E501
    """Returns a list movie.

     # noqa: E501


    :rtype: str
    """
    return 'do some magic!'


def controller_get_average_score_for_director(director_name):  # noqa: E501
    """Returns average score of all movie of this director.

     # noqa: E501

    :param director_name: 
    :type director_name: str

    :rtype: float
    """
    return 'do some magic!'


def controller_get_average_score_for_each_director():  # noqa: E501
    """Returns a list movie.

     # noqa: E501


    :rtype: List[Director]
    """
    return 'do some magic!'


def controller_get_average_score_for_each_director_in_each_year(title_year):  # noqa: E501
    """Returns a list movie.

     # noqa: E501

    :param title_year: 
    :type title_year: int

    :rtype: List[Director]
    """
    return 'do some magic!'


def controller_get_average_score_of_actor(actor_name):  # noqa: E501
    """Returns average score of all movie of this director.

     # noqa: E501

    :param actor_name: 
    :type actor_name: str

    :rtype: Actor
    """
    return 'do some magic!'


def controller_get_average_score_of_movies_in_each_year():  # noqa: E501
    """Returns a list movie.

     # noqa: E501


    :rtype: List[AverageEachYear]
    """
    return 'do some magic!'


def controller_get_average_score_of_movies_in_that_year(title_year):  # noqa: E501
    """Returns full detail of the movies that have this title.

     # noqa: E501

    :param title_year: 
    :type title_year: int

    :rtype: float
    """
    return 'do some magic!'


def controller_get_best_director():  # noqa: E501
    """Returns a list movie.

     # noqa: E501


    :rtype: str
    """
    return 'do some magic!'


def controller_get_best_movies():  # noqa: E501
    """Returns a list movie that ahve imdb scor more than 9.5.

     # noqa: E501


    :rtype: List[Movie]
    """
    return 'do some magic!'


def controller_get_movie_by_year(title_year):  # noqa: E501
    """Returns full detail of the movies that have this title.

     # noqa: E501

    :param title_year: 
    :type title_year: int

    :rtype: Movie
    """
    return 'do some magic!'


def controller_get_movie_detail_by_movie_title(movie_title):  # noqa: E501
    """Returns full detail of the movies that have this title.

     # noqa: E501

    :param movie_title: 
    :type movie_title: str

    :rtype: Movie
    """
    return 'do some magic!'


def controller_get_movies():  # noqa: E501
    """Returns a list movie.

     # noqa: E501


    :rtype: List[Movie]
    """
    return 'do some magic!'


def controller_get_movies_directed_by_director_name(director_name):  # noqa: E501
    """Returns a list of movies that this director has directed.

     # noqa: E501

    :param director_name: 
    :type director_name: str

    :rtype: Movie
    """
    return 'do some magic!'


def controller_get_movies_from_actor(actor_name):  # noqa: E501
    """Returns a list of movies that this director has directed.

     # noqa: E501

    :param actor_name: 
    :type actor_name: str

    :rtype: Movie
    """
    return 'do some magic!'
