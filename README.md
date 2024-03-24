# Environment Monitor

Environment Monitor is a comprehensive platform designed to provide real-time environmental data monitoring. Using a Raspberry Pi with an Enviro+ sensor, it collects various environmental parameters such as temperature, pressure, humidity, and particulate matter levels.

## Features

- **Real-time Environment Monitoring:** The application collects real-time data from a Raspberry Pi with Enviro+ sensor.

- **Data Visualization:** The frontend, built with SvelteKit and styled with Tailwind CSS, provides a user-friendly interface to visualize the collected data using Chart.js.

- **Local and Remote Access:** The application is containerized using Docker Compose, which allows it to be deployed and accessed both locally and remotely.

- **Database Integration:** The application uses a MySQL database to store the collected data. This allows for historical data tracking and analysis.

## Getting Started

Setting up dashboard:

1. Clone the repository
2. Run `docker-compose up --build`
3. Access frontend on `localhost:3000`

Seeding database with local data:

1. Clone the repository on a Raspberry Pi with Enviro+
2. Navigate to script: `cd .\frontend\
3. Install requirements: `pip install -r requirements.txt`
4. Run script: `python populate-db.py`

## Technologies Used

[![My Skills](https://skillicons.dev/icons?i=svelte,js,tailwind,flask,py,mysql,docker)](https://skillicons.dev)

- **Frontend:** SvelteKit with Javascript
- **Styling:** Tailwind CSS
- **Backend:** Flask
- **Database:** MySQL
- Containerised using Docker

## Project Preview

![alt text](https://i.imgur.com/LrWrVHQ.png)

## License

MIT license @ tonytwei
