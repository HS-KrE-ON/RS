# RecommendationSystem
This is a project of a lecture-based project. This read-me provides information how you can run this recommender system on your local environment.

## Epic
Netflix streams movies to its users andshared its data to provide improved movie recommendations. You are tasked to create a recommenation system for its users.
To do this exercise, the company provides several files, such as information on the movies, and user ratings, summing up to a total of 480189 unique users and 17770 movies. As the movie details provided in the data-set you are expected to take advantage of publicly available information, such as the latest IMDb information here https://www.imdb.com/interfaces/.
Further details can be found here https://www.kaggle.com/datasets/netflix-inc/netflix-prize-data

## Project Management
The project was managed with the SCRUM method in four sprints with CI/CD. To view our tasks and overall progress checkout: 
https://github.com/orgs/HS-KrE-ON/projects/1

To have a closer look on our CI/CD pipeline, also checkout:
https://github.com/HS-KrE-ON/RS/actions

## Access via Frontend
The frontend of this application is available via https://rs-api-end.herokuapp.com/
Here you can type in up to five movies you liked and the system provides ten recommendations. 

## Deployment TODO
The API is deployed via a ci/cd pipeline using github actions. With the deployment of new changes the python file is tested and later pushed to the heroku app.

Both the linting and code validity is checked before doing so.

Only after the build step is completed the deploy step begins

The three relevant enpoints are as follows:

This index html file
https://recommender-system-hs.herokuapp.com/

The list of available movies
https://recommender-system-hs.herokuapp.com/movies

A recommendation based on a given movie id
https://recommender-system-hs.herokuapp.com/recommendation?movies=111

or for multiple

https://recommender-system-hs.herokuapp.com/recommendation?movies=111,420,69

## How to use TODO
git clone https://github.com/MBulti/HS_Sem5_ProgrammingProject.git
pip3 install virtualenv
python -m venv env
.\evn\Scripts\activate
pip3 install -r .\requirements.txt
## Run API
python .\app.py
## Create Datafiles
The data you need to run the system is provided in this repository.

Optional:
If you want to use the data provided by Netflix visit https://www.kaggle.com/datasets/netflix-inc/netflix-prize-data and download following data:
- movies_titles.csv
- combined_data_1.txt
- combined_data_2.txt
- combined_data_3.txt
- combined_data_4.txt

Afterwards checkout the Colab-Notebook to create the files as they are in this repository:
https://colab.research.google.com/drive/17Xrvob4h9hZ6adA0KF0ah8yMI9ZF5k3U?usp=sharing