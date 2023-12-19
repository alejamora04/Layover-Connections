
![Main Banner](https://github.com/alejamora04/Layover-Connections/blob/main/media/airport-departure-board-cropped.jpg)

# Welcome to Layover Connections
Layover Connections is an app designed to connect people who are stuck at the airport in the same city during an extended layover. Users will be able to find other travelers to hang out with and to explore the city. Together groups both large and small will be able to coordinate social events. The app will launch in Beta with support for flyers located in Chicago at either the O’Hare or Midway airports. Whether you’re in the city for 2 hours or over 16 hours this will provide a greet service to meet cool people.





## App Features and functionality
This app will allow users to schedule events for when they have a layover in Chicago. Events will be organized via categories and will allow any interested guest to join an existing or upcoming event. Events will either be open to the public or require host approval beforehand.


## Installation & Setup
To run Layover Connections the application repository source code has been containerized using Docker via a compose.yaml file. In order to install and run all dependencies Docker Compose must be installed in the target machine.

### Application Prerequisites 
- Docker Engine
- Docker Compose

### Application Setup
1. Install Docker Compose and Docker Engine by following Docker's documentation for installation instructions depending on your OS.
   
   a. Docker Engine Setup (Optional): Required to modify existing docker containers of the repository.  
   https://docs.docker.com/engine/install/

   b. Docker Compose Installation (Required): Necessary for running application.    
   https://docs.docker.com/compose/install/standalone/  
   **Note: Unless configured within your docker installation all docker commands require sudo permissions!**

3. Clone the git repository and cd into the project root directory.  
    `$ /Layover-Connections`

5. Build an image of the container reflecting the current state of the project with changes to the source code reflected.  
        `$ docker compose build`

6. Run updated containers for both the database as well as the application.  
       `$ docker compose up -d`

7. Apply existing migrations to the Django project database to reflect the state of the database from the command line.
       
       
       `$ docker compose exec web python manage.py makemigrations --noinput`


       `$ docker compose exec web python manage.py migrate --noinput`


8. Open the running appplication within your web browser via the specified localhost http: port.  
        http://localhost:8000
   
9. To stop any running images.  
        `$ docker compose down`


## App Architecture
Layover Connections is a full stack application built with the Django web framework. It follows progressive web design conventions and principles. The project and apps are structured to have Django render the templates and HTML. The rendered HTML is then displayed and styled in the browser using CSS along with Bootstrap and enhanced with JavaScript to handle the UI along with other client-side functions.

## How to Contribute:
At the moment any and all contributors are welcome to make contributions to improve the application.
### Languages & Frameworks in Use:
### Backend:
-	Django
-	Python
-	PostgreSQL

### Frontend:
-	CSS + Bootstrap
-	JavaScript
  
### Development Pipeline:
-	Docker

## Current Objectives
### Beta Features (Current Roadmap)
-	Build User Profiles to show traveler details [Complete]
-	Build an Event App where travelers can join and host [Complete]
- Migrate db build to PostgreSQL. [Complete]
- Containerize Application with Docker. [Complete]
-	Develop Automated Unit Test for application components with Pytest.
-	Perform Django Pre-deploy checks and audit
-	Deploy Beta version of the application.
### Post Beta Features
-	Build a messaging app to allow users to communicate amongst one another.
-	Consider user feedback to suggestions and fixes.
-	Extend Unit Testing
-	Expand scope of features via 3rd party API interactivity (i.e. Implementing Yelp Suggestions based on user location.)
-	Integrate Smart Watch compatibility
-	Have any other awesome ideas? Let us know!