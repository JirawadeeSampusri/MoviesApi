# MoviesApi
Our project is used to gather information about movies in each year we have so many movies then we came up with the idea that we can find the year that has the most interesting movie from the average rating in that year and find the director that is the best one of all time or each year.

## Members
- Jirawadee Sampusri 6110545457
- Kasidit Wongpaiboon 6110545422

## For class
01219335 Data Acquisition and Integration. SKE,Kasetsart University.

## Datasource
- https://rapidapi.com/
- https://data.world/

## Requirement
- Python version 3.6 or greater is required.
- Node.js
- Java

## Instructions for building and running
1. clone our project from this link https://github.com/JirawadeeSampusri/MoviesApi.git
2. Download [openapi-generator-cli](https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/4.3.1/openapi-generator-cli-4.3.1.jar)
and place it in your project directory
3. Go to your project directory 
    ```
    cd to/your/directory
    ```
4. Open virtual environment
    ```
    virtualenv env
    ```
    then
    ```
    . env/bin/activate
    ```
3. Generate open-api
    ```
    java -jar openapi-generator-cli-4.3.1.jar generate -i openapi movies-api.yaml -o autogen -g python-flask
    ```
4. Run the application
    ```
    python3 app.py
    ```
5. Enter url in the Browser /movie/v3
## The end point that we have
- /movies
- /movies/{director_name}
- /movies/{director_name}/score
- /movies/{title_year}
- /movies/{title_year}/year-score
- /movies/{title_year}/EachDirectorScore/
- /movies/{movie_title}
- /movies/{actor_name}
- /movies/{actor_name}/all-score
- /movies/best-movies
- /movies/EachYearScore
- /movies/MostYearScore
- /movies/EachDirectorScore
- /movies/BestDirector