# enviro-monitor

### Getting Started

- run `docker-compose up --build`
- access frontend on `localhost:8000`

To start populate db script

- navigate to /scripts
- `docker build -t populate_db .`
- `docker run -it --rm -populate_db`
