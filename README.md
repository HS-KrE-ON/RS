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
# How to use
## If not already installed
- Install python: https://www.digitalocean.com/community/tutorials/install-python-windows-10
- Install git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
## Open Command Prompt and type in the following commands:
1. git clone https://github.com/HS-KrE-ON/RS
2. cd RS
3. pip3 install virtualenv
4. python -m venv env
5. pip3 install -r .\requirements.txt
## Run API
6. python .\app.py    -> Copy the first created link and open it in your browser
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
