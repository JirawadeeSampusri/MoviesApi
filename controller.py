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
        return result

def get_movies_directed_by_director_name(director_name):
    with db_cursor() as cs:
        cs.execute("""
            SELECT movie_title
            FROM Movies
            WHERE director_name=%s
            """, [director_name])
        result = [models.Movie(*row) for row in cs.fetchall()]
    return result

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
    return result

def get_average_score_for_director(director_name):
    with db_cursor() as cs:
        cs.execute("""
            SELECT AVG(imdb_score)
            FROM Movies
            WHERE director_name=%s;
            """, [director_name])
        result = cs.fetchone()
    return result

def get_best_movies():
    with db_cursor() as cs:
        cs.execute("""
            SELECT * 
            FROM Movies
            WHERE imdb_score > 9""")
        result = [models.Movie(*row) for row in cs.fetchall()]
        return result
def get_movies_of_actor(actor_1_name):
    with db_cursor() as cs:
        cs.execute("""
            SELECT movie_title
            FROM Movies
            WHERE actor_1_name={actor_1_name};
            """)
        result = [models.Movie(*row) for row in cs.fetchall()]
    return result

def get_average_score_of_actor(actor_name):
    with db_cursor() as cs:
        cs.execute("""
            SELECT AVG(imdb_score)
            FROM Movies
            WHERE actor_1_name={actor_1_name};
            """)
        result = cs.fetchone()
    return result

# def get_basin_geom(basinId):
#     with db_cursor() as cs:
#         cs.execute("""
#             SELECT ST_AsText(geom)
#             FROM basin_geom
#             INNER JOIN basin on basin.basin_id = basin_geom.basin_id
#             WHERE basin.basin_id=%s
#             """, [basinId])
#         result = cs.fetchone()
#     if result:
#         return result[0]
#     else:
#         abort(404)

# def get_stations_in_basin(basinId):
#     with db_cursor() as cs:
#         cs.execute("""
#             SELECT station_id,basin_id,ename,lat,lon
#             FROM station WHERE basin_id=%s
#             """, [basinId])
#         result = [models.Station(*row) for row in cs.fetchall()]
#         return result

# def get_station_details(stationId):
#     with db_cursor() as cs:
#         cs.execute("""
#             SELECT station_id,basin_id,ename,lat,lon 
#             FROM station 
#             WHERE station_id=%s
#             """, [stationId])
#         result = cs.fetchone()
#     if result:
#         return models.Station(*result)
#     else:
#         abort(404)

# def get_basin_annual_rainfall(basinId,year):
#     with db_cursor() as cs:
#         cs.execute("""
#             SELECT AVG(total_amount)
#             FROM (
#                 SELECT SUM(r.amount) as total_amount
#                 FROM rainfall r
#                 INNER JOIN station s ON r.station_id = s.station_id
#                 INNER JOIN basin b ON s.basin_id = b.basin_id
#                 WHERE b.basin_id=%s AND r.year=%s
#                 GROUP BY r.station_id
#             ) station_total
#             """, [basinId,year])
#         result = cs.fetchone()
#     if result and result[0]:
#         amount = round(result[0],2)
#         return amount
#     else:
#         abort(404)

# def get_basin_monthly_average(basinId):
#     with db_cursor() as cs:
#         cs.execute("""
#             SELECT month, AVG(monthly_amount)
#             FROM (
#                 SELECT SUM(r.amount) as monthly_amount, month
#                 FROM rainfall r
#                 INNER JOIN station s ON r.station_id = s.station_id
#                 INNER JOIN basin b ON s.basin_id = b.basin_id
#                 WHERE b.basin_id=%s
#                 GROUP BY r.station_id, month, year
#             ) monthly
#             GROUP BY month
#             """, [basinId])
#         months = ['Jan','Feb','Mar','Apr','May','Jun',
#                   'Jul','Aug','Sep','Oct','Nov','Dec']
#         result = [
#                 models.MonthlyAverage(months[month-1],month,round(amount,2))
#                 for month,amount in cs.fetchall()
#             ]
#         return result
