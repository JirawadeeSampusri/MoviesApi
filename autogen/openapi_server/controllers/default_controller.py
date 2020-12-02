import connexion
import six

from openapi_server.models.movie import Movie  # noqa: E501
from openapi_server import util


def controller_get_average_score_for_director(director_name):  # noqa: E501
    """Returns average score of all movie of this director.

     # noqa: E501

    :param director_name: 
    :type director_name: str

    :rtype: float
    """
    return 'do some magic!'


def controller_get_average_score_of_actor(actor_1_name):  # noqa: E501
    """Returns average score of all movie of this director.

     # noqa: E501

    :param actor_1_name: 
    :type actor_1_name: str

    :rtype: float
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


def controller_get_movies_of_actor(actor_1_name):  # noqa: E501
    """Returns a list of movies that this director has directed.

     # noqa: E501

    :param actor_1_name: 
    :type actor_1_name: str

    :rtype: Movie
    """
    return 'do some magic!'
