# My React Flask App

This project is a full-stack application that combines a Flask backend with a React frontend, all running in Docker containers. The backend connects to a MongoDB database, while the frontend provides a user interface.

## Project Structure

```
my-react-flask-app
├── backend
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend
│   ├── src
│   │   ├── App.js
│   │   ├── index.js
│   │   └── components
│   │       └── ExampleComponent.js
│   ├── public
│   │   └── index.html
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd my-react-flask-app
   ```

2. Build and run the application using Docker Compose:
   ```
   docker-compose up --build
   ```

### Usage

- The Flask backend will be accessible at `http://localhost:5000`.
- The React frontend will be accessible at `http://localhost:3000`.

### Contributing

Feel free to submit issues or pull requests for improvements or bug fixes. 

### License

This project is licensed under the MIT License.