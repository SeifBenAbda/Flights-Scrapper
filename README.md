# Flight Scraping Project

This project is a Flask web application for scraping flight information from three different platforms: booking.com, kayak.de, and cheapflights.com. The application is containerized using Docker and Docker Compose to streamline deployment and development.

## Python Version

The project uses Python 3.12-slim.

## Project Structure


```
├── api
│ ├── routes
│ ├── services
│ ├── utils
│ └── init.py
├── classes
├── node_modules
├── static
├── templates
├── venv
├── app.py
├── docker-compose.yml
├── Dockerfile
├── package.json
├── package-lock.json
├── requirements.txt
└── tailwind.config.js
```


## Getting Started

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [PyCharm](https://www.jetbrains.com/pycharm/)

### Building the Project

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
2. **Build the Docker image:**:
   ```bash
   docker build -t flight-scraper
3. **Run the application using Docker Compose::**:
   ```bash
   docker-compose up
The application should now be accessible at [http://localhost:5000](http://localhost:5000).

## Setting Up Docker Compose in PyCharm
1. **Open your project in PyCharm**:
   * Ensure that your Dockerfile and docker-compose.yml are in the root of your project.

2. **Configure Docker in PyCharm**:
   * Go to File > Settings > Build, Execution, Deployment > Docker.
   * Click the `+` icon to add a Docker configuration.
   * Choose Docker for your Docker Desktop setup, and ensure Docker is running.

3. **Set Up Docker Compose**:
   * Go to File > Settings > Build, Execution, Deployment > Docker Compose.
   * Click the `+` icon to add a new Docker Compose configuration.
   * Set the `Service` to `web` (or the appropriate service name from your docker-compose.yml).
   * In the Docker Compose File field, navigate to and select your docker-compose.yml file.
   * Click Apply and OK to save the configuration.

# Contributing
  * `We may make this project open for learning purposes`

> ⚠️ **Warning:** Scrapping data is strictly forbidden . This is only a learning Project

