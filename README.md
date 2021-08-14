# LATENEWS
## Author
Fredrick Wambua

## Description
This is an application that will enable users to list and preview news articles from various sources.

## User Stories
- As a user, I would like to see various news sources on the homepage of the application.
- As a user, I would also want to select a news source and see all news articles from the selected news source in the application.
- As a user, I would want to see the image, description and the time a news article was created.
- As a user, I would want to click on an article and read the full article on the source website.


## Specifications (Behaviour)
- Displays a page with news sources list on load
- On clicking the news sources links, you are directed to the articles page of that specific news source. Each artcle has a title,
author, date of publish, image and a link to the news source website.
- On clicking the url on the articles page, you are directed to the original news source website to access all the information.


## Technologies used
- Python3
- Flask

## Cloning the app Instructions
- You are welcome to make any changes to this application by following this process:
- See the discription of what the project does and understand its objectives.
- Open an issue to discuss what you would want to change.
- Fork and clone the repository to your local machine.
- Work on the changes and commit.
- Create a pull request.
- Await to see if your commited changes were accepted and implimented.

## Installation requirements
## Prerequisites
- Python3
- pip
## installations
### setting virtual environment
```
$ python3 -m venv pip install virtual
$ python3 source virtual/bin/activate
```
### installing flask and other packages dependencies
```
$ python3 -m pip install Flask
$ python3 -m pip install Flask-Script
```
### getting api key
- To accompish the objectives of this project, access an api key by creating an account with [Newsapi](https://newsapi.org/).
- Configure the api key in the configuration file in the application directory.

## Known bugs
The search functionality in the search form do not query results
This bug is being solved as ther is continuous development and modification of the app to meet all the functionalities.

## Deployment
To see how the application works, visit [latenews](https://cathupnews.herokuapp.com/)

## Licence
Copyright 2021 Fredrick Wambua Musyoki

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



