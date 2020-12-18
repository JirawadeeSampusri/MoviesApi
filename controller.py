import sys
from flask import abort
import pymysql as mysql
from config import OPENAPI_AUTOGEN_DIR, DB_HOST, DB_USER, DB_PASSWD, DB_NAME

sys.path.append(OPENAPI_AUTOGEN_DIR)
from openapi_server import models

def db_cursor():
    return mysql.connect(host=DB_HOST,user=DB_USER,passwd=DB_PASSWD,db=DB_NAME).cursor()

def get_movies():
    with db_cursor() as cs:
        cs.execute("""
            SELECT *
            FROM Movies""")
        result = [models.Movie(*row) for row in cs.fetchall()]
    if result:
        return result
    else:
        abort(404)

def get_movies_directed_by_director_name(director_name):
    with db_cursor() as cs:
        cs.execute("""
            SELECT *
            FROM Movies
            WHERE director_name=%s
            """, [director_name])
        result = [models.Movie(*row) for row in cs.fetchall()]
    if result:
        return result
    else:
        abort(404)

def get_movie_detail_by_movie_title(movie_title):
    with db_cursor() as cs:
        cs.execute("""
            SELECT *
            FROM Movies
            WHERE movie_title=%s
            """, [movie_title])
        result = [models.Movie(*row) for row in cs.fetchall()]
    return result
def get_movie_by_year(title_year):
    with db_cursor() as cs:
        cs.execute("""
            SELECT *
            FROM Movies
            WHERE title_year=%s
            """, [title_year])
        result = [models.Movie(*row) for row in cs.fetchall()]
    if result:
        return result
    else:
        abort(404)

def get_average_score_for_director(director_name):
    with db_cursor() as cs:
        cs.execute("""
            SELECT AVG(imdb_score)
            FROM Movies
            WHERE director_name=%s;
            """, [director_name])
        result = cs.fetchone()
    if result:
        return result
    else:
        abort(404)

def get_best_movies():
    with db_cursor() as cs:
        cs.execute("""
            SELECT * 
            FROM Movies
            WHERE imdb_score > 9""")
        result = [models.Movie(*row) for row in cs.fetchall()]
    if result:
        return result
    else:
        abort(404)
def get_movies_from_actor(actor_name):
    actor_1_name = actor_name
    actor_2_name = actor_name
    actor_3_name = actor_name
    with db_cursor() as cs:
        cs.execute("""
            SELECT *
            FROM Movies
            WHERE actor_1_name=%s OR actor_2_name=%s OR actor_3_name=%s;
            """, [actor_1_name,actor_2_name,actor_3_name])
        result = [models.Actor(*row) for row in cs.fetchall()]
    if result:
        return result
    else:
        abort(404)

def get_average_score_of_actor(actor_name):
    actor_1_name = actor_name
    actor_2_name = actor_name
    actor_3_name = actor_name
    with db_cursor() as cs:
        cs.execute("""
            SELECT AVG(imdb_score)
            FROM Movies
            WHERE actor_1_name=%s OR actor_2_name=%s OR actor_3_name=%s;
            """, [actor_1_name,actor_2_name,actor_3_name])
        result = cs.fetchone()
    if result:
        score = result
        return score
    else:
        abort(404)

def get_average_score_of_movies_in_each_year():
    with db_cursor() as cs:
        cs.execute("""
            SELECT title_year, AVG(imdb_score)
            FROM Movies
            GROUP BY title_year
            ORDER BY title_year
            """)
        result = [models.AverageEachYear(*row) for row in cs.fetchall()]
    if result:
        return result
    else:
        abort(404)
def get_average_score_of_movies_in_that_year(title_year):
    with db_cursor() as cs:
        cs.execute("""
            SELECT AVG(imdb_score)
            FROM Movies
            WHERE title_year=%s
            """,  [title_year])
        result = cs.fetchone()
    if result:
        return result
    else:
        abort(404)

def find_most_score_of_year():
    result = get_average_score_of_movies_in_each_year()
    max_score = 0
    for i in result:
        if i.imdb_avg_score > max_score:
            max_score = i.imdb_avg_score
            year = i.title_year
    if result:
        return f"{year} : {max_score}"
    else:
        abort(404)

def get_average_score_for_each_director():
    with db_cursor() as cs:
        cs.execute("""
            SELECT director_name,AVG(imdb_score)
            FROM Movies
            GROUP BY director_name;
            """)
        result = [models.Director(*row) for row in cs.fetchall()]
    if result:
        return result
    else:
        abort(404)
def get_average_score_for_each_director_in_each_year(title_year):
    with db_cursor() as cs:
        cs.execute("""
            SELECT director_name,AVG(imdb_score)
            FROM Movies
            WHERE title_year=%s
            GROUP BY director_name;
            """, [title_year])
        result = [models.Movie(*row) for row in cs.fetchall()]
    if result:
        return result
    else:
        abort(404)

def get_best_director():
    result = get_average_score_for_each_director()
    max_score = 0
    for i in result:
        if i.imdb_avg_score > max_score:
            max_score = i.imdb_avg_score
            director_name = i.director_name
    if result:
        return f"{director_name} : {max_score}"
    else:
        abort(404)