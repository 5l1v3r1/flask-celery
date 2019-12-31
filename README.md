## Running flask with celery

## Spesification
1. python 3.8
2. celery 4.4.0

### Run docker

Define how many worker do you want to use
```
docker-compose up -d --scale worker=5 --build
```
### Stop docker
```
docker-compose down
```

## Flower monitoring
Monitoring with flower [http://localhost:5555](http://localhost:5555)