# test Senoee

## FastAPI Application with PostgreSQL and docker

### Usage :

#### Start containers

```docker
docker-compose up -d --build 
```

Test it out at [http://localhost:8000](http://localhost:8000).

For api documentations  [http://localhost:8000/docs](http://localhost:8000/docs).

#### Run the tests

```docker
docker-compose exec web pytest . 
```

#### Getting inside postgreSQL container

```docker
docker-compose exec db psql --username=user --dbname=test 
```

#### Project structure

```
project
├── src
│   ├── api
│   │   ├── controllers
│   │   ├── models
│   │   ├── repositories
│   │   ├── services
│   │   ├── db.py
│   │   └── main.py
│   └── tests
│   │   ├── conftest.py
│   │   └── test_apparaisors.py
│   ├── Dockerfile
│   └── requirements.txt
├── .gitignore
├── docker-compose.yml
└── README.md
```